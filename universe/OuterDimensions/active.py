# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

import rsa
import packaging
from textwrap import indent
from platform import python_version
from datetime import datetime
from time import time as t
from telethon import __version__
from py._version import version

from .. import univ, start_time, __version, __license
from ..Configuration import MultiVerse
from ..EquipmentTools import deleted, tf
from ..UniverseLogger import tz

category = "core"


@univ.universe_cloud(
    pattern="active",
    command=("active", category),
)
async def _(incident):
    my_uptime = tf((t() - start_time) * 1000)
    time_stamp = datetime.now(tz).strftime("%I:%M:%S %p UTC%z")
    text_active = f"""
__“We are connected on the inside.”__
-----
`[]`  › `Uptime: {my_uptime}`
`[]`  › `Py: {version}`
`[]`  › `RSA: {rsa.__version__}`
`[]`  › `Python: {str(python_version())}`
`[]`  › `Packaging: {packaging.__version__}`
`[]`  › `Telethon: {__version__}`
`[]`  › `Version: {__version}`
`[]`  › `License:` [{str(__license)}](https://opensource.org/licenses/GPL-3.0)
-----
[Repository](https://github.com/unknownkz/universe) // [Author](https://t.me/xelyourslurred) // [Support](https://t.me/kastaot)
-----
**{time_stamp} {MultiVerse.TZ}**
"""
    wrp = indent(text_active, " ", lambda line: True)
    await deleted(incident)
    await univ.send_file(
        incident.chat_id, file=MultiVerse.Info_Active, caption=wrp
    )
