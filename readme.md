
# Golinks
Golinks is an internal URL shortener. If you’re on the company network, you can type in <code>go/keyword</code> in your browser, and that will redirect you to some other site.


## Running locally

Setup project requirements

```
make setup
make setup-frontend
```

Run

```
make run
make run-frontend
```

Browse to http://localhost:8080

## Build Docker images

Run docker build and push

```
make build-docker
```

# Deploy on Kubernetes

Start Minikube

```
minikube start
eval (minikube docker-env)
```

Setup database passwords

```
MYSQLROOTPASS="myrootpassword"
MYSQLUSER="admin"
MYSQLPASS="mypassword"
```

Deploy with helm
```
cd helm
helm dependency update golinks
helm install golinks --set mysql.mysqlRootPassword=${MYSQLROOTPASS},mysql.mysqlUser=${MYSQLUSER},mysql.mysqlPassword=${MYSQLPASS} --set secrets.DATABASE_URL=mysql+pymysql://${MYSQLUSER}:${MYSQLPASS}@golinks-mysql:3306/golinks -f golinks/values.yaml -n golinks
```

Get the ingress name


`k get ingress`

```
NAME      HOSTS           ADDRESS        PORTS   AGE
golinks   golinks.local   192.168.64.3   80      45h
```

Edit hosts file `/etc/hosts`

```
192.168.64.3     golinks.local
```

Browse to http://golinks.local


## Vue Frontend Configuaration

Install vue

```
npm install -g @vue/cli@3.7.0
vue create frontend
```


Select "Babel", "Router", and "Linter / Formatter" like so:

```
Vue CLI v3.7.0
? Please pick a preset: Manually select features
? Check the features needed for your project:
 ◉ Babel
 ◯ TypeScript
 ◯ Progressive Web App (PWA) Support
❯◉ Router
 ◯ Vuex
 ◯ CSS Pre-processors
 ◉ Linter / Formatter
 ◯ Unit Testing
 ◯ E2E Testing
```

Use the history mode for the router. Select "ESLint + Airbnb config" for the linter and "Lint on save". Finally, select the "In package.json" option so that configuration is placed in the package.json file instead of in separate configuration files.

You should see something similar to:

```
Vue CLI v3.7.0
? Please pick a preset: Manually select features
? Check the features needed for your project: Babel, Router, Linter
? Use history mode for router? Yes
? Pick a linter / formatter config: Airbnb
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, PostCSS, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) No
```


## Running Flask Locally

```
virtualenv -p python3 venv
source venv/bin/activate.fish
pip install -r requirements
export FLASK_APP=manage.py
export FLASK_ENV=development
flask shell
from app import db
db.create_all()
flask run
```
```
