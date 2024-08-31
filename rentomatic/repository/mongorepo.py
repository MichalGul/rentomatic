import pymongo

from rentomatic.domain import room


class MongoRepo:
    def __init__(self, configuration):
        client = pymongo.MongoClient(host=configuration["MONGODB_HOSTNAME"],
                                     port=int(configuration["MONGODB_PORT"]),
                                     username=configuration["MONGODB_USER"],
                                     password=configuration["MONGODB_PASSWORD"],
                                     authSource="admin")
        self.db = client[configuration["APPLICATION_DB"]]

    def _create_room_objects(self, results):
        return [room.Room(
            code=r["code"],
            size=r["size"],
            price=r["price"],
            latitude=r["latitude"],
            longitude=r["longitude"]) for r in results]


    def list(self, filters=None):
        collections = self.db.rooms

        if filters is None:
            results = collections.find()
        else:
            mongo_filter = {}

            for key, value in filters.items():
                key, operator = key.split("__")

                filter_value = mongo_filter.get(key, {})

                if key == "price":
                    value = int(value)

                filter_value[f"${operator}"] = value # $gt, $lt i tak dalej
                mongo_filter[key] = filter_value

            results = collections.find(mongo_filter)
        return self._create_room_objects(results)
