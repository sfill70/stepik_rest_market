from typing import Any, Dict, List


def convert_json_market(convert_json: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'title': convert_json['name'],
        'description': convert_json['about'],
        'price': convert_json['price'],
        'weight': convert_json['weight_grams'],
        'inner_id': convert_json["inner_id"],
    }


def list_market_json(market_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    market_list = [convert_json_market(recipient) for recipient in market_list]
    return market_list


def convert_json_market_2(convert_json: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'title': convert_json['name'],
        'description': convert_json['about'],
        'price': convert_json['price'],
        'weight': convert_json['weight_grams'],
    }


def list_market_json_2(market_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    market_list = [convert_json_market_2(recipient) for recipient in market_list]
    return market_list


beauty_url = "https://stepik.org/media/attachments/course/73594/beautyboxes.json"
food_url = "https://stepik.org/media/attachments/course/73594/foodboxes.json"
presents_url = "https://stepik.org/media/attachments/course/73594/presentsboxes.json"
# presents_url = "https://stepik.org/media/attachments/course/735941/presentsboxes.json"
