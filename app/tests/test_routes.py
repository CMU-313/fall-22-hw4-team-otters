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

def test_get_applicants_route_request_without_post():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.get(url)

    assert response.status_code == 200
    # Should return default with all attribute values = 0
    assert response.get_data() == b'{"Dalc":0,"absences":0,"address_int":0,"age":0,"failures":0,"health":0,"high' 
    +  b'er_int":0,"internet_int":0,"paid_int":0,"studytime":0}\n'


def test_post_applicants_route_invalid_format():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.post(url, json=100)

    assert response.status_code == 500 # Internal server error: 100 is not iterable

def test_post_applicants_route_invalid_input():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/applicants'

    response = client.post(url, json={
        'age': 16, 'absences': 3, 'failures': 0, 'Dalc': 0, 'internet_int': 0, 
        'higher_int': 0, 'paid_int': 0, 'studytime': 0, 'address_int': 0
    })

    assert response.status_code == 400 # Not all attributes found (health)
    assert response.get_data() == b"Invalid input: dictionary should contain 'health', 'absences', 'age', 'failures', \
                    'Dalc', 'internet_int', 'higher_int', 'paid_int', 'studytime', and 'address_int' attributes."


def test_predict_route_without_post():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == 0


def test_get_applicants_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    # when I post to /applicants, I should be able to get that data back
    response = client.post('/applicants', json={
        'age': 16, 'absences': 3, 'health': 95, 'failures': 0, 'Dalc': 0, 'internet_int': 1, 
        'higher_int': 1, 'paid_int': 1, 'studytime': 1, 'address_int': 0
    })
    assert response.status_code == 200
    assert response.get_data() == { 'age': 16, 'absences': 3, 'health': 95, 'failures': 0, 'Dalc': 0,
        'internet_int': 1, 'higher_int': 1, 'paid_int': 1, 'studytime': 1, 'address_int': 0 }
    
    
def test_get_predict_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    
    # when I post to client via the applicant endpoint, 
    # I should get the model prediction from the predict endpoint
    client.post('/applicants', json={
        'age': 16, 'absences': 3, 'health': 95, 'failures': 0, 'Dalc': 0, 'internet_int': 1, 
        'higher_int': 1, 'paid_int': 1, 'studytime': 1, 'address_int': 0
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
    
