import json
from decimal import Decimal

from lib.domain.model.humouword_factory import HumouWordFactory
from lib.domain.model.humouword import WordId
from app.infrastructure.humouword import HumouWordDataSource
from app.application.humouword import HumouWordRegisterService
from app.application.humouword import HumouWordGetService
from app.application.humouword import HumouWordDeleteService
from app.application.humouword import GetHumouService


def register_humou_word_handler(event, context):
    params = json.loads(event['body'])
    humou_word = HumouWordFactory.create(params)

    humou_word_datasource = HumouWordDataSource()
    humou_word_register_service = HumouWordRegisterService(humou_word_datasource)
    result = humou_word_register_service.register(humou_word)

    if result is True:
        body = {
            "message": "HumouWord Create Request successfully!",
            "word_id": humou_word.word_id.value
        }
        return create_response(200, body)
    else:
        body = {
            "message": "HumouWord Create Request failure!",
        }
        return create_response(500, body)


def find_humou_word_handler(event, context):
    humou_word_datasource = HumouWordDataSource()
    humou_word_register_service = HumouWordGetService(humou_word_datasource)
    results = humou_word_register_service.find_all()

    humou_word_dict_list = []
    for result in results:
        humou_word_dict = result.to_dict()
        humou_word_dict_list.append(humou_word_dict)

    body = {
        "message": "Get HumouWord Request successfully!",
        "humou_word_list": humou_word_dict_list
    }
    return create_response(200, body)


def delete_humou_word_handler(event, context):
    params = json.loads(event['body'])
    humou_word_datasource = HumouWordDataSource()
    humou_word_get_service = HumouWordGetService(humou_word_datasource)
    humou_word_delete_service = HumouWordDeleteService(humou_word_datasource)

    humou_word_list =[]
    for param in params:
        word_id = WordId(param['word_id'])
        hummou_word = humou_word_get_service.find_by_id(word_id)
        humou_word_list.append(hummou_word)

    result = humou_word_delete_service.delete_multi(humou_word_list)

    if result is True:
        body = {
            "message": "HumouWord Delete Request successfully!",
        }
        return create_response(200, body)
    else:
        body = {
            "message": "HumouWord Delete Request failure!",
        }
        return create_response(500, body)


def get_humou_handler(event, context):
    humou_word_datasource = HumouWordDataSource()
    get_humou_service = GetHumouService(humou_word_datasource)
    result = get_humou_service.get()

    body = {
        "message": "Get Humou Request successfully!",
        "humou": result
    }
    return create_response(200, body)


def create_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "x-custom-header": "my custom header value"
        },
        "body": json.dumps(body, default=decimal_default_proc)
    }


def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj
