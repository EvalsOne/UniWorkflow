class UniWorkflowException(Exception):
    """Base exception for UniWorkflow"""
    pass

class ProviderNotFoundError(UniWorkflowException):
    """Raised when a provider is not found"""
    pass

class WorkflowExecutionError(UniWorkflowException):
    """Raised when there's an error executing a workflow"""
    pass
