from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    """GET /health returns a 200 status code."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    """POST /tasks with a valid payload returns a 201 status code."""
    payload = {"title": "Learn CI/CD pipelines", "done": False}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "Learn CI/CD pipelines"


def test_get_tasks_grows():
    """GET /tasks returns a list, and the list grows after a task is created."""
    # Get initial count
    initial_response = client.get("/tasks")
    initial_count = len(initial_response.json())

    # Create a new task
    client.post("/tasks", json={"title": "Another Task"})

    # Check new count
    new_response = client.get("/tasks")
    new_count = len(new_response.json())
    assert new_count == initial_count + 1


def test_create_task_empty_title_fails():
    """POST with an empty title returns a 400 Bad Request error."""
    payload = {"title": "   ", "done": False}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 400
    assert "Title cannot be empty" in response.json()["detail"]