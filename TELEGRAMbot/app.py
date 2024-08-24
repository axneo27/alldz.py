from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
import asyncio
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_command_list import commandsList
from aiogram.types import BotCommandScopeAllPrivateChats

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_routers(user_private_router)
    dp.include_routers(user_group_router)
    await bot.set_my_commands(commands=commandsList, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

asyncio.run(main())