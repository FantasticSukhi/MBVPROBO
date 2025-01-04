class Config(object):
    LOGGER = True
    API_ID =20353207 
    API_HASH = "e5b2ac2f9c37bda345fa9fb5ade66961"
    TOKEN = "7803412058:AAFLOVUwVwCxLSF0X0rtkKQQbv6zSCsz5wE"  
    OWNER_ID=6713994904
    
    SUPPORT_CHAT = "-1002124344872" 
    START_IMG = "https://i.ibb.co/mTqzjHK/file-6723.jpg"
    EVENT_LOGS = (-1002138809373)
    MONGO_DB_URI= "mongodb+srv://SUKHI:starboy333@mamba.jb9uy.mongodb.net/?retryWrites=true&w=majority&appName=Mamba"
   
    DATABASE_URL = "postgres://mcclbjwx:CqMrbec47cqL5KbaZOUDlVQWOscjNcKR@peanut.db.elephantsql.com/mcclbjwx"  # A sql database url from elephantsql.com
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
