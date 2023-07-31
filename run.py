from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import app


if __name__ == '__main__':
    app.application.run(debug=True)