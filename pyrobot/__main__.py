import importlib
import sys
import asyncio

from pyrobot import BOT, LOGS, __copystring__, __version__
from pyrobot.modules import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("pyrobot.modules." + module_name)

async def start_bot():
    if len(sys.argv) not in (1, 3, 4):
        quit(1)
    else:
        await BOT.start()
        #ME = await BOT.get_me().username
        print(__copystring__)
        #LOGS.info(f"You're logged in as \"{ME}\"! Test it by typing .alive in any chat.")
        LOGS.info(f"Your bot is Version {__version__}\n")
        await BOT.idle()
        await BOT.stop()
        await print("\nUserbot Stopped")
        await BOT.run()
asyncio.run(start_bot())
