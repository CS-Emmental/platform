.PHONY: build-dev run-dev build-prod build-prod-back build-prod-front run-prod dev


all: dev

dev: build-dev run-dev
prod: build-prod run-prod

# Alias for dev
run: run-dev
build: build-dev

# Atomic receipes
build-dev:
	docker-compose -f "docker-compose.yml" build 

run-dev:
	docker-compose -f "docker-compose.yml" up -d --build

build-prod: build-prod-front build-prod-back
	
build-prod-front:
	docker build ./front/ -f ./front/prod.Dockerfile -t front --no-cache

build-prod-back:	
	docker build ./back/ -f ./back/prod.Dockerfile -t back --no-cache
	
run-prod:
	docker-compose -f "docker-compose-prod.yml" up
