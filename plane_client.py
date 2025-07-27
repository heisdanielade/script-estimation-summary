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

        self.workspace_slug = os.getenv('WORKSPACE_SLUG')
        self.project_id = os.getenv('PROJECT_ID')
        self.cycle_id = os.getenv('CYCLE_ID')

        if not self.TOKEN or not self.BASE_URL:
            raise ValueError("(e) Missing API Base URL or Token")

    def get_project_details(self, workspace_slug: str = None, project_id: str = None) -> dict:
        """
        Get details of a project.
        Returns:
            Dictionary with project details
        """
        if workspace_slug is None:
            workspace_slug = self.workspace_slug
        if project_id is None:
            project_id = self.project_id

        url = f"{self.BASE_URL}/workspaces/{workspace_slug}/projects/{project_id}/"

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise PlaneAPIError(
                f"(e) Error fetching project details: {e}") from e
        except Exception as e:
            raise PlaneAPIError(f"(e) Unexpected error occured: {e}") from e

        return response.json()

    def get_cycle_details(self, workspace_slug: str = None, project_id: str = None, cycle_id: str = None) -> dict:
        """
        Get details of a project.
        Returns:
            Dictionary with project details
        """
        if workspace_slug is None:
            workspace_slug = self.workspace_slug
        if project_id is None:
            project_id = self.project_id
        if cycle_id is None:
            cycle_id = self.cycle_id

        url = f"{self.BASE_URL}/workspaces/{workspace_slug}/projects/{project_id}/cycles/{cycle_id}"

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise PlaneAPIError(
                f"(e) Error fetching project details: {e}") from e
        except Exception as e:
            raise PlaneAPIError(f"(e) Unexpected error occured: {e}") from e

        return response.json()

    def get_issues_by_cycle(self, workspace_slug: str = None, project_id: str = None, cycle_id: str = None) -> list:
        """
        Get all issues in a cycle.
        Returns:
            List of issues
        """
        if workspace_slug is None:
            workspace_slug = self.workspace_slug
        if project_id is None:
            project_id = self.project_id
        if cycle_id is None:
            cycle_id = self.cycle_id

        url = f"{self.BASE_URL}/workspaces/{workspace_slug}/projects/{project_id}/issues/"

        params = {
            "cycle": cycle_id,
            "expand": "estimate_point"
        }

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise PlaneAPIError(f"(e) Error fetching isssues: {e}") from e
        except Exception as e:
            raise PlaneAPIError(f"(e) Unexpected error occured: {e}") from e

        data = response.json().get("results", [])

        return data
