# Copyright Lion
# For @LionHelp coded by @xditya
# Kangers keep credits else I'll take down š§

import random
import sys

from telethon import version

from Lion import ALIVE_NAME
from Lion.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lion User"

ONLINESTR = [
    "āāāāāāāāāāāāāāāāāāāā \nāāā¦āā¦āāā¦āāāāāāā¦āāāāā  āāāāāā āāāāāāāāāāā āāā \nāāāā©āāāāāāāāāā©āā©āāāā \nāāāāāāāāāāāāāāāāāāāā \n\n**Lion is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Team Lion](tg://user?id=1837687523) \n\n**More help -** @LionXUpdates \n\n           [š§ GitHub Repository š§](https://github.com/TeamLion-X/Lion-X)",
    f"ā¦āā¦āāā¦āāāāāāā¦āāā\nāāāā āāāāāāāāāāā ā\nāā©āāāāāāāāāā©āā©āā\n              **Welcome to Lion**\n\n**Hey master! I'm alive. All systems online and functioning normally ā**\n\n**āļø Telethon version:** `{version.__version__}` \n\n**āļø Python:** `{sys.version}` \n\nāļø More info: @LionXUpdates \n\nāļø Created by: [Team Lion](tg://user?id1837687523=) \n\n**āļø Database status:** All ok š \n\n**āļø My master:** {DEFAULTUSER} \n\n        [š Github repository š](https://github.com/TeamLion-X/Lion-X)",
]


@Lion.on(admin_cmd(outgoing=True, pattern="online"))
@Lion.on(sudo_cmd(allow_sudo=True, pattern="online"))
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))
