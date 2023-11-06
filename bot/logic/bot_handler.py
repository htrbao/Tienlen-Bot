from abc import ABC, abstractmethod


class BotHandler(ABC):
    def __init__(self, device: str):
        self.device = device
    @abstractmethod
    def handle_hit_card(self, obs: dict):
        pass