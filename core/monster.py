from abc import ABC, abstractmethod
import random


class Monster(ABC):

    def __init__(self):
        self.weapon = random.choice(["knife", "sword", "hammer"])

        @abstractmethod
        def speak():
            pass

        @abstractmethod
        def attack():
            pass

        @abstractmethod
        def chek_hp():
            pass