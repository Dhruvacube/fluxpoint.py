__title__ = 'fluxpoint'
__author__ = 'Dhruva Shaw'
__license__ = 'GNU GENERAL PUBLIC LICENSE'
__copyright__ = 'Copyright 2021-present Dhruvacube'
__version__ = '0.1.1'
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from typing import NamedTuple, Literal
import logging

from .http import *
from .enums import *
from .paths import *
from .client import *
from .errors import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0, minor=1, micro=1, releaselevel='final', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, NamedTuple, Literal, VersionInfo
