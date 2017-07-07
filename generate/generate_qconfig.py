# -*- coding: utf-8 -*-

"""
.. module:: generate_mm.py
   :platform: Unix, Windows
   :synopsis: Rewrites a CMIP6 realm specialization to ES-DOC Questionnaire qconfig file.

.. moduleauthor:: Allyn Treshansky <allyn.treshansky@colorado.edu>

"""
from collections import OrderedDict
import datetime
import json

from cim_profile import CIM_PROFILE

from utils_parser import RealmSpecializationParser

import re

QCONFIG_BASE_ONTOLOGY = "cim_2.0.0"

QCONFIG_ATOMIC_PROPERTY_TYPE = "ATOMIC"
QCONFIG_ENUMERATION_PROPERTY_TYPE = "ENUMERATION"
QCONFIG_RELATIONSHIP_PROPERTY_TYPE = "RELATIONSHIP"

# mapping to go from specializations to schemas
_SPECIALIZATION_TO_SCHEMA_MAP = OrderedDict()
_SPECIALIZATION_TO_SCHEMA_MAP['realm'] = "science.realm"
_SPECIALIZATION_TO_SCHEMA_MAP['grid'] = "science.topic"
_SPECIALIZATION_TO_SCHEMA_MAP['key-properties'] = "science.topic"
_SPECIALIZATION_TO_SCHEMA_MAP['process'] = "science.topic"
_SPECIALIZATION_TO_SCHEMA_MAP['sub-process'] = "science.topic"


# mapping to go from specialization/schema types to questionnaire types
QCONFIG_ATOMIC_TYPE_MAP = {
    # TOOD: WHAT ABOUT 'email' AND 'time' ?
    "BOOLEAN": "BOOLEAN",
    "date": "DATE",
    "datetime": "DATETIME",
    "FLOAT": "DECIMAL",
    "INTEGER": "INTEGER",
    "STRING": "STRING",
    "unicode": "STRING",
    "uri": "URL",
    "uuid": "STRING",
}


def find_object_in_sequence(dct, sequence):
    """
    searches a JSON array for an object w/ the specified key/value pairs
    :param dct: key/value pairs to check
    :param sequence: JSON array to search
    :return: 1st matching JSON object or None
    """

    def _is_dct_in_item(item):
        for k, v in dct.iteritems():
            if k not in item or item[k] != v:
                return False
        return True

    for item in sequence:
        if _is_dct_in_item(item):
            return item
    return None


def emit_property(name=None, id=None, is_meta=False, documentation="", category_id=None, cardinality=None, is_nillable=True, property_type=None, atomic_type=None, enumeration_is_open=True, enumeration_members=None, relationship_targets=None, is_hierarchical=False, values=[]):

    """
    returns an OrderedDict representing a single property; all of the event handlers use this
    """

    assert name is not None and cardinality is not None and property_type is not None

    new_qconfig_property = OrderedDict()
    new_qconfig_property["name"] = name
    new_qconfig_property["cardinality"] = cardinality
    new_qconfig_property["property_type"] = property_type
    new_qconfig_property["is_meta"] = is_meta
    new_qconfig_property["is_nillable"] = is_nillable
    new_qconfig_property["documentation"] = documentation

    if property_type == QCONFIG_ATOMIC_PROPERTY_TYPE:
        assert atomic_type is not None
        new_qconfig_property["atomic_type"] = atomic_type
    elif property_type == QCONFIG_ENUMERATION_PROPERTY_TYPE:
        assert enumeration_members is not None
        new_qconfig_property["enumeration_is_open"] = enumeration_is_open
        new_qconfig_property["enumeration_members"] = enumeration_members
    elif property_type == QCONFIG_RELATIONSHIP_PROPERTY_TYPE:
        assert relationship_targets is not None
        new_qconfig_property["relationship_targets"] = relationship_targets
        new_qconfig_property["is_hierarchical"] = is_hierarchical
    else:
        msg = "Unknown property_type: {0}".format(property_type)
        raise Exception(msg)

    if id is not None:
        new_qconfig_property["id"] = id
    if category_id is not None:
        new_qconfig_property["category_id"] = category_id

    new_qconfig_property["values"] = values

    return new_qconfig_property


