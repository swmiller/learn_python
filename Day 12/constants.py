# Mathematical constants
PI = 3.14159
EULER_NUMBER = 2.71828

# Application-specific constants
MAX_USERS = 1000
DEFAULT_TIMEOUT = 30  # in seconds

# File paths
LOG_FILE_PATH = "/logs/app.log"
CONFIG_FILE_PATH = "/config/settings.json"

# Detect and print global variables
global_vars = list(globals().items())  # Create a static copy of globals()
for name, value in global_vars:
    if not name.startswith("__"):  # Exclude built-in variables
        print(f"{name} = {value}")
