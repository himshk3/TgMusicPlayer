from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

import callsmusic

import converter
import youtube
import queues

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError
from helpers.filters import command, other_filters
from helpers.wrappers import errors

@Client.on_message(
    filters.command(["play", "play@VCPlay_Robot"])
    & filters.group
    & ~ filters.edited
)
@errors
async def play(client: Client, message_: Message):
    audio = (message_.reply_to_message.audio or message_.reply_to_message.voice) if message_.reply_to_message else None

    res = await message_.reply_text("😴 Processing...")

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {audio.duration / 60} minute(s)"
            )

        file_name = audio.file_id + audio.file_name.split(".")[-1]
        file_path = await convert(await message_.reply_to_message.download(file_name))
    else:
        messages = [message_]
        text = ""
        offset = None
        length = None

        if message_.reply_to_message:
            messages.append(message_.reply_to_message)

        for message in messages:
            if offset:
                break

            if message.entities:
                for entity in message.entities:
                    if entity.type == "url":
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break

        if offset == None:
            await res.edit_text("Give me a youtube link nub😒")
            return

        url = text[offset:offset+length]

        file_path = await convert(download(url))

    try:
        is_playing = False
    except:
        is_playing = True

    if is_playing == False:
        await res.edit_text("🥳 Playing...")
        tgcalls.pytgcalls.join_group_call(message_.chat.id, file_path, 48000)
        mystryque = None

    if mystryque is None:
        position = await sira.add(message_.chat.id, file_path)
        await res.edit_text(f"🔥 Song is postioned at {position}th.")
