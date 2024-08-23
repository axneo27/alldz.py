from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
import random
from HG.goodbyes import goodbyes
from HG.hellos import hellos

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"hehehe your username is  {message.from_user.full_name}")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"PAPAPAPAPA there is no help")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.reply("This is some photo.")

for i in range(len(hellos)):
    if F.text==hellos[i].lower():
        @router.message(F.text== hellos[i].lower())
        async def hello(message: Message):
            a = random.randrange(0, len(hellos))
            await message.answer(hellos[a])

for j in range(len(goodbyes)):
    if F.text==goodbyes[j].lower():
        @router.message(F.text== goodbyes[j].lower())
        async def bye(message: Message):
            a = random.randrange(0, len(goodbyes))
            await message.answer(goodbyes[a])
