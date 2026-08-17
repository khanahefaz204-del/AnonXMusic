from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 33104596))
        self.API_HASH = getenv("API_HASH", "51f399f1fe29e2df98a3d887b91aa02b")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8933764200:AAHZlADFBHHyKdy1-Y_qfvxrWxUyAEWddX4")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", -1003150808065))
        self.OWNER_ID = int(getenv("OWNER_ID", 7916680074))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "BQIvqxMAAP-eUqgBxRpVTiOFtAvuDTXyeU7IWUfvr38HZ1Qm82XBdICNm1Jhuf-yxcKl52xH0z4exEh8XHToUMgMjB95U9Nk1NqAATZkLI1w1w0NUSr6dWwvVpoKlwjBZDPVun8mjKOuUR6nodd9Cet73n-ZBxftoXJlUUQHjgkXvw9JrsTtyHkz8Ni8pXSlfycnvHx_-yTY1CpfiSlqf55VZ4p7ZmJvwE7eEs-XRXbmodoeqEdwsKBhCylyIjfpRC2GklCU1lz3Tp_ONshhLnXjcUA7CAsCuxR9-C7KbOqWH5RQvy2ISz3r-auV0gkb3-LF-_gT4avV2oiLnMp0E6ch3fBObgAAAAH1K81xAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fallenx")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"

        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/deejay").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
