# Don't Remove Credit @kr_1updates
# Subscribe YouTube Channel For Amazing Bot @kr_1updates
# Ask Doubt on telegram @KR5updates


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7260188955:AAGXsDir_WyU2jWoItc2QAkVItaK0yajL_E")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN",7260188955:AAGXsDir_WyU2jWoItc2QAkVItaK0yajL_E "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot kr_1updates
             # Ask Doubt on telegram @KR5updates

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @kr_1updates
# Subscribe YouTube Channel For Amazing Bot KR5updates
# Ask Doubt on telegram @kr_1updates
