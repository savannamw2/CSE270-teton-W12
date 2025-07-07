import requests
import pytest

def test_authentication_failed(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    # Create the mock response object
    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''

    # Patch requests.get to return the mock response
    mocker.patch('requests.get', return_value=mocked_response)

    # Make the GET request
    response = requests.get(url, params=params)

    # Assertions
    assert response.status_code == 401
    assert response.text.strip() == ''


def test_authentication_successful(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    # Create the mock response object
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''

    # Patch requests.get to return the mock response
    mocker.patch('requests.get', return_value=mocked_response)

    # Make the GET request
    response = requests.get(url, params=params)

    # Assertions
    assert response.status_code == 200
    assert response.text.strip() == ''


def test_authentication_failed(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'admin'
    }

    # Create the mock response object
    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''

    # Patch requests.get to return the mock response
    mocker.patch('requests.get', return_value=mocked_response)

    # Make the GET request
    response = requests.get(url, params=params)

    # Assertions
    assert response.status_code == 401
    assert response.text.strip() == ''


def test_authentication_successful(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {
        'username': 'admin',
        'password': 'qwerty'
    }

    # Create the mock response object
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''

    # Patch requests.get to return the mock response
    mocker.patch('requests.get', return_value=mocked_response)

    # Make the GET request
    response = requests.get(url, params=params)

    # Assertions
    assert response.status_code == 200
    assert response.text.strip() == ''

pytest.main()