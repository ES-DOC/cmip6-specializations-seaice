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
    'description': 'Key properties of sea ice raditative processes',
    'properties':[
        ('implementation_overview','str', '1.1',
            "General overview description of the implementation of this part of the process."),
        ('keywords','str', '0.N',
            "Keywords to help re-use and discovery of this information."),
        ('citations','shared.citation', '0.N',
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
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# PROCESS: SUB PROCESS
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES['si_radiative_process_methods'] = {
    'description': 'Properties of radiation in sea ice thermodynamics',
    'details': ['details'],
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESS DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESSES['si_radiative_process_methods:details'] = {
    'description': 'Additional information about radiative processes in sea ice.',
    'properties': [
        ('surface_albedo', 'ENUM:seaice_albedo', '0.N',
         'Method used to handle surface albedo'),
        ('ice_radiation_transmission', 'str', '0.1',
         'Method by which solar radiation through sea ice is handled'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['seaice_albedo'] = {
    'description': 'Surface albedo of sea ice component',
    'is_open': True,
    'members': [
        ('Delta-Eddington', None),
        ('Linear dependence on temperature', None),
        ('Spectral dependence on temperature', None),
        ('Specified values of albedo for e.g. cold/melting snow, melting sea ice', None),
        ('melt ponds', None)
    ]
}