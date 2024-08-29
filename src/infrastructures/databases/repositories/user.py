from src.infrastructures.databases.schemas.user import User
from sqlalchemy.orm.session import Session


class UserRepository:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def save(self, entity: User) -> User:
        self._session.add(entity)
        self._session.flush()

        return entity

    def delete(self, entity: User):
        self._session.delete(entity)
        self._session.flush()

    def find_by_id(self, id: int) -> User | None:
        entity = self._session.query(User).filter(User.id == id).first()

        return entity

    def find_all(self, offset: int, limit: int) -> tuple[list[User], int]:
        query = self._session.query(User)

        total = query.count()
        entities = query.offset(offset * limit).limit(limit).all()

        return entities, total
