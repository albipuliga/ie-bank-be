from iebank_api.models import Account


def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account("John Doe", "€", "Italy")
    assert account.name == "John Doe"
    assert account.currency == "€"
    assert account.account_number is not None
    assert account.balance == 0.0
    assert account.status == "Active"
    assert account.country == "Italy"
    
def test_edit_account():
    """
    GIVEN a Account model
    WHEN a new Account is created and edited
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account("John Doe", "€", "Italy")
    account.name = "Jane Doe"
    account.currency = "$"
    account.country = "USA"
    assert account.name == "Jane Doe"
    assert account.currency == "$"
    assert account.country == "USA"
    assert account.account_number is not None
    assert account.balance == 0.0
    assert account.status == "Active"