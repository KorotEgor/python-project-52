run:
	uv run python manage.py runserver

comp_langs:
	uv run django-admin compilemessages

db:
	sudo service postgresql start