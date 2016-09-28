"""A realm key-properties sepecialization.
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
# KEY PROPERTIES
#
# High level list of key properties.
# --------------------------------------------------------------------
DESCRIPTION = 'Key properties of sea ice'

IMPLEMENTATION_OVERVIEW = ('str', '1.1', "General overview description of the implementation of this part of the process.")

KEYWORDS = ('str', '0.1', "keywords to help re-use and discovery of this information.")
#TODO is this needed for sea ice
TIME_STEP = ('float', '0.1', "Timestep (in seconds) of overall component.")

CITATIONS = ('shared.citation', '0.N', "Set of pertinent citations."),

# --------------------------------------------------------------------
# KEY PROPERTIES: DETAILS
#
# Sets of details for the key properties
# --------------------------------------------------------------------
DETAILS = OrderedDict()
#TODO check if model family needed for sea ice
DETAILS['general'] = {
    'description': 'General key properties in sea ice',
    'properties': [
        ('model_family', 'ENUM:model_family_types', '1.1',
            'Type of sea ice model.'),
        ('basic_approximations', 'ENUM:seaice_basic_approx_types', '1.N',
            'Basic approximations made in the ice.',),
        ('prognostic_variables', 'ENUM:prognostic_vars_types', '1.N',
            'List of prognostic variables in the sea ice component.'),
        ]
}

#TODO adapt correctly to sea ice

DETAILS['seawater_properties'] = {
    'description': 'Physical properties of seawater relevant to sea ice',
    'properties' : [
        ('eos_type', 'ENUM:seawater_eos_types', '1.1',
            'Type of EOS for sea water'),
        ('eos_functional_temp', 'ENUM:seawater_eos_func_temp', '1.1',
            'Temperature used in EOS for sea water'),
        ('eos_functional_salt', 'ENUM:seawater_eos_func_salt', '1.1',
            'Salinity used in EOS for sea water'),
        ('eos_functional_depth', 'ENUM:seawater_eos_func_depth', '1.1',
            'Depth or pressure used in EOS for sea water ?'),
        ('ocean_freezing_point', 'ENUM:seawater_freezing_point', '1.1',
            'Equation used to compute the freezing point (in deg C) of seawater, as a function of salinity and pressure'),
        ('ocean_specific_heat', 'float', '1.1',
            'Specific heat in ocean (cpocean) in J/(kg K)'),
        ('ocean_reference_density', 'float', '1.1',
            'Boussinesq reference density (rhozero) in kg / m3'),
        ]
}

#TODO adapt correctly to sea ice

#DETAILS['nonoceanic_waters'] = {
#    'description': 'Non oceanic waters treatement in ocean',
#    'properties': [
#        ('isolated_seas','str', '0.1',
#         'Describe if/how isolated seas is performed'),
#        ('river_mouth','str', '0.1',
#         'Describe if/how river mouth mixing or estuaries specific treatment is performed'),
#       ]
#}
#

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTENT
#
# <DESCRIPTION NEEDED>
# --------------------------------------------------------------------
EXTENT = OrderedDict()

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTENT DETAILS
#
# Sets of details for the extent.
# --------------------------------------------------------------------
EXTENT_DETAILS = OrderedDict()

# --------------------------------------------------------------------
# KEY PROPERTIES: RESOLUTION
#
# The resolution of the grid.
# --------------------------------------------------------------------
RESOLUTION = OrderedDict()

#TODO adapt correctly to sea ice
RESOLUTION['resolution'] = {
    'description': 'Resolution in the sea ice grid',
    'properties': [
        ('name', 'str', '1.1',
             "This is a string usually used by the modelling group to describe the resolution of this grid, e.g. N512L180 or T512L70 etc."),
        ('canonical_horizontal_resolution', 'str', '0.1',
             "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '0.1',
             "Total number of horizontal (XY) points (or degrees of freedom) on computational grid."),
        ('is_adaptive_grid', 'bool', '0.1',
             "Default is False. Set true if grid resolution changes during execution."),
        ('citations', 'str', '0.N',
             "Set of pertinent citations."), 
        ],
    # Sets of extra properties
    'details': [ 
        'thickness_level_1',
    ],
}

# --------------------------------------------------------------------
# KEY PROPERTIES: RESOLUTION DETAILS
#
# Sets of details for the resolution
# --------------------------------------------------------------------
RESOLUTION_DETAILS = OrderedDict()

RESOLUTION_DETAILS['thickness_level_1'] = (
    'float', '1.1', 'Thickness of first surface ocean level (in meters)')

# --------------------------------------------------------------------
# KEY PROPERTIES: TUNING APPLIED
#
# Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
TUNING_APPLIED = OrderedDict()

# TODO review wrt toplevel tuning questions !!
# TODO not sure it is right to have data.variable.collection in the following - should be free text
TUNING_APPLIED['tuning_applied'] = {
    'description': 'Tuning applied to sea ice component',
    'properties': [
        ('description', 'str', '1.1',
             "General overview description of tuning."),
        ('tuning target', 'str', '1.1',
             "What was the aim of tuning, e.g. correct sea ice minima, correct seasonal cycle etc."),
        ('tuning simulations', 'str', '1.1',
             "Which simulations had tuning applied, e.g. all, not historical, only pi-control? "),
        ('tuning_metrics_used', 'str', '1.1',
             "Which metrics have been used in tuning model parameters."),
        ('citations', 'shared.citation', '0.N',
             "Set of pertinent citations."), 
    ],
    # Extra properties
    'details': [],
}

# --------------------------------------------------------------------
# KEY PROPERTIES: TUNING APPLIED DETAILS
#
# Sets of details for the tuning
# --------------------------------------------------------------------
TUNING_APPLIED_DETAILS = OrderedDict()

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTRA CONSERVATION PROPERTIES
#
# Details of methodology needed to conserve variables between
# processes
# --------------------------------------------------------------------
EXTRA_CONSERVATION_PROPERTIES = OrderedDict()

#TODO adapt correctly to sea ice
EXTRA_CONSERVATION_PROPERTIES['conservation'] = {
    'description': 'Conservation in the sea ice component',
    'properties': [
        ('description', 'str', '1.1', 'Brief description of conservation methodology'),
        ('corrected_conserved_prognostic_variables', 'data.variable_collection', '0.1', # Can we constrains these variable
             "Set of variables which are conserved by *more* than the numerical scheme alone."),
        ('flux_correction_was_used', 'bool', '0.1',
             "Does conservation involved flux correction ?"),
        ('citations', 'shared.citation', '0.N',
             "Set of pertinent citations."), 
    ],
    # Extra properties
    'details': ['details'],
}

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTRA CONSERVATION PROPERTIES DETAILS
#
# Sets of details for the conservation
# --------------------------------------------------------------------
EXTRA_CONSERVATION_PROPERTIES_DETAILS = OrderedDict()
#TODO is this needed for sea ice
EXTRA_CONSERVATION_PROPERTIES_DETAILS['details'] = {
    'description': 'Extra properties of conservation in the ocean component',
    'properties': [
        ('scheme', 'ENUM:conservation_props_types', '1.N',
            'Properties conserved in the ocean by the numerical schemes'),
        ('consistency_properties', 'str','0.1',
            'Any additional consistency properties (energy conversion, pressure gradient discretisation, ...)?'),
    ]
}

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

#TODO is this needed for sea ice
ENUMERATIONS['model_family_types'] = {
    'description': 'Types of sea ice models',
    'is_open': True,
    'members': [
        ('OGCM', None),
        ('slab ocean', None),
        ('mixed layer ocean', None)
    ]
}

#TODO check which are correct for sea ice
ENUMERATIONS['seaice_basic_approx_types'] = {
    'description': 'Types of basic approximation in sea ice',
    'is_open': True,
    'members': [
        ('Isotropic', None),
        ('Primitive equations', None),
        ('Non-hydrostatic', None),
        ('Boussinesq', None)
    ]
}

#TODO update for sea ice
ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'List of prognostic variables in sea ice',
    'is_open': True,
    'members': [
        ('Potential temperature', None),
        ('Conservative temperature', None),
        ('Salinity', None),
        ('U-velocity', None),
        ('V-velocity', None),
        ('W-velocity', None),
        ('SSH', 'Sea Surface Height')
    ]
}

#TODO is this needed for sea ice
ENUMERATIONS['seawater_eos_types'] = {
    'description': 'Types of seawater Equation of State in ocean',
    'is_open': True,
    'members': [
        ('Linear', None),
        ('Mc Dougall et al.', None),
        ('Jackett et al. 2006', None),
        ('TEOS 2010', None)
        ]
}

#TODO is this needed for sea ice
ENUMERATIONS['seawater_eos_func_temp'] = {
    'description': 'Types of temperature used in EOS in ocean',
    'is_open': False,
    'members': [
        ('Potential temperature', None),
        ('Conservative temperature', None),
        ]
}

#TODO is this needed for sea ice
ENUMERATIONS['seawater_eos_func_salt'] = {
    'description': 'Types of salinity used in EOS in ocean',
    'is_open': False,
    'members': [
        ('Practical salinity Sp', None),
        ('Absolute salinity Sa', None),
        ]
}

#TODO is this needed for sea ice
ENUMERATIONS['seawater_eos_func_depth'] = {
    'description': 'Types of depth used in EOS in ocean',
    'is_open': False,
    'members': [
        ('Pressure (dbars)', None),
        ('Depth (meters)', None),
        ]
}

#TODO is this needed for sea ice
ENUMERATIONS['seawater_freezing_point'] = {
    'description': 'Types of seawater freezing point equation in sea ice',
    'is_open': True,
    'members': [
        ('TEOS 2010', None)
        ]
}

#TODO check salt and freshwater should be here
ENUMERATIONS['conservation_props_types'] = {
    'description': 'List of properties that can be conserved in sea ice',
    'is_open': True,
    'members': [
        ('Energy', None),
        ('Mass', None),
        ('Salt', None),
        ('Freshwater', None),
        ]
}