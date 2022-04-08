# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from carbon import Carbon, CarbonOptions
from time import sleep
from asyncio.exceptions import TimeoutError as AsyncTimeout
from telethon.errors import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from contextlib import suppress
from io import StringIO

from .. import univ, Rooters
from ..EquipmentTools import giu
from ..Ground import Rotation

category = "service"


async def sg_(sangmata_list):
    for nm in sangmata_list:
        if nm.startswith("🔗"):
            sangmata_list.remove(nm)
    search = 0
    for nm in sangmata_list:
        if nm.startswith("Username History"):
            break
        search += 1
    usrnm = sangmata_list[search:]
    nam = sangmata_list[:search]
    return nam, usrnm


async def __outer(folk, mkz, kz):
    with suppress(BaseException):
        arc = folk
        language = "auto"
        options = CarbonOptions(code=arc, language=language)
        cb = Carbon()
        image = Rotation.run_until_complete(cb.generate(options))
        Rotation.run_until_complete(image.save("sangmata"))
        fg = "sangmata.png"
        await univ.send_file(
            mkz,
            file=fg,
            reply_to=kz,
            force_document=True,
            silent=True,
        )
        (Rooters / fg).unlink(missing_ok=True)


@univ.universe_cloud(
    pattern=r"csang(-u)?(?:\s|$)([\s\S]*)",
    command=("csang|-u <reply/id/username>", category),
)
async def _cs(incident):
    point = incident.pattern_match.group(1)
    mkz = incident.chat_id
    messg = None
    COSMIC = True
    resp = []
    await incident.delete()
    kz = await univ.send_message(mkz, "Getting...", silent=True)
    sleep(5)
    userid, _ = await giu(incident, 2)
    if not userid:
        await univ.send_message(mkz, "Please re-check the username/id.", reply_to=kz, silent=True)
        await kz.delete()
        return False

    sangmata = "@SangMataInfo_bot"
    async with univ.conversation(sangmata) as conver:
        try:
            await conver.send_message("/search_id {}".format(userid.id))
        except YouBlockedUserError:
            await univ(UnblockRequest(sangmata))
            await conver.send_message("/search_id {}".format(userid.id))

        while COSMIC:
            try:
                res = await conver.get_response(timeout=5)
            except AsyncTimeout:
                await kz.delete()
                break
            resp.append(res.text)
        await univ.send_read_acknowledge(conver.chat_id)

    if not resp:
        await univ.send_message(mkz, "`Can't fetch results.`", reply_to=kz, silent=True)

    elif "No records found" in resp:
        await univ.send_message(mkz, "No records found", reply_to=kz, silent=True)

    else:
        nam, usrnm = await sg_(resp)
        messg = None
        check = usrnm if point == "-u" else nam
        for folk in check:
            if messg:
                await univ.send_message("`Empety`")
            else:
                await __outer(folk, mkz, kz)


@univ.universe_cloud(
    pattern=r"sang(-u)?(?:\s|$)([\s\S]*)",
    command=("sang|-u <reply/id/username>", category),
)
async def _s(incident):
    point = incident.pattern_match.group(1)
    mkz = incident.chat_id
    messg = None
    COSMIC = True
    resp = []
    await incident.delete()
    kz = await univ.send_message(mkz, "Getting...", silent=True)
    sleep(5)
    userid, _ = await giu(incident, 2)
    if not userid:
        await univ.send_message(mkz, "Please re-check the username/id.", reply_to=kz, silent=True)
        await kz.delete()
        return False

    sangmata = "@SangMataInfo_bot"
    async with univ.conversation(sangmata) as conver:
        try:
            await conver.send_message("/search_id {}".format(userid.id))
        except YouBlockedUserError:
            await univ(UnblockRequest(sangmata))
            await conver.send_message("/search_id {}".format(userid.id))

        while COSMIC:
            try:
                res = await conver.get_response(timeout=5)
            except AsyncTimeout:
                await kz.delete()
                break
            resp.append(res.text)
        await univ.send_read_acknowledge(conver.chat_id)

    if not resp:
        await univ.send_message(mkz, "`Can't fetch results.`", reply_to=kz, silent=True)

    elif "No records found" in resp:
        await univ.send_message(mkz, "No records found", reply_to=kz, silent=True)

    else:
        nam, usrnm = await sg_(resp)
        messg = None
        check = usrnm if point == "-u" else nam
        for folk in check:
            if messg:
                await univ.send_message(mkz, folk, silent=True, reply_to=kz, parse_mode="html")
            else:
                await kz.reply(folk, silent=True, parse_mode="html")
