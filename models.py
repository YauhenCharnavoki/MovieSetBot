from peewee import *


db = SqliteDatabase("movieset.db")

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    year = IntegerField()
    link = CharField()

    class Meta:
        database = db

class Arthouse(BaseModel):
    pass

class With_friends(BaseModel):
    pass

class With_family(BaseModel):
    pass

class Comedy(BaseModel):
    class Meta:
        db_table = "comedies"

class Thriller(BaseModel):
    class Meta:
        db_table = "thrillers"

class Movies_90(BaseModel):
    pass

class Movies_00(BaseModel):
    pass

class With_couple(BaseModel):
    pass

class Сartoon(BaseModel):
    class Meta:
        db_table = "cartoons"

class Christmas(BaseModel):
    pass

class Motivation(BaseModel):
    pass

class Horror(BaseModel):
    class Meta:
        db_table = "horrors"

class Kinomonster(BaseModel):
    class Meta:
        db_table = "kinomonstra"

class Alone(BaseModel):
    pass
