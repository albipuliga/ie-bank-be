from flask import request

from iebank_api import app, db
from iebank_api.models import Account


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/skull", methods=["GET"])
def skull():
    text = "Hi! This is the BACKEND SKULL!"

    if db.engine.url.database:
        text = text + "<br/>Database URL:" + db.engine.url.database
    if db.engine.url.host:
        text = text + "<br/>Database host:" + db.engine.url.host
    if db.engine.url.port:
        text = text + "<br/>Database port:" + str(db.engine.url.port)
    if db.engine.url.username:
        text = text + "<br/>Database user:" + db.engine.url.username
    if db.engine.url.password:
        text = text + "<br/>Database password:" + db.engine.url.password
    return text


@app.route("/accounts", methods=["POST"])
def create_account():
    if not request.json:
        return {"error": "Invalid input"}, 400

    name = request.json.get("name")
    currency = request.json.get("currency")
    country = request.json.get("country")
    account = Account(name, currency, country)
    db.session.add(account)
    db.session.commit()
    return format_account(account)


@app.route("/accounts", methods=["GET"])
def get_accounts():
    accounts = Account.query.all()
    return {"accounts": [format_account(account) for account in accounts]}


@app.route("/accounts/<int:id>", methods=["GET"])
def get_account(id):
    account = Account.query.get(id)
    return format_account(account)


@app.route("/accounts/<int:id>", methods=["PUT"])
def update_account(id):
    account = Account.query.get(id)
    if not request.json:
        return {"error": "Invalid input"}, 400
    if account is None:
        return {"error": "Account not found"}, 404

    account.name = request.json.get("name")
    account.country = request.json["country"]
    db.session.commit()
    return format_account(account)


@app.route("/accounts/<int:id>", methods=["DELETE"])
def delete_account(id):
    account = Account.query.get(id)
    db.session.delete(account)
    db.session.commit()
    return format_account(account)


def format_account(account):
    return {
        "id": account.id,
        "name": account.name,
        "account_number": account.account_number,
        "balance": account.balance,
        "currency": account.currency,
        "country": account.country,
        "status": account.status,
        "created_at": account.created_at,
    }
