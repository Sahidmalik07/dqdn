import os, re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '19455849'))
API_HASH = environ.get('API_HASH', '71498d69fad014add7e9f717bfde4b79')
BOT_TOKEN = environ.get('BOT_TOKEN', '5338333469:AAEiqFHWVcxwBOicg52apOrpRqsxAzDCDLQ')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()
MALIK_PH = environ.get("MALIK_PH", "https://telegra.ph/file/0547d69b90b596ad6bae1.jpg")
VIDEO_VD = environ.get("VIDEO_VD", "https://telegra.ph/file/566ff238e36d9f2425568.mp4")
PHT = environ.get("PHT", "https://telegra.ph/file/9b77b96a9d2f5dda7764b.jpg")
PHTT = environ.get("PHTT", "https://telegra.ph/file/7dc82878492b8f64bb7eb.jpg")
M_NT_F = environ.get("M_NT_F", "https://telegra.ph/file/b9c8a8240590623ba43ee.jpg")

#part 1

DEL_SECOND = int(os.environ.get("DEL_SECOND", "300"))
CREATOR_USERNAME = os.environ.get("CREATOR_USERNAME", "sahid_malik")
CREATOR_NAME = os.environ.get("CREATOR_NAME", "sahid malik")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "hjhjvjjjvbot")

#part 2
MALIK = environ.get("malik", "https://telegra.ph/file/a35a995c9c411048adfab.jpg")
MALIK5 = environ.get("malik5", "https://telegra.ph/file/a00c405a374d21ea7cfb7.jpg")


AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
AUTO_DELETE2 = is_enabled((environ.get('AUTO_DELETE2', "True")), True)

#part 3

FILTER_BUTTONS = os.environ.get("FILTER_BUTTONS", "10")
DB_AUTO_DELETE = is_enabled((environ.get('DB_AUTO_DELETE', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)


PMFILTER = bool(environ.get("PMFILTER", True))
G_FILTER = bool(environ.get("G_FILTER", True))
BUTTON_LOCK = bool(environ.get("BUTTON_LOCK", True))
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")

PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5217619970').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001687091406').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
PM_LOG_CHANNEL = int(environ.get('PM_LOG_CHANNEL', 0))
LOG_CHANNEL2 = int(environ.get('LOG_CHANNEL2', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'm_house786')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<code>{file_name}</code>\n\n┏━━━━•❅•°•❈•°•❅••━━━━┓\n✰👑 <b>𝐉𝐨𝐢𝐧  [ 𝙈𝙤𝙫𝙞𝙚𝙨 𝙂𝙧𝙤𝙪𝙥 ](https://t.me/+FAgX05kGByNkZjJl)</b>  👑✰\n┗━━━━•❅•°•❈•°•❅•━━━━┛")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", None)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

SHORTENER_API = environ.get("SHORTENER_API", "iQ2iqO9EXFbcjek412Dg5j6stWu2")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shareus.in")
SHORT_URL = is_enabled((environ.get('SHORT_URL', "False")), False)
TUTORIAL_LINK = environ.get("TUTORIAL_LINK", "https://youtu.be/MKNd7AP5xLE")



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


REQ_GRP = int(environ.get('REQ_GRP', '-1001566860282'))
