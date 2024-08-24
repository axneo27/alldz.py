from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
import random
from HG.goodbyes import goodbyes
from HG.hellos import hellos
from filters.chat_filters import ChatTypeFilter
from common.bot_command_list import commandListLabels
from common.functions import*

typelist= ['nature', 'space', 'city']

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"hehehe your username is  {message.from_user.full_name}")

@user_private_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"PAPAPAPAPA there is no help")

@user_private_router.message(Command('menu'))
async def cmd_help(message: Message):
    await message.answer(f"The commands are:\n{commandListLabels[0]}\n{commandListLabels[1]}\n{commandListLabels[2]}")

@user_private_router.message(F.photo)
async def get_photo(message: Message):
    await message.reply("This is some photo.")

@user_private_router.message(Command("dog"))
async def cmd_dog(message:Message):
    await message.answer_photo(get_random_dog())

@user_private_router.message(Command(commandListLabels[3]))
async def cmd_img(message:Message):
    await message.reply("Enter category: ")
    res = message.text
    await message.answer_photo(get_random(res))

for i in range(len(hellos)):
    if F.text==hellos[i].lower():
        @user_private_router.message(F.text== hellos[i].lower())
        async def hello(message: Message):
            a = random.randrange(0, len(hellos))
            await message.answer(hellos[a])

for j in range(len(goodbyes)):
    if F.text==goodbyes[j].lower():
        @user_private_router.message(F.text== goodbyes[j].lower())
        async def bye(message: Message):
            a = random.randrange(0, len(goodbyes))
            await message.answer(goodbyes[a])