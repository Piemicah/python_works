import asyncio
import websockets
import json


async def hello(websocket):
    name = await websocket.recv()
    print(f"Server Received: {name}")
    greeting = f"Hello {name}!"

    await websocket.send(json.dumps({"a": 9, "b": 2}))
    print(f"Server Sent: {greeting}")


async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
