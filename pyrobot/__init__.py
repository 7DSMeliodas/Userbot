import logging
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

import dotenv
from pyrogram import Client

# We need logging this early for our Version Check
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARN)
LOGS = logging.getLogger(__name__)

# Check for Python 3.6 or newer
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGS.error("You MUST use at least Python 3.6. Bot Quitting")
    quit(1)

# Now for the rest
__version__ = '0.3.3'
__author__ = 'Nicolas "Colin" Neht'
__source__ = 'https://git.colinshark.de/PyroBot/PyroBot'
__copyright__ = 'Copyright (c) 2019 ' + __author__
__copystring__ = f"PyroBot v{__version__} | {__copyright__}"

# Load our .env file
dotenv.load_dotenv()

# Get the Values from our .env
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

LOGGER = os.getenv("LOGGER")
try:
    LOGGER_GROUP = int(os.getenv("LOGGER_GROUP"))
except ValueError:
    LOGGER_GROUP = os.getenv("LOGGER_GROUP")

ACCGEN_API = os.getenv("ACCGEN_API")
CC_API = os.getenv("CC_API")
SAUCE_API = os.getenv("SAUCE_API")

# Create Database if there is none yet.
PYRO_DB = str(Path(__file__).parent.parent / 'pyrobot.db')

LOGS.info("Checking Database...")
db = sqlite3.connect(PYRO_DB)
c = db.cursor()
c.executescript(
    "CREATE TABLE IF NOT EXISTS video_notes "
    "(name TEXT UNIQUE ON CONFLICT FAIL, file_id TEXT UNIQUE ON CONFLICT FAIL);"
    "CREATE TABLE IF NOT EXISTS welcome "
    "(chat_id INT UNIQUE ON CONFLICT FAIL, greet TEXT, chat_title TEXT);")
db.commit()
db.close()
LOGS.info("Check done.")


# Prepare the bot
BOT = Client(
    session_name="PyroBot",
    api_id=API_ID,
    api_hash=API_HASH,
    app_version=f"PyroBot \U0001f525\U0001F916 v{__version__}")

# Global Variables
ISAFK = False
AFK_REASON = "No Reason"
START_TIME = datetime.now()
