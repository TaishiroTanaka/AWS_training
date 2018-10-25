import json
import random

from app.infrastructure.dynamodb import DataSource
from lib.domain.model.humouword import HumouWord
from lib.domain.model.humouword import WordId


class HumouWordDataSource:
    def __init__(self):
        self.datasource = DataSource.get_dynamodb()

    def register(self, humou_word: HumouWord) -> None:
        humou_word_table_name = 'HumouWord'
        humou_word_table = self.datasource.Table(humou_word_table_name)
        humou_word_dict = DataSource.dynamo_type_encode(humou_word.to_dict())
        humou_word_table.put_item(Item=humou_word_dict)

    def delete(self, humou_word: HumouWord) -> None:
        humou_word_table_name = 'HumouWord'
        humou_word_table = self.datasource.Table(humou_word_table_name)
        humou_word_dict = DataSource.dynamo_type_encode(humou_word.to_dict())
        humou_word_table.delete_item(Key={'word_id': humou_word_dict['word_id']})

    def get_top_word_random(self) -> HumouWord:
        humou_word_list = self.find_all()

        top_word_list = []
        for humou_word in humou_word_list:
            if humou_word.type.name == 'top':
                top_word_list.append(humou_word)

        return random.choice(top_word_list)

    def get_bottom_word_random(self) -> HumouWord:
        humou_word_list = self.find_all()

        bottom_word_list = []
        for humou_word in humou_word_list:
            if humou_word.type.name == 'bottom':
                bottom_word_list.append(humou_word)

        return random.choice(bottom_word_list)

    def find_all(self) -> list:
        humou_word_table_name = 'HumouWord'
        humou_word_table = self.datasource.Table(humou_word_table_name)
        results = humou_word_table.scan()

        humou_word_list = []
        for result in results['Items']:
            humou_word = HumouWord.from_dict(result)
            humou_word_list.append(humou_word)

        return humou_word_list

    def find_by_id(self, word_id: WordId) -> HumouWord:
        humou_word_table_name = 'HumouWord'
        humou_word_table = self.datasource.Table(humou_word_table_name)
        result = humou_word_table.get_item(Key={'word_id': word_id.value})
        item = result['Item']
        humou_word = HumouWord.from_dict(item)

        return humou_word
