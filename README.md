# Книга рецептов для хлебопечек

Простая книга рецептов хлеба для использования с хлебопечкой.

## Требования

* Python 3.8+

## Зависимости

### Python

* Django 4.0
* Pillow
* django-storages (Azure)

### Внешние

* MySQL - основная база данных приложения;
* Azure Blob Storage - хранение фотографий, должен быть разрешен анонимный доступ к файлам контейнера.

## Переменные окружения

Приложение использует переменные окружения для получения настроек. Также возможно использование файла `.env` с настройками. Пример находится в файле [.env.example](.env.example).

Доступные переменные окружения:

* `SECRET_KEY` - секретный ключ для механизмов безопасности;
* `DEBUG` - признак работы в режиме разработки и отладки;
* `DB_NAME` - название БД MySQL;
* `DB_USER` - пользователь БД MySQL;
* `DB_PASSWORD` - пароль БД MySQL;
* `DB_HOST` - адрес БД MySQL, по-умолчанию `localhost`;
* `DB_PORT` - порт БД MySQL, по-умолчанию `3306`;
* `AZURE_ACCOUNT_NAME` - имя учетной записи хранения;
* `AZURE_ACCOUNT_KEY` - ключ учетной записи хранения;
* `AZURE_CONTAINER` - имя контейнера с анонимным доступом.

## Запуск

### Локально

Рекомендуется использовать виртуальное окружение `python3 -m venv env`.

```sh
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

### В Docker

Для запуска приложения в Docker используется `docker-compose`:

```sh
make docker-up-silent
```

Чтобы создать суперпользователя необходимо зайти в контейнер:

```sh
make docker-exec
python3 manage.py createsuperuser
```

## План

- [x] Использовать переменные окружения для параметров подключения к БД и секретов.
- [x] Загрузка фотографии для рецепта.
- [x] Главная страница сайта - список рецептов.
- [x] Информация о конкретном рецепте.
- [ ] Социальные элементы: авторизация (через сторонние сервисы), лайк/дизлайк, комментарии.
- [ ] Контейнеризация.
- [ ] Автоматическая сборка и публикация контейнера.
- [ ] Автоматическое развертывание.
- [ ] Отдельное поле для шагов приготовления (если поле заполнено, то отмечать это отдельной иконкой, чтобы была сразу видна необходимость дополнительных шагов).
- [ ] Примечание для ингредиента рецепта, например, "порезанное на кубики".
- [ ] Себестоимость хлеба. Для каждого ингредиента указываем цену и на основании этого считаем стоимось буханки. В идеале должна быть история цен ингредиентов.
- [ ] Отображение долей: вместо `1,75` отображать `1 3/4`.
- [ ] Тэги для рецептов. Возможность использования тэгов как групп (отдельный флаг).
- [ ] Поддержка выпечки в духовке (не указывается цвет корочки, нужно отдельное поле для шагов приготовления).

## Участие

Для участия сделайте форк репозитория, внесите необходимые изменения и проверьте их, после чего создайте pull-request.

## Лицензия

Apache 2.0
