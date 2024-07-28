import json


class RoomJsonEncoder(json.JSONEncoder):
    # override defauly to support encoding Room objects
    def default(self, o):
        try:
            # not using o.as_dict because uid.UUID is not json serializable.
            # to_serialize = {
            #     "code": str(o.code),
            #     "size": o.size,
            #     "price": o.price,
            #     "latitude": o.latitude,
            #     "longitude": o.longitude
            # }

            # or this below manually handle uid.UUID field
            to_serialize = o.to_dict()
            to_serialize['code'] = str(to_serialize['code'])

            return to_serialize

        except AttributeError:
            return json.JSONEncoder.default(self, o)
