import asyncio
import websockets
import json


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"Client sent: {name}")

        from_server = await websocket.recv()
        data = json.loads(from_server)
        print(f"Client received: {data['b']}")


if __name__ == "__main__":
    asyncio.run(hello())
