import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from time import time
from datetime import datetime

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(contact_filter & filters.command(['ping'], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.reply_text("`...`")
   delta_ping = time() - start
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m_reply.edit(f"`🤺♦️ Ping Pong felas da pota {delta_ping * 1000:.3f} ms ≛` \n**♦️ Tempo ⏳** - `{uptime}`")

@Client.on_message(contact_filter & filters.command(['restart'], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
   await m.reply("`Reiniciando...`")
   os.execl(sys.executable, sys.executable, *sys.argv)
   # You probably don't need it but whatever
   quit()

@Client.on_message(contact_filter & filters.command(['help'], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
   HELP = f"**♦️ ᵐᵉⁿᵘ ᵈᵒˢ ᶜᵒᵐᵃⁿᵈᵒˢ 🛠** \n\n__COMANDOS DE USUÁRIO__ (Qualquer um pode usar ou não :) depende de mim parceiro): \n`{HNDLR}play` \n`{HNDLR}vplay` \n`{HNDLR}stream` (Para links de rádio) \n`{HNDLR}vstream` (For .m3u8 / live links) \n`{HNDLR}playfrom [canal] ; [n]` - Reproduzir uma vossa música no canal \n`{HNDLR}playlist` / `{HNDLR}queue` \n\n__COMANDOS DO SUDO USER__ (Só pode ser acessado por Mim e meus contatos): \n`{HNDLR}ping` \n`{HNDLR}skip` \n`{HNDLR}pause` e `{HNDLR}resume` \n`{HNDLR}stop` / `{HNDLR}end` \n`{HNDLR}help` \n`{HNDLR}restart`"
   await m.reply(HELP)
