import random 
from pyrogram import Client as FilterBot, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from configs import BOT_PICS, StartTxT, HelpTxT, AboutTxT, LOGGER
from FilterBot.database import db

@FilterBot.on_message(filters.private & filters.command("start"))
async def startCMD(client: FilterBot, message: Message):

    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.first_name, message.from_user.id)

    bot = await client.get_me()
    keyboard = [[
      InlineKeyboardButton('Add Me To Your Chat', url=f"https://t.me/{bot.username}?startgroup=true")
      ],[
      InlineKeyboardButton('Help', callback_data='main#help'),
      InlineKeyboardButton('About', callback_data='main#about')
      ],[
      InlineKeyboardButton('Update', url='https://t.me/Mo_Tech_YT'),
      InlineKeyboardButton('Support', url='https://t.me/motechgroup')
      ]]

    if "motech" in BOT_PICS:
        await message.reply_text(text=StartTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await message.reply_photo(photo=random.choice(BOT_PICS), caption=StartTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))

@FilterBot.on_message(filters.private & filters.command("help"))
async def helpCMD(client: FilterBot, message: Message):

    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.first_name, message.from_user.id)

    keyboard = [[ InlineKeyboardButton('Home', callback_data='main#start'),
                  InlineKeyboardButton('Close', callback_data='main#close') ]]

    if "motech" in BOT_PICS:
        await message.reply_text(text=HelpTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await message.reply_photo(photo=random.choice(BOT_PICS), caption=HelpTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))

@FilterBot.on_message(filters.private & filters.command("about"))
async def aboutCMD(client: FilterBot, message: Message):

    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.first_name, message.from_user.id)

    keyboard = [[ InlineKeyboardButton('Tutorial', url='https://youtu.be/hDGgPNgjo9o'),
                   InlineKeyboardButton('Repo', url='https://github.com/PR0FESS0R-99/FilterBot') ],
                [ InlineKeyboardButton('Home', callback_data='main#start'),
                  InlineKeyboardButton('Help', callback_data='main#help') ]]

    if "motech" in BOT_PICS:
        await message.reply_text(text=AboutTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await message.reply_photo(photo=random.choice(BOT_PICS), caption=AboutTxT.format(mention=message.from_user.mention), reply_markup=InlineKeyboardMarkup(keyboard))


@FilterBot.on_callback_query(filters.regex('main'))
async def maincallback(client: FilterBot, message):

    try:
        x, type = message.data.split("#")
    except:
        await message.answer("Error....")
        await message.message.delete()
        return
