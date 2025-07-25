import pytest
import requests
from plane_client import PlaneClient

MOCK_PROJECT_DETAILS = {
    "name": "Project X",
    "total_cycles": 1,
    "network": 2
}


@pytest.fixture
def plane_client():
    """Return fresh instance of PlaneClient object for api calls."""
    return PlaneClient()


class MockResponse:
    """
    Mock response object to simule response object recieved from 'requests.get(url)'
    Provided:
        .json()
        .raise_for_status()
    """

    def __init__(self, json_data: dict, status_code: int = 200) -> None:
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if self.status_code > 299:
            raise requests.HTTPError(f"HTTP {self.status_code}")


mock_get = lambda *args, **kwargs: MockResponse(MOCK_PROJECT_DETAILS)


def test_get_project_details_success(monkeypatch, plane_client):
    """Ensure successful retrieval of a project's details by project id."""

    monkeypatch.setattr(plane_client.session, "get", mock_get)

    random_project_id = "00918ea1-52f7-48bd-abe3-d3efe76ff7dd"

    response = plane_client.get_project_details(project_id=random_project_id)

    assert response.get("name") == "Project X"
    assert response.get("total_cycles") == 1
    assert response.get("network") == 2
