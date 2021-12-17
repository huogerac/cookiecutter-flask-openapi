import pytest

import sqlalchemy as sa
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.ext.database import db
from {{cookiecutter.project_slug}}.models.users import User
from {{cookiecutter.project_slug}}.services.token import generate_token


@pytest.fixture(scope="session")
def app():
    app = create_app()
    with app.app_context():
        db.create_all(app=app)
        yield app
        db.drop_all(app=app)


@pytest.fixture(autouse=True)
def db_session(app):
    conn = db.engine.connect()
    trans = conn.begin()

    session = Session(bind=conn)
    session.begin_nested()

    # then each time that SAVEPOINT ends, reopen it
    @sa.event.listens_for(db.session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.expire_all()
            session.begin_nested()

    db.session.begin_nested()

    yield db.session

    # rollback everything
    trans.rollback()
    conn.close()
    db.session.remove()


@pytest.fixture()
def user_mock(db_session):
    new_user = User(username="jd", email="john@doe.com", name="John Doe")
    db_session.add(new_user)
    db_session.commit()
    return new_user


@pytest.fixture()
def token_valid_mock(user_mock):
    return generate_token(user_mock)
