import requests
from .base import BaseProvider
from ..exceptions import WorkflowExecutionError

class MakeProvider(BaseProvider):
    def __init__(self, api_key):
        self.api_key = api_key if api_key else None

    def execute(self, workflow_url, method="GET", data=None):
        """
        Execute a Make.com workflow.
        
        :param workflow_url: The full URL of the workflow to execute
        :param data: A dictionary containing the data to send to the workflow
        :return: A tuple containing the response data and status code
        """
        headers = {
            'Content-Type': 'application/json'
        }
        
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'

        try:
            if method == "GET":
                response = requests.get(workflow_url, headers=headers, params=data)
            elif method == "POST":
                response = requests.post(workflow_url, headers=headers, json=data)
            response.raise_for_status()  # This will raise an HTTPError for bad responses

            if response.status_code == 200:
                response_data = response.json()
                result = response_data.get('data', {})
                return result, response_data, 200
            else:
                raise WorkflowExecutionError(f"Workflow execution failed with status code: {response.status_code}")

        except requests.RequestException as e:
            raise WorkflowExecutionError(f"Error in Make.com workflow call: {str(e)}")
