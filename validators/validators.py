def validate_status_code(response, expected_status):
    assert response.status_code == expected_status

def validate_response_key(response_json, key, expected_value):
    assert response_json.get(key) == expected_value, f"Expected {key} to be {expected_value},  but got {response_json.get(key)}"