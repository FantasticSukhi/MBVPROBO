class Config(object):
    LOGGER = True
    API_ID =20353207 
    API_HASH = "e5b2ac2f9c37bda345fa9fb5ade66961"
    TOKEN = "7803412058:AAFlrT_BOEXAQTY7DrEwap3U-LnFHfuQFys"  
    OWNER_ID=6713994904
    SUPPORT_CHAT = "MBV_CHATS" 
    START_IMG = "https://i.ibb.co/mTqzjHK/file-6723.jpg"
    EVENT_LOGS = (-1002138809373)
    MONGO_DB_URI= "mongodb+srv://Sukhi:starboy333@cluster0.jb9uy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_URL = "postgres://mcclbjwx:CqMrbec47cqL5KbaZOUDlVQWOscjNcKR@peanut.db.elephantsql.com/mcclbjwx"
    CASH_API_KEY = (
        "cpzwadqyiwbplccvissfnapimzloqwvl"
    )
    TIME_API_KEY = "9LMMJQ30GM49"

    
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
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
