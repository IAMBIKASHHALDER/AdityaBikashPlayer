import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4c219126032d7b0f31b22.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🐯 Hҽʅʅσ Wҽʅƈσɱҽ Tσ Aɾɳαʋ Mυʂιƈ Bσƚ, I αɱ Sυρҽɾϝαʂƚ Hιɠԋ Qυαʅιƚყ 
Nσ Lαɠ Vƈ Aɾɳαʋ Mυʂιƈ Pʅαყҽɾ Bσƚ.

┏━━━━━━━━━━━━━━━━━┓
┣★ Cɾҽαƚσɾ 🛠️  [Aɾɳαʋ Sιɳɠԋ](https://t.me/Op_cutearnav123)
┣★ Cɾҽαƚσɾ 🛠️ [AႦσυƚ Aɾɳαʋ](https://t.me/OP_ARNAV_SINGH)
┣★ Uρԃαƚҽʂ 📢 [Aɾɳαʋ Nҽƚɯσɾƙ](https://t.me/KING_COBRA_NETWORK)
┣★ YσυƚυႦҽ ☣️ [Aɾɳαʋ Cԋαƚ](https://youtube.com/channel/UCUw4ZmMC_H2SYdcka9teJ7A)
┣★ Cԋαƚƚιɳɠ ©️ [Aɾɳαʋ Cԋαƚ](https://t.me/Final_Countdown_Survivors)
┗━━━━━━━━━━━━━━━━━┛

🗽 Jυʂƚ Aԃԃ Mҽ » Tσ Yσυɾ Gɾσυρ Aɳԃ
Eɳʝσყ Bҽʂƚ Qυαʅιƚყ ❥︎ Aɾɳαʋ Mυʂιƈ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Aԃԃ Mҽ Tσ Yσυɾ Gɾσυρ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"/start@{BOT_USERNAME}", "/alive", "/Arnav",  ".Kaal"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4c219126032d7b0f31b22.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛪ Jσιɳ Oυɾ Cԋαƚ Gɾσυρ  🗽", url=f"https://t.me/link_copied")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "Arnav", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4c219126032d7b0f31b22.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛪ Cʅιƈƙ Mҽ Tσ Gҽƚ Rҽρσ 🗽", url=f"https://t.me/Op_cutearnav123")
                ]
            ]
        ),
    )
