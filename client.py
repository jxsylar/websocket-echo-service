# -*- coding: utf-8 -*-

import asyncio
import os

import websockets
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get('HOST', '127.0.0.1')
port = os.environ.get('PORT', 3033)


async def send_message():
    async with websockets.connect(f'ws://{host}:{port}') as ws:
        while True:
            message = input("Input message, <enter> to send, 'q' to exit: ")
            if message == 'q':
                break

            await ws.send(message)
            print(f"Send: {message}")

            try:
                response = await asyncio.wait_for(ws.recv(), timeout=60)
                print(f"Received: {response}")
            except asyncio.TimeoutError:
                print("Received timeout")

        await ws.close()
        print("Websocket closed")


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(send_message())
