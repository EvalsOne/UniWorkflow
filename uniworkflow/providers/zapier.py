import requests
from .base import BaseProvider
from ..exceptions import WorkflowExecutionError

class ZapierProvider(BaseProvider):
    def __init__(self, timeout=120):
        self.timeout = timeout
        pass  # No API key is required for triggering Zapier webhooks

    def execute(self, webhook_url, method="POST", headers={}, data=None):
        """
        Execute a Zapier workflow via webhook.

        :param webhook_url: The full URL of the Zapier webhook to trigger
        :param method: The HTTP method to use ('POST' or 'GET')
        :param data: A dictionary containing the data to send to the webhook
        :return: A tuple containing the result, response data, and status code
        """
        headers = {
            'Content-Type': 'application/json',
            **headers
        }

        try:
            if method.upper() == "GET":
                response = requests.get(webhook_url, headers=headers, params=data, timeout=self.timeout)
            elif method.upper() == "POST":
                response = requests.post(webhook_url, headers=headers, json=data, timeout=self.timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()  # Raise HTTPError for bad responses

            # Zapier webhooks typically do not return content, but we can attempt to parse
            try:
                response_data = response.json()
                result = response_data.get('data', response_data)
            except ValueError:
                response_data = response.text
                result = response_data

            return result, response_data, response.status_code

        except requests.RequestException as e:
            raise WorkflowExecutionError(f"Error executing Zapier workflow: {str(e)}")