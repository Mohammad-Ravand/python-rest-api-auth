from flask import Flask, request
from flask_restful import Resource, Api
from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=True)  # New field: active
    token = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username