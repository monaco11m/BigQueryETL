from abc import ABC,abstractmethod
import pandas as pd

class BaseExtractor(ABC):
    @abstractmethod
    def extract(dataset) -> pd.DataFrame:
        pass