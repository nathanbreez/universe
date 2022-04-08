# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from time import sleep

from .. import univ
from ..Configuration import MultiVerse
from ..EquipmentTools import deleted, eor
from ..UniverseLogger import UniverseLogger as UL

category = "admins"

p = MultiVerse.Trigger


async def remove_users(chat_id, gets):
    try:
        await univ.kick_participant(chat_id, gets)
        return True, None
    except Exception as excp:
        return False, str(excp)


@univ.universe_cloud(
    pattern="delcount(?: |$)(-clean)?(?: |$)(.*)",
    command=("delcount -clean", category),
    groups_only=True,
)
async def _(incident):
    cleaning = incident.pattern_match.group(1)
    if cleaning == "-clean":
        chats = await incident.get_chat()
        if not chats.admin_rights and not chats.creator:
            await incident.edit("You aren't an admin.")
            return False

    else:
        return False

    amount_user = 0
    read = 0
    kicked = 0
    failed = 0

    searching = await eor(incident, "Clean-up...")
    async for gets in incident.client.iter_participants(incident.chat_id):
        read += 1

        if not gets.deleted:
            cleaning_text = "Your group is already clean."
            sleep(5)
            await searching.edit(cleaning_text)
            return False

        if gets.deleted:
            amount_user += 1
            try:
                await remove_users(incident.chat_id, gets.id)
                sleep(5)
                kicked += 1
            except Exception as excp:
                UL.error(str(excp))
                failed += 1

    sans = f"""
Information :

The number of deleted accounts exists {amount_user},
Kick {kicked} out of {read} members.
Failed {failed} account, coz user is admin.
I didn't get permission.
"""
    sleep(5)
    await searching.edit(sans)
    return deleted(incident)
