"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""

# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Ruth Petrie'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Ruth Petrie, Bryan Lawrence'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
#
# Scientific context of the process
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the Sea Ice Dynamics'

IMPLEMENTATION_OVERVIEW = ('str', '1.1', "General overview description of the implementation of this part of the process.")

KEYWORDS = ('str', '0.1', "keywords to help re-use and discovery of this information.")

CITATIONS = ('shared.citation', '0.N', "Set of pertinent citations."),

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['horizontal_advection'] = {
    'description': 'Method of horizontal advection',
    'details': ['transport_method']
}

SUB_PROCESSES['transport_in_thickness_space'] = {
    'description': 'Method of ice migration in thickness',
    'details': ['transport_method']
}

SUB_PROCESSES['redistribution'] = {
    'description': 'Sea Ice Mechanical Redistribution',
    'details': ['ice_redistribution']
}

SUB_PROCESSES['rheology'] = {
    'description': 'Sea ice deformation',
    'details': ['ice_deformation_method']
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['horizontal_advection:transport_method'] = {
    'description': 'Horizontal advection of sea ice',
    'properties': [
        ('transport_method', 'ENUM:transport_methods', '0.1',
             'Method of horizontal advection')
    ]
}

SUB_PROCESS_DETAILS['transport_in_thickness_space:transport_method'] = {
    'description': 'Method of migration of sea ice in thickness',
    'properties': [
        ('transport_method', 'ENUM:transport_methods', '0.1',
             'Method of ice migration in thickness')
    ]
}
       
SUB_PROCESS_DETAILS['redistribution:ice_redistribution'] = {
    'description': 'Methods of mechanical redistribution of sea ice',
    'properties': [
        ('processes', 'ENUM:redistribution_types', '0.N',
             'Additional processes which can redistribute sea ice.'),        
        ('ice_strength_formulation', 'str', '0.1',
             'Describe how ice-strength is formulated'),
    ]
}

SUB_PROCESS_DETAILS['rheology:ice_deformation_method'] = {
    'description': 'Methods of sea ice deformation',
    'properties': [
        ('ice_deformation_method', 'ENUM:rheology_types', '1.1',
             'Ice deformation method')
   ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['transport_methods'] = {
    'description': 'Transport Methods',
    'is_open': True,
    'members': [
        ('Incremental Re-mapping', '(including Semi-Lagrangian)'),
        ('Prather', None),
        ('Eulerian', None)
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
        ('visco-plastic', None),
        ('elastic-visco-plastic', 'EVP'),
        ('Elastic-aniostropic-plastic', None,),
        ('granular', None),
        ('other', None)
    ]
}


