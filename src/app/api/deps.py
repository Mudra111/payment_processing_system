from src.app.infrastructure.database.session import LocalSession


def get_db():
    session = LocalSession()

    try:
        yield session
    finally:
        session.close()
