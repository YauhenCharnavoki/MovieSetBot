from peewee import *
from openpyxl import open
from models import db
from keyboards import models


movie_sets = open("movieset.xlsx", read_only=True)

with db:
    db.create_tables(models)
    # проходимся по таблице всех листов excel-файла, считываем данные и заносим в базу данных
    for i in range(len(movie_sets.worksheets)):
        sheet = movie_sets.worksheets[i]
        movie_set= []
        for row in range(2, sheet.max_row+1):
            name = sheet[row][1].value
            year = sheet[row][2].value
            link = sheet[row][3].value
            movie_set.append({"name": name, "year": year, "link": link})
        movies = models[i].insert_many(movie_set).execute()
