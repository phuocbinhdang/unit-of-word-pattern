from contextlib import contextmanager

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.session import Session

from src.infrastructures.databases.repositories.post import PostRepository
from src.infrastructures.databases.repositories.user import UserRepository


class UnitOfWork:
    _session: Session
    _session_factory: scoped_session | sessionmaker
    _user_repository: UserRepository
    _post_repository: PostRepository

    def __init__(self, session_factory: scoped_session | sessionmaker):
        self._session_factory = session_factory

    @property
    def user_repository(self) -> UserRepository:
        if not self._user_repository:
            self._user_repository = UserRepository(self._session)

        return self._user_repository

    @property
    def post_repository(self) -> PostRepository:
        if not self._post_repository:
            self._post_repository = PostRepository(self._session)

        return self._post_repository

    @contextmanager
    def transaction(self):
        self._session = self._session_factory()
        try:
            yield
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e
        finally:
            self._session.close()
