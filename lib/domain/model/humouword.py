from enum import Enum, auto


class WordId:
    def __init__(self, word_id: int) -> None:
        self.value = word_id


class Word:
    def __init__(self, word: str) -> None:
        self.value = word


class Type(Enum):
    top = auto()
    bottom = auto()


class HumouWord:
    def __init__(self, word_id: WordId, word: Word, type: Type) -> None:
        self.word_id = word_id
        self.word = word
        self.type = type

    def to_dict(self) -> dict:
        return {
            "word_id": self.word_id.value,
            "word": self.word.value,
            "type": self.type.name,
        }

    @staticmethod
    def from_dict(humouword_dict: dict) -> 'HumouWord':
        _dict = humouword_dict.copy()

        return HumouWord(
            word_id=WordId(_dict['word_id']),
            word=Word(_dict['word']),
            type=Type[_dict['type']],
        )
    