GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
WHITE="\033[1;37m"
NO_COLOUR="\033[0m"


run:
	echo ${GREEN}Running app${NO_COLOUR}
	foreman start

crawler:
	# make crawler 
	#    url=http://periodicos.ufca.edu.br/ojs/index.php/folhaderosto/ 
	#    id-inicial=1 id-final=3 id-journal=9
	echo ${GREEN}Running crawler${NO_COLOUR}
	python server/manage.py crawler --url=$(url) --id-inicial=$(id-inicial) --id-final=$(id-final) --id-journal=$(id-journal)

lint:
	echo ${GREEN}Running linter${NO_COLOUR}
	flake8 .

fix:
	echo ${GREEN}Fixing unused imports and variables${NO_COLOUR}
	find . -name '*.py'|grep -v migrations|xargs autoflake --in-place --remove-all-unused-imports --remove-unused-variables
	echo ${GREEN}Fixing pep8 issues${NO_COLOUR}
	autopep8 --in-place --recursive --max-line-length=100 --exclude="*/migrations/*" .
	echo ${YELLOW}Linter statistics${NO_COLOUR}
	flake8 --statistics --count -qq

heroku-dump-db:

	#
	# pg_restore --verbose --clean --no-acl --no-owner -h localhost -U myuser -d mydb latest.dump
	#

	echo ${GREEN}Downloading dump database${NO_COLOUR}
	heroku pg:backups:capture --app infinite-meadow-72957
	heroku pg:backups:download --app infinite-meadow-72957
	mv latest.dump data/

migrate:
	echo ${GREEN}Running migrations${NO_COLOUR}
	python server/manage.py makemigrations
	python server/manage.py migrate

.PHONY: run
