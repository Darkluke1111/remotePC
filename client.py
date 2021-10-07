#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

        msg = await websocket.recv()
        print("Server sent: {}".format(msg))

asyncio.get_event_loop().run_until_complete(hello())