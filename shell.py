# the following code awas joint contribution by all authors that collaborated
import main
import threading
from main import free_ip
import asyncio

async def release_ip(ip):
    global free_ip
    await asyncio.sleep(60)
    free_ip.append(ip)

async def shell():
    while True:
        command = input("> ")
        if command.lower() == 'ask':
            given_ip = main.delegate()
            await release_ip(given_ip)

asyncio.run(shell())