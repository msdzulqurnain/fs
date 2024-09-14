# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import base64
import re

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

from config import *


async def sub1(filter, client, update):
    if not FSUB1:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FSUB1, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub2(filter, client, update):
    if not FSUB2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FSUB2, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub3(filter, client, update):
    if not FSUB3:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FSUB3, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub4(filter, client, update):
    if not FSUB4:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FSUB4, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]



async def sub5(filter, client, update):
    if not FSUB5:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FSUB5, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub6(filter, client, update):
    if not FSUB6:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FSUB6, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub7(filter, client, update):
    if not FSUB7:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FSUB7, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub8(filter, client, update):
    if not FSUB8:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FSUB8, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub9(filter, client, update):
    if not FSUB9:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FSUB9, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def sub10(filter, client, update):
    if not FSUB10:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FSUB10, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def is_subscribed(filter, client, update):
    if not FSUB1:
        return True
    if not FSUB2:
        return True
    if not FSUB3:
        return True
    if not FSUB4:
        return True
    if not FSUB5:
        return True
    if not FSUB6:
        return True
    if not FSUB7:
        return True
    if not FSUB8:
        return True
    if not FSUB9:
        return True
    if not FSUB10:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FSUB1, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB2, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB3, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB4, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB5, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB6, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB7, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB8, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB9, user_id=user_id
        )
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FSUB10, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string


async def get_messages(client, message_ids):
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temb_ids = message_ids[total_messages : total_messages + 200]
        try:
            msgs = await client.get_messages(
                chat_id=client.db_channel.id, message_ids=temb_ids
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await client.get_messages(
                chat_id=client.db_channel.id, message_ids=temb_ids
            )
        except BaseException:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages


async def get_message_id(client, message):
    if (
        message.forward_from_chat
        and message.forward_from_chat.id == client.db_channel.id
    ):
        return message.forward_from_message_id
    elif message.forward_from_chat or message.forward_sender_name or not message.text:
        return 0
    else:
        pattern = "https://t.me/(?:c/)?(.*)/(\\d+)"
        matches = re.match(pattern, message.text)
        if not matches:
            return 0
        channel_id = matches.group(1)
        msg_id = int(matches.group(2))
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(client.db_channel.id):
                return msg_id
        elif channel_id == client.db_channel.username:
            return msg_id


subs1 = filters.create(sub1)
subs2 = filters.create(sub2)
subs3 = filters.create(sub3)
subs4 = filters.create(sub4)
subs5 = filters.create(sub5)
subs6 = filters.create(sub6)
subs7 = filters.create(sub7)
subs8 = filters.create(sub8)
subs9 = filters.create(sub9)
subs10 = filters.create(sub10)
subsall = filters.create(is_subscribed)
