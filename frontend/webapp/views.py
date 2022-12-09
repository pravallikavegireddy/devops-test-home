from flask import render_template
import requests
from webapp import app
from webapp.default_settings import API_ENDPOINT


@app.route('/')
def index():
    endpoint = app.config.get("API_ENDPOINT")
    app.logger.info('Loading Main Page')
    response = requests.get("http://"+ endpoint + "/menu")
    data = response.json()
    app.logger.info(data)
    
    return render_template('index.html', data=data)