"""
Заполнение данных в БД через скрипт python.
Для заполнения, достаточно просто запустить скрипт.

Так же приведенные команды в блоке (if __name__ == "__main__":)
можно аналогично выполнить в окружении запускаемом командой
python manage.py shell

В случае вызова консоли (python manage.py shell), то так же как и в
приведенном блоке (if __name__ == "__main__":) необходимо
импортировать модели с которыми будете работать и далее выполнять команды с БД.
"""

import os
from time import time
from datetime import date, datetime
import re
from json import load, dump
import asyncio

from django.core.exceptions import ValidationError
from django.core.files import File
from django.utils import timezone
from faker import Faker

# _____________Для работы с БД в Django через скрипт - этот блок обязателен !___
from django import setup
# Блок обязательно должен быть определен до импорта моделей БД
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # Передача параметров в окружение
setup()  # Загрузка настроек Django
# ______________________________________________________________________________

from django.contrib.auth.models import User  # Загрузка базового пользователя

# _____________Блок с созданием пользователей___________________________________

fake = Faker("ru")  # Создаём объект для генерации фейковых данных
Faker.seed(42)  # Фиксируем значение seed, чтобы случайные генерации были воспроизводимы

def create_fake_users(num_users=10, save_data=True):
    """Создаем несуществующих пользователей и записываем их, чтобы был доступ"""
    t1 = time()
    data = []
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.free_email()
        password = fake.password()
        User.objects.create_user(username=username, email=email,
                                 password=password)
        data.append({"username": username,
                     "email": email,
                     "password": password
                     })
    print(f"Время выполнения создания {num_users} пользователей через "
          f"синхронный цикл равно {time() - t1:.4f} c")

    if save_data:
        with open("users.json", "w", encoding="utf-8") as f:
            dump(data, f, indent=4)


async def async_create_fake_users(num_users=10):
    """Асинхронно создаем несуществующих пользователей"""
    t1 = time()
    data_user, data = [], []

    for _ in range(num_users):
        username = fake.user_name()
        email = fake.free_email()
        password = fake.password()
        data_user.append(
            User(username=username, email=email, password=password))
        data.append({"username": username,
                     "email": email,
                     "password": password
                     })
    # У объекта БД есть метод save(), а для асинхронного сохранения применяют asave()
    await asyncio.gather(*[user.asave() for user in data_user])
    """
    asyncio.gather - это функция из библиотеки asyncio в Python, которая позволяет вам запускать 
    несколько корутин (асинхронных функций) параллельно и ожидать их завершения.
    В функцию передаются объекты (выполняемые функции), которые необходимо запустить асинхронно
    """

    print(f"Время выполнения создания {num_users} пользователей через "
          f"асинхронный цикл равно {time() - t1:.4f} c")

    # Запись в файл
    if os.path.exists("users.json"):
        with open("users.json", encoding="utf-8") as f:
            users = load(f)
        users += data  # Дозаписываем данные к уже имеющимся
        with open("users.json", "w", encoding="utf-8") as f:
            dump(users, f, indent=4)
    else:
        with open("users.json", "w", encoding="utf-8") as f:
            dump(data, f, indent=4)
# ______________________________________________________________________________

# _____________Чтение данных из json для добавления в БД________________________
with open("data/json_data/blogs.json", encoding="utf-8") as f:
    data_blog = load(f)
with open("data/json_data/authors.json", encoding="utf-8") as f:
    data_author = load(f)
with open("data/json_data/authors_profile.json", encoding="utf-8") as f:
    data_author_profile = load(f)
with open("data/json_data/entrys.json", encoding="utf-8") as f:
    data_entry = load(f)
with open("data/json_data/tags.json", encoding="utf-8") as f:
    data_tag = load(f)
with open("data/json_data/comments.json", encoding="utf-8") as f:
    data_comment = load(f)
# ______________________________________________________________________________

