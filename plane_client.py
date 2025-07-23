import os
import requests
from dotenv import load_dotenv

load_dotenv()


class PlaneAPIError(Exception):
    """To handle API Errors."""
    ...


class PlaneClient:
    """
    Sends GET requests to API.
    Fetch issues in specific cycle.
    Return the data needed for estimation.
    """

    def __init__(self) -> None:
        self.BASE_URL = os.getenv("PLANE_BASE_URL")
        self.TOKEN = os.getenv("PLANE_API_KEY")
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-Key": f"{self.TOKEN}",
            "Accept": "application/json"
        })

        self.WORKSPACE_SLUG = os.getenv('WORKSPACE_SLUG')
        self.PROJECT_ID = os.getenv('PROJECT_ID')
        self.CYCLE_ID = os.getenv('CYCLE_ID')

        if not self.TOKEN or not self.BASE_URL:
            raise ValueError("(e) Missing API Base URL or Token")


    def get_issues_by_cycle(self, workspace_slug: str = None, project_id: str = None, cycle_id: str = None) -> list:
        """
        Get all issues in a cycle.
        Returns:
            List of issues
        """
        if workspace_slug is None:
            workspace_slug = self.WORKSPACE_SLUG
        if project_id is None:
            project_id = self.PROJECT_ID
        if cycle_id is None:
            cycle_id = self.CYCLE_ID

        url = f"{self.BASE_URL}/workspaces/{workspace_slug}/projects/{project_id}/issues/"

        params = {
            "cycle": cycle_id
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise PlaneAPIError(f"(e) Error fetching isssues: {e}") from e

        data = response.json().get("results", [])

        return data

    def get_estimate_value_map(self, workspace_slug: str = None, project_id: str = None) -> dict:
        """
        Plane.so uses a linkind system, so each estimation point is an entity.
        This method gets the numeric value of estimation points via the id.
        Returns:
            Dictionary mapping
        """
        if workspace_slug is None:
            workspace_slug = self.WORKSPACE_SLUG
        if project_id is None:
            project_id = self.PROJECT_ID

        # TODO: Get correct endpoint
        url = f"{self.BASE_URL}/workspaces/{workspace_slug}/projects/{project_id}/estimate-values/"

        try:
            response = self.session.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise PlaneAPIError(
                f"(e) Error fetching estimate values: {e}") from e

        estimates = response.json()

        return {
            item["id"]: item["value"] for item in estimates
        }
