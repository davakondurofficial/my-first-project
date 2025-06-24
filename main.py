
import logging
from aiogram import Bot, Dispatcher, executor, types

# ❗ Временно жёстко вставленный токен
API_TOKEN = "8148785440:AAFub-M6r6BOPWE_YyqLYYBJiccJsOsSJ_w"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "Добро пожаловать в DEVIL BAILEI.\n\n"
        "Сила. Сушка. Сталь.\n"
        "Никакой мотивации. Только система.\n\n"
        "Выбери команду:\n"
        "/press — пресс\n"
        "/arms — руки\n"
        "/legs — ноги\n"
        "/dry — сушка\n"
        "/nutrition — питание\n\n"
        "Здесь не говорят. Здесь делают."
    )


@dp.message_handler(commands=["press"])
async def press(message: types.Message):
    await message.answer("Программа на пресс: 4 круга по 4 упражнения, по 30 сек каждое.")


@dp.message_handler(commands=["arms"])
async def arms(message: types.Message):
    await message.answer("Программа на руки: бицепс + трицепс, 3 подхода по 12 повторений.")


@dp.message_handler(commands=["legs"])
async def legs(message: types.Message):
    await message.answer("Программа на ноги: присед, выпады, жим ногами, 4 подхода.")


@dp.message_handler(commands=["dry"])
async def dry(message: types.Message):
    await message.answer("Сушка: интервальные кардио-тренировки, 20–30 мин.")


@dp.message_handler(commands=["nutrition"])
async def nutrition(message: types.Message):
    await message.answer("Питание: высокобелковое, дефицит калорий, 5 приёмов пищи.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
