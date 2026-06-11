pythonuser := myvenv/Scripts/python -u
python := myvenv/Scripts/python
# pythonuser := myvenv/bin/python3 -u
# python := myvenv/bin/python3
fix := fixtures/db.json

compose := docker compose -f docker-compose.local.yml


python:
	$(python)

container-build:
	$(compose) build

container-down:
	$(compose) down --remove-orphans -t 0

daemon:
	$(compose) up -d

crawl:
	$(python) manage.py crawl

crawls:
	$(python) manage.py crawls

load:
	$(python) manage.py load

read:
	$(python) manage.py read

super-user:
	$(python) manage.py  createsuperuser

system-clean:
	bash bash/docker-clean.sh

logs:
	$(compose) logs -f

logs-django:
	$(compose) logs -f django nginx postgres celeryworker

delete:
	sudo rm -r ./data ./staticfiles ./dist

locale-create:
	$(python) manage.py makemessages --all

locale-save:
	$(python) manage.py compilemessages

celery:
	$(python) -m  celery -A config.celery_app worker -l INFO --pool solo

start:
	$(python) manage.py runserver

script:
	$(python) manage.py runscript orm_script
# script:
# 	$(python) manage.py runscript count_script

server:
	$(python) -m gunicorn --config gunicorn-cfg.py config.wsgi

migrate:
	$(python) manage.py migrate

migratesocial:
	$(python) manage.py migrate socialaccount

migrations:
	$(python) manage.py makemigrations


static:
	$(python) manage.py collectstatic --noinput
flush:
	$(python) manage.py flush --noinput
shell:
	$(python) manage.py shell_plus
dev:
	npm run dev

build:
	npm run build

clean:
	npm run clean

format:
	$(python) -m djlint ./api/templates/**/**/**/*.html --format-css --format-js --reformat

format-check:
	$(python) -m djlint ./api/templates/**/**/**/*.html --format-css --format-js --check

# dumpdata:
# 	$(python) manage.py dumpdata -e apps.ChapterImage users apps home --indent 4
dumpdata:
	$(python) manage.py dumpdata users apps home --indent 4 -o $(fix)


loaddata:
	$(python) manage.py loaddata --ignorenonexistent --force-color  db.json

test:
	$(python) manage.py test

compilemessages:
	$(python) manage.py compilemessages

makemessages:
	$(python) manage.py makemessages --all --no-location

git-push:
	git add --all ; git commit -m 'updated my Templates'; git push -u origin main
