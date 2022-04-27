.PHONY: run
run:
	python3 manage.py runserver

.PHONY: migration
migration:
	python3 manage.py makemigrations && \
	python3 manage.py migrate

.PHONY: docker-up
docker-up:
	docker-compose -f docker-compose-dev.yml up

.PHONY: docker-up-silent
docker-up-silent:
	docker-compose -f docker-compose-dev.yml up -d

.PHONY: docker-exec
docker-exec:
	docker-compose -f docker-compose-dev.yml exec web sh

.PHONY: docker-down
docker-down:
	docker-compose -f docker-compose-dev.yml down
