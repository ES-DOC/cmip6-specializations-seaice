# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.scientific_realm'

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = None

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization authors.
# --------------------------------------------------------------------
AUTHORS = None

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# REALM IDENTIFIER
#
# Set to 'cmip6.<REALM>'
# --------------------------------------------------------------------
ID = 'cmip6.seaice'

# --------------------------------------------------------------------
# REALM: REALM
#
# Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'seaice'

# --------------------------------------------------------------------
# REALM: GRID
#
# The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'seaice_grid'

# --------------------------------------------------------------------
# REALM: KEY PROPERTIES
#
# Key properties for the domain which differ from model defaults
# (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = None

# --------------------------------------------------------------------
# REALM: PROCESSES
#
# Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'seaice_dynamics',
	'seaice_thermodynamics',
    'seaice_radiative_processes'
    ]