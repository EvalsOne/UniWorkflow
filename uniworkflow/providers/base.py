from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def execute(self, workflow_id, method="GET", headers={}, data=None):
        pass

