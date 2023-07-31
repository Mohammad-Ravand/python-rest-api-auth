# python rest api authentication
## python with flask

[![N|Solid](data:image/png;base64,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)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

simple jwt authnetication with flask in  python

- ✨Magic ✨

## Features

- login user
- register user
- migration with Flask-Migrate
- seperate models
- seperate routes
- own python environment


## Installation

requires [python](https://www.python.org/downloads/) v3.x+ to run.

Install the dependencies and devDependencies and start the server.

```sh
#step 1 go to project folder
cd python-rest-api-auth

#step 2 activate python environment
#windows
.venv\Script\activate.bat

#linux source ./.venv/bin/activate

#step 3 install dependencies
pip install -r requirements.txt

#step 4 run project
python ./run.py
```



## dependencies

project using this dependencies

| Dependency | README |
| ------ | ------ |
| flask | [https://flask.palletsprojects.com/en/2.3.x/][PlDb] |
| flask-restful | [https://flask-restful.readthedocs.io/en/latest/][PlGh] |
| flask-jwt-extended | [https://flask-jwt-extended.readthedocs.io/en/stable/][PlGd] |
| Flask-SQLAlchemy | [https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/][PlOd] |
| Flask-Migrate | [https://flask-migrate.readthedocs.io/en/latest/][PlMe] |




## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
