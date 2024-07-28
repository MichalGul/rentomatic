import pytest
import uuid
from unittest import mock

from rentomatic.domain.room import Room
from rentomatic.use_cases.room_list import room_list_use_case


@pytest.fixture
def domain_rooms():
    # add 4 rooms to the list
    return [
        Room(
            code=uuid.uuid4(),
            size=215,
            price=39,
            longitude=-0.09998975,
            latitude=51.75436293,
        ),
        Room(
            code=uuid.uuid4(),
            size=405,
            price=66,
            longitude=-0.18228006,
            latitude=51.74640997,
            ),
        Room(
            code=uuid.uuid4(),
            size=56,
            price=60,
            longitude=0.27891557,
            latitude=51.45994069,
        ),
        Room(
            code=uuid.uuid4(),
            size=200,
            price=10,
            longitude=0.33894476,
            latitude=51.39916678,
        )
    ]


def test_room_list_without_parameters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    result = room_list_use_case(repo)
    repo.list.assert_called_once_with()
    assert result == domain_rooms
