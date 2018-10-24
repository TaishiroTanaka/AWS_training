import json
from decimal import Decimal

from lib.domain.model.humouword_factory import HumouWordFactory
from app.infrastructure.humouword import HumouWordDataSource
from app.application.humouword import HumouWordRegisterService


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
