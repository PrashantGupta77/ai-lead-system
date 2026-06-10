from src.auth.security import (
    create_access_token
)


def test_create_token():

    token = create_access_token(
        {
            "sub": "testuser",
            "role": "USER"
        }
    )

    assert token is not None

    assert isinstance(token, str)