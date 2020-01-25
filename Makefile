run:
	docker-compose -f "docker-compose.yml" up --build -d 

build:
	docker-compose -f "docker-compose.yml" build 

build-prod:
	docker build ./back/ -f ./back/prod.Dockerfile -t back --no-cache
	docker build ./front/ -f ./front/prod.Dockerfile -t front --no-cache

run-prod:
	docker-compose -f "docker-compose-prod.yml" up