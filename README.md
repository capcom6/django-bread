# Книга рецептов для хлебопечек

Простая книга рецептов хлеба для использования с хлебопечкой.

## Требования

* Python 3.8+

## Зависимости

* Django 4.0

## Запуск

Рекомендуется использовать виртуальное окружение `python3 -m venv env`.

```sh
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```

## План

- [ ] Использовать переменные окружения для параметров подключения к БД и секретов
- [ ] Загрузка фотографии для рецепта
- [ ] Главная страница сайта - список рецептов
- [ ] Информация о конкретном рецепте
- [ ] Социальные элементы: авторизация (через сторонние сервисы), лайк/дизлайк, комментарии.

## Участие

Для участия сделайте форк репозитория, внесите необходимые изменения и проверьте их, после чего создайте pull-request.

## Лицензия

Apache 2.0
