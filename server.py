# -*- coding: utf-8 -*-

import asyncio
import os

import websockets
from dotenv import load_dotenv

load_dotenv()


async def handle_connection(websocket, path):
    print(f"Connection path: {path}")
    try:
        while True:
            message = await websocket.recv()
            print(f"Receive: {message}")
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Disconnected")


if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    port = os.environ.get('PORT', 3033)
    start_server = websockets.serve(handle_connection, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    print(f"Server started at {host}:{port}")
    asyncio.get_event_loop().run_forever()
