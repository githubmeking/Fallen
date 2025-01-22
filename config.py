from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID",'20213849'))
API_HASH = getenv("API_HASH","e97df0eca2a9531c80202c1a7d3f5721")

BOT_TOKEN = getenv("BOT_TOKEN","6591274198:AAFFsE0pTw3tUE9kq49QjUBarwLaQTdjurY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID",6180151150))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AgDY4YEATvn3sIR0kiN1sOLkAONRhouL-KGZtyDH-EMS-34a_muXwk60pfuL4b-uqq-MniAlll9wQRb2Fc7SVpPILHAxvp38bzLHssWLvSl0O9Evo1BtB9Pki1awykxVgeOjiVJxBaU1ynHkvm_dPhNHhYnOJMDTiqWL0v9O6UMvcpF8OS9OnbQuvsDDE-xCu7lhLMAiQb_sk-wpGYyE9bpzvb89whwUMPp1Zv-03VZZIjPUrcWU-qheggjhD7AiwxaWFBsP69RaNCZ_NTz18T8yl6Cnx6xiwsEPrJFxINrw3RHC5n9Eu-2FToZlrEhIaxeOZHsje0RQ_yCdyRs0BzC5HpwR4gAAAAE1ZEE9AA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6180151150").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
