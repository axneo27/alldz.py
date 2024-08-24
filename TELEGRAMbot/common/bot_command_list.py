from aiogram.types import BotCommand

commandListLabels = [
    "start", "help", "dog", "return_image_category"
]

commandsList = [
    BotCommand(command="start", description="This command does pretty nothing"),
    BotCommand(command="help", description="This command helps"),
    BotCommand(command="menu", description="Avaliable commands"),
    BotCommand(command="dog", description="idk"),
    BotCommand(command="return_image_category", description="idk idk")
    
]