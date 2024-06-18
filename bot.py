#GRACE GRADUATION BOT
import sqlite3
import telebot
from time import sleep
import utils
import user_utils
from constants import Constants
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

logger = utils.get_logger(__name__)


#check user to "ban"
def is_banned(user_id):
    with sqlite3.connect("data.db") as cursor:
        ban = cursor.execute("SELECT ban FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
    if ban != None:
        if ban:
            bot.send_message(user_id, f"You don't have access!")
            logger.info(f"user {user_id} tried use bot")
            return True
        else:
            return False
    else:
        return None


#admin code section
def admin_code_section(message):
    logger.debug("admin_code_section...")

#default code section
def default_code_section(message):
    logger.debug("default_code_section...")
    team_code = user_utils.get_team_code(message.from_user.id)

    if team_code is None:
        logger.debug("team_code is None...")
        result = False
        
        if message.text == Constants.TEAM_CODE_1.value:
            logger.debug("set team_code_1...")
            result = user_utils.update_user(message.from_user.id, Constants.TEAM_CODE_1.value, 0)
        elif message.text == Constants.TEAM_CODE_2.value:
            logger.debug("set team_code_2...")
            result = user_utils.update_user(message.from_user.id, Constants.TEAM_CODE_2.value, 0)
        elif message.text == Constants.TEAM_CODE_3.value:
            logger.debug("set team_code_3...")
            result = user_utils.update_user(message.from_user.id, Constants.TEAM_CODE_3.value, 0)
        elif message.text == Constants.TEAM_CODE_4.value:
            logger.debug("set team_code_4...")
            result = user_utils.update_user(message.from_user.id, Constants.TEAM_CODE_4.value, 0)

        if result: #START FIRST ROUND
            logger.debug("result is true...")
            bot.send_message(message.from_user.id, f"{Constants.TEXT_1.value}")

    else:
        progress = user_utils.get_progress(message.from_user.id)
        if team_code == Constants.TEAM_CODE_1.value:
            logger.debug("team_code_1...")

            if message.text == Constants.FIFTH_ROUND_CODE.value and progress == 3:
                logger.debug("start first round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_2.value)

            elif message.text == Constants.FIRST_ROUND_CODE.value and progress == 0:
                logger.debug("start second round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_3.value)

            elif message.text == Constants.THIRD_ROUND_CODE.value and progress == 1:
                logger.debug("start third round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_4.value)

            elif message.text == Constants.FOURTH_ROUND_CODE.value and progress == 2:
                logger.debug("start fourth round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_5.value)

            elif message.text == Constants.SECOND_ROUND_CODE.value and progress == 4:
                logger.debug("start final...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_FINAL.value)

        elif team_code == Constants.TEAM_CODE_2.value:
            logger.debug("team_code_2...")

            if message.text == Constants.THIRD_ROUND_CODE.value and progress == 2:
                logger.debug("start first round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_2.value)

            elif message.text == Constants.FIFTH_ROUND_CODE.value and progress == 1:
                logger.debug("start second round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_3.value)

            elif message.text == Constants.SECOND_ROUND_CODE.value and progress == 3:
                logger.debug("start third round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_4.value)

            elif message.text == Constants.FIRST_ROUND_CODE.value and progress == 0:
                logger.debug("start fourth round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_5.value)

            elif message.text == Constants.FOURTH_ROUND_CODE.value and progress == 4:
                logger.debug("start final...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_FINAL.value)

        elif team_code == Constants.TEAM_CODE_3.value:
            logger.debug("team_code_3...")

            if message.text == Constants.FOURTH_ROUND_CODE.value and progress == 1:
                logger.debug("start first round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_2.value)

            elif message.text == Constants.SECOND_ROUND_CODE.value and progress == 2:
                logger.debug("start second round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_3.value)

            elif message.text == Constants.FIRST_ROUND_CODE.value and progress == 0:
                logger.debug("start third round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_4.value)

            elif message.text == Constants.THIRD_ROUND_CODE.value and progress == 3:
                logger.debug("start fourth round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_5.value)

            elif message.text == Constants.FIFTH_ROUND_CODE.value and progress == 4:
                logger.debug("start final...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_FINAL.value)

        elif team_code == Constants.TEAM_CODE_4.value:
            logger.debug("team_code_4...")

            if message.text == Constants.FIRST_ROUND_CODE.value and progress == 0:
                logger.debug("start first round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_2.value)

            elif message.text == Constants.FOURTH_ROUND_CODE.value and progress == 3:
                logger.debug("start second round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_3.value)

            elif message.text == Constants.FIFTH_ROUND_CODE.value and progress == 2:
                logger.debug("start third round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_4.value)

            elif message.text == Constants.SECOND_ROUND_CODE.value and progress == 1:
                logger.debug("start fourth round...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_5.value)

            elif message.text == Constants.THIRD_ROUND_CODE.value and progress == 4:
                logger.debug("start final...")
                user_utils.update_user(message.from_user.id, team_code, progress+1)
                bot.send_message(message.from_user.id, Constants.TEXT_FINAL.value)


#COMMAND START
@bot.message_handler(commands=['start'])
def start(message):
    logger.debug(f"user {message.from_user.id} tried use command \"start\"...")
    if not user_utils.check_user_id(message.from_user.id):
        user_utils.add_to_database(message.from_user.id, message.from_user.username)
        bot.send_message(message.from_user.id, f"Welcome!")

#TEXT
@bot.message_handler(content_types=['text'])
def text(message):
    logger.debug(f"user {message.from_user.id} tried use section \"text\"")
    if not is_banned(message.from_user.id):
        if message.text[0] == "/":
            admin_code_section(message) #admin code section
        else:
            default_code_section(message) #default code section


#looping start bot
run_bot = True
while run_bot:
    try:
        logger.info("START BOT...")
        bot.polling()
    except Exception as e:
        logger.critical(e)
        sleep(2)
