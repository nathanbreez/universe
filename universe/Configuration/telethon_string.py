# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from os import getenv as then_get
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from dotenv import find_dotenv, load_dotenv
from telethon.errors import PhoneCodeInvalidError, SessionPasswordNeededError, FloodError

load_dotenv(find_dotenv("string.env"))


desc = """
Thank you very much for using this script.

<code>Telethon_String</code>:

<code>{}</code>

⚠️ <b>Please be carefull to pass this value to third parties</b>

Credits : @TelethonUpdates

Managed by : @GroupTidakDiketahui
"""
print("")
print("\x1b[1;93m[ Telethon ]")
print("")
print("""Maintainer : @xelyourslurred <unknownkz@outlook.co.id>""")
print("")
print("")
Api_ID = int(then_get("Api_ID"))
Api_Hash = str(then_get("Api_Hash"))
MobilePhoneNumber = then_get("MobilePhoneNumber")

FlyMeToTheMoon = True


while FlyMeToTheMoon:
    try:
        with TelegramClient(StringSession(), api_id=Api_ID, api_hash=Api_Hash).start(
            phone=MobilePhoneNumber
        ) as StartUniverse:
            StartUniverse.send_code_request(phone=MobilePhoneNumber)
            print("")
            galaxy = StartUniverse.session.save()
            messages_temp = desc.format(galaxy)
            StartUniverse.send_message("me", messages_temp, parse_mode="html")
            print("Your Telethon_String value have been sent to ur Telegram <Saved Messages>")
    except BaseException as excp:
        print(excp)
    except ValueError as value:
        print(value)
    except PhoneCodeInvalidError as invalid:
        print(invalid)
    except SessionPasswordNeededError as pw:
        print(pw)
    except FloodError as cx:
        print(cx)
    except ConnectionError:
        raise RuntimeError
        continue
    break
