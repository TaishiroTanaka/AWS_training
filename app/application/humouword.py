from app.infrastructure.humouword import HumouWordDataSource
from lib.domain.model.humouword import HumouWord
from lib.domain.model.humouword import WordId
from lib.domain.model.humou import Humou
from lib.domain.model.humou_factory import HumouFactory


class HumouWordRegisterService:
    def __init__(self, humou_word_datasource: HumouWordDataSource) -> None:
        self.humou_word_datasource = humou_word_datasource

    def register(self, humou_word: HumouWord) -> bool:
        self.humou_word_datasource.register(humou_word)
        return True


class HumouWordGetService:
    def __init__(self, humou_word_datasource: HumouWordDataSource) -> None:
        self.humou_word_datasource = humou_word_datasource

    def find_all(self) -> list:
        humou_word_list = self.humou_word_datasource.find_all()
        return humou_word_list

    def find_by_id(self, word_id: WordId) -> HumouWord:
        humou_word = self.humou_word_datasource.find_by_id(word_id)
        return humou_word


class HumouWordDeleteService:
    def __init__(self, humou_word_datasource: HumouWordDataSource) -> None:
        self.humou_word_datasource = humou_word_datasource

    def delete(self, humou_word: HumouWord) -> bool:
        self.humou_word_datasource.delete(humou_word)
        return True

    def delete_multi(self, humou_word_list: list) -> bool:
        for humou_word in humou_word_list:
            self.humou_word_datasource.delete(humou_word)

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
