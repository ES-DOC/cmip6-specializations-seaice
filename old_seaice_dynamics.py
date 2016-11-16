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

# Default process details pulled from CIM.
DETAILS['CIM'] = {
    'description': 'Key properties of sea ice dynamics',
    'properties': [
        ('implementation_overview','str', '1.1',
            "General overview description of the implementation of this part of the process."),
        ('keywords','str', '0.N',
            "Keywords to help re-use and discovery of this information."),
        ('citations','shared.citation', '0.N',
            "Set of pertinent citations."),
    ]
}

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
# DESCRIPTION
#
# Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Sea Ice Dynamics'

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

SUB_PROCESSES['seaice_dynamics'] = {
    'description': 'Methods of mechanical redistribution of sea ice',
    'detail_sets': ['horizontal_transport',
                    'transport_in_thickness',
                    'ice_strength_formulation',
                    'ice_redistribution',
                    'ice_deformation',
                   ]
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESSES['seaice_dynamics:horizontal_transport'] = {
    'description': 'Horizontal advection of sea ice',
    'properties': [
        ('horizontal_transport_method', 'ENUM:transport_methods', '0.1',
         'Method of horizontal advection')
    ]
}

SUB_PROCESSES['seaice_dynamics:transport_in_thickness'] = {
    'description': 'Method of migration of sea ice in thickness',
    'properties': [
        ('transport_in_thickness_method', 'ENUM:transport_methods', '0.1',
         'Method of ice migration in thickness space')
    ]
}

SUB_PROCESSES['seaice_dynamics:ice_strength_formulation'] = {
    'description': 'How the sea ice strength is formulated',
    'properties': [
        ('ice_strength_formulation_method', 'str', '1.1',
         'Describe how ice-strength is formulated'),
    ]
}

SUB_PROCESSES['seaice_dynamics:ice_redistribution'] = {
    'description': 'Methods of mechanical redistribution of sea ice',
    'properties': [
        ('ice_redistribution_processes', 'ENUM:redistribution_types', '0.N',
         'Additional processes which can redistribute sea ice.'),
    ]
}

SUB_PROCESSES['seaice_dynamics:ice_deformation'] = {
    'description': 'Methods of sea ice deformation',
    'properties': [
        ('ice_deformation_method', 'ENUM:rheology_types', '1.1',
         'Ice deformation method')
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

