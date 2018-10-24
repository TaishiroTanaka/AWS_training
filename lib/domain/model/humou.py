from lib.domain.model.humouword import HumouWord


class Nickname:
    def __init__(self, nickname: str) -> None:
        self.value = nickname


class Humou:
    def __init__(self, nickname: Nickname, top_word: HumouWord, bottom_word: HumouWord) -> None:
        self.nickname = nickname
        self.top_word = top_word
        self.bottom_word = bottom_word

    def to_dict(self) -> dict:
        return {
            'nickname': self.nickname.value,
            'top_word': self.top_word.to_dict(),
            'bottom_word': self.bottom_word.to_dict(),
        }
