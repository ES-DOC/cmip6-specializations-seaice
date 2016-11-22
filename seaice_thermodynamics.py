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
"""DETAILS['general'] = {
    'description': 'General properties of sea ice thermodynamics',
    'properties': [
        ('budget', 'str', '0.1',
            "What information required to close the thermodynamics budget?"),
        ('transport_in_thickness_space', 'ENUM:transport_methods', '0.1',
            "What is the method of sea ice transport in thickness space (i.e. thickness categories)?"),
        ]
    }
"""
# --------------------------------------------------------------------
# SUB-PROCESS: Ice thermodynamic processes.
# --------------------------------------------------------------------
SUB_PROCESSES['energy_conservation'] = {
    'description': 'Energy conservation in sea ice thermodynamics',
    'properties': [
        ('enthalpy_formulation', 'ENUM:energy_formulation', '1.N',
            "Formulation of energy conservation"),
        ('thermal_conductivity', 'ENUM:thermal_conductivity_type', '1.N',
            "Method of thermal conductivity"),
        ('heat_diffusion', 'ENUM:heat_diffusion_type', '1.N',
            "Method of heat diffusion"),
        ('basal_heat_flux', 'ENUM:basal_heat_flux_method', '0.1',
            "Method by which basal ocean heat flux is handled"),
#        ('fixed_salinity_value', 'float', '0.1',
#         """If you have selected "Thermal properties depend on S-T (with fixed salinity)
#            please supply the fixed salinity value for each sea ice layer."""),
    ]
    }

#('heat_content_precip', 'str', '0.1',
# "Method by which the heat content of precipitation is handled ?")

SUB_PROCESSES['mass_conservation'] = {
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

SUB_PROCESSES['salt_conservation'] = {
    'description': 'Salt conservation in sea ice thermodynamics.',
    'properties': [
        ('has_constant_salinity', 'bool', '1.1',
             "Set to True if sea ice has constant salinity for both ice thermodynamics and ice-ocean exchanges."),
        ('has_prescribed_salinity_profile', 'str', '1.1',
            """Set to true if sea ice has prescribed salinity profile for ice thermodynamics
               but has constant salinity for ice-ocean exchanges"""),
        ('constant_salinity_value', 'float', '0.1',
            "If using a constant salinity value specify this value in PSU?"),
        ('prognostic_bulk_salinity', 'str', '1.1',
            "Describe the prognostic bulk salinity, parameterized profile shape."),
        ('prognostic_salinity_profile', 'str', '1.1',
            "Describe the prognostic salinity profile method used."),
        ]
    }

SUB_PROCESSES['ice_thickness_distribution'] = {
    'description': 'Characteristics of melt ponds.',
    'properties': [
        ('representation', 'ENUM:ice_thickness_representation', '1.1',
            "Representation of the sea ice thickness distribution"),
        ('transport_in_thickness_space', 'ENUM:transport_methods', '0.1',
            "What is the method of sea ice transport in thickness space (i.e. thickness categories)?"),
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
        ('process_type', 'ENUM:snow_process_types', '1.N',
            "Snow processes in sea ice thermodynamics"),
    ],
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
        ('linear', None),
        ('quadratic', None),
        ('prescribed', None),
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

ENUMERATIONS['transport_methods'] = {
    'description': 'Transport Methods',
    'is_open': True,
    'members': [
        ('Incremental Re-mapping', '(including Semi-Lagrangian)'),
        ('Prather', None),
        ('Eulerian', None),
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

