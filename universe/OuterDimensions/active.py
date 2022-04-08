# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from platform import python_version
from datetime import datetime
from time import time as t
from telethon import __version__

from .. import univ, start_time
from ..Configuration import MultiVerse
from ..EquipmentTools import deleted, tf
from ..Ground import UniverseVersion

category = "core"


@univ.universe_cloud(
    pattern="active",
    command=("active", category),
)
async def _(incident):
    my_uptime = tf((t() - start_time) * 1000)
    text_active = f"""
__“We are connected on the inside.”__

   › `Uptime: {my_uptime}`
   › `Python: {str(python_version())}`
   › `Telethon: {__version__}`
   › `Version: {UniverseVersion}`

[Repository](https://github.com/unknownkz/universe) // [Maintainer](https://t.me/xelyourslurred) // [Support](https://t.me/kastaot)
"""
    await deleted(incident)
    await univ.send_file(incident.chat_id, file=MultiVerse.Info_Active, caption=text_active)
