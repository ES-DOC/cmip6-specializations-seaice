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
    'description': 'Type of discretisation scheme in ocean',
    'details': ['type']
}

# --------------------------------------------------------------------
# GRID: DISCRETISATION DETAILS
#
# Sets of details for the discretisation
# --------------------------------------------------------------------
DISCRETISATION_DETAILS = OrderedDict()

DISCRETISATION_DETAILS['type'] = {
    'description': 'NEEDS DESCRIPTION',
    'properties': [
        ('layering_type', 'ENUM:layering_types', '1.1',
            'Type of sea` ice layering')
    ]
}

#-------------------------------------------------------
# GRID: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['layering_types'] = {
    'description': 'Sea ice layering types',
    'is_open': True,
    'members': [
        ('2-levels', 'Simulation uses two layers.'),
        ('Multi-level', 'Simulation uses more than two layers'),
        ('Ice-Types', 'Simulation does not use layers, but has multiple ice types per grid cell'),
    ]
}
