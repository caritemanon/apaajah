import sys
import time
import asyncio

from telethon import TelegramClient, events
from telethon.sessions import StringSession
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import FloodWaitError


a = API_ID
b = API_HASH
rommel = STRING
tata = STRING2
siska = STRING3
koko = STRING4
ojie = STRING5



rml = ""
tta = ""
ska = ""
kko = ""
oji = ""



que = {}

ROMMEL_USERS = []
for x in SUDO: 
    ROMMEL_USERS.append(x)
    
async def start_yukki():
    global rml
    global tta
    global ska
    global kko
    global oji
    if rommel:
        session_name = str(rommel)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
