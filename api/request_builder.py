class RequestBuilder:

    def __init__(self):

        self.request_data = {

            "headers": {},

            "params": {},

            "payload": {}
        }

    def add_headers(
        self,
        headers
    ):

        self.request_data[
            "headers"
        ].update(headers)

        return self

    def add_params(
        self,
        params
    ):

        self.request_data[
            "params"
        ].update(params)

        return self

    def add_payload(
        self,
        payload
    ):

        self.request_data[
            "payload"
        ].update(payload)

        return self

    def build(self):

        return self.request_data