import uuid
from src.domain.room import Room


def test_room_model_init():
    code = uuid.uuid4()
    room = Room(
        code,
        size=10,
        price=100,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    assert room.code == code
    assert room.size == 10
    assert room.price == 100
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "size": 10,
        "price": 100,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    }
    room = Room.from_dict(init_dict)

    assert init_dict["code"] == code
    assert init_dict["size"] == 10
    assert init_dict["price"] == 100
    assert init_dict["longitude"] == -0.09998975
    assert init_dict["latitude"] == 51.75436293
