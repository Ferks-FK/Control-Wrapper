from .control_wrapper import ControlWrapper
from typing import NamedTuple, Literal

class Version(NamedTuple):
    major: int
    minor: int
    micro: int
    release: Literal["alpha", "beta", "candidate", "final"]

version: Version = Version(major=1, minor=0, micro=0, release="alpha")