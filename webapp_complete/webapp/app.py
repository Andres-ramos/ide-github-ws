from flask import Flask, render_template
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
# from db import db
import os 
from .db import get_db
from .quantum_ml import QuantumMLModel  


def create_app() -> None:
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'temperature.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    @app.route("/")
    def render_temperatures():
        temperature = get_db().execute(
            'SELECT * FROM temperature'
        ).fetchall()
        temperatures_json = [{"temp": entry[-2], "date": entry[-1].strftime("%m/%d/%Y/%H")} for entry in temperature]
        table_data= temperatures_json
        
        temperature_list = [entry[-2] for entry in temperature]
        model = QuantumMLModel()
        qllm_result = model.predict(temperature_list)[0]
        formatted_qllm_result = "{:.2f}".format(qllm_result)
        return render_template('table.html', table_data=table_data, qllm_result=formatted_qllm_result)
    
    return app

