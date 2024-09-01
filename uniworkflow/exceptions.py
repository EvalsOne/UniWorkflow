class UniwWorkflowException(Exception):
    """Base exception for UniwWorkflow"""
    pass

class ProviderNotFoundError(UniwWorkflowException):
    """Raised when a provider is not found"""
    pass

class WorkflowExecutionError(UniwWorkflowException):
    """Raised when there's an error executing a workflow"""
    pass
