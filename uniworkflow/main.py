# uniworkflow/main.py

from .providers.make import MakeProvider
from .providers.dify import DifyProvider
from .providers.n8n import N8nProvider
from .providers.coze import CozeProvider
# from .providers.zapier import ZapierProvider
from .exceptions import ProviderNotFoundError, WorkflowExecutionError

class UniWorkflow:
    providers = {
        "make": MakeProvider,
        "dify": DifyProvider,
        "n8n": N8nProvider,
        "coze": CozeProvider,
        # "zapier": ZapierProvider
    }

    @classmethod
    def execute(cls, provider_name, workflow_url, method="GET", headers={}, **kwargs):
        """
        Execute a workflow for the specified provider.

        :param provider_name: Name of the provider (e.g., "make", "dify", "zapier")
        :param kwargs: Additional arguments required for the specific provider
        :return: Result of the workflow execution
        """
        if provider_name not in cls.providers:
            raise ProviderNotFoundError(f"Provider '{provider_name}' not found")

        provider_class = cls.providers[provider_name]
        
        # Extract API key and timeout from kwargs
        api_key = kwargs.pop('api_key', None)
        timeout = kwargs.pop('timeout', 120)
        
        if not workflow_url:
            raise ValueError("Workflow URL is required")
        
        if not method:
            raise ValueError("Method is required")
        
        # convert method to uppercase
        method = method.upper()
        if method not in ["GET", "POST", "PUT", "DELETE"]:
            raise ValueError("Invalid method")

        # Initialize provider with timeout
        provider = provider_class(api_key, timeout)

        try:
            # Execute the workflow
            result, response_data, status_code = provider.execute(workflow_url=workflow_url, method=method, headers=headers, **kwargs)
            return result, response_data, status_code
        except Exception as e:
            raise WorkflowExecutionError(f"Error executing workflow: {str(e)}")

    @classmethod
    def add_provider(cls, name, provider_class):
        """
        Add a new provider to the UniWorkflow.

        :param name: Name of the provider
        :param provider_class: Class of the provider
        """
        cls.providers[name] = provider_class
