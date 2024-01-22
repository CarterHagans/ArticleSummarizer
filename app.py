from website import create_app,create_socketio
import os
from flask import url_for

from flask_socketio import SocketIO, send   





if __name__ == "__main__":
    flask_app = create_app()
    socketio = create_socketio()

    @flask_app.context_processor
    def override_url_for():
        return dict(url_for=dated_url_for)


    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                file_path = os.path.join(flask_app  .root_path,
                                    endpoint, filename)
                values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)
    override_url_for()


    socketio.run(flask_app,host="0.0.0.0",debug=True) # change this to local host when working locally and server ip     when pushing to server