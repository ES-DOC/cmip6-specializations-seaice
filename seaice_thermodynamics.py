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
DESCRIPTION = 'Characteristics of sea ice thermodynamics processes'

IMPLEMENTATION_OVERVIEW = ('str', '1.1', "General overview description of the implementation of this part of the process.")

KEYWORDS = ('str', '0.1', "keywords to help re-use and discovery of this information.")

CITATIONS = ('shared.citation', '0.N', "Set of pertinent citations."),

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['budget'] = (
    'str', '0.1',
    'Information required to close the thermodynamics budget')

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['thermo_processes'] = {
    'description': 'Information about basal heat flux and brine inclusions',
    'details': ['details'],
}

SUB_PROCESSES['snow_processes'] = {
    'description': 'Snow processes in sea ice thermodynamics',
    'details': ['process_type'],
}

SUB_PROCESSES['vertical_heat_diffusion'] = {
    'description': 'Characteristics of vertical heat diffusion in sea ice.',
    'details': ['details'],
}

SUB_PROCESSES['additional_processes'] = {
    'description': 'Additonal processes not elsewhere described',
    'details': ['details'],
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['thermo_processes:details'] = {
    'description': 'Information about basal heat flux and brine inclusions',
    'properties': [
        ('brine_inclusion_method', 'ENUM:thermo_brine_types', '0.1',
         'Method by which basal heat flux is handled'),
        ('fixed_salinity_value', 'float', '0.1',
        'If you have selected "Thermal properties depend on S-T (with fixed salinity)" please supply the salinity value used.'),
        ('basal_heat_flux', 'str', '0.1',
        'Method by which basal heat flux is handled'),
    ]
}

SUB_PROCESS_DETAILS['snow_processes:process_type'] = {
    'description': 'Snow on ice processes',
    'properties': [
        ('process_type', 'ENUM:snow_process_types', '1.N', 
             'Snow processes in sea ice thermodynamics'),
        ('heat_content_precip', 'str', '0.1',
         'Method by which the heat content of precipitation is handled')
    ]
}

SUB_PROCESS_DETAILS['vertical_heat_diffusion:details'] = {
    'description': 'Characteristics of vertical heat diffusion in sea ice.',
    'properties': [
        ('num_of_layers', 'int', '1.1',
         'Number of layers used for vertical heat diffusion'),
        ('regular_grid', 'bool', '0.1',
         'If multiple layers, are they regularly distributed?'),
        ('based_on_semtner', 'bool', '1.1',
         'Is method based on Semtner 1976?')
    ]
}

SUB_PROCESS_DETAILS['melt_ponds:details'] = {
    'description': 'Characteristics of melt ponds.',
    'properties': [
        ('melt_ponds_included', 'bool', '1.1',
         'Are melt ponds included in sea ice model?'),
        ('melt_pond_formulation', 'str', '0.1',
         'Method by which melt ponds are included'),
        ('melt_pond_processes', 'enum:melt_pond_proc', '0.N',
         'Processes included in melt pond scheme')
    ]
}



# TODO these should be incorporated within other processes
SUB_PROCESS_DETAILS['additional_processes:details'] = {
    'description': 'Additonal processes not elsewhere described',
    'properties': [
        ('processes', 'ENUM:add_processes', '0.N',
         'Additional processes')
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

# TODO If fixed salinity want to ask what is the salinity constant used
# TODO Ask: Does the sea ice salinity impact the thermal properties of sea ice
ENUMERATIONS['thermo_brine_types'] = {
    'description': 'Brine Inclusion Methodology',
    'is_open': True,
    'members': [
        ('None', 'No brine inclusions included in sea ice thermodynamics'),
        ('Heat Reservoir', 'Brine inclusions treated as a heat reservoir'),
        ('Thermal Fixed Salinity', 'Thermal properties depend on S-T (with fixed salinity)'),
        ('Thermal Varying Salinity', 'Thermal properties depend on S-T (with varying salinity'),
    ]
}

# TODO Find out if snow redistribution schemes are implemented if so maybe need a separate
# sub process
ENUMERATIONS['snow_process_types'] = {
    'description': 'Types of snow processes',
    'is_open': True,
    'members': [
        ('single-layered heat diffusion', None),
        ('multi-layered heat diffusion', None),
        ('snow aging scheme', None),
        ('snow ice scheme', None),
        ('snow redistribution scheme', 'Is there a scheme to redistribute snow on sea ice by wind or melting processes?'),
    ]
}

ENUMERATIONS['add_processes'] = {
    'description': 'Additional processes',
    'is_open': True,
    'members': [
        ('New ice formation', None),
        ('Ice lateral melting', None),
        ('Ice surface sublimation', None),
        ('Ice radiation transmission', None),
        ('Frazil ice', None),
    ]
}

ENUMERATIONS['melt_pond_proc'] = {
    'description': 'Melt pond processes',
    'is_open': True,
    'members': [
        ('impact on albedo', None),
        ('latent heat flux', None),
        ('freshwater', None)
    ]
}

