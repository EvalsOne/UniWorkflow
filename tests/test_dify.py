import pytest
from unittest.mock import patch, Mock
from uniworkflow import UniwWorkflow
from uniworkflow.exceptions import ProviderNotFoundError, WorkflowExecutionError

@pytest.fixture
def mock_dify_provider(monkeypatch):
    mock_provider = Mock()
    monkeypatch.setattr('uniworkflow.providers.dify.DifyProvider', mock_provider)
    return mock_provider

def test_execute_workflow_successful(mock_dify_provider):
    # Arrange
    expected_result = {
        "formatted_text": "..."
    }
    mock_dify_provider.execute.return_value = expected_result, 200

    kwargs = {
        "workflow_url": "https://api.dify.ai/v1/workflows/run",
        "method": "POST",
        "data": {"TASK": "Write a meeting note"},
        "api_key": "test_api_key"
    }

    # Act
    result, status_code = UniwWorkflow.execute("dify", **kwargs)
    # Assert
    assert isinstance(result, dict)
    assert "formatted_text" in result
    assert status_code == 200

def test_execute_workflow_missing_api_key():
    # Arrange
    kwargs = {
        "workflow_url": "https://api.dify.ai/v1/workflows/run",
        "data": {"topic": "Test Topic"}
    }

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        UniwWorkflow.execute("dify", **kwargs)

    assert str(exc_info.value) == "API key is required"

def test_execute_workflow_invalid_provider():
    # Arrange
    kwargs = {
        "workflow_url": "https://api.dify.ai/v1/workflows/run",
        "data": {"key": "value"},
        "api_key": "test_api_key"
    }

    # Act & Assert
    with pytest.raises(ProviderNotFoundError) as exc_info:
        UniwWorkflow.execute("invalid_provider", **kwargs)

    assert "Provider 'invalid_provider' not found" in str(exc_info.value)