#!/usr/bin/env python3

import asyncio
import websockets
from time import time

# Define the handler for incoming WebSocket connections
async def echo(websocket):
    async for message in websocket:
        print("\x1b[H\x1b[2J\x1b[3J") # Clear
        print(f"Received: {message}")
        name = "%d.mp4" % (time(),)
        with open(name, "xb") as f:
            f.write(message)
            print("Wrote %s\n" % (name,))
#        await websocket.send(message)
#        print(f"Sent: {message}")

# Main function to start the WebSocket server
async def main():
    async with websockets.serve(echo, "localhost", 8765, max_size=None):
        await asyncio.Future()  # Run forever

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
