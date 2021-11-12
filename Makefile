RUN_CONTEXT?=docker compose run --rm npm

pull-env:
	npm run pull-env

up: pull-env
	docker compose up

bash:
	docker compose run --rm -p 3000:3000 server /bin/bash

npm-install:
	$(RUN_CONTEXT) npm install

lint:
	$(RUN_CONTEXT) npm run lint
