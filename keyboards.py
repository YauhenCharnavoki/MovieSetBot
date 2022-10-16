from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from models import Arthouse, With_friends, With_family, With_couple, \
                   Kinomonster, Comedy, Thriller, Movies_90, Movies_00, \
                   Сartoon, Christmas, Motivation, Horror, Alone, db
from random import randint


keyboard_sets = ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)

btn_with_friends = KeyboardButton(text="🍻 Просмотр с друзьями")
btn_with_family = KeyboardButton(text="👨‍👩‍👧‍👦 Семейный просмотр")
btn_movies_90 = KeyboardButton(text="📼 Культовые фильмы 90-х")
btn_movies_00 = KeyboardButton(text="💿 Культовые фильмы 00-х")
btn_with_couple = KeyboardButton(text="👫 Просмотр со своей половинкой")
btn_comedies = KeyboardButton(text="😄 Комедии")
btn_thrillers = KeyboardButton(text="😳 Триллеры")
btn_cartoons = KeyboardButton(text="🦁 Мультфильмы")
btn_christmas = KeyboardButton(text="🎄 Новый год и рождество")
btn_motivation = KeyboardButton(text="🏆 Мотивирующие фильмы")
btn_horrors = KeyboardButton(text="🤡 Культовые фильмы ужасов")
btn_kinomonstra = KeyboardButton(text="🧛🏻‍♂️ Классические киномонстры")
btn_alone = KeyboardButton(text="🧘🏻‍♂️ Когда хочется побыть одному")
btn_arthouse = KeyboardButton(text="🧐 Артхаус")
btn_random = KeyboardButton(text="🤷🏻‍♂️ Случайный фильм")

buttons = [
    btn_with_friends, btn_with_family, btn_movies_90, btn_movies_00, btn_with_couple, btn_comedies, btn_thrillers,
    btn_cartoons, btn_christmas, btn_motivation, btn_horrors, btn_kinomonstra, btn_alone, btn_arthouse
]

models = [
    With_friends, With_family, Movies_90, Movies_00, With_couple, Comedy, Thriller,
    Сartoon, Christmas, Motivation, Horror, Kinomonster, Alone, Arthouse
]

for i in range(len(buttons)):
    keyboard_sets.insert(buttons[i])
keyboard_sets.add(btn_random)

def get_keybord(model):
    """Возвращает inline-клавиатуру с кнопками, после нажатия на которые перенаправляет на страничку фильма"""
    with db:
        movies = model.select()
        movies_keybord = InlineKeyboardMarkup(row_width=2)
        for i in range(len(movies)):
            btn_movie = InlineKeyboardButton(text=f"{movies[i].name} ({movies[i].year})", url=movies[i].link)
            movies_keybord.insert(btn_movie)
    return movies_keybord

def get_random_keybord():
    """Возвращает inline-клавиатуру с одной кнопкой со случаным фильмом, 
    после нажатия на которую перенаправляет на страничку фильма"""
    with db:
        random_movie_keybord = InlineKeyboardMarkup()
        random_movie = []
        for model in models:
            category = model.select()
            for i in range(len(category)):
                random_movie.append(category[i])
        random_number = randint(0, len(random_movie))
        btn_random_movie = InlineKeyboardButton(text=f"{random_movie[random_number].name} ({random_movie[random_number].year})", 
                                                url=random_movie[random_number].link)
        random_movie_keybord.add(btn_random_movie)
    return random_movie_keybord
