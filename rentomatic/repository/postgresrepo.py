from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rentomatic.domain import room
from rentomatic.repository.postgres_objects import Base, Room

class PostgresRepo:
    def __init__(self, configuration):
        connection_string = f"postgresql+psycopg2://{configuration['POSTGRES_USER']}:{configuration['POSTGRES_PASSWORD']}@{configuration['POSTGRES_HOSTNAME']}:{configuration['POSTGRES_PORT']}/{configuration['APPLICATION_DB']}"
        self.engine = create_engine(connection_string)

        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    def _create_room_objects(self, results):
        return [
            room.Room(
                code=r.code,
                size=r.size,
                price=r.price,
                longitude=r.longitude,
                latitude=r.latitude
            )
            for r in results
        ]

    def list(self, filters=None):
        DBSession = sessionmaker(self.engine)
        session = DBSession()

        query = session.query(Room)

        if filters is None:
            return self._create_room_objects(query.all())

        if "code__eq" in filters:
            query = query.filter(Room.code == filters["code__eq"])

        if "price__eq" in filters:
            query = query.filter(Room.price == filters["price__eq"])

        if "price__lt" in filters:
            query = query.filter(Room.price < filters["price__lt"])

        if "price__gt" in filters:
            query = query.filter(Room.price > filters["price__gt"])

        return self._create_room_objects(query.all())
