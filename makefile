run:
	uv run python manage.py runserver

comp_langs:
	uv run django-admin compilemessages

db:
	sudo service postgresql start

remake_po:
	django-admin makemessages --ignore="static" --ignore=".env" -l ru

migrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

cr_sup_user:
	uv run manage.py createsuperuser