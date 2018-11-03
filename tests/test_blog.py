import pytest
from flask.db import get_db

def test_index(client):
    response = client.get('/')
    assert b"New List" in response.data
    assert b"Add Recipe" in response.data
    assert b"Create Food List" in response.data
    assert b"Add New Recipe" in response.data
    assert b"Edit Recipe" in response.data
    
@pytest.mark.parametrize('path', (
        '/))