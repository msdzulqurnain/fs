# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FSUB1, FSUB2, FSUB3, FSUB4, FSUB5, FSUB6, FSUB7, FSUB8, FSUB9, FSUB10
from pyrogram.types import InlineKeyboardButton


BTN = [
    [
       InlineKeyboardButton(text="Tentang saya👤", callback_data="about"),
    ],
    [
       InlineKeyboardButton(text="Perintah", callback_data="cmd"),
       InlineKeyboardButton(text="Button", callback_data="btn"),
    ],
    [
       InlineKeyboardButton(text="Tutorial", callback_data="tutor"),
       InlineKeyboardButton(text="Jasa bot", url="https://t.me/DezetStore/4"),
    ],
    [
       InlineKeyboardButton(text="Tutup", callback_data="close"),
    ],
  ]
  
  
def start_button(client):
    buttons = BTN
    return buttons


def fsub_button(client, message):
    if FSUB1 and not FSUB2 and not FSUB3 and not FSUB4 and not FSUB5 and not FSUB6 and not FSUB7 and not FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and not FSUB3 and not FSUB4 and not FSUB5 and not FSUB6 and not FSUB7 and not FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and not FSUB4 and not FSUB5 and not FSUB6 and not FSUB7 and not FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and FSUB4 and not FSUB5 and not FSUB6 and not FSUB7 and not FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
             pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and FSUB4 and FSUB5 and not FSUB6 and not FSUB7 and not FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink4),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and FSUB4 and FSUB5 and FSUB6 and not FSUB7 and not FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink5),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink6),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and FSUB4 and FSUB5 and FSUB6 and FSUB7 and not FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink4),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink6),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink7),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and FSUB4 and FSUB5 and FSUB6 and FSUB7 and FSUB8 and not FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink4),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink7),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink8),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and FSUB4 and FSUB5 and FSUB6 and FSUB7 and FSUB8 and FSUB9 and not FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink6),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink7),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink8),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink9),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FSUB1 and FSUB2 and FSUB3 and FSUB4 and FSUB5 and FSUB6 and FSUB7 and FSUB8 and FSUB9 and FSUB10:
        buttons = [
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink2),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink4),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink7),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink8),
            ],
            [
                InlineKeyboardButton(text="Join Disini", url=client.invitelink9),
                InlineKeyboardButton(text="Join Disini", url=client.invitelink10),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
