from application import application


def test_home_page_loads():
    client = application.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Flask App" in response.data


def test_health_check_returns_healthy():
    client = application.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_message_route_returns_name():
    client = application.test_client()
    response = client.get("/message?name=Student")
    assert response.status_code == 200
    assert b"Hello, Student" in response.data