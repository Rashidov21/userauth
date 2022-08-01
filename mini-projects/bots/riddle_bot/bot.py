import random
import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from settings.config import TOKEN, group_id
from keyboard import markup_request

from settings.db import connect_db
# Configure logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom men konkurs botman. Menga telefon raqamingizni jo'nating.", reply_markup=markup_request)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def contacts(msg: types.Message):
    print(msg)
    print(dir(msg))
    await msg.answer(f"Твой location успешно получен:",
                     reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contacts(msg: types.Message):
    conn = connect_db()
    cur = conn.cursor()

    phone = msg.contact.phone_number
    sql = f"""
        INSERT INTO users
        VALUES({msg.from_user.id},'{phone}','empty');
        """
    cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()
    await msg.answer(f"Success", reply_markup=types.ReplyKeyboardRemove())

    # @dp.callback_query_handler(lambda c: c.data == "get")
    # async def some_callback_handler(callback_query: types.CallbackQuery):
    #     conn = sqlite3.connect("./settings/main.db")
    #     cur = conn.cursor()
    #     puzzels = cur.execute("SELECT * FROM puzzels").fetchall()
    #     r_puzzle = random.choice(puzzels)
    #     global current_puzzle_id
    #     global answer
    #     current_puzzle_id = int(r_puzzle[0])
    #     answer = r_puzzle[2]
    #     print(current_puzzle_id)
    #     print(answer)
    #     await bot.send_message(callback_query.from_user.id, f"{r_puzzle[1]}")

    # @dp.message_handler(commands=['get'])
    # async def send_welcome(message: types.Message):
    #     conn = sqlite3.connect("./settings/main.db")
    #     cur = conn.cursor()
    #     puzzels = cur.execute("SELECT * FROM puzzels").fetchall()
    #     r_puzzle = random.choice(puzzels)
    #     await message.reply(f"{r_puzzle[1]}")

    # @dp.message_handler()
    # async def echo(message: types.Message):

    #     if f"({message.text})" in answer:
    #         await message.answer("To'g'ri", reply_markup=kb)
    #     else:
    #         await message.answer("Boshqa topishmoq", reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
