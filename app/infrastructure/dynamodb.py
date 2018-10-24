import boto3

from datetime import date as Date
from datetime import datetime as DateTime


class DataSource:
    @staticmethod
    def get_dynamodb():
        return boto3.resource('dynamodb')

    @staticmethod
    def dynamo_type_encode(obj):
        if type(obj) == dict:
            new_dict: dict = dict()
            for key, value in obj.items():
                new_value = DataSource.dynamo_type_encode(value)
                if new_value is None or new_value == "":
                    continue
                new_dict[key] = new_value
            return new_dict
        elif type(obj) == list:
            return [DataSource.dynamo_type_encode(elem) for elem in obj]
        elif type(obj) == DateTime:
            return obj.isoformat()
        elif type(obj) == Date:
            return obj.isoformat()
        else:
            return obj
