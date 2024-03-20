import asyncio
import importlib
from pyrogram import idle
from PROTECTOR import PROTECTOR
from PROTECTOR.modules import ALL_MODULES

LOGGER_ID = -1001931272658

loop = asyncio.get_event_loop()

async def CODERZ():
    for all_module in ALL_MODULES:
        importlib.import_module("PROTECTOR.modules." + all_module)
    print("Bot Started Successfully")
    await idle()
    print("𝗜'𝗺 𝗡𝗼𝗼𝗯𝗱 𝗖𝗼𝗱𝗲𝗿𝘇 𝗧𝗵𝗮𝘁'𝘀 𝗪𝗵𝘆 𝗘𝗿𝗿𝗼𝗿 𝗡𝗼𝘁 𝗖𝗼𝗺𝗲 ")
    await PROTECTOR.send_message(LOGGER_ID, "**𝗬𝗼𝘂𝗿 𝗖𝗼𝗽𝘆𝗿𝗶𝗴𝗵𝘁 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗼𝗿 𝗕𝗼𝘁 𝗛𝗮𝘃𝗲 𝗕𝗲𝗲𝗻 𝗗𝗲𝗽𝗹𝗼𝘆𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 \n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ  [𝗡𝗢𝗢𝗕 𝗖𝗢𝗗𝗘𝗥𝗭](https://t.me/noob_coderzz)**")

if __name__ == "__main__":
    loop.run_until_complete(CODERZ())
    
