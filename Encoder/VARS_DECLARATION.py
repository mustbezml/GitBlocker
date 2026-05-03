from enum import Enum
from abc import abstractmethod, ABC

class VARS_CONTEXT(ABC):
    @abstractmethod
    def get_origin(encrypt: str):
        pass

    @abstractmethod
    def get_encrypted(origin: str):
        pass


class ENCODE_CONTEXT(Enum, VARS_CONTEXT):
    ... # Будет описан, как напишу модуль полностью
