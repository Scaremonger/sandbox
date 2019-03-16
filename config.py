## BASICS OF A CONFIG PARSER MODULE
## STATE: UNFINISHED

# Need to create file with default values if it does not exist
# Need to wrap this with a class so configParser and default file creation is hidden

# Need to decide if file will be YAML or INI
## I could support both, but use one as preferred. If renamed it would use the other
## This would help with the Modular nature of MIoT, in that the owner could use a config file
## the way they like it. The config module would need to hide this from the apps.

# Need to make config module an export from miot_core module
## import config from miot_core (For example)

import configparser
config = configparser.configParser

try:
    with open("/etc/opt/miot/miot_core.conf") as source:
        config.read("/etc/opt/miot/miot_core.conf")
    except IOError:
        ##tbc


