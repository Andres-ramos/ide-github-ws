from flask import Flask, render_template
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
# from db import db
import os 
from .db import get_db

# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # initialize Database configuration
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jeje.db'


    # db.init_app(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'temperature.sqlite'),
    )
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    @app.route("/")
    def hello_world():
        temperature = get_db().execute(
            'SELECT * FROM temperature'
        ).fetchall()
        # print(temperature[0][1])
        temperatures_json = [{"temperature": entry[-2], "date": entry[-1].strftime("%m/%d/%Y/%H")} for entry in temperature]
        # print(temperatures_json)
        table_data= temperatures_json
        return render_template('table.html', table_data=table_data)
    


    return app