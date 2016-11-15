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
    'description': 'Key properties of the sea ice thermodynamics',
    'properties':[
        ('implementation_overview','str', '1.1',
            "General overview description of the implementation of this part of the process."),
        ('keywords', 'str', '0.N',
            "Keywords to help re-use and discovery of this information."),
        ('citations', 'shared.citation', '0.N',
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
DESCRIPTION = 'Sea Ice Thermodynamics'

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES['thermo_budget'] = {
    'description': 'Closing the thermodynamics budget',
    'details': ['details'],
}

SUB_PROCESSES['ice_thermo_processes'] = {
    'description': 'Thermodynamic processes in sea ice',
    'detail_sets': [
        'brine',
        'basal_heat_flux',
        'vertical_heat_diffusion',
        'melt_ponds',
        'new_ice_formation',
        'ice_lateral_melting',
        'ice_surface_sublimation',
        'ice_radiation_transmission',
        'frazil_ice',
    ],
}

SUB_PROCESSES['snow_thermo_processes'] = {
    'description': 'Thermodynamic processes in snow on sea ice',
    'details': ['process_type'],
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
SUB_PROCESSES['thermo_budget:details'] = {
    'description': 'Closing the thermodynamics budget',
    'properties': [
        ('therm_budget', 'str', '0.1',
         'What information required to close the thermodynamics budget?'),
    ]
}

SUB_PROCESSES['ice_thermo_processes:brine'] = {
    'description': 'Information about brine inclusions',
    'properties': [
        ('brine_inclusion_method', 'ENUM:thermo_brine_types', '0.1',
         'Method by which basal heat flux is handled'),
        ('fixed_salinity_value', 'float', '0.1',
         'If you have selected "Thermal properties depend on S-T (with fixed salinity)" &'
         'please supply the fixed salinity value for each sea ice layer.'),
    ]
}

SUB_PROCESSES['ice_thermo_processes:basal_heat_flux'] = {
    'description': 'Information about basal heat flux',
    'properties': [
        ('basal_heat_flux', 'ENUM:basal_heat_flux_method', '0.1',
         'Method by which basal heat flux is handled'),
     ]
}

SUB_PROCESSES['ice_thermo_processes:vertical_heat_diffusion'] = {
    'description': 'Characteristics of vertical heat diffusion in sea ice.',
    'properties': [
        ('is_single_layer', 'bool', '0.1',
         'Is there a single layer for vertical heat diffusion?'),
        ('is_multi_layer', 'bool', '0.1',
         'Are there multiple layers for vertical heat diffusion?'),
        ('num_of_layers', 'int', '1.1',
         'If there are multiple layers for vertical heat diffusion specify how many?'),
        ('regular_grid', 'bool', '0.1',
         'If multiple layers, are they regularly distributed?'),
        ('based_on_semtner', 'bool', '1.1',
         'Is method based on Semtner 1976?')
    ]
}

SUB_PROCESSES['ice_thermo_processes:melt_ponds'] = {
    'description': 'Characteristics of melt ponds.',
    'properties': [
        ('melt_ponds_included', 'bool', '1.1',
         'Are melt ponds included in sea ice model?'),
        ('melt_pond_formulation', 'str', '0.1',
         'Method by which melt ponds are included'),
        ('melt_pond_processes', 'ENUM:melt_pond_proc', '0.N',
         'Processes included in melt pond scheme?')
    ]
}

SUB_PROCESSES['ice_thermo_processes:new_ice_formation'] = {
    'description': 'new sea ice formation',
    'properties': [
        ('new_ice_formation_method', 'str', '1.1', 'Method by which new sea ice is formed'),
    ]
}

SUB_PROCESSES['ice_thermo_processes:ice_lateral_melting'] = {
    'description': 'sea ice lateral melting',
    'properties': [
        ('ice_lateral_melting_method', 'str', '1.1', 'Method of sea ice lateral melting'),
    ]
}

SUB_PROCESSES['ice_thermo_processes:ice_surface_sublimation'] = {
    'description': 'surface sea ice sublimation',
    'properties': [
        ('ice_surface_sublimation_method', 'str', '1.1', 'Method sea ice surface sublimation'),
    ]
}

SUB_PROCESSES['ice_thermo_processes:frazil_ice'] = {
    'description': 'frazil ice',
    'properties': [
        ('frazil_ice_method', 'str', '1.1', 'Method of including frazil ice'),
    ]
}

# TODO where should the heat content of precipitiation go?
SUB_PROCESSES['snow_thermo_processes:process_type'] = {
    'description': 'Snow on ice processes',
    'properties': [
        ('process_type', 'ENUM:snow_process_types', '1.N',
         'Snow processes in sea ice thermodynamics'),
        ('heat_content_precip', 'str', '0.1',
         'Method by which the heat content of precipitation is handled?')
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

# TODO If fixed salinity want to ask what is the salinity constant used
# TODO Ask: Does the sea ice salinity impact the thermal properties of sea ice
ENUMERATIONS['thermo_brine_types'] = {
    'description': 'Brine inclusion methodology',
    'is_open': True,
    'members': [
        ('None', 'No brine inclusions included in sea ice thermodynamics'),
        ('Heat Reservoir', 'Brine inclusions treated as a heat reservoir'),
        ('Thermal Fixed Salinity', 'Thermal properties depend on S-T (with fixed salinity)'),
        ('Thermal Varying Salinity', 'Thermal properties depend on S-T (with varying salinity'),
    ]
}

ENUMERATIONS['basal_heat_flux_method'] = {
    'description': 'Basal heat flux methodology',
    'is_open': True,
    'members': [
        ('Prescribed', None),
        ('Parametrized in sea ice', None),
        ('Parametrized in ocean', None),
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

ENUMERATIONS['melt_pond_proc'] = {
    'description': 'Melt pond processes',
    'is_open': True,
    'members': [
        ('impact on albedo', None),
        ('latent heat flux', None),
        ('freshwater', None)
    ]
}

