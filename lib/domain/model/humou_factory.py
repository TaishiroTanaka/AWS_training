from lib.domain.model.humouword import HumouWord
from lib.domain.model.humou import Nickname
from lib.domain.model.humou import Humou


class HumouFactory:
    @staticmethod
    def create(top_word: HumouWord, bottom_word: HumouWord):
        nickname = Nickname(top_word.word.value + bottom_word.word.value)

        return Humou(
            nickname=nickname,
            top_word=top_word,
            bottom_word=bottom_word,
        )
