import pandas as pd
import websocket
import threading
import time


def on_message(ws, message):
    print(f"Received message: {message}")


def on_error(ws, error):
    print(f"Error occurred: {error}")


def on_close(ws):
    print("Connection closed. Trying to reconnect...")
    ws.run_forever()


def on_open(ws):
    print("Connection opened")


def run_websocket(ws_url, auth_header):
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url,
                                header={'Sec-WebSocket-Protocol': auth_header},
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()


if __name__ == "__main__":
    # Membaca data dari file Excel
    df = pd.read_excel('nama_file_excel.xlsx')
    # Mengambil URL websocket dan header authentication dari file Excel
    urls = df['URL'].tolist()
    headers = df['Header'].tolist()

    while True:
        for url, header in zip(urls, headers):
            threading.Thread(target=run_websocket, args=(url, header)).start()
        time.sleep(10)  # Jeda sebelum mencoba kembali
