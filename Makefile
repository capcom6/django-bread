run:
	python3 manage.py runserver

migration:
	python3 manage.py makemigrations && \
	python3 manage.py migrate
	