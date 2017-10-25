GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
WHITE="\033[1;37m"
NO_COLOUR="\033[0m"

run:
	echo ${GREEN}Running App${NO_COLOUR}
	DEBUG=True DATABASE_URL=postgres://infinite:infinite@infinite.cehmr8mdcpeo.us-east-2.rds.amazonaws.com:5432/infinite foreman start

lint:
	echo ${GREEN}Running Linter${NO_COLOUR}
	flake8 .

fix:
	echo ${GREEN}Fixing unused imports and variables${NO_COLOUR}
	find . -name '*.py'|grep -v migrations|xargs autoflake --in-place --remove-all-unused-imports --remove-unused-variables
	echo ${GREEN}Fixing pep8 issues${NO_COLOUR}
	autopep8 --in-place --recursive --max-line-length=100 --exclude="*/migrations/*" .

.PHONY: run
