import os
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, get_readable_time as grt
from platform import python_version, uname
import time
from userbot import UpTime
from telethon import events, version

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
PLUSPIC = ALIVE_PIC

@borg.on(admin_cmd(pattern="alive"))
async def iamalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = grt((time.time() - UpTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
        
    if PLUSPIC:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🗺️** \n\n`🔸 Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @buddhhu \n`🔹 Bot creator:` [//•𝙺𝚞𝚖𝚊𝚛•𝙰𝚖𝚒𝚝•//](tg://user?id=667805879)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @xtratgplus `For Help` \n\n                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus)  \n\n   "
    	await borg.send_file(alive.chat_id, PLUSPIC, caption=ALIVE)
    	await alive.delete()
    else:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🗺️** \n\n`🔸 Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @buddhhu \n`🔹 Bot creator:` [//•𝙺𝚞𝚖𝚊𝚛•𝙰𝚖𝚒𝚝•//](tg://user?id=667805879)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @xtratgplus `For Help` \n\n                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus)  \n\n   "
    	await alive.edit(f"{ALIVE}")

@borg.on(admin_cmd(pattern="sudoalive", allow_sudo=True))
async def iamalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = grt((time.time() - UpTime))
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
        
    if PLUSPIC:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🗺️** \n\n`🔸 Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @buddhhu \n`🔹 Bot creator:` [//•𝙺𝚞𝚖𝚊𝚛•𝙰𝚖𝚒𝚝•//](tg://user?id=667805879)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @xtratgplus `For Help` \n\n                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus)  \n\n   "
    	await borg.send_file(alive.chat_id, PLUSPIC, caption=ALIVE)
    	await alive.delete()
    else:
    	ALIVE = f"**MADE IN 🇮🇳 , MADE FOR 🗺️** \n\n`🔸 Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Fork by:` @buddhhu \n`🔹 Bot creator:` [//•𝙺𝚞𝚖𝚊𝚛•𝙰𝚖𝚒𝚝•//](tg://user?id=667805879)\n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 My owner:` **{DEFAULTUSER}**  \n`🔸 Join` @xtratgplus `For Help` \n\n                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FX-tra-TG-plus)  \n\n   "
    	await alive.reply(f"{ALIVE}")
