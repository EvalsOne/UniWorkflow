import pytest
from unittest.mock import patch, Mock
from uniworkflow import UniwWorkflow
from uniworkflow.exceptions import ProviderNotFoundError, WorkflowExecutionError

@pytest.fixture
def mock_make_provider(monkeypatch):
    mock_provider = Mock()
    monkeypatch.setattr('uniworkflow.providers.make.MakeProvider', mock_provider)
    return mock_provider

def test_execute_workflow_successful(mock_make_provider):
    # Arrange
    expected_result = {
        "video_url": "......",
        "description": "..."
    }
    mock_make_provider.execute.return_value = expected_result, 200

    kwargs = {
        "workflow_url": "your_workflow_url",
        "method": "GET",
        "data": {"url": "https://www.youtube.com/watch?v=VGjorrrxh2Y&t=4s"},
        "api_key": "test_api_key"
    }

    # Act
    result, status_code = UniwWorkflow.execute("make", **kwargs)
    print(result)
    # Assert
    assert isinstance(result, dict)
    assert "video_url" in result
    assert "description" in result
    assert status_code == 200

def test_execute_workflow_error(mock_make_provider):
    # Arrange
    mock_make_provider.execute.side_effect = Exception("Workflow execution failed")

    kwargs = {
        "workflow_url": "your_workflow_url",
        "data": {"topic": "Test Topic"},
        "api_key": "test_api_key"
    }

    # Act & Assert
    with pytest.raises(WorkflowExecutionError) as exc_info:
        UniwWorkflow.execute("make", **kwargs)

    assert str(exc_info.value) == "Error executing workflow: Workflow execution failed"

def test_execute_workflow_missing_api_key():
    # Arrange
    kwargs = {
        "workflow_url": "your_workflow_url",
        "data": {"topic": "Test Topic"}
    }

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        UniwWorkflow.execute("make", **kwargs)

    assert str(exc_info.value) == "API key is required"

def test_execute_workflow_invalid_provider():
    # Arrange
    kwargs = {
        "workflow_url": "your_workflow_url",
        "data": {"key": "value"},
        "api_key": "test_api_key"
    }

    # Act & Assert
    with pytest.raises(ProviderNotFoundError) as exc_info:
        UniwWorkflow.execute("invalid_provider", **kwargs)

    assert "Provider 'invalid_provider' not found" in str(exc_info.value)