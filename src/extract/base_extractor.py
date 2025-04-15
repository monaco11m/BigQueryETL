from abc import ABC,abstractmethod
import pandas as pd

class BaseExtractor(ABC):
    @abstractmethod
    def extract(self) -> pd.DataFrame:
        pass