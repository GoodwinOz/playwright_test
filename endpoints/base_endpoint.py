class Endpoint:
    response = None
    response_json = None

    def _safe_json(self):
        try:
            return self.response.json()
        except ValueError:
            return None
    
    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_response_is_404(self):
        assert self.response.status_code == 404

    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id