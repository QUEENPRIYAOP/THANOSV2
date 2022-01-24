import datetime
import time

from THANOSBOT import *
from THANOSBOT.clients import *
from THANOSBOT.config import Config
from THANOSBOT.helpers import *
from THANOSBOT.utils import *
from THANOSBOT.random_strings import *
from THANOSBOT.version import __hell__
from THANOSBOT.sql.gvar_sql import gvarstat
from telethon import version

THANOS_logo = "./THANOSBOT/resources/pics/hellbot_logo.jpg"
cjb = "./THANOSBOT/resources/pics/cjb.jpg"
restlo = "./THANOSBOT/resources/pics/rest.jpeg"
shuru = "./THANOSBOT/resources/pics/shuru.jpg"
shhh = "./THANOSBOT/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
THANOS_ver = __THANOS__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "Its_HellBot"
my_group = Config.MY_GROUP or "HellBot_Chat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/its_hellbot"
THANOS_channel = f"[†hê Hêllẞø†]({chnl_link})"
grp_link = "https://t.me/HellBot_Chat"
THANOS_grp = f"[Hêllẞø† Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# THANOSBOT
