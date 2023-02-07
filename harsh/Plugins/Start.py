Form Pyrogram import filters, client 

@client.on_message(filters.command(["start"  "st"]) & filters       
 
async def _(app: client, message): 
     await message.reply_text("Hii There") 
