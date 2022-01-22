from telethon.errors.rpcerrorlist import YouBlockedUserError
from SkyzuRobot import telethn as tbot
from SkyzuRobot.events import register
from SkyzuRobot import ubot2 as ubot
from asyncio.exceptions import TimeoutError


@register(pattern="^/sg ?(.*)")
async def lastname(steal):
    steal.pattern_match.group(1)
    puki = await steal.reply("```Kau siapa sih, ane kepo kalau gk terima pc @WikiTapiStres itu owner ane ye😑..```")
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await puki.edit("```Mohon Balas Ke Pesan Pengguna.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await puki.edit("```Balas Pesan Pengguna Asli.```")
        return
    await puki.edit("```Tunggu sebentar...```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply("```Kesalahan, laporkan ke @WikiTapiGroup```")
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await puki.edit(f"`{r.message}`")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await puki.edit(
                    "```Saya Tidak Dapat Menemukan Informasi Pengguna Ini, Pengguna Ini Belum Pernah Mengubah Namanya Sebelumnya.```"
                )
                await ubot.delete_messages(conv.chat_id, [msg.id, r.id, response.id])
                return
            else:
                respond = await conv.get_response()
                await puki.edit(f"```{response.message}```")
            await ubot.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await puki.edit("`Aku Sakit Maaf...`")
