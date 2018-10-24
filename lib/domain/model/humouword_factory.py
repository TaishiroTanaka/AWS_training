import random

from lib.domain.model.humouword import WordId
from lib.domain.model.humouword import Word
from lib.domain.model.humouword import Type
from lib.domain.model.humouword import HumouWord


class HumouWordFactory:
    @staticmethod
    def create(params):
        word_id = random.randint(1000000, 9999999)

        return HumouWord(
            word_id=WordId(word_id),
            word=Word(params['word']),
            type=Type[params['type']],
        )
