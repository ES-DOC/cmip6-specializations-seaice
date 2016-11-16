"""
A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
SUB_PROCESSES = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Ruth Petrie'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Ruth Petrie, Bryan Lawrence'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Sea Ice Dynamics'

# --------------------------------------------------------------------
# DETAILS : General process details.
# --------------------------------------------------------------------
DETAILS['general'] = {
    'description': 'Methods of mechanical redistribution of sea ice',
    'properties': [
        ('horizontal_transport_method', 'ENUM:transport_methods', '0.1',
            "Method of horizontal advection"),
        ('transport_in_thickness_method', 'ENUM:transport_methods', '0.1',
            "Method of ice migration in thickness space"),
        ('ice_strength_formulation_method', 'str', '1.1',
             "Describe how ice-strength is formulated"),
        ('ice_redistribution_processes', 'ENUM:redistribution_types', '0.N',
             "Additional processes which can redistribute sea ice."),
        ('ice_deformation_method', 'ENUM:rheology_types', '1.1',
             "Ice deformation method")
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['transport_methods'] = {
    'description': 'Transport Methods',
    'is_open': True,
    'members': [
        ('Incremental Re-mapping', '(including Semi-Lagrangian)'),
        ('Prather', None),
        ('Eulerian', None),
    ]
}

ENUMERATIONS['redistribution_types'] = {
    'description':'Sea Ice Redistribution Types',
    'is_open': True,
    'members': [
        ('Rafting', None),
        ('Ridging', None),
    ]
}

ENUMERATIONS['rheology_types'] = {
    'description': 'Sea Ice rheology types',
    'is_open': True,
    'members': [
        ('free-drift', None),
        ('Mohr-Coloumb', None),
        ('visco-plastic', 'VP'),
        ('elastic-visco-plastic', 'EVP'),
        ('Elastic-aniostropic-plastic', None,),
        ('granular', None),
        ('other', None)
    ]
}


