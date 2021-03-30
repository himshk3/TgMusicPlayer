import queue

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

import queues
import cache.admins

from helpers.filters import command, other_filters, other_filters2
from helpers.wrappers import errors, admins_only


@Client.on_message(command(["pause", "pause@Mahi_bhai_7_bot"]) & other_filters)
@errors
@admins_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text("❕ Nothing is playing.")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("⏸ Paused.")

@Client.on_message(command("pause") & other_filters2)
async def pause_(_, message: Message):
    await message.reply_text(
        "❕ This command works in groups only")


@Client.on_message(command(["resume", "resume@Mahi_bhai_7_bot"]) & other_filters)
@errors
@admins_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text("❕ Nothing is paused.")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("▶️ Resumed.")

@Client.on_message(command("resume") & other_filters2)
async def resume_(_, message: Message):
    await message.reply_text(
        "❕ This command works in groups only")


@Client.on_message(command(["end", "end@Mahi_bhai_7_bot"]) & other_filters)
@errors
@admins_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❕ Nothing is streaming.")
    else:
        try:
            queues.clear(message.chat.id)
        except queue.Empty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("⏹ Ended streaming.")

@Client.on_message(command("end") & other_filters2)
async def stop_(_, message: Message):
    await message.reply_text(
        "❕ This command works in groups only")


@Client.on_message(command(["next", "next@Mahi_bhai_7_bot"]) & other_filters)
@errors
@admins_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❕ Nothing is playing to skip to next song.")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(message.chat.id, queues.get(message.chat.id)["file_path"])

        await message.reply_text("⏩ Playing next the current song.")

@Client.on_message(command("next") & other_filters2)
async def skip_(_, message: Message):
    await message.reply_text(
        "❕ This command works in groups only")


@Client.on_message(command(["admincache", "admincache@Mahi_bhai_7_bot"]) & other_filters)
@errors
@admins_only
async def admincache(_, message: Message):
    cache.admins.set(
        message.chat.id,
        [member.user for member in await message.chat.get_members(filter="administrators")]
    )
    await message.reply_text("❇ Admin cache refreshed!")

@Client.on_message(command("admincache") & other_filters2)
async def admincache_(_, message: Message):
    await message.reply_text(
        "❕ This command works in groups only")
