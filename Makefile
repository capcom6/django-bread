run:
	python3 manage.py runserver

migration:
	python3 manage.py makemigrations && \
	python3 manage.py migrate
	
docker-up:
	docker-compose -f docker-compose-dev.yml up

docker-exec:
	docker-compose -f docker-compose-dev.yml exec web sh

docker-down:
	docker-compose -f docker-compose-dev.yml down

