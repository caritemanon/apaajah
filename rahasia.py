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
