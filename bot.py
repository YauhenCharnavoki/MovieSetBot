from aiogram import Bot, types, Dispatcher, executor
from config import token
from keyboards import keyboard_sets, buttons, btn_random, models, get_keybord, get_random_keybord


bot = Bot(token) 
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id, 
                                   f"Добро пожаловать, {message.from_user.first_name}. Выбери подборку фильмов, которая тебе по душе.", 
                                   reply_markup=keyboard_sets)

@dp.message_handler(content_types=["text"])
async def movies(message: types.Message):
    # создаём список с текстом каждой кнопки из списка кнопок 
    buttons_text = list(map(lambda btn: btn.text, buttons))
    # создаём словарь: ключ - текст каждой кнопки, значение - модель с фильмами каждой подборки
    buttons_models = dict(zip(buttons_text, models))
    if message.text in buttons_text:
        await message.bot.send_message(message.from_user.id, 
                                       f"Бот Movie Set 📽 советует эти фильмы из подборки {message.text}.", 
                                       reply_markup=get_keybord(buttons_models[message.text]))                                 
    elif message.text == btn_random.text:
        await message.bot.send_message(message.from_user.id, 
                                       f"Бот Movie Set 📽 выбрал случайный фильм.", 
                                       reply_markup=get_random_keybord())
    else:
        await message.reply('Это ты мне написал? Я же просто бот. Нажми на кнопку на выдвежной клавиатуре 😜')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
