import requests, json
from .base import BaseProvider
from ..exceptions import WorkflowExecutionError

class DifyProvider(BaseProvider):
    def __init__(self, api_key):
        if api_key is not None:
            self.api_key = api_key
        else:
            raise ValueError("API key is required")

    def execute(self, workflow_url, method="GET", data=None):
        """
        Execute a Make.com workflow.
        
        :param workflow_url: The full URL of the workflow to execute
        :param data: A dictionary containing the data to send to the workflow
        :return: A tuple containing the response data and status code
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        inputs = {key: value for key, value in data.items() if key not in []}
        payload = {
            'inputs': inputs,
            'response_mode': "blocking",
            'user': "workflow-user"
        }
        
        try:
            if method == "GET":
                response = requests.get(workflow_url, headers=headers, params=payload)
            elif method == "POST":
                response = requests.post(workflow_url, headers=headers, json=payload)
            response.raise_for_status()  # This will raise an HTTPError for bad responses

            if response.status_code == 200:
                response_data = response.json()
                output = response_data.get('data', {}).get('outputs', {})
                return output, response_data, 200                
            else:
                raise WorkflowExecutionError(f"Workflow execution failed with status code: {response.status_code}")

        except requests.RequestException as e:
            raise WorkflowExecutionError(f"Error in Dify workflow call: {str(e)}")
