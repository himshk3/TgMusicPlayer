from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command


@Client.on_message(command(["start", "start@Mahi_bhai_7_bot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>
I am @Mahi_bhai_7_bot an open-source bot that lets you play music in your Telegram groups.
Use the buttons below to know more about me.
Use /help for more info""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡️Owner⚡️", url="https://t.me/Mahi_bhai_7"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Assistant", url="https://t.me/Mahi_bhai_007"
                    )
                ]
            ]
        )
    )
