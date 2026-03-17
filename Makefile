export:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

build:
	docker build -t temp .

run:
	docker run --rm --name temp --env-file .env temp
