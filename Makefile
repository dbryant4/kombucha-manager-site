test:
	docker-compose up -d
	docker-compose run web python manage.py test
	docker-compose down
