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
DESCRIPTION = 'Sea Ice Radiative Processes'

# --------------------------------------------------------------------
# SUB PROCESS: Properties of radiation in sea ice
# --------------------------------------------------------------------
SUB_PROCESSES['methods'] = {
    'description': "Properties of radiation in sea ice",
    'properties': [
        ('surface_albedo', 'ENUM:seaice_albedo', '0.N',
            "Method used to handle surface albedo"),
#        ('ice_radiation_transmission_per_category', 'str', '1.1',
#            "Is solar radiation through ice done per ice category?"),
        ('ice_radiation_transmission', 'ENUM:ice_trans', '1.N',
            "Method by which solar radiation through sea ice is handled"),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['seaice_albedo'] = {
    'description': "Surface albedo of sea ice component",
    'is_open': True,
    'members': [
        ('Delta-Eddington', None),
        ('Parameterized', 'Sea ice albedo is parameterized'),
        ('Multi-band albedo', 'Albedo value has a spectral dependence'),
    ]
}

ENUMERATIONS['ice_trans'] = {
    'description': "Surface albedo of sea ice component",
    'is_open': True,
    'members': [
        ('Exponential attenuation', None),
        ('Delta-Eddington', None),
        ('ice_radiation_transmission_per_category', None)
    ]
}
