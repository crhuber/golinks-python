### --------------------------------------------------------------------------------------------------------------------
### Variables
### (https://www.gnu.org/software/make/manual/html_node/Using-Variables.html#Using-Variables)
### --------------------------------------------------------------------------------------------------------------------
.ONESHELL:
VENV ?= venv
API_BASE_URL=""

# Other config
NO_COLOR=\033[0m
OK_COLOR=\033[32;01m
ERROR_COLOR=\033[31;01m
WARN_COLOR=\033[33;01m
### --------------------------------------------------------------------------------------------------------------------
### RULES
### (https://www.gnu.org/software/make/manual/html_node/Rule-Introduction.html#Rule-Introduction)
### --------------------------------------------------------------------------------------------------------------------
.PHONY: requirements

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  run         to run the service"
	@echo "  test        to run unit tests"
	@echo "  setup       to setup the working virtual environment, and to install requirements for development"
	@echo "  clean       to remove the created virtualenv folder"
	@echo "  code-style  to run pep8 on src"

build-s3:
	cd $(CURDIR)/frontend; npm install
	cd $(CURDIR)/frontend; npm run build

build-s3-zappa:
	echo VUE_APP_API_BASE_URL="https://goapi.intra.io" > $(CURDIR)/frontend/.env.production
	cd $(CURDIR)/frontend; npm install
	cd $(CURDIR)/frontend; npm run build

build-docker:
	docker build -t crhuber/golinks-api $(CURDIR)/
	docker build --build-arg VUE_APP_API_BASE_URL=$(API_BASE_URL) -t crhuber/golinks-frontend $(CURDIR)/frontend/
	docker push crhuber/golinks-api:latest
	docker push crhuber/golinks-frontend:latest

deploy-s3:
	aws s3 sync --delete $(CURDIR)/frontend/dist s3://go.intra.io --acl public-read --exclude ".git/*"

deploy-zappa:
	( \
	source $(CURDIR)/$(VENV)/bin/activate; \
	$(CURDIR)/$(VENV)/bin/pip3 install -r zappa==0.48.2
	zappa deploy production; \
	)

setup: clean virtualenv requirements

setup-frontend: npm-install setup-envfiles

setup-envfiles:
	echo VUE_APP_API_BASE_URL=http://localhost:5000 > $(CURDIR)/frontend/.env.local
	echo VUE_APP_API_BASE_URL="" > $(CURDIR)/frontend/.env.production

run:
	( \
	source $(CURDIR)/$(VENV)/bin/activate; \
	export FLASK_APP=manage.py; \
	export FLASK_ENV=development; \
	flask db upgrade; \
	flask run; \
	)

run-frontend:
	cd $(CURDIR)/frontend; npm run serve

npm-install: 
	cd $(CURDIR)/frontend; npm install

test: code-style test-unit

test-unit:
	PYTHONPATH=$(CURDIR) nose2 --with-coverage

code-style:
	flake8 --ignore E501 manage.py

virtualenv:
	virtualenv -p python3 $(CURDIR)/$(VENV)

clean:
	rm -rf venv

requirements:
	$(CURDIR)/$(VENV)/bin/pip3 install -r requirements.txt