if __name__ == "__main__":
    from app.models import Blog, Author, AuthorProfile, Entry, Tag, Comment

    # _____________Создание пользователей_______________________________________
    ## Создание администратора
    User.objects.create_superuser("admin", password="123")
    print("Админ создан \n    Логин: admin\n    Пароль: 123")

    create_fake_users(5)  # Работает долго, так как используется цикл и каждый раз создаётся транзакция в БД

    # Используем asyncio.run() для запуска асинхронной функции
    asyncio.run(async_create_fake_users(25))  # Работает намного быстрее чем
    # стандартный цикл, так как все транзакции отправляются почти параллельно
    # и происходит ожидание когда процесс завершится.

    print()  # Просто, чтобы сделать отступ в консоли

    # ______Работа с объектами таблицы Blog_____________________________________
    """Пример записи в БД с последующим сохранением"""
    obj = Blog(name=data_blog[0]["name"], slug_name=data_blog[0]["slug_name"],
               headline=data_blog[0]["headline"], description=data_blog[0]["description"])
    obj.save()

    """Пример записи в БД с сохранением (в нашем случае, так как работаем с словарём,
    то можно применить распаковку **)"""
    Blog.objects.create(**data_blog[1])

    """Никто не запрещает использовать циклы, минус в том, что при работе с циклами
    каждая запись сохраняется в БД по одному, что может создавать дополнительную
    нагрузку на БД"""
    for data in data_blog[2:]:
        Blog.objects.create(**data)

    # ______Работа с объектами таблицы Author___________________________________
    """Если необходимо записать объекты пакетом, то для этих целей существует bulk_create,
    Однако он записывает данные в БД, если это контейнер подготовленных объектов
    к записи, а не сырые данные."""
    data_for_write = [Author(**data) for data in data_author[:10]] # Здесь
    # просто создались объекты, записи в БД не было
    Author.objects.bulk_create(data_for_write)  # А здесь произошла пакетная запись в БД

    """
    При использовании Django ORM в Python - скрипте или через оболочку shell,
    встроенные проверки полей моделей автоматически не выполняются при сохранении
    объектов в базу данных. Однако возможно явно вызвать эти проверки и обработать
    возможные исключения, чтобы убедиться, что данные соответствуют заданным
    ограничениям полей для этого у объекта, который создали для записи необходимо
    вызвать метод full_clean()

    Для более наглядной части создам функцию с проверкой
    """
    def check_obj_for_write_to_db(obj, save=True):
        try:
            obj.full_clean()
        except ValidationError as e:
            fields = obj._meta.fields  # Получение
            # всех полей у объекта, необходимо чтобы вывести в трассировке
            # с какими параметрами был объект с ошибками. Выводит без полей с
            # отношениями с другими таблицами
            params = ""
            for field in fields:
                field_name = field.name
                field_value = getattr(obj, field_name)
                params += f"{field_name}={field_value!r}, "
            print(f"Ошибка при создании объекта: {e}\n"
                  f"Объект: {obj.__class__.__name__}({params[:-2]})")
        else:
            if save:
                obj.save()  # Объект успешно создан
            return True
        return False

    """Пример одиночной записи с проверкой, в случае удачных проверок - запишется,
    если нет, то появится ошибка, но выполнению кода это не помешает, так как
    был специально написан обработчик исключения в check_obj_for_write_to_db"""
    obj = Author(**data_author[10])
    check_obj_for_write_to_db(obj)

    """Пример с ошибкой"""
    obj = Author(name="user", email="user")
    check_obj_for_write_to_db(obj)
    """
    В консоль выведется
    Ошибка при создании объекта: {'email': ['Enter a valid email address.']}
    Объект: Author(id=None, name='user', email='user')"""

    """
    К сожалению для Author.objects.create(**data_author[10]) не получится провести
    встроенные проверки, так как внутри вызывается save() который делает базовые проверки.

    Для bulk_create аналогичная ситуация, однако можно провести проверки в момент
    формирования контейнера объектов для записи. Ниже приведён пример как можно
    это сделать. В рассматриваемом примере если существует хотя бы одна ошибка,
    то весь блок не записывается.
    """

    """Пример с ошибкой в блоке"""
    raw_data = [{"name": "user1", "email": "user1"}] + data_author[11:]
    data_for_write = list(filter(lambda x: check_obj_for_write_to_db(x, False),
                                 (Author(**data) for data in raw_data)))
    if len(data_for_write) == len(raw_data):
        Author.objects.bulk_create(data_for_write)
    """
    В консоль выведется
    Ошибка при создании объекта: {'email': ['Enter a valid email address.']}
    Объект: Author(id=None, name='user1', email='user1')"""

    """Рабочий пример"""
    raw_data = data_author[11:]
    data_for_write = list(
        filter(lambda x: check_obj_for_write_to_db(x, False),
               (Author(**data) for data in raw_data)))
    if len(data_for_write) == len(raw_data):
        Author.objects.bulk_create(data_for_write)

    # ______ Работа с объектами таблицы AuthorProfile __________________________
    """Далее рассмотрим создание объектов с отношениями. Для того чтобы создать
    запись в БД в таблице где есть отношение, то в это поле необходимо передавать
    объект базы данных связанный с необходимым ключом(значением).

    """
    for data in data_author_profile:
        author = Author.objects.get(name=data["author"])
        # Создаём автора с иконкой по умолчанию
        obj = AuthorProfile(author=author,
                            bio=data["bio"],
                            phone_number=data["phone_number"],
                            city=data["city"])

        check = check_obj_for_write_to_db(obj)

        """чтобы провести теже действия, что проводит Django при сохранении файла
        необходимо вызвать save от этого поля, это немного отличается от ранее
        рассмотренной валидации, так как тут рассматривается конкретное поле со своей спецификой
        """
        if check and data["avatar"] is not None:  # Если ошибок нет, и картинку нужно поменять (так как есть путь до
            # картинки), то запускаем протокол сохранения картинки
            with open(data["avatar"], 'rb') as file:  # Считываем картинку
                image_file = File(file)  # Создаём объект File
                obj.avatar.save(os.path.basename(data["avatar"]), image_file)  # Сохраняем картинку
                # (запускается механизм переноса картинки в хранилище)

    ## ______ Работа с объектами таблицы Tag ___________________________________
    for tag in data_tag:
        Tag.objects.create(**tag)

    ## ______ Работа с объектами таблицы Entry _________________________________
    blogs = Blog.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    re_split = re.compile(r'[ :-]')
    for entry in data_entry:
        blog = blogs.get(name=entry["blog"])
        author = authors.filter(name__in=entry["authors"])
        tag = tags.filter(name__in=entry["tags"])
        # pub_date в моделях объявлен как DateTimeField, поэтому на вход необходимо подавать объект datetime
        pub_date = datetime(*map(int, re_split.split(entry["pub_date"]))) if \
            entry["pub_date"] is not None else datetime.now()
        pub_date = timezone.make_aware(pub_date)  # добавляем данных о часовом поясе, так как могут быть проблемы с БД и Django
        obj = Entry(blog=blog,
                    headline=entry["headline"],
                    slug_headline=entry["slug_headline"],
                    summary=entry["summary"],
                    body_text=entry["body_text"],
                    pub_date=pub_date,
                    number_of_comments=entry["number_of_comments"],
                    number_of_pingbacks=entry["number_of_pingbacks"],
                    rating=entry["rating"] if entry["rating"] is not None else 0.0)

        check_obj_for_write_to_db(obj)
        obj.authors.set(author)  # Запись отношение многое ко многому немного специфичная
        # необходимо сначала сохранить в БД, а затем установить значения отношений
        obj.tags.set(tag)

    ## ______ Работа с объектами таблицы Comment _______________________________
    for comment in data_comment:
        entry = Entry.objects.get(headline=comment["entry"])
        user = User.objects.get(id=comment["user_id"])
        Comment.objects.create(user=user,
                               entry=entry,
                               text=comment["text"])