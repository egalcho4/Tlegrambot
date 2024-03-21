

import logging

from telegram import * # ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.ext import *
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("how can i help you , Please select from list \n result,incomplete,missing_exam")
async def result(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    #await update.message.reply_text("Enter your username")
    name =update.message.text 
    
    await get_result(name,update,context)
async def get_result(name,update:Update,context:ContextTypes.DEFAULT_TYPE) -> None:
	if name=="egalcho":
		reply_keyboard=[["egalcho","elias"]]
		await update.message.reply_text("You Score grade A+",reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, input_field_placeholder="egalcho or elias"))
	
	  
		  
	elif name=="elias":
		reply_keyboard=[["egalcho","elias"]]
		await update.message.reply_text("You Score grade A",reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, input_field_placeholder="egalcho or elias"))
	
		#await update.message.reply_text("You Score grade A")
	else:
		reply_keyboard=[["egalcho","elias"]]
		await update.message.reply_text("invalid input",reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, input_field_placeholder="egalcho or elias"))
	
		#await update.message.reply_text("Your input is invalid ")
	
def do_something(user_input):
         answer = f"You have wrote me '{ user_input}'"
         return  answer

def reply(update:Update,context:ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.from_user
    update.message.reply_text(do_something(user_input))

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def main() -> None:
	
    application = Application.builder().token("7012216435:AAGJN0oAVyfTyGK6JMVVEopBrNMNRg3mhwc").build()
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    #application.add_handler(CommandHandler(filters.TEXT, result))
    
    application.add_handler(CommandHandler("hello", reply))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, result))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()