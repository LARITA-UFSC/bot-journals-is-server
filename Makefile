GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
WHITE="\033[1;37m"
NO_COLOUR="\033[0m"

# postgres://infinite:infinite@infinite.cehmr8mdcpeo.us-east-2.rds.amazonaws.com:5432/infinite
export DATABASE_URL=postgres://infinite:infinite@infinite.cehmr8mdcpeo.us-east-2.rds.amazonaws.com:5432/infinite

# psql -h infinite.cehmr8mdcpeo.us-east-2.rds.amazonaws.com -U infinite -d infinite -p 5432
# postgres://yhkwgjpzocdvxp:b8e01ffe882c4042df1adb673fec46de6880b94c32c869b34feb4c800c5f2c52@ec2-50-19-218-160.compute-1.amazonaws.com:5432/dfquvos8et8l34

export DEBUG=True

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

.PHONY: run
