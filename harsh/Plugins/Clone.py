Form Pyrogram import filters, client
Form nihar import app, API_ID, API_HASH

@app.on message(filter.private & filter.command("client")) 
async def -(app, massage):
     reply = await massage.reply("usege:\n\n /clone <token>"
     Token = massage.command[1]
     try:
         await reply.edit("booting your client")
         client = client (name="OK", api_id=API_ID, api_hash=API_HASH, bot_token, in_memory=true, plugins=dict(root="nihar/plugins")
         await client start()
         await reply.edit("successfully booting your client")         
     expert Experience as e:
       await reply.edit(f"Error:\n`{e}`")
