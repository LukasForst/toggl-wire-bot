import json

import websocket

from Utils.systemUtils import getRomanToken
from Wire.MessageHandler import processMessage

try:
    import thread
except ImportError:
    import _thread as thread
import time


def on_message(ws, message):
    data = json.loads(message)
    print(data)
    processMessage(data)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")
    thread.start_new_thread(runWebsocket, ())


def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")

    thread.start_new_thread(run, ())


def runWebsocket():
    websocket.enableTrace(True)
    token = getRomanToken()
    ws = websocket.WebSocketApp(
        f"ws://proxy.services.zinfra.io/await/{token}",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws.run_forever(ping_interval=30)
