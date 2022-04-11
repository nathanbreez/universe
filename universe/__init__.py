# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @notudope
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from sys import platform, maxsize, version_info, exit
from time import time
from pathlib import Path

from .UniverseLogger import UniverseLogger as UL
from .Ground.another import univ

start_time = time()


__version = "Infinity"
__license = "GNU GPL-3.0 License"

if platform.startswith("linux") and maxsize == 2 ** 63 - 1:
    platform = "Linux"
    architecture = "aarch64"
    UL.info(
        "You're running universe on the system {} {}".format(
            platform,
            architecture,
        )
    )
else:
    platform = "linux"
    architecture = "aarch64"
    UL.error(
        "You've to use {} {} system first!".format(platform, architecture)
    )
    exit(1)


if (
    version_info.major >= 3
    or version_info.minor >= 10
    or version_info.micro >= 0
):
    major = version_info.major
    minor = version_info.minor
    micro = version_info.micro
    UL.info(
        "You're running universe on the python {}.{}.{}".format(
            str(round(major)),
            str(round(minor)),
            str(round(micro)),
        )
    )
elif (
    version_info.major >= 3
    or version_info.minor >= 9
    or version_info.macro >= 0
):
    major = version_info().major
    minor = version_info().minor
    micro = version_info().micro
    UL.info(
        "You're running universe on the python {}.{}.x".format(
            str(round(major)),
            str(round(minor)),
            str(round(micro)),
        )
    )
else:
    major = 3
    minor = 9
    UL.error(
        "You've to use python version of at least >= {}.{}.x ! quitting..".format(
            str(round(major)),
            str(round(minor)),
        )
    )
    exit(1)


Rooters: Path = Path(__file__).parent.parent

dirs = ["cache"]
for _ in dirs:
    if not (Rooters / _).exists():
        (Rooters / _).mkdir(parents=True, exist_ok=True)
    else:
        for f in (Rooters / _).rglob("*.*"):
            if f.exists():
                f.unlink(missing_ok=True)
