import asyncio
import signal
from datetime import datetime
from multiprocessing.connection import Connection, Listener

from pyrogram import Client
from pyrogram.errors import PeerIdInvalid

from settings import (
    API_HASH,
    API_ID,
    AUTH_KEY,
    CLIENT_NAME,
    CLOSE_SERVER_FLAG,
    IPC_IP,
    IPC_PORT,
)


async def send_notify(app: Client, receivers: list[int | str], message: str):
    failed_receivers: list[int | str] = []

    for receiver in receivers:
        try:
            await app.send_message(receiver, message, disable_web_page_preview=True)

        except PeerIdInvalid:
            failed_receivers.append(receiver)

    if failed_receivers:
        await app.send_message("me", f"無法傳送訊息給 {failed_receivers}。")


async def start_script(listener: Listener):
    await app.start()

    print("Script started.")
    loop = asyncio.get_event_loop()

    while True:
        try:
            conn: Connection = await loop.run_in_executor(None, listener.accept)

        except OSError:
            print("Server closed, exiting...")
            break

        print("訊息來自：", listener.last_accepted)
        received = conn.recv()

        if received == CLOSE_SERVER_FLAG:
            conn.close()
            break

        if isinstance(received, list):
            await send_notify(app, received[0], received[1])
            conn.close()
            print(f"地震通報結束於時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    await app.stop()


app: Client = Client(CLIENT_NAME, api_id=API_ID, api_hash=API_HASH)
listener: Listener = Listener((IPC_IP, IPC_PORT), authkey=AUTH_KEY)


def signal_handler(signum, frame):
    print("Stopping script with signal SIGINT...")
    listener.close()


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    app.run(start_script(listener))
