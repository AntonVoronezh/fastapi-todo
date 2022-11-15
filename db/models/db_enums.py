from sqlalchemy import Enum

from shared.enums.todos import TodoTypeEnum, DaysOfTheWeekEnum


__all__ = [
    "enum_todo_type",
    "enum_days_of_the_week",
]

enum_todo_type = Enum(TodoTypeEnum, name="enum_todo_type")
enum_days_of_the_week = Enum(DaysOfTheWeekEnum, name="enum_days_of_the_week")
