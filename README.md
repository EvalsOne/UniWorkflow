# UniWorkflow

[English Version](README.md) | [中文版](README_zh.md)


UniWorkflow is a Python library that provides a unified interface for integrating with various workflow providers such as Make.com and Dify.

## Installation

You can install UniWorkflow using pip:

```
pip install uniworkflow
```

## Quick Start

### Run a make.com workflow
Here's a simple example of how to use UniWorkflow:

```python
# import the library
from uniworkflow import UniWorkflow

# prepare the kwargs
kwargs = {
    "workflow_url": "https://example.make.com/your-workflow-hook",
    "method": "GET",
    "api_key": "your_api_key_here",
    "data": {"key1": "value1", "key2": "value2", ......},
}

# Execute a workflow
result = UniWorkflow.execute("make", **kwargs)

# print the result
print(result)
```

### Run a dify workflow

```python
# import the library
from uniworkflow import UniWorkflow

# prepare the kwargs
kwargs = {
    "workflow_url": "https://api.dify.ai/v1/workflows/run",
    "method": "POST",
    "api_key": "your_api_key_here",
    "data": {"key1": "value1", "key2": "value2", ......},
}

# Execute a workflow
result = UniWorkflow.execute("dify", **kwargs) 

# print the result
print(result)
```

## Parameters

- `workflow_url`: The URL of the workflow to execute.
- `method`: The HTTP method to use (GET, POST, etc.).
- `api_key`: The API key to use for the workflow.
- `data`: The data to pass to the workflow.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Running Tests

To run the tests for UniWorkflow, you can use pytest. Make sure you have pytest installed and replace the parameters in the test cases with your own.

```
pip install pytest
```

Then, run the tests:

```
pytest -s tests/test_make.py
pytest -s tests/test_dify.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.