# Книга рецептов для хлебопечек

Простая книга рецептов хлеба для использования с хлебопечкой.

## Требования

* Python 3.8+

## Зависимости

* Django 4.0

## Переменные окружения

Приложение использует переменные окружения для получения настроек. Также возможно использование файла `.env` с настройками. Пример находится в файле [.env.example](.env.example).

Доступные переменные окружения:

* `SECRET_KEY` - секретный ключ для механизмов безопасности;
* `DEBUG` - признак работы в режиме разработки и отлажки;
* `DB_NAME` - названием БД MySQL, только для `DEBUG == False`;
* `DB_USER` - пользователь БД MySQL, только для `DEBUG == False`;
* `DB_PASSWORD` - пароль БД MySQL, только для `DEBUG == False`;
* `DB_HOST` - адрес БД MySQL, по-умолчанию `localhost`, только для `DEBUG == False`;
* `DB_PORT` - порт БД MySQL, по-умолчанию `3306`, только для `DEBUG == False`;

## Запуск

Рекомендуется использовать виртуальное окружение `python3 -m venv env`.

```sh
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```

## План

- [x] Использовать переменные окружения для параметров подключения к БД и секретов;
- [ ] Загрузка фотографии для рецепта;
- [ ] Главная страница сайта - список рецептов;
- [ ] Информация о конкретном рецепте;
- [ ] Социальные элементы: авторизация (через сторонние сервисы), лайк/дизлайк, комментарии;
- [ ] Контейнеризация;
- [ ] Автоматическая сборка и публикация контейнера;
- [ ] Автоматическое развертывание.

## Участие

Для участия сделайте форк репозитория, внесите необходимые изменения и проверьте их, после чего создайте pull-request.

## Лицензия

Apache 2.0
