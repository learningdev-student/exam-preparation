from login import login


def test_login():

    username = "testuser"
    password = "testpassword"
    expected_output = f"Login successful for user: {username} Please check your email."

    assert login(username, password) == expected_output
