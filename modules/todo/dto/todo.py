from fastapi_camelcase import CamelModel

from shared.enums.todos import TodoTypeEnum


# todo_id = Column(Integer, primary_key=True, comment="Идентификатор записи что сделать")
# name = Column(String(255), nullable=False, unique=True)
# description = Column(Text, nullable=False)
# on_offer = Column(Boolean, default=False)
# weight = Column(Integer, nullable=False)
# priority = Column(enum_todo_type, comment="Тип записи")  TodoTypeEnum


class TodoBaseDto(CamelModel):
    name: str
    description: str
    active: bool
    weight: int
    priority: TodoTypeEnum


# class PolicyCreateDto(PolicyBaseDto):
#     policy_action: list[PolicyActionCreateParentDto]
#     policy_objects: list[PolicyObjectCreateParentDto]
#     policy_subjects: list[PolicySubjectCreateParentDto]


class TodoDto(TodoBaseDto):
    todo_id: int
    # policy_action: list[PolicyActionDto] | None
    # policy_objects: list[PolicyObjectDto] | None
    # policy_subjects: list[PolicySubjectDto] | None

    class Config:
        orm_mode = True


# class PolicyUpdateDto(PolicyBaseDto):
#     policy_action: list[PolicyActionCreateParentDto]
#     policy_objects: list[PolicyObjectCreateParentDto]
#     policy_subjects: list[PolicySubjectCreateParentDto]
