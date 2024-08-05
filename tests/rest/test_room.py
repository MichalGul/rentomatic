import json
from unittest import mock

from rentomatic.domain.room import Room

rooms_dicts = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
    {
        "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "size": 405,
        "price": 66,
        "longitude": 0.18228006,
        "latitude": 51.74640997,
    },
    {
        "code": "913694c6-435a-4366-ba0d-da5334a611b2",
        "size": 56,
        "price": 60,
        "longitude": 0.27891577,
        "latitude": 51.45994069,
    },
    {
        "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
        "size": 93,
        "price": 48,
        "longitude": 0.33894476,
        "latitude": 51.39916678,
    },
]

rooms = [Room.from_dict(room_dict) for room_dict in rooms_dicts]


@mock.patch('application.rest.room.room_list_use_case') #mock import
def test_get(mock_use_case, client):
    # client is fixture from pytest-flask
    mock_use_case.return_value = rooms
    http_response = client.get('/rooms')
    assert json.loads(http_response.data.decode("UTF-8")) == rooms_dicts
    mock_use_case.assert_called()
    assert http_response.status_code == 200
    assert http_response.content_type == 'application/json'
