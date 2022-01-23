import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from THANOSBOT import *
from THANOSBOT.clients import *
from THANOSBOT.helpers import *
from THANOSBOT.config import *
from THANOSBOT.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from THANOSBOT.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import THANOSBOT.utils

        path = Path(f"hellbot/plugins/{shortname}.py")
        name = "THANOSBOT.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("THANOSBOT - Successfully imported " + shortname)
    else:
        import THANOSBOT.utils

        path = Path(f"hellbot/plugins/{shortname}.py")
        name = "THANOSBOT.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = THANOS
        mod.H1 = THANOS
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.THANOS = THANOS
        mod.THANOSBOT = THANOSBOT
        mod.tbot = THANOSBOT
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = THANOSBOT.utils
        mod.Config = Config
        mod.borg = bot
        mod.THANOSBOT = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_hell = delete_hell
        mod.eod = delete_hell
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.THANOS_cmd = THANOS_cmd
        mod.sudo_cmd = sudo_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = THANOSBOT.utils
        sys.modules["userbot"] = THANOSBOT
        # support for paperplaneextended
        sys.modules["userbot.events"] = THANOSBOT
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["THANOSBOT.plugins." + shortname] = mod
        LOGS.info("⚡ THANOSBOT† ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"THANOSBOT.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

# THANOSBOT
