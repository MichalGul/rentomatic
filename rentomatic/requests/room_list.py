from collections.abc import Mapping
from typing import Union


class RoomListInvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({
            'parameter': parameter,
            'message': message
        })

    def has_errors(self):
        return len(self.errors) > 0

    def __bool__(self):
        return False

    def to_dict(self):
        return {
            'errors': self.errors
        }


class RoomListValidRequest:
    def __init__(self, filters: Mapping=None):
        self.filters = filters

    def __bool__(self):
        return True


def build_room_list_request(filters: Mapping = None) -> Union[RoomListValidRequest, RoomListInvalidRequest]:
    accepted_filters = ["code__eq", "price__eq", "price__gt", "price__lt"]
    invalid_request = RoomListInvalidRequest()

    if filters is not None:
        if not isinstance(filters, Mapping):
            invalid_request.add_error("filters", "Invalid type. Not Iterable")
            return invalid_request

        for key, value in filters.items():
            if key not in accepted_filters:
                invalid_request.add_error("filters", f"Invalid filter '{key}'")

        if invalid_request.has_errors():
            return invalid_request

    return RoomListValidRequest(filters=filters)













