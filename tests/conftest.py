import pytest

from iebank_api import app, db
from iebank_api.models import Account


@pytest.fixture
def testing_client(scope="module"):
    with app.app_context():
        db.create_all()
        account = Account("Test Account", "€", country="Italy")
        db.session.add(account)
        db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    with app.app_context():
        db.drop_all()
