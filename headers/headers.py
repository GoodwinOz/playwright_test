def get_headers(auth_token=None):
    headers = {
        'Content-Type': 'application/json',
    }
    if auth_token:
        headers['Accept'] = 'application/json'
        headers['Cookie'] = f'token={auth_token}'
    return headers