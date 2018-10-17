from os import environ
from SOSial import app, db


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = "0.0.0.0"
    try:
        # PORT = int(environ.get('SERVER_PORT', '5555'))
        PORT = 5000
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)

