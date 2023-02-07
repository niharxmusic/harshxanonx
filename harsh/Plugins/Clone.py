Form Pyrogram import filters, client
Form nihar import app

@app.on message(filter.private & filter.command("client")) 
async def _ (app, massage):
     reply = await massage.reply("usege:\n\n /clone <token>"
     Token = massage.command[1]
     try:
         await reply.edit(booting your client")
      
