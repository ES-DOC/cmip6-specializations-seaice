"""A realm grid sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Ruth Petrie'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Ruth Petrie'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Sea Ice grid'

# --------------------------------------------------------------------
# DISCRETISATION: Description of the numerics of the discretisation.
# --------------------------------------------------------------------
DETAILS['discretisation'] = {
    'description': 'Sea ice discretisation',
    'properties': [
        ('layering_type', 'ENUM:layering_types', '1.N',
            "What method is used to represent sea ice layering ?"),
        ]
    }

DETAILS['discretisation:horizontal'] = {
    'description': 'How the sea ice is horizontally discretised?',
    'properties': [
        ('horizontal', 'ENUM:sea_ice_grid', '1.1',
            "Type of sea ice horizontal discretisation ?"),
        ('additional_details', 'str', '0.1',
            "Specify any additional grid discretisation details.")
        ]
    }

# --------------------------------------------------------------------
# SEAICE-CATEGROIES: Description of method used to represent sea ice categories.
# --------------------------------------------------------------------
DETAILS['seaice_categories'] = {
    'description': 'What method is used to represent sea ice categories ?',
    'properties': [
        ('number_of_categories', 'str', '0.1',
            "If using multiple sea ice categories specify how many."),
        ('category_limits', 'str', '0.1',
            "If using multiple sea ice categories specify the category limits."),
        ('thickness_distribution_scheme', 'str', '0.1',
            "If applicable describe the sea ice thickness distribution scheme"),
        ]
    }

# --------------------------------------------------------------------
# ??? .
# --------------------------------------------------------------------
DETAILS['snow_on_seaice'] = {
    'description': 'Method used to represent snow on sea ice',
    'properties': [
        ('has_snow_on_ice', 'bool', '1.1',
            "Is snow on ice represented in this model ?"),
        ('number_of_snow_levels', 'str', '0.1',
            "Number of vertical levels of snow on ice ?")
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['sea_ice_grid'] = {
    'description': 'Grid which is the sea ice horizontally discretised on?',
    'is_open': True,
    'members': [
        ('Ocean grid',
            'Sea ice is horizontally discretised on the ocean grid'),
        ('Atmosphere Grid',
            'Sea ice is horizontally discretised on the atmospheric grid'),
        ('Own Grid',
            'Sea ice is horizontally discretised on it`s own independent grid'),
        ]
    }

ENUMERATIONS['layering_types'] = {
    'description': 'Sea ice layering types',
    'is_open': True,
    'members': [
        ('zero-layer',
            'Simulation has no internal ice thermodynamics.'),
        ('2-levels',
            'Simulation uses two layers.'),
        ('Multi-level',
            'Simulation uses more than two layers'),
        ('ice types',
            'Simulation does not use layers, but has multiple ice types per grid cell'),
        ]
    }
