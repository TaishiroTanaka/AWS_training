import json

from app.infrastructure.dynamodb import DataSource
from lib.domain.model.humouword import HumouWord


class HumouWordDataSource:
    def __init__(self):
        self.datasource = DataSource.get_dynamodb()

    def register(self, humou_word: HumouWord) -> None:
        humou_word_table_name = 'HumouWord'
        humou_word_table = self.datasource.Table(humou_word_table_name)
        humou_word_dict = DataSource.dynamo_type_encode(humou_word.to_dict())
        humou_word_table.put_item(Item=humou_word_dict)
