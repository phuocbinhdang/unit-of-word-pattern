from sqlalchemy.orm.session import Session

from src.infrastructures.databases.schemas.post import Post


class PostRepository:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def save(self, entity: Post) -> Post:
        self._session.add(entity)
        self._session.flush()

        return entity

    def delete(self, entity: Post):
        self._session.delete(entity)
        self._session.flush()

    def find_by_id(self, id: int) -> Post | None:
        entity = self._session.query(Post).filter(Post.id == id).first()

        return entity

    def find_all(self, offset: int, limit: int) -> tuple[list[Post], int]:
        query = self._session.query(Post)

        total = query.count()
        entities = query.offset(offset * limit).limit(limit).all()

        return entities, total
