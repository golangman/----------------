from peewee import (
    BigIntegerField,
    CharField,
    ForeignKeyField,
    DateTimeField,
    PostgresqlDatabase,
    Model,
    BooleanField,
    CompositeKey,
    SmallIntegerField,
    AutoField,
)


from utils import config_get_params

_name, _host, _port, _user, _password = config_get_params(
    [
        "database_name",
        "database_host",
        "database_port",
        "database_username",
        "database_password",
    ]
)


driver = PostgresqlDatabase

database = driver(_name, host=_host, port=_port, user=_user, password=_password,)

# * Базовая модель моделей базы данных для наследования драйвера
class BaseModel(Model):
    class Meta:
        database = database


# * Модель пользователей
class Users(BaseModel):
    login = CharField(max_length=32, primary_key=True, null=False)
    password = CharField(max_length=32)


# * Модель сложностей
class Complexity(BaseModel):
    complexity = CharField(max_length=16, primary_key=True, null=False)


# * Модель профессоров ( преподавателей )
class Professors(BaseModel):
    id = AutoField()
    first_name = CharField(max_length=16, null=False)
    last_name = CharField(max_length=16, null=False)
    patronymic = CharField(max_length=16, null=False)


# * Модель учебных предметов
class AcademicSubject(BaseModel):
    professor = ForeignKeyField(
        Professors,
        to_field="id",
        on_delete="CASCADE",
        on_update="CASCADE",
        backref="subjects",
    )

    name = CharField(max_length=32, null=False)


# * Модель заданий
class Tasks(BaseModel):
    text = CharField(max_length=32, primary_key=True, null=False)
    complexity = ForeignKeyField(
        Complexity,
        to_field="complexity",
        on_update="CASCADE",
        on_delete="CASCADE",
        backref="tasks",
    )


# * Инициализация таблиц базы данных
if database:
    Users.create_table(True)
    Complexity.create_table(True)
    Professors.create_table(True)
    AcademicSubject.create_table(True)
    Tasks.create_table(True)
