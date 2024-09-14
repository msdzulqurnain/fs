# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from bot import Bot
from config import *
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from .button import start_button
from .data import *

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "home":
        out = start_button(client)
        await query.message.edit_text(
            text=START_MSG.format(
                first=query.from_user.first_name,
                last=query.from_user.last_name,
                username=f"@{query.from_user.username}"
                if query.from_user.username
                else None,
                mention=query.from_user.mention,
                id=query.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(out),
            disable_web_page_preview=True
            )
    elif data == "about":
        await query.message.edit_text(
            text=INFO,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Kembali", callback_data="home")]]
            ),
        )
    elif data == "cmd":
        await query.message.edit_text(
            text=CMD_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Kembali", callback_data="home")]]
            ),
        )
    elif data == "btn":
        await query.answer(
            text=BTN_TEXT.format(BUTTONS),
            show_alert=True
            )
    elif data == "tutor":
        await query.message.edit_text(
            text=TUTOR_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Kembali", callback_data="home")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
