# Copyright (C) 2022 By ArnavSinghPlayer

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "post", "send"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**`🍁 Sƚαɾƚιɳɠ Bɾσαԃƈαʂƚιɳɠ ...`**")
        if not message.reply_to_message:
            await wtf.edit("**🌀 Pʅҽαʂҽ Rҽρʅყ Tσ α Mҽʂʂαɠҽ ...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**🌀 BɾσαԃCαʂƚιɳɠ ...** \n\n**✔️ Sҽɳƚ T𝐨:** `{sent}` **Cԋαƚʂ** \n**❌ Fαιʅҽԃ Iɳ:** `{failed}` **Cԋαƚʂ**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**🌀 Gƈαʂƚ Sυƈƈҽʂʂϝυʅʅყ ...**\n\n**✔️ Sҽɳƚ Tσ:** `{sent}` **Cԋαƚʂ**\n**❌ Fαιʅҽԃ Iɳ:** `{failed}` **Cԋαƚʂ**")
