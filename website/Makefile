build:
	docker build --force-rm $(option) -t website:latest .

build-prod:
	$(Make) build options="--target production"

compose-start:
	docker-compose up --remove-orphans $(options)	

compose-stop:
	docker-compose down --remove-orphans $(options)