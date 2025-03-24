import requests
from .base import BaseProvider
from ..exceptions import WorkflowExecutionError

class N8nProvider(BaseProvider):
    def __init__(self, api_key, timeout=120):
        self.api_key = api_key if api_key else None
        self.timeout = timeout

    def execute(self, workflow_url, method="GET", headers={}, data=None):
        """
        Execute a N8n workflow.
        
        :param workflow_url: The full URL of the workflow to execute
        :param data: A dictionary containing the data to send to the workflow
        :return: A tuple containing the response data, response_data, and status code
        """
        headers = {
            'Content-Type': 'application/json',
            **headers
        }
        
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'

        try:
            if method == "GET":
                response = requests.get(workflow_url, headers=headers, params=data, timeout=self.timeout)
            elif method == "POST":
                response = requests.post(workflow_url, headers=headers, json=data, timeout=self.timeout)
            response.raise_for_status()  # This will raise an HTTPError for bad responses

            if response.status_code == 200:
                try:
                    response_data = response.json()
                    result = response_data.get('data', {})
                    return result, response_data, 200
                except:
                    return None, response.text, 422
            else:
                # 首先尝试获取 text，如果失败则使用 content
                try:
                    error_message = response.text
                except:
                    error_message = response.content.decode('utf-8', errors='replace')
                return None, error_message, response.status_code

        except requests.RequestException as e:
            # 同样地，安全地获取错误信息
            try:
                error_message = getattr(e.response, 'text', None)
                if error_message is None:
                    error_message = getattr(e.response, 'content', str(e))
                    if isinstance(error_message, bytes):
                        error_message = error_message.decode('utf-8', errors='replace')
            except:
                error_message = str(e)
            return None, error_message, 500
