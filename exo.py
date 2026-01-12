from typing import List, Dict, Any, Union

def process_user_data(user_data: Dict[str, Any], include_history: bool = False) -> Dict[str, Any]:
    user_id = user_data["id"]
    name = user_data["name"]
    
    result: Dict[str, Any] = {
        "display_name": f"User {name}",
        "normalized_id": str(user_id).zfill(8)
    }
    
    if include_history:
        result["history"] = get_user_history(user_id)
    
    return result

def get_user_history(user_id: int) -> List[Dict[str, str]]:
    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]

sample_user: Dict[str, Union[str, int]] = {"id": 42, "name": "Alice"}
processed = process_user_data(sample_user, True)
print(processed)