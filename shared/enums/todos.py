from enum import Enum

__all__ = [
    "TodoTypeEnum",
    "DaysOfTheWeekEnum",
]


class TodoTypeEnum(str, Enum):
    FORBID = "FORBID"
    ALLOW = "ALLOW"


class DaysOfTheWeekEnum(str, Enum):
    SUN_DAY = 'SUN_DAY'
    MON_DAY = 'MON_DAY'
    TUES_DAY = 'TUES_DAY'
    WEDNES_DAY = 'WEDNES_DAY'
    THURS_DAY = 'THURS_DAY'
    FRI_DAY = 'FRI_DAY'
    SATUR_DAY = 'SATUR_DAY'

