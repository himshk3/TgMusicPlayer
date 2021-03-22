from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command


@Client.on_message(command(["start", "start@VCPlay_Robot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am @VCPlay_Robot an open-source bot that lets you play music in your Telegram groups.
Use the buttons below to know more about me.
Use /help for more info""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡️Owner⚡️", url="https://t.me/DetectiveVI"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Assistant", url="https://t.me/VCPlayAssistant"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["search", "search@VCPlay_Robot"]) & other_filters)
async def search(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("search") & other_filters2)
async def search(_, message: Message):
    await message.reply_text(
        "❕ This command works only in groups only")