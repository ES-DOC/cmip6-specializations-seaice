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
        ('ice_radiation_transmission', 'str', '0.1',
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
        ('Linear dependence on temperature', None),
        ('Spectral dependence on temperature', None),
        ('Specified values of albedo for e.g. cold or melting snow, melting sea ice', None),
        ('melt ponds', None)
    ]
}