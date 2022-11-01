from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_post_applicants_route_invalid_format():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.post(url)
    assert response.status_code == 400

def test_get_applicants_route_invalid_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.get(url)
    assert response.status_code == 400

def test_get_applicants_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.post(url)
    assert response.status_code == 200

    response = client.get(url)
    assert response.status_code == 400

def test_predict_route_invalid_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url)

    assert response.status_code == 400
    
def test_predict_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == 1 or response.get_data() == 0