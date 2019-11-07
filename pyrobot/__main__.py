import importlib
import sys

from pyrobot import BOT, LOGS, __copystring__, __version__
from pyrobot.modules import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("pyrobot.modules." + module_name)

if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    BOT.start()
    ME = BOT.get_me().username
    print(__copystring__)
    LOGS.info(f"You're logged in as \"{ME}\"! Test it by typing .alive in any chat.")
    LOGS.info(f"Your bot is Version {__version__}\n")
    BOT.idle()
    BOT.stop()
    print("\nUserbot Stopped")
