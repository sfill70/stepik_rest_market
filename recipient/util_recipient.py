import requests
from requests.exceptions import Timeout
from typing import Any, Dict, Optional, List


def convert_json_recipient(convert_json: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'surname': convert_json['info']['surname'],
        'name': convert_json['info']['name'],
        'patronymic': convert_json['info']['patronymic'],
        'phoneNumber': convert_json['contacts']['phoneNumber'],
    }


def list_recipient_json(recipient_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    try:
        recipient_list = [convert_json_recipient(recipient) for recipient in recipient_list]
    except Exception as exc:
        raise exc
    return recipient_list


recipients_url = "https://stepik.org/media/attachments/course/73594/recipients.json"

