import time
from pyrogram import Client, filters

@Client.on_message(
    filters.command(["ping", "ping@VCPlay_Robot"])
    & filters.group
    & ~ filters.edited
)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pong!")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@Client.on_message(
    filters.command("ping")
    & filters.private
    & ~ filters.edited
)
async def ping_(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pong!")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
