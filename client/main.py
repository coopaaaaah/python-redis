import redis
import random
from datetime import datetime, timedelta
from enum import Enum
import time
import random
import os
class Type(Enum):
    BARTER_PAYOUT = "BARTER_PAYOUT"
    F4B_PAYOUT_BANK_TRANSFER = "F4B_PAYOUT_BANK_TRANSFER"
    ACQUIRED_COM_CARD = "ACQUIRED_COM_CARD"
    PAYPAL = "PAYPAL"
    ANDROID_POS = "ANDROID_POS"
    FAWRY_PAY = "FAWRY_PAY"
    F4B_PAYOUT_WALLET = "F4B_PAYOUT_WALLET"
    F4R = "F4R"
    WITHDRAWAL = "WITHDRAWAL"
    MVISA_QR = "MVISA_QR"
    BARTER_TO_BARTER = "BARTER_TO_BARTER"
    MOBILEMONEY = "MOBILEMONEY"
    VOUCHER = "1VOUCHER"
    FLUTTERWAVE = "FLUTTERWAVE"
    CPOS_TERMINAL = "CPOS_TERMINAL"
    APPLEPAY = "APPLEPAY"
    CRYPTOCURRENCY = "CRYPTOCURRENCY"
    BARTER_PAYMENT = "BARTER_PAYMENT"
    BANKREFERENCE = "BANKREFERENCE"

r = redis.Redis(host='cache', port=6379, db=0)
KEY = os.getenv("KEY")

for v in range(100000):
    expiration = datetime.now() - timedelta(hours=0, minutes=1)
    value = {random.choice(list(Type)).value: time.mktime(expiration.timetuple())}
    print(f"{value} coming in...")
    r.zadd(KEY, value, gt=True)
    time.sleep(random.randint(1, 5))    