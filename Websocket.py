import websocket, json
import datetime

milliseconds_since_epoch = datetime.datetime.now().timestamp() * 1000


def on_message(ws, message):
    emitedmessage  = json.loads(message)
    print(emitedmessage["result"]["data"][0]["bids"])


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("connection opened")
    subReq = {
        "id": 11,
        "method": "subscribe",
        "params": {
            "channels": ["book.CRO_USDT.10"]
        },
        "nonce": milliseconds_since_epoch,
    }
    ws.send(json.dumps(subReq))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://stream.crypto.com/v2/market",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
    
