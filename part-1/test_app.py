import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_jokes(client, mocker):
    mock_response = {
        "categories":[],
        "created_at":"2020-01-05 13:42:26.194739",
        "icon_url":"https://api.chucknorris.io/img/avatar/chuck-norris.png",
        "id":"ZYuYuFQVSfamBUYfzFADMQ",
        "updated_at":"2020-01-05 13:42:26.194739",
        "url":"https://api.chucknorris.io/jokes/ZYuYuFQVSfamBUYfzFADMQ",
        "value":"Chuck Norris has more subscribers than Pewdiepie."
    }
    mocker.patch('requests.get').return_value.json.return_value = mock_response

    response = client.get('/getJokes')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 10
    assert all(joke == mock_response['value'] for joke in data)

def test_get_jokes_failure(client, mocker):
    mocker.patch('requests.get').side_effect = Exception('API failure')

    response = client.get('/getJokes')
    assert response.status_code == 500
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Error fetching jokes: API failure'
    