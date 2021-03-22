from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

PM_HELP_TEXT = """Add @VCPlayAssistant and @VCPlay_Robot to your group\n
**Usage:**
Inline - `@VCPlay_Robot Yt video name`
Normal - `/play Yt link`\n
**Other Commands:**
/start : `Just for fun XD`
/search : `For inline search buttons`
/pause : `to pause the song`
/resume : `to resume the song`
/end : `to stop streaming`
/next : `to play next song`
/ping : `to check the ping`
/admincache : `to refresh the admin cache`\n
For queries contact owner"""


@Client.on_message(filters.command(["help", "help@VCPlay_Robot"]))
async def help(client, message):
    await message.reply_text(
     PM_HELP_TEXT,
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('👑Owner👑', url='https://t.me/DetectiveVI')
                ],
                [

                    InlineKeyboardButton('🎸Assistant🎸', url='https://t.me/VCPlayAssistant')
                ]
            ]
        )
    ) 
