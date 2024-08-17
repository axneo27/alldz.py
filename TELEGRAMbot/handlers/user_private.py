from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
import random

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"hehehe your username is  {message.from_user.full_name}")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"PAPAPAPAPA there is no help")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.reply("This is some photo. So how would it help you to solve the Navier-Stokes equations?")

hellos = ['Hello', 'Hi', 'Yo', 'Sunny Init']
for i in range(len(hellos)):
    if F.text==hellos[i]:
        @router.message(F.text== hellos[i])
        async def hello(message: Message):
            a = random.randrange(0, len(hellos))
            await message.answer(hellos[a]) 
