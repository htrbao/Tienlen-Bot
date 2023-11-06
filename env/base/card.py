EnvCard2RealCard = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q',
                    13: 'K', 14: 'A', 17: '2'}

RealCard2EnvCard = {'3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                    '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12,
                    'K': 13, 'A': 14, '2': 17}

EnvShape2RealShape = {0: 's', 1: 'c', 2: 'd', 3: 'h'}

RealShape2EnvShape = {'s': 0, 'c': 1, 'd': 2, 'h': 3}

class Card:
    def __init__(self, card_id: str):
        self.card_id = card_id #2B = 4

        self.type: str = card_id[0]
        self.shape: str = card_id[1]

        # if 2 <= self.card_id // 4 <= 12:
        #     self.type: str = EnvCard2RealCard[self.card_id // 4 + 1]
        # elif self.card_id // 4 == 0:
        #     self.type: str = EnvCard2RealCard[14]
        # elif self.card_id // 4 == 1:
        #     self.type: str = EnvCard2RealCard[17]

        
        self.id: int = self.get_type() * 4 + self.get_shape()

    def get_type(self):
        return RealCard2EnvCard[self.type]

    def get_shape(self):
        return RealShape2EnvShape[self.shape]

    def __eq__(self, other) -> bool:
        if isinstance(other, Card):
            return self.id == other.id
        else:
            # don't attempt to compare against unrelated types
            return NotImplemented
        
    def __ne__(self, __value: object) -> bool:
        if isinstance(__value, Card):
            return self.id != __value.id
        else:
            # don't attempt to compare against unrelated types
            return NotImplemented

    def __repr__(self):
        return f"{self.card_id}"

    QUAN_BAI_NONE = 13
    CHAT_NONE = 4
