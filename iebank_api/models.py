import random
import string
from datetime import datetime

from iebank_api import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    account_number = db.Column(db.String(20), nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    currency = db.Column(db.String(1), nullable=False, default="€")
    country = db.Column(db.String(32), nullable=False, default="Unknown")
    status = db.Column(db.String(10), nullable=False, default="Active")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Event %r>" % self.account_number

    def __init__(self, name, currency, country):
        self.name = name
        self.account_number = "".join(random.choices(string.digits, k=20))
        self.currency = currency
        self.balance = 0.0
        self.country = country
        self.status = "Active"
