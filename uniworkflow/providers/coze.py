import requests, json
from .base import BaseProvider
from ..exceptions import WorkflowExecutionError

class CozeProvider(BaseProvider):
    def __init__(self, api_key, timeout=120):
        if api_key is not None:
            self.api_key = api_key
        else:
            raise ValueError("API key is required")
        self.timeout = timeout

    def execute(self, workflow_url, method="GET", headers={}, data=None):
        """
        Execute a Coze.com workflow.
        
        :param workflow_url: The full URL of the workflow to execute
        :param data: A dictionary containing the data to send to the workflow
        :return: A tuple containing the response data and status code
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            **headers
        }
        inputs = {key: value for key, value in data.items() if key not in []}

        # extract workflow_id from workflow_url
        workflow_id = workflow_url.split('#')[-1]
        # remove workflow_id from workflow_url
        workflow_url = workflow_url.replace(f"#{workflow_id}", "")
        payload = {
            'workflow_id': workflow_id,
            'parameters': inputs
        }
        
        try:
            if method == "GET":
                response = requests.get(workflow_url, headers=headers, params=payload, timeout=self.timeout)
            elif method == "POST":
                response = requests.post(workflow_url, headers=headers, json=payload, timeout=self.timeout)
            response.raise_for_status()  # This will raise an HTTPError for bad responses
            if response.status_code == 200:
                response_data = response.json()
                raw_data = response_data.get('data', {})
                output_data = json.loads(raw_data).get("data", {})
                try:
                    output_data = json.loads(output_data)
                except:
                    output_data = output_data

                return output_data, response_data, 200                
            else:
                raise WorkflowExecutionError(f"Workflow execution failed with status code: {response.status_code}")

        except requests.RequestException as e:
            raise WorkflowExecutionError(f"Error in Coze workflow call: {str(e)}")