# emit_property(
#     name=None,
#     id=None,
#     is_meta=False,
#     documentation="",
#     category_id=None,
#     cardinality=None,
#     is_nillable=True,
#     property_type=None,
#     atomic_type=None,
#     enumeration_is_open=True,
#     enumeration_members=None,
#     relationship_targets=None,
#     is_hierarchical=False,
#     values=[]
# )


class Generator(RealmSpecializationParser):
    """Specialization to qconfig generator.

    """

    def __init__(self, realm):
        """
        Instance constructor.
        """
        super(Generator, self).__init__(realm)

        self.qconfig = OrderedDict()

        self.qconfig["name"] = realm.name
        self.qconfig["version"] = realm.change_history[-1][0]
        self.qconfig["documentation"] = realm.description
        self.qconfig["ontology_type"] = "SPECIALIZATION"
        # TODO: "ontology_base" OUGHT TO BE DEFINED MANUALLY IN THE QUESTIONNAIRE, RIGHT?
        self.qconfig["ontology_base"] = QCONFIG_BASE_ONTOLOGY
        self.qconfig["date"] = str(datetime.datetime.now())
        self.qconfig["classes"] = {"inherited": [], "excluded": [], "defined": []}

        self.current_model = None
        self.current_category = None
        self.current_property = None

    def get_output(self):
        """Returns generated output as text

        """
        return json.dumps(self.qconfig, indent=2)

    def on_realm_parse(self, realm):
        """On realm parse event handler.

        """

        schema_class = _SPECIALIZATION_TO_SCHEMA_MAP[realm.type_key]
        schema_properties = CIM_PROFILE.get(schema_class)

        # record the inherited classes...
        pass

        # record the excluded classes...
        pass

        # create the defined class...
        new_qconfig_class = OrderedDict()
        new_qconfig_class_package, new_qconfig_class_name = schema_class.split('.')
        new_qconfig_class["name"] = new_qconfig_class_name
        new_qconfig_class["package"] = new_qconfig_class_package
        new_qconfig_class["id"] = realm.id
        new_qconfig_class["documentation"] = realm.description
        new_qconfig_class["is_document"] = True

        new_qconfig_class["categories"] = {"inherited": [], "excluded": [], "defined": []}

        new_qconfig_class["properties"] = {"inherited": [], "excluded": [], "defined": []}

        # record any inherited properties...
        if schema_properties:
            new_qconfig_class["properties"]["inherited"] = schema_properties["include"]

        # record any excluded properties...
        if schema_properties:
            new_qconfig_class["properties"]["excluded"] = schema_properties["exclude"]

        # create the defined properties...
        # (the corresponding classes will be created in specific event handlers)

        grid = realm.grid
        new_qconfig_property = emit_property(
            name="grid",
            id=None,  # ?!?
            is_meta=False,
            documentation="",
            cardinality="0.1",
            is_nillable=True,
            property_type=QCONFIG_RELATIONSHIP_PROPERTY_TYPE,
            relationship_targets=["science.topic"],
            is_hierarchical=True,
            values=[grid.id]
        )
        new_qconfig_class["properties"]["defined"].append(new_qconfig_property)

        key_properties = realm.key_properties
        new_qconfig_property = emit_property(
            name="key_properties",
            id=None,  # ?!?
            is_meta=False,
            documentation="",
            cardinality="1,1",
            is_nillable=False,
            property_type=QCONFIG_RELATIONSHIP_PROPERTY_TYPE,
            relationship_targets=["science.topic"],
            is_hierarchical=True,
            values=[key_properties.id]
        )
        new_qconfig_class["properties"]["defined"].append(new_qconfig_property)

        processes = realm.processes
        new_qconfig_property = emit_property(
            name="processes",
            id=None,  # ?!?
            is_meta=False,
            documentation="",
            cardinality="{0}.{1}".format(len(processes), len(processes)),
            property_type=QCONFIG_RELATIONSHIP_PROPERTY_TYPE,
            relationship_targets=["science.topic"],
            is_hierarchical=True,
            values=[p.id for p in processes]
        )
        new_qconfig_class["properties"]["defined"].append(new_qconfig_property)

        self.qconfig["classes"]["defined"].append(new_qconfig_class)
        self.current_model = realm

    def on_grid_parse(self, grid):
        """
        On grid parse event handler.
        """
        if self.current_model:
            parent_model = find_object_in_sequence({"id": self.current_model.id}, self.qconfig["classes"]["defined"])
            assert parent_model is not None
            if self.current_category:
                parent_category = find_object_in_sequence({"id": self.current_category.id}, parent_model["categories"]["defined"])
                # assert parent_category is not None
            if self.current_property:
                parent_property = find_object_in_sequence({"name": self.current_property.name}, parent_model["properties"]["defined"])
                # assert parent_property is not None

        schema_class = _SPECIALIZATION_TO_SCHEMA_MAP[grid.type_key]
        schema_properties = CIM_PROFILE.get(schema_class)

        new_qconfig_class = OrderedDict()
        new_qconfig_class_package, new_qconfig_class_name = schema_class.split('.')
        new_qconfig_class["name"] = new_qconfig_class_name
        new_qconfig_class["id"] = grid.id
        new_qconfig_class["package"] = new_qconfig_class_package
        new_qconfig_class["documentation"] = grid.description
        new_qconfig_class["is_document"] = True

        new_qconfig_class["categories"] = {"inherited": [], "excluded": [], "defined": []}

        new_qconfig_class["properties"] = {"inherited": [], "excluded": [], "defined": []}

        # record any inherited properties...
        if schema_properties:
            new_qconfig_class["properties"]["inherited"] = schema_properties["include"]

        # record any excluded properties...
        if schema_properties:
            new_qconfig_class["properties"]["excluded"] = schema_properties["exclude"]

        self.qconfig["classes"]["defined"].append(new_qconfig_class)
        self.current_model = grid

    def on_keyproperties_parse(self, key_properties):
        """
        On key_properties parse event handler.
        """

        if self.current_model:
            parent_model = find_object_in_sequence({"id": self.current_model.id}, self.qconfig["classes"]["defined"])
            assert parent_model is not None
            if self.current_category:
                parent_category = find_object_in_sequence({"id": self.current_category.id}, parent_model["categories"]["defined"])
                # assert parent_category is not None
            if self.current_property:
                parent_property = find_object_in_sequence({"name": self.current_property.name}, parent_model["properties"]["defined"])
                # assert parent_property is not None

        schema_class = _SPECIALIZATION_TO_SCHEMA_MAP[key_properties.type_key]
        schema_properties = CIM_PROFILE.get(schema_class)

        new_qconfig_class = OrderedDict()
        new_qconfig_class_package, new_qconfig_class_name = schema_class.split('.')
        new_qconfig_class["name"] = new_qconfig_class_name
        new_qconfig_class["id"] = key_properties.id
        new_qconfig_class["package"] = new_qconfig_class_package
        new_qconfig_class["documentation"] = key_properties.description
        new_qconfig_class["is_document"] = False

        new_qconfig_class["categories"] = {"inherited": [], "excluded": [], "defined": []}

        new_qconfig_class["properties"] = {"inherited": [], "excluded": [], "defined": []}

        # record any inherited properties...
        if schema_properties:
            new_qconfig_class["properties"]["inherited"] = schema_properties["include"]

        # record any excluded properties...
        if schema_properties:
            new_qconfig_class["properties"]["excluded"] = schema_properties["exclude"]

        self.qconfig["classes"]["defined"].append(new_qconfig_class)
        self.current_model = key_properties

    def on_process_parse(self, process):
        """
        On process parse event handler.

        """

        if self.current_model:
            parent_model = find_object_in_sequence({"id": self.current_model.id}, self.qconfig["classes"]["defined"])
            assert parent_model is not None
            if self.current_category:
                parent_category = find_object_in_sequence({"id": self.current_category.id}, parent_model["categories"]["defined"])
                # assert parent_category is not None
            if self.current_property:
                parent_property = find_object_in_sequence({"name": self.current_property.name}, parent_model["properties"]["defined"])
                # assert parent_property is not None

        schema_class = _SPECIALIZATION_TO_SCHEMA_MAP[process.type_key]
        schema_properties = CIM_PROFILE.get(schema_class)

        new_qconfig_class = OrderedDict()
        new_qconfig_class_package, new_qconfig_class_name = schema_class.split('.')
        new_qconfig_class["name"] = new_qconfig_class_name
        new_qconfig_class["id"] = process.id
        new_qconfig_class["package"] = new_qconfig_class_package
        new_qconfig_class["documentation"] = process.description
        new_qconfig_class["is_document"] = False

        new_qconfig_class["categories"] = {"inherited": [], "excluded": [], "defined": []}

        new_qconfig_class["properties"] = {"inherited": [], "excluded": [], "defined": []}

        # record any inherited properties...
        if schema_properties:
            new_qconfig_class["properties"]["inherited"] = schema_properties["include"]

        # record any excluded properties...
        if schema_properties:
            new_qconfig_class["properties"]["excluded"] = schema_properties["exclude"]

        self.qconfig["classes"]["defined"].append(new_qconfig_class)
        self.current_model = process

    def on_subprocess_parse(self, subprocess):
        """
        On sub-process parse event handler.
        """

        if self.current_model:
            parent_model = find_object_in_sequence({"id": self.current_model.id}, self.qconfig["classes"]["defined"])
            assert parent_model is not None
            if self.current_category:
                parent_category = find_object_in_sequence({"id": self.current_category.id}, parent_model["categories"]["defined"])
                # assert parent_category is not None
            if self.current_property:
                parent_property = find_object_in_sequence({"name": self.current_property.name}, parent_model["properties"]["defined"])
                # assert parent_property is not None

        # TODO: AM I SURE THAT A SUB-PROCESS MAPS TO A CATEGORY ?!?

        new_qconfig_category = OrderedDict()
        new_qconfig_category["name"] = subprocess.name
        new_qconfig_category["id"] = subprocess.id
        new_qconfig_category["documentation"] = subprocess.description

        parent_model["categories"]["defined"].append(new_qconfig_category)
        self.current_category = subprocess

    def on_topic_property_set_parse(self, prop_set):
        """
        On topic property set parse event handler.

        """
        if self.current_model:
            parent_model = find_object_in_sequence({"id": self.current_model.id}, self.qconfig["classes"]["defined"])
            assert parent_model is not None
            if self.current_category:
                parent_category = find_object_in_sequence({"id": self.current_category.id}, parent_model["categories"]["defined"])
                # assert parent_category is not None
            if self.current_property:
                parent_property = find_object_in_sequence({"name": self.current_property.name}, parent_model["properties"]["defined"])
                # assert parent_property is not None

        new_qconfig_category = OrderedDict()
        new_qconfig_category["name"] = prop_set.name
        new_qconfig_category["id"] = prop_set.id
        new_qconfig_category["documentation"] = prop_set.description

        parent_model["categories"]["defined"].append(new_qconfig_category)
        self.current_category = prop_set

    def on_topic_property_parse(self, prop):
        """
        On property parse event handler.
        """
        if self.current_model:
            parent_model = find_object_in_sequence({"id": self.current_model.id}, self.qconfig["classes"]["defined"])
            assert parent_model is not None
            if self.current_category:
                parent_category = find_object_in_sequence({"id": self.current_category.id}, parent_model["categories"]["defined"])
                # assert parent_category is not None
            if self.current_property:
                parent_property = find_object_in_sequence({"name": self.current_property.name}, parent_model["properties"]["defined"])
                # assert parent_property is not None

        if prop.typeof_label == "ENUM":
            enumeration_members = []
            for i, member in enumerate(prop.enum.choices):
                enumeration_member = OrderedDict()
                enumeration_member["order"] = i
                enumeration_member["value"] = member.value
                if member.description:
                    enumeration_member["documentation"] = member.description
                enumeration_members.append(enumeration_member)
            new_qconfig_property = emit_property(
                name=prop.name,
                id=prop.id,
                is_meta=False,
                documentation=prop.description,
                cardinality=prop.cardinality,
                property_type=QCONFIG_ENUMERATION_PROPERTY_TYPE,
                enumeration_is_open=prop.enum.is_open,
                enumeration_members=enumeration_members,
            )
        else:
            new_qconfig_property = emit_property(
                name=prop.name,
                id=prop.id,
                is_meta=False,
                documentation=prop.description,
                cardinality=prop.cardinality,
                property_type=QCONFIG_ATOMIC_PROPERTY_TYPE,
                atomic_type=QCONFIG_ATOMIC_TYPE_MAP[prop.typeof_label],
            )
        if parent_category is not None:
            new_qconfig_property["category_id"] = parent_category.get("id")

        parent_model["properties"]["defined"].append(new_qconfig_property)
        self.current_property = prop
