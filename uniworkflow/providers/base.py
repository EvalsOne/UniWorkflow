from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def execute(self, workflow_id, data=None):
        pass

