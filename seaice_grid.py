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
    'properties': [],
    'detail_sets': [
        'horizontal',
        'vertical',
        ]
    }

DETAILS['discretisation:horizontal'] = {
    'description': 'Sea ice discretisation',
    'properties': [
        ('grid', 'ENUM:horizontal_grid', '1.1',
            "Grid on which sea ice is horizontal discretised?"),
        ('grid_type', 'ENUM:grid_structure', '1.1',
            "What is the type of sea ice grid?"),
        ('scheme', 'ENUM:numerical_scheme', '1.1',
            "What is the advection scheme?"),
        ('thermodynamics_time_step', 'int', '1.1',
            "What is the time step in the sea ice model thermodynamic component in seconds."),
        ('dynamics_time_step', 'int', '1.1',
            "What is the time step in the sea ice model dynamic component in seconds."),
        ('additional_details', 'str', '0.1',
            "Specify any additional horizontal discretisation details.")
        ]
    }

DETAILS['discretisation:vertical'] = {
    'description': 'Sea ice discretisation',
    'properties': [
        ('layering', 'ENUM:vertical_layering', '1.N',
            "What type of sea ice vertical layers are implemented?"),
        ('multi-layers', 'str', '1.1',
            "If using multi-layers specify how many."),
        ('additional_details', 'str', '0.1',
            "Specify any additional vertical discretisation details.")
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
        ('has_ice_types', 'bool', '1.1',
            "Set to True if using ice types rather than ice thickness categories."),
        ('ice_types_details', 'str', '1.1',
            "If using ice types specify any additional details."),
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
            "Number of vertical levels of snow on ice ?"),
        ('assumed_snow_fraction', 'str', '0.1',
            "Describe the assumed snow fraction on ice."),
        ('additional_details', 'str', '0.1',
            "Specify any additional details related to snow on ice.")
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['horizontal_grid'] = {
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

ENUMERATIONS['vertical_layering'] = {
    'description': 'Sea ice layering types',
    'is_open': True,
    'members': [
        ('zero-layer',
            'Simulation has no internal ice thermodynamics.'),
        ('2-levels',
            'Simulation uses two layers.'),
        ('Multi-level',
            'Simulation uses more than two layers'),
       ]
    }

ENUMERATIONS['numerical_scheme'] = {
    'description': 'Numerical scheme',
    'is_open': True,
    'members': [
        ('Finite differences', None),
        ('Finite elements', None),
        ('Finite volumes',  None),
       ]
    }

ENUMERATIONS['grid_structure'] = {
    'description': 'Numerical scheme',
    'is_open': True,
    'members': [
        ('Structured grid', None),
        ('Unstructured grid', None),
       ]
    }