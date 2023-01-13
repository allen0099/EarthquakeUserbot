import sys
from multiprocessing.connection import Client

from settings import AUTH_KEY, IPC_IP, IPC_PORT, SENDING_TARGETS, SENDING_TEXT

if __name__ == "__main__":
    args: list[str] = sys.argv[1:]

    conn: Client = Client((IPC_IP, IPC_PORT), authkey=AUTH_KEY)
    conn.send(
        [
            SENDING_TARGETS,
            SENDING_TEXT.format(level=args[0], seconds=args[1]),
        ]
    )
    conn.close()
