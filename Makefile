.PHONY: build-dev run-dev build-prod run-prod dev


all: dev

dev: build-dev run-dev
prod: build-prod run-prod

# Alias for dev
run: run-dev
build: build-dev

# Atom receipes
build-dev:
	docker-compose -f "docker-compose.yml" build 

run-dev:
	docker-compose -f "docker-compose.yml" up -d 

build-prod:
	docker build ./back/ -f ./back/prod.Dockerfile -t back --no-cache
	docker build ./front/ -f ./front/prod.Dockerfile -t front --no-cache

run-prod:
	docker-compose -f "docker-compose-prod.yml" up
