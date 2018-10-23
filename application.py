from os import environ
from SOSial import app, db
import subprocess

if __name__ == '__main__':
    subprocess.call("./setup.sh")
    HOST = environ.get('SERVER_HOST', 'localhost')
    HOST = "0.0.0.0"
    try:
        # PORT = int(environ.get('SERVER_PORT', '5555'))
        PORT = 5000
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT, debug=True)

