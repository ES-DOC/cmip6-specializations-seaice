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
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Ruth Petrie'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Ruth Petrie, Bryan Lawrence'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Sea Ice Thermodynamics'

# --------------------------------------------------------------------
# DETAILS : General process details.
# --------------------------------------------------------------------
"""
DETAILS['general'] = {
    'description': 'General properties of sea ice thermodynamics',
    'properties': [
        ]
    }
"""
# --------------------------------------------------------------------
# SUB-PROCESS: Ice thermodynamic processes.
# --------------------------------------------------------------------
SUB_PROCESSES['energy'] = {
    'description': 'Energy conservation in sea ice thermodynamics',
    'properties': [
        ('enthalpy_formulation', 'ENUM:energy_formulation', '1.1',
            "Formulation of energy conservation"),
        ('thermal_conductivity', 'ENUM:thermal_conductivity_type', '1.1',
            "Method of thermal conductivity"),
        ('heat_diffusion', 'ENUM:heat_diffusion_type', '1.N',
            "Method of heat diffusion"),
        ('basal_heat_flux', 'ENUM:basal_heat_flux_method', '0.1',
            "Method by which basal ocean heat flux is handled"),
        ('fixed_salinity_value', 'float', '0.1',
         """If you have selected "Thermal properties depend on S-T (with fixed salinity)
            please supply the fixed salinity value for each sea ice layer."""),
        ('heat_content_precip', 'str', '1.1',
         "Method by which the heat content of precipitation is handled ?")
    ]
    }


SUB_PROCESSES['mass'] = {
    'description': 'Mass conservation in sea ice thermodynamics',
    'properties': [
        ('new_ice_formation', 'str', '1.1',
             "Method by which new sea ice is formed in open water"),
        ('ice_vertical_growth_and_melt', 'str', '1.1',
             "Method describing the vertical growth and melt of sea ice."),
        ('ice_surface_sublimation', 'str', '1.1',
             "Method sea ice surface sublimation"),
        ('frazil_ice', 'str', '1.1',
             "Method of frazil ice formation"),
        ('ice_lateral_melting', 'ENUM:lateral_melting_types', '1.1',
             "Method of sea ice lateral melting"),
        ]
    }

SUB_PROCESSES['salt'] = {
    'description': 'Salt conservation in sea ice thermodynamics.',
    'properties': [
        ('has_multiple_sea_ice_salinities', 'bool', '1.1',
         """Does your model use two different salinities for thermodynamic
         calculations and for the salt budget?"""),
        ('sea_ice_salinity_thermal_impacts', 'bool', '1.1',
         "Does sea ice salinity impact the thermal properties of sea ice?"),
    ],
    'detail_sets': [
        'mass_transport',
        'thermodynamics',
    ]
}

SUB_PROCESSES['salt:mass_transport']={
    'description':'Mass transport of salt',
    'properties': [
        ('salinity_type', 'ENUM:salinity_method', '1.1',
            "Some text"),
        ('constant_salinity_value_mass_transport', 'float', '0.1',
             "If using a constant salinity value specify this value in PSU?"),
        ('additional_details', 'str', '1.1',
            "Describe the prognostic salinity profile method used."),
        ]
    }

SUB_PROCESSES['salt:thermodynamics']={
    'description':'Salt thermodynamics',
    'properties': [
        ('salinity_type', 'ENUM:salinity_method', '1.1',
            "Some text"),
        ('constant_salinity_value_thermodynamics', 'float', '0.1',
             "If using a constant salinity value specify this value in PSU?"),
        ('additional_details', 'str', '1.1',
            "Describe the prognostic salinity profile method used."),
        ]
    }


SUB_PROCESSES['ice_thickness_distribution'] = {
    'description': 'Characteristics of melt ponds.',
    'properties': [
        ('representation', 'ENUM:ice_thickness_representation', '1.1',
            "Representation of the sea ice thickness distribution"),
        ]
    }


