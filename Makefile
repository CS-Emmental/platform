run:
	docker-compose -f "docker-compose.yml" up --build -d 

build:
	docker-compose -f "docker-compose.yml" build 

prod:
	docker-compose -f "docker-compose-prod.yml" up --build -d 