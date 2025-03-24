# UniWorkflow

[English Version](README.md) | [中文版](README_zh.md)

UniWorkflow 是一个 Python 库，为集成各种工作流提供商（如 Make.com 和 Dify）提供统一接口。

## 安装

您可以使用 pip 安装 UniWorkflow：

```
pip install uniworkflow
```

## 快速开始

### 运行 make.com 工作流
以下是使用 UniWorkflow 的简单示例，它接受一个url参数从youtube上获取：

```python
# import the library
from uniworkflow import UniWorkflow

# prepare the kwargs
kwargs = {
    "workflow_url": "https://example.make.com/your-workflow-hook",
    "method": "GET",
    "api_key": "your_api_key_here",
    "data": {"key1": "value1", "key2": "value2", ......}
}

# Execute a workflow
result = UniWorkflow.execute("make", **kwargs)

# print the result
print(result)
```

### 运行 dify 工作流

```python
# import the library
from uniworkflow import UniWorkflow

# prepare the kwargs
kwargs = {
    "workflow_url": "https://mock.dify.com/v1/workflows/run",
    "method": "POST",
    "api_key": "mock_api_key",
    "data": {"key1": "value1", "key2": "value2", ......}
}

# Execute a workflow
result = UniWorkflow.execute("dify", **kwargs) 

# print the result
print(result)
```

## 参数

- `workflow_url`: 要执行的工作流的 URL。
- `method`: 要使用的 HTTP 方法（GET, POST 等）。
- `api_key`: 用于工作流的 API 密钥。
- `data`: 要传递给工作流的参数, 字典类型。

## 贡献

欢迎贡献！请随时提交一个 Pull Request。

## 运行测试

要运行 UniWorkflow 的测试，可以使用 pytest。确保您已安装 pytest 并替换测试用例中的参数。

```
pip install pytest
```

然后，运行测试：

```
pytest -s tests/test_make.py
pytest -s tests/test_dify.py
```

## 许可证

本项目采用 MIT 许可证 - 请参阅 [LICENSE](LICENSE) 文件了解更多信息。
