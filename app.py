from flask import Flask, Blueprint

def create_app():
    app = Flask(__name__)
    return app