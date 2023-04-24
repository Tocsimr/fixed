import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://telegra.ph/file/d2a23fbe48129a7957887.jpg",
    "https://telegra.ph/file/ddf30888de58d77911ee1.jpg",
    "https://telegra.ph/file/268d66cad42dc92ec65ca.jpg",
    "https://telegra.ph/file/13a0cbbff8f429e2c59ee.jpg",
    "https://telegra.ph/file/bdfd86195221e979e6b20.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="📍𝐎𝐰𝐧𝐞𝐫📍", url=f"tg://user?id={OWNER_ID}"),
    ],
]

lol = "https://graph.org/file/d874fc40ddf9ead0cad6b.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**━━━━▰☛•мυsιc αι•☚▰━━━━

💥 тεℓεgяαм мσsт υℓтяα мυsιc вσт ησ ℓαg яυηηιηg ση vρs sεяvεя.💙

┏━━━━━━━━━━━━━━━━━┓
┣★ Oᴡɴᴇʀ     : @xsexa
┣★ Uᴘᴅᴀᴛᴇs : @AI_ARMY
┗━━━━━━━━━━━━━━━━━┛
👀нσω тσ α∂∂ вσт ιη үσυя gяσυρ?

💙∂м мε ғσя α∂∂ιηg @хsєхα

ιғ үσυ нαvε αηү qυεsтιση ∂м мε""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
__mod_name__ = "♨️ᴀʟɪᴠᴇ♨️"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............𝙱𝚈 » [𝚅𝙸𝙿 𝙱𝙾𝚈](https://t.me/the_vip_boy)............☆"""
