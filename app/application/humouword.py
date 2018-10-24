from app.infrastructure.humouword import HumouWordDataSource
from lib.domain.model.humouword import HumouWord
from lib.domain.model.humou import Humou
from lib.domain.model.humou_factory import HumouFactory


class HumouWordRegisterService:
    def __init__(self, humou_word_datasource: HumouWordDataSource) -> None:
        self.humou_word_datasource = humou_word_datasource

    def register(self, humou_word: HumouWord) -> bool:
        self.humou_word_datasource.register(humou_word)
        return True


class GetHumouService:
    def __init__(self, humou_word_datasource: HumouWordDataSource) -> None:
        self.humou_word_datasource = humou_word_datasource

    def get(self) -> dict:
        top_word = self.humou_word_datasource.get_top_word_random()
        bottom_word = self.humou_word_datasource.get_bottom_word_random()

        humou = HumouFactory.create(top_word=top_word,
                                    bottom_word=bottom_word)

        return humou.to_dict()
