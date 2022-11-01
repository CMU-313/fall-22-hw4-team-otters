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

    response = client.post(url, json=100)

    assert response.status_code == 404 # Not found: age, absences, and health attributes


def test_get_applicants_route_invalid_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.get(url)

    assert response.status_code == 404 # Not found: age, absences, and health attributes


def test_post_applicants_route_invalid_input():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.post(url, json={
        'age': 16, 'absences': 3
    })

    assert response.status_code == 404 # Not found: health attribute


def test_predict_route_invalid_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url)

    assert response.status_code == 500 # Internal server error: nothing was posted
    

def test_applicants_and_predict_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    response = client.post('/applicants', json={
        'age': 16, 'absences': 3, 'health': 95
    })
    assert response.status_code == 200

    response = client.get('/applicants')
    assert response.status_code == 200
    assert response.get_data() == { 'age': 16, 'absences': 3, 'health': 95 }

    response = client.get('/predict')

    assert response.status_code == 200
    assert response.get_data() == 1 or response.get_data() == 0