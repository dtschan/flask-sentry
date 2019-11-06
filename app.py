#!/usr/bin/env python3

import os

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

app = Flask(__name__)


sentry_sdk.init(
    os.environ['SENTRY_DSN'],
    debug=True,
    integrations=[FlaskIntegration()]
)


@app.route('/')
def hello():
    sentry_sdk.capture_message("Hello World")  # Will create an event.
    a = 1/0
    return "Hello World!"

if __name__ == '__main__':
    app.run()
