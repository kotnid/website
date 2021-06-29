build:
	docker build --force-rm $(option) -t website:latest .

build-prod:
	$(Make) build options="--target production"

compose-start:
	docker-compose up --remove-orphans $(options)	

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --rm $(option) website python manage.py $(cmd)
		