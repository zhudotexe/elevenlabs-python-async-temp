# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ReviewStatus(str, enum.Enum):
    NOT_REQUESTED = "not_requested"
    PENDING = "pending"
    DECLINED = "declined"
    ALLOWED = "allowed"
    ALLOWED_WITH_CHANGES = "allowed_with_changes"

    def visit(
        self,
        not_requested: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        allowed: typing.Callable[[], T_Result],
        allowed_with_changes: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewStatus.NOT_REQUESTED:
            return not_requested()
        if self is ReviewStatus.PENDING:
            return pending()
        if self is ReviewStatus.DECLINED:
            return declined()
        if self is ReviewStatus.ALLOWED:
            return allowed()
        if self is ReviewStatus.ALLOWED_WITH_CHANGES:
            return allowed_with_changes()