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
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS['general'] = {
    'description': 'General properties of sea ice thermodynamics',
    'properties': [
        ('therm_budget', 'str', '0.1',
            "What information required to close the thermodynamics budget?"),
        ('additional_processes', 'str', '0.1',
            "List any additional processes not elsewhere described")
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Ice thermodynamic processes.
# --------------------------------------------------------------------
SUB_PROCESSES['ice_processes'] = {
    'description': 'Thermodynamic processes in sea ice',
    'properties': [
        ('basal_heat_flux', 'ENUM:basal_heat_flux_method', '0.1',
            "Method by which basal heat flux is handled"),
        ('new_ice_formation_method', 'str', '1.1',
            "Method by which new sea ice is formed"),
        ('ice_lateral_melting_method', 'str', '1.1',
            "Method of sea ice lateral melting"),
        ('ice_surface_sublimation_method', 'str', '1.1',
            "Method sea ice surface sublimation"),
        ('frazil_ice_method', 'str', '1.1',
            "Method of including frazil ice"),
        ]
    }

SUB_PROCESSES['ice_processes:brine'] = {
    'description': 'Information about brine inclusions',
    'properties': [
        ('inclusion_method', 'ENUM:thermo_brine_types', '0.1',
            "Method by which basal heat flux is handled"),
        ('fixed_salinity_value', 'float', '0.1',
            """If you have selected "Thermal properties depend on S-T (with fixed salinity)
               please supply the fixed salinity value for each sea ice layer."""),
        ]
    }

SUB_PROCESSES['ice_processes:vertical_heat_diffusion'] = {
    'description': 'Characteristics of vertical heat diffusion in sea ice.',
    'properties': [
        ('is_single_layer', 'bool', '0.1',
            "Is there a single layer for vertical heat diffusion?"),
        ('is_multi_layer', 'bool', '0.1',
            "Are there multiple layers for vertical heat diffusion?"),
        ('number_of_layers', 'int', '1.1',
            "If there are multiple layers for vertical heat diffusion specify how many ?"),
        ('regular_grid', 'bool', '0.1',
            "If multiple layers, are they regularly distributed ?"),
        ('is_based_on_semtner', 'bool', '1.1',
            "Is method based on Semtner 1976 ?")
        ]
    }

SUB_PROCESSES['ice_processes:melt_ponds'] = {
    'description': 'Characteristics of melt ponds.',
    'properties': [
        ('are_included', 'bool', '1.1',
            "Are melt ponds included in sea ice model?"),
        ('formulation_method', 'str', '0.1',
            "Method by which melt ponds are included"),
        ('processes', 'ENUM:melt_pond_proc', '0.N',
            "Processes included in melt pond scheme ?")
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Snow thermodynamic processes.
# --------------------------------------------------------------------
SUB_PROCESSES['snow_processes'] = {
    'description': 'Thermodynamic processes in snow on sea ice',
    'properties': [
        ('process_type', 'ENUM:snow_process_types', '1.N',
            "Snow processes in sea ice thermodynamics"),
        ('heat_content_precip', 'str', '0.1',
            "Method by which the heat content of precipitation is handled ?")
    ],
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
