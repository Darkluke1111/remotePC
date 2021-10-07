#!/usr/bin/env python

import asyncio
import websockets
import aioconsole

async def consumer_handler(websocket, path):
    async for message in websocket:
        await consumer(message)

async def producer_handler(websocket, path):
    while True:
        message = await producer()
        await websocket.send(message)

async def handler(websocket, path):
    consumer_task = asyncio.ensure_future(
        consumer_handler(websocket, path))
    producer_task = asyncio.ensure_future(
        producer_handler(websocket, path))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()

async def producer():
    msg = await aioconsole.ainput('Is this your line? ')
    return msg

async def consumer(msg):
    print("> {}".format(msg))

start_server = websockets.serve(handler, '0.0.0.0', 80)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()