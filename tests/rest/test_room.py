import json
from unittest import mock

import pytest

from rentomatic.domain.room import Room
from rentomatic.responses import ResponseTypes, ResponseSuccess, ResponseFailure

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
    mock_use_case.return_value = ResponseSuccess(rooms)
    http_response = client.get('/rooms')

    assert json.loads(http_response.data.decode("UTF-8")) == rooms_dicts
    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args

    assert args[1].filters == {}
    assert http_response.status_code == 200
    assert http_response.content_type == 'application/json'


@mock.patch("application.rest.room.room_list_use_case")
def test_get_with_filters(mock_use_case, client):
    mock_use_case.return_value = ResponseSuccess(rooms)

    http_response = client.get(
        "/rooms?filter_price__gt=2&filter_price__lt=6"
    )

    assert json.loads(http_response.data.decode("UTF-8")) == rooms_dicts

    mock_use_case.assert_called()
    args, kwargs = mock_use_case.call_args
    assert args[1].filters == {"price__gt": "2", "price__lt": "6"}

    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"


@pytest.mark.parametrize(
    "response_type, expected_status_code",
    [
        (ResponseTypes.PARAMETERS_ERROR, 400),
        (ResponseTypes.RESOURCE_ERROR, 404),
        (ResponseTypes.SYSTEM_ERROR, 500),
    ],
)
@mock.patch("application.rest.room.room_list_use_case")
def test_get_response_failures(
    mock_use_case,
    client,
    response_type,
    expected_status_code,
):
    mock_use_case.return_value = ResponseFailure(
        response_type,
        message="Just an error message",
    )

    http_response = client.get("/rooms?dummy_request_string")

    mock_use_case.assert_called()

    assert http_response.status_code == expected_status_code


