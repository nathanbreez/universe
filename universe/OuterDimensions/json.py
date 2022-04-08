# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from telethon.tl.types import MessageEntityPre
from telethon.utils import add_surrogate

from .. import univ
from ..EquipmentTools import etd, deleted

category = "tools"


def json_parse(text):
    text = text.strip()
    return (
        text,
        [MessageEntityPre(offset=0, length=len(add_surrogate(text)), language="")],
    )


@univ.universe_cloud(
    pattern="js(?: |$)(-on)?(?: |$)(.*)",
    command=("js -on <reply>", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)
    replied = await incident.get_reply_message() if incident.reply_to_msg_id else incident

    if point == "-on":
        get_json = replied.stringify()
        await etd(incident, get_json, parse_mode=json_parse)
        await deleted(incident)

    else:
        return False
