import re
import sys
from os import getenv


from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()



API_ID = 20650066

API_HASH = getenv("7a4f8ed638f1369a40693574c2835217")



BOT_TOKEN = getenv("7970949227:AAHHqi_yNrnpN4w0criBvVri_YX6D1BmUKg")



MONGO_DB_URI = getenv("mongodb+srv://anjlnobita:tCUPU9Ty1FFvLumv@cluster0.appf0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")




LOG_GROUP_ID = -1002372313866


# Your User ID.
OWNER_ID = 6777860063


DRAGONS = 6777860063
DEV_USERS = 6777860063
DEMONS = 6777860063
TIGERS = 6777860063
WOLVES = 6777860063



SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/anjlnobita"
)


SUPPORT_CHAT = getenv(
    "SUPPORT_GROUP", "https://t.me/anime_societyy"
)



BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
TEMP_DB_FOLDER = "anjlnobita"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
votemode = {}
confirmer = {}
autoclean = []


EVENT_LOGS = ()  


BL_CHATS = [] 
DRAGONS = [] 
DEV_USERS = []  
DEMONS = []  
TIGERS = [] 
WOLVES = [] 


ALLOW_CHATS = True
ALLOW_EXCL = True
DEL_CMDS = True
INFOPIC = True
LOAD = []
NO_LOAD = []
STRICT_GBAN = True
WORKERS = 8