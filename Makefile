init:
	pip install -r requirements.txt

init-dev: init
	pip install -r requirements-dev.txt

start:
	python3 manage.py runserver

migration:
	python3 manage.py makemigrations

up-dev:
	docker-compose -f deployments/docker-compose-dev.yml up --build

up-dev-silent:
	docker-compose -f deployments/docker-compose-dev.yml up -d

exec-dev:
	docker-compose -f deployments/docker-compose-dev.yml exec web sh

down-dev:
	docker-compose -f deployments/docker-compose-dev.yml down

test:
	python3 manage.py test

test-cov:
	coverage run --source='.' manage.py test recipes \
		&& coverage report

.PHONY: init init-dev start migration up-dev up-dev-silent exec-dev down-dev test
