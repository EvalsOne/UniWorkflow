import requests, json
from .base import BaseProvider
from ..exceptions import WorkflowExecutionError

class ZapierProvider(BaseProvider):
    def __init__(self, workflow_url, method, **kwargs):
        super().__init__(workflow_url, method, **kwargs)
        self.zapier_url = "https://zapier.com/developer/public/api/v1/recipes/"
    
    def execute(self, workflow_url, method="GET", data=None):
        """
        Execute the workflow
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        try:
            if method == "GET":
                response = requests.get(workflow_url, headers=headers, params=data)
            elif method == "POST":
                response = requests.post(workflow_url, headers=headers, json=data)
            response.raise_for_status()  # This will raise an HTTPError for bad responses

            if response.status_code == 200:
                response_data = response.json()
                result = response_data.get('data', {})
                return result, 200
            else:
                raise WorkflowExecutionError(f"Workflow execution failed with status code: {response.status_code}")

        except requests.RequestException as e:
            raise WorkflowExecutionError(f"Error in Zapier workflow call: {str(e)}")