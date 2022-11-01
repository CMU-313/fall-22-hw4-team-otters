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
    
def test_get_applicants_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    # when I post to /applicants, I should be able to get that data back
    response = client.post('/applicants', json={
        'age': 16, 'absences': 3, 'health': 95
    })
    assert response.status_code == 200
    assert response.get_data() == { 'age': 16, 'absences': 3, 'health': 95 }
    
    
def test_get_predict_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    
    # when I post to client via the applicant endpoint, 
    # I should get the model prediction from the predict endpoint
    client.post('/applicants', json={
        'age': 16, 'absences': 3, 'health': 95
    })
    
    response = client.get('/predict')

    assert response.status_code == 200
    assert response.get_data() == 1 or response.get_data() == 0
    
def test_undefined_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/undefined'

    response = client.get('/undefined')
    assert response.status_code == 404
    
def test_post_undefined_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/undefined'

    response = client.post(url, json={
        'age': 16, 'absences': 3, 'health': 90
    })

    assert response.status_code == 404 # resource not found
    
