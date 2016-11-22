"""
A realm key-properties sepecialization.
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
DESCRIPTION = 'Sea Ice key properties'

# --------------------------------------------------------------------
# GENERAL details.
# --------------------------------------------------------------------
# TODO check if model family needed for sea ice
DETAILS['general'] = {
    'description': "General key properties in sea ice",
    'properties': [
        #        ('basic_approximations', 'ENUM:seaice_basic_approx_types', '0.N',
        #    "Basic approximations made in the ice."),
        ('prognostic_variables', 'ENUM:prognostic_vars_types', '1.N',
            "List of prognostic variables in the sea ice component."),
        ]
    }

DETAILS['seawater_properties'] = {
    'description': "Physical properties of seawater relevant to sea ice",
    'properties': [
        ('ocean_freezing_point', 'ENUM:seawater_freezing_point', '1.1',
            "Equation used to compute the freezing point (in deg C) of seawater, as a function of salinity and pressure"),
        ('ocean_freezing_point_value', 'float', '0.1',
            "If using a constant seawater freezing point, specify this value."),
        ]
    }

# --------------------------------------------------------------------
# RESOLUTION: Description of the resolution in the sea ice grid.
# --------------------------------------------------------------------
DETAILS['resolution'] = {
    'description': "Resolution in the sea ice grid",
    'properties': [
        ('name', 'str', '1.1',
          """This is a string usually used by the modelling group to describe the resolution of this grid
               e.g. N512L180, T512L70, ORCA025 etc."""),
        ('canonical_horizontal_resolution', 'str', '0.N',
            "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc."),
        ('number_of_horizontal_gridpoints', 'int', '0.1',
            "Total number of horizontal (XY) points (or degrees of freedom) on computational grid."),
        ('is_adaptive_grid', 'bool', '0.1',
            "Default is False. Set true if grid resolution changes during execution."),
        ]
    }

# --------------------------------------------------------------------
# TUNING APPLIED: Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': "Tuning applied to sea ice model component",
    'properties': [
        ('description', 'str', '1.1',
            """General overview description of tuning: explain and motivate the main targets and metrics retained.
               Document the relative weight given to climate performance metrics versus process oriented metrics,
               and on the possible conflicts with parameterization level tuning. In particular describe any struggle
               with a parameter value that required pushing it to its limits to solve a particular model deficiency."""),
        ('target', 'str', '0.1',
            "What was the aim of tuning, e.g. correct sea ice minima, correct seasonal cycle."),
        ('simulations', 'str', '0.1',
            "Which simulations had tuning applied, e.g. all, not historical, only pi-control? "),
        ('metrics_used', 'str', '0.1',
            "List any observed metrics used in tuning model/parameters"),
        ('variables', 'str', '0.1',
             "Which variables were changed during the tuning process."),
        ]
    }

# --------------------------------------------------------------------
# ASSUMPTIONS: Any key assumptions made in this realm
# --------------------------------------------------------------------
# TODO Check this section in detail with Alex Jahn

DETAILS['assumptions'] = {
    'description': "Assumptions made in the sea ice model",
    'properties': [
        ('description', 'str', '0.N',
            """General overview description of any key assumptions made in this model,
               particularly where this may affect the diagnostic sea ice variables."""),
        ('on_diagnostic_variables', 'str', '0.N',
            """General overview description of any key assumptions made in this model,
               particularly where this may affect the diagnostic sea ice variables."""),
        ('missing_processes', 'str', '0.N',
             "Are there any *key* processes missing in this model configuration that affect the diagnostic sea ice variables?"),
        ]
    }

# --------------------------------------------------------------------
# EXTRA CONSERVATION PROPERTIES: Details of methodology needed to conserve variables between processes
# --------------------------------------------------------------------
# TODO Check budget information

DETAILS['conservation'] = {
    'description': "Conservation in the sea ice component",
    'properties': [
        ('description', 'str', '1.1',
            "Description of conservation methodology"),
        ('properties', 'ENUM:conservation_props_types', '1.N',
            "Properties conserved in sea ice by the numerical schemes"),
        ('budget', 'str', '1.1',
            "For each conserved property, specify the output variables which close the related budget"),
        ('was_flux_correction_used', 'bool', '0.1',
            "Does conservation involved flux correction ?"),
        ('corrected_conserved_prognostic_variables', 'str', '0.N',
            "List any variables which are conserved by *more* than the numerical scheme alone."),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'List of prognostic variables in sea ice',
    'is_open': True,
    'members': [
        ('Sea ice Temperature', None),
        ('Sea ice concentration', None),
        ('Sea ice thickness', None),
        ('Sea ice U-velocity', None),
        ('Sea ice V-velocity', None),
        ('Internal ice stress', None),
        ('Salinity', None),
        ('Snow temperature', 'Snow on ice temperature'),
        ('Snow depth', 'Snow on ice thickness'),
    ]
}

ENUMERATIONS['seawater_freezing_point'] = {
    'description': 'Types of seawater freezing point equation in sea ice.',
    'is_open': True,
    'members': [
        ('TEOS XXX', None),
# todo check
        ('TEOS ', None),
        ('TEOS 2010', None),
        ('Constant', 'Constant value of seawater freezing point is used.'),
        ]
}

ENUMERATIONS['conservation_props_types'] = {
    'description': 'List of properties that can be conserved in sea ice',
    'is_open': True,
    'members': [
        ('Energy', None),
        ('Mass', None),
        ('Salt', None),
    ]
}
