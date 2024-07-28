import json
import uuid


from rentomatic.domain.room import Room
from rentomatic.serializers.room import RoomJsonEncoder


def test_serialize_domain_room():
    code = uuid.uuid4()

    room = Room(
        code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    # double curly braces are user to avoid clash with f-string formater
    expected_json = f"""
        {{
            "code": "{code}",
            "size": 200,
            "price": 10,
            "longitude": -0.09998975,
            "latitude": 51.75436293
        }}
    """

    # override standard json dumps encoder with custom created
    json_room = json.dumps(
        room,
        cls=RoomJsonEncoder
    )

    # convert back to dicts to avoid order of attribute mistakes
    assert json.loads(json_room) == json.loads(expected_json)
