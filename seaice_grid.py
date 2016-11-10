"""A realm grid sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# Default process details pulled from CIM.
#DETAILS['CIM'] = {
#    'description': 'Key properties of the sea ice grid',
#    'properties':[
#        ('implementation_overview', 'str', '1.1',
#            "General overview description of the implementation of this part of the process."),
#        ('keywords', 'str', '0.N',
#            "Keywords to help re-use and discovery of this information."),
#        ('citations', 'shared.citation', '0.N',
#            "Set of pertinent citations."),
#    ]
# }

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
AUTHORS = 'Ruth Petrie'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# GRID: DETAILS
#
# Sets of details for the grid
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# DISCRETISATION: Description of the numerics of the discretisation.
# --------------------------------------------------------------------
DETAILS['discretisation'] = {
    'description': 'Types of sea ice discretisation',
    'details': [
        'horizontal',
        'layering'
        ]
}

DETAILS['discretisation:horizontal'] = {
    'description': 'How the sea ice is horizontally discretised',
    'properties': [
        ('horizontal', 'ENUM:sea_ice_grid', '1.1',
            'Type of sea` ice horizontal discretisation'),
        ('Additional grid details', 'str', '0.1',
            'Specify any additional grid details')
    ]
}

DETAILS['discretisation:layering'] = {
    'description': 'Method used to represent sea ice layering',
    'properties': [
        ('layering_type', 'ENUM:layering_types', '0.N',
            'Type of sea` ice layering'),
    ]
}

DETAILS['seaice_categories'] = {
    'description': 'Method used to represent sea ice categories',
    'properties': [
        ('Number of sea ice categories', 'str', '0.1', 'If using multiple sea ice category specify how many'),
        ('Sea ice category limits', 'str', '0.1', 'If using multiple sea ice categories specify the category limits'),
        ('Sea ice thickness distribution scheme', 'str', '0.1', 'If applicable describe the sea ice thickness distribution scheme'),
    ]
}

DETAILS['snow_on_seaice'] = {
    'description': 'Method used to represent snow on sea ice',
    'properties': [
        ('Snow on yes', 'str', '0.1', 'Snow on ice'),
        ('Vertical levels of snow on ice', 'str', '0.1', 'Number of snow levels')
    ]
}

#-------------------------------------------------------
# GRID: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['sea_ice_grid'] = {
    'description': 'Grid which is the sea ice horizontally discretised on',
    'is_open': True,
    'members': [
        ('Ocean grid', 'Sea ice is horizontally discretised on the ocean grid'),
        ('Atmosphere Grid', 'Sea ice is horizontally discretised on the atmospheric grid'),
        ('Own Grid', 'Sea ice is horizontally discretised on it`s own independent grid'),
    ]
}
ENUMERATIONS['layering_types'] = {
    'description': 'Sea ice layering types',
    'is_open': True,
    'members': [
        ('zero-layer', 'Simulation has no internal ice thermodynamics.'),
        ('2-levels', 'Simulation uses two layers.'),
        ('Multi-level', 'Simulation uses more than two layers'),
        ('ice types', 'Simulation does not use layers, but has multiple ice types per grid cell'),
    ]
}
