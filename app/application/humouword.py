from app.infrastructure.humouword import HumouWordDataSource
from lib.domain.model.humouword import HumouWord


class HumouWordRegisterService:
    def __init__(self, humou_word_datasource: HumouWordDataSource) -> None:
        self.humou_word_datasource = humou_word_datasource

    def register(self, humou_word: HumouWord) -> bool:
        self.humou_word_datasource.register(humou_word)
        return True
