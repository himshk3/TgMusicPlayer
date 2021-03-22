import time
from pyrogram import Client

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command(["ping", "ping@VCPlay_Robot"]) & other_filters)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pong!")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@Client.on_message(command("ping") & other_filters2)
async def ping_(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pong!")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
