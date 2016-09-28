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
            'Type of sea` ice horizontal discretisation')

    ]
}

DISCRETISATION_DETAILS['layering'] = {
    'description': 'Method used to represent sea ice layering',
    'properties': [
        ('layering_type', 'ENUM:layering_types', '1.1',
            'Type of sea` ice layering'),
        ('ice_types', 'ENUM:ice_types', '0.N',
            'Type of sea` ice categories')
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
        ('2-levels', 'Simulation uses two layers.'),
        ('Multi-level', 'Simulation uses more than two layers'),
        ('ice_types', 'Simulation does not use layers, but has multiple ice types per grid cell'),
    ]
}
ENUMERATIONS['ice_types'] = {
    'description': 'Detail of ice_types per grid cell',
    'is_open': True,
    'members': [
        ('Number of ice categories', None),
        ('Category limits',  None),
        ('Ice thickness distribution scheme', None),
    ]
}
