from typing import List, Any

""" класс для создание базовых шагов в частности списка для хранения """
class BaseSteps:
    def __init__(self, created_obj: List[Any]):
        self.created_obj = created_obj