SUB_PROCESSES['melt_ponds'] = {
    'description': 'Characteristics of melt ponds.',
    'properties': [
        ('are_included', 'bool', '1.1',
            "Are melt ponds included in sea ice model?"),
        ('formulation', 'ENUM:melt_pond_formulation', '0.1',
            "Method of melt pond formulation"),
        ('impacts', 'ENUM:melt_pond_impacts', '0.N',
            "Impacts of the melt ponds?")
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Snow thermodynamic processes.
# --------------------------------------------------------------------
SUB_PROCESSES['snow_processes'] = {
    'description': 'Thermodynamic processes in snow on sea ice',
    'properties': [
        ('has_snow_aging', 'bool', '1.N', "Snow redistribution"),
        ('snow_aging_schem', 'str', '1.N', "Snow redistribution"),
        ('has_snow_ice_formation', 'bool', '1.N', "Snow ice formation"),
        ('snow_ice_formation_scheme', 'str', '1.N', "Snow ice formation"),
        ('redistribution', 'str', '1.N', "What is the impact of ridging on snow cover?"),
        ('heat_diffusion', 'ENUM:snow_process_types', '1.1',
            "Snow processes in sea ice thermodynamics"),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
# TODO If fixed salinity want to ask what is the salinity constant used
# TODO Ask: Does the sea ice salinity impact the thermal properties of sea ice
ENUMERATIONS['energy_formulation'] = {
    'description': 'Thermodynamic formulation of energy conservation',
    'is_open': True,
    'members': [
        ('Pure ice latent heat (Semtner 0-layer)', None),
        ('Pure ice latent and sensible heat', None),
        ('Pure ice latent and sensible heat + brine heat reservoir (Semtner 3-layer)', None),
        ('Pure ice latent and sensible heat + explicit brine inclusions (Bitz and Lipscomb)', None),
    ]
}

ENUMERATIONS['thermal_conductivity_type'] = {
    'description': 'Thermal conductivity in sea ice thermodynamics',
    'is_open': True,
    'members': [
        ('Pure ice', None),
        ('Saline ice', None),
    ]
}

ENUMERATIONS['basal_heat_flux_method'] = {
    'description': 'Basal ocean heat flux methodology',
    'is_open': True,
    'members': [
# TODO Check with Martin
#        ('linear', None),
#        ('quadratic', None),
#        ('prescribed', None),
        ('Heat Reservoir', 'Brine inclusions treated as a heat reservoir'),
        ('Thermal Fixed Salinity', 'Thermal properties depend on S-T (with fixed salinity)'),
        ('Thermal Varying Salinity', 'Thermal properties depend on S-T (with varying salinity'),
    ]
}

ENUMERATIONS['heat_diffusion_type'] = {
    'description': 'Thermal conductivity in sea ice thermodynamics',
    'is_open': True,
    'members': [
        ('Conduction fluxes', None),
        ('Conduction and radiation heat fluxes', None),
        ('Conduction, radiation and latent heat transport', None),
    ]
}

ENUMERATIONS['lateral_melting_types'] = {
    'description': 'Ice lateral melting method',
    'is_open': True,
    'members': [
        ('Floe-size dependent (Bitz et al 2001)', None),
        ('Virtual thin ice melting (for single-category)', None),
    ]
}

ENUMERATIONS['ice_thickness_representation'] = {
    'description': 'Type of sea ice thickness representation',
    'is_open': True,
    'members': [
        ('Explicit', None),
        ('Virtual (enhancement of thermal conductivity, thin ice melting)', None),
    ]
}

ENUMERATIONS['thermo_brine_types'] = {
    'description': 'Brine inclusion methodology',
    'is_open': True,
    'members': [
        ('Heat Reservoir', 'Brine inclusions treated as a heat reservoir'),
        ('Thermal Fixed Salinity', 'Thermal properties depend on S-T (with fixed salinity)'),
        ('Thermal Varying Salinity', 'Thermal properties depend on S-T (with varying salinity'),
    ]
}

ENUMERATIONS['melt_pond_formulation'] = {
    'description': 'Formulation of melt ponds.',
    'is_open': True,
    'members': [
        ('Flocco and Feltham (year)', None),
        ('Level-ice melt ponds', None),
    ]
}

ENUMERATIONS['melt_pond_impacts'] = {
    'description': 'Melt ponds have impacts on',
    'is_open': True,
    'members': [
        ('Albedo', None),
        ('Freshwater', None),
        ('Heat', None),
    ]
}

ENUMERATIONS['snow_process_types'] = {
    'description': 'Types of snow processes',
    'is_open': True,
    'members': [
        ('single-layered heat diffusion', None),
        ('multi-layered heat diffusion', None),
    ]
}

ENUMERATIONS['salinity_method'] = {
    'description': 'Salinity',
    'is_open': True,
    'members': [
        ('constant', None),
        ('prescribed salinity profile', None),
        ('prognostic salinity profile', None),
    ]
}

