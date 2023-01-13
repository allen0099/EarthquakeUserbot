API_ID: int = 12345  # TG API ID
API_HASH: str = "abcdefg1234567"  # TG API Hash
CLIENT_NAME: str = "EarthquakeNotifier"  # Session 名稱

IPC_IP: str = "localhost"  # 溝通用的 IP
IPC_PORT: int = 24680  # 溝通用的 port
AUTH_KEY: bytes = (
    b"change_me"  # 執行 `python -c "import os; print(os.urandom(16))"` 來產生一組新的 key
)
CLOSE_SERVER_FLAG: str = "close server"  # 關閉伺服器的 flag

SENDING_TARGETS: list[str] = [
    "-1001234567890",  # 群組 ID
    "@allen0099",  # 或是使用者 ID，群組 ID 也行
    # 可以往下加更多
]
SENDING_TEXT: str = (
    "[有感地震警報] "
    "<b><u>新北市 板橋區</u></b>\n"
    "發生 <b>{level}</b> 級地震，"
    "預計於 <b>{seconds}</b> 秒後抵達。\n"
    "\n"
    "請保持冷靜，保護頭頸安全並就地趴下尋找掩護。\n"
    "地震發生後如需疏散，請先關閉火源及電源。\n"
    "疏散時請勿使用電梯，並注意踩踏障礙物。\n"
    "\n"
    "資料來源：\n"
    "[地牛 Wake up!](https://eew.earthquake.tw/)\n"
    "[氣象局](https://www.cwb.gov.tw/V8/C/E/index.html)\n"
    "* 此為 <b><u>自動化發送</u></b> 訊息\n"
    "* 請以氣象局資料為準"
)
# 把 SENDING_TEXT 改成你想要的訊息，其中 {level} 會被替換成地震等級，{seconds} 會被替換成距離抵達的秒數
# For more info, read https://www.runoob.com/python/att-string-format.html
