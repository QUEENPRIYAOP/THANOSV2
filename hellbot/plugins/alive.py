import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from THANOSBOT.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>๐ฅ๐ฅษฆษสสษฎึt ษจs ึีผสษจีผษ๐ฅ๐ฅ</b></i>
<i><b>โผ รwรฑรชr โ</i></b> : ใ <a href='tg://user?id={}'>{}</a> ใ
โญโโโโโโโโโโโโโโ
โฃโ <b>ยป Telethon ~</b> <i>{}</i>
โฃโ <b>ยป Hรชllแบรธโ  ~</b> <i>{}</i>
โฃโ <b>ยป Sudo ~</b> <i>{}</i>
โฃโ <b>ยป Uptime ~</b> <i>{}</i>
โฃโ <b>ยป Ping ~</b> <i>{}</i>
โฐโโโโโโโโโโโโโโ
<b><i>ยปยปยป <a href='https://t.me/its_hellbot'>[ โ hรช Hรชllแบรธโ  ]</a> ยซยซยซ</i></b>
"""
#-------------------------------------------------------------------------------

@THANOS_cmd(pattern="alive$")
async def up(event):
    cid = await client_id(event)
    ForGo10God, THANOS_USER, THANOS_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    THANOS = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    if a is not None:
        b = a.split(" ")
        c = []
        if len(b) >= 1:
            for d in b:
                c.append(d)
        PIC = random.choice(c)
    else:
        PIC = "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
    THANOS_pic = PIC
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, THANOS_USER, tel_ver, THANOS_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=hell_pic, caption=omk, parse_mode="HTML")
    await THANOS.delete()


msg = """{}\n
<b><i>๐ ๐ฑ๐๐ ๐๐๐๐๐๐ ๐</b></i>
<b>Telethon โ</b>  <i>{}</i>
<b>Hรชllแบรธโ  โ</b>  <i>{}</i>
<b>Uptime โ</b>  <i>{}</i>
<b>Abuse โ</b>  <i>{}</i>
<b>Sudo โ</b>  <i>{}</i>
"""
botname = Config.BOT_USERNAME

@THANOS_cmd(pattern="thanoa$")
async def hell_a(event):
    cid = await client_id(event)
    ForGo10God, THANOS_USER, THANOS_mention = cid[0], cid[1], cid[2]
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>ยปยป ะฝัโโะฒฯั ฮนั ฯะธโฮนะธั ยซยซ</b>"
    try:
        THANOS = await event.client.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, THANOS_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "thanos", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "โ Harmless Module"
).add()
