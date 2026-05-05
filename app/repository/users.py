from sqlalchemy.orm import Session

from app.models import User


def get_user(db: Session, login: str) -> User | None:
    return db.query(User).filter(User.login == login).scalar()
    # scalar - чтобы алхимия превратила результат в экземпляр класса User


def create_user(db: Session, login: str) -> User:
    user = User(login=login)
    db.add(user)
    db.flush() # Производиться INSERT в базе, но не коммитится
    return user