"""A realm grid sepecialization.
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
AUTHORS = 'Ruth Petrie'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# GRID: DESCRIPTION
#
# Scientific context of the grid
# --------------------------------------------------------------------
DESCRIPTION = 'Sea ice grid and discretisation'

IMPLEMENTATION_OVERVIEW = ('str', '1.1', "General overview description of the implementation of this part of the process.")

KEYWORDS = ('str', '0.1', "keywords to help re-use and discovery of this information.")

CITATIONS = ('shared.citation', '0.N', "Set of pertinent citations."),

# --------------------------------------------------------------------
# GRID: DETAILS
#
# Sets of details for the grid
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# GRID: DISCRETISATION
#
# Description of the numerics of the discretisation
# --------------------------------------------------------------------
DISCRETISATION = OrderedDict()

DISCRETISATION['discretisation'] = {
    'description': 'Types of sea ice discretisation',
    'details': [
        'horizontal',
        'layering'
        ]
}

# --------------------------------------------------------------------
# GRID: DISCRETISATION DETAILS
#
# Sets of details for the discretisation
# --------------------------------------------------------------------
DISCRETISATION_DETAILS = OrderedDict()

DISCRETISATION_DETAILS['horizontal'] = {
    'description': 'How the sea ice is horizontally discretised',
    'properties': [
        ('horizontal', 'ENUM:sea_ice_grid', '1.1',
            'Type of sea` ice horizontal discretisation'),
        ('Additional grid details', 'str', '0.1',
            'Specify any additional grid details')

    ]
}

DISCRETISATION_DETAILS['layering'] = {
    'description': 'Method used to represent sea ice layering',
    'properties': [
        ('layering_type', 'ENUM:layering_types', '1.N',
            'Type of sea` ice layering'),
    ]
}

DISCRETISATION_DETAILS['Sea ice categories'] = {
    'description': 'Method used to represent sea ice layering',
    'properties': [
        ('Number of sea ice categories', 'str', '0.1', 'If using multiple sea ice category specify how many'),
        ('Sea ice category limits', 'str', '0.1', 'If using multiple sea ice categories specify the category limits'),
        ('Sea ice thickness distribution scheme', 'str', '0.1', 'If applicable describe the sea ice thickness distribution scheme'),        
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
        ('snow layer', 'Simulation has at least one snow layer'),
    ]
}
