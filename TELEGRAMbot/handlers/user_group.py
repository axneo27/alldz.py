from aiogram.types import Message
from aiogram import Router
from aiogram.types import FSInputFile
from filters.chat_filters import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

bad_words = {'bad', 'word', 'bad_word' 'badword'}
good_words= {'sls', 'artemis', "rocket engine", "satellite", "buran", "shuttle"}

@user_group_router.message()
@user_group_router.edited_message()
async def check_words(message:Message):
    if good_words.intersection(set(message.text.lower().split())):
        await message.reply("Oh so you are into space huh?")
    elif bad_words.intersection(set(message.text.lower().split())):
        await message.delete()
        await message.answer('You cannot type this. Shame on you')
    else:
        phot = FSInputFile('TELEGRAMbot/img/coooool.jpg', 'rb')
        await message.reply_photo(phot, caption="cool, no bad words", has_spoiler=False)