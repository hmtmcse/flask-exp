class Address(object):
    first_name = None
    last_name = None
    address = None

    def get_data(self):
        map = {}
        for name, value in self.__dict__.items():
            if name == "address":
                name = "extended_address"
            map[name] = value
        return map


class CustomerData(object):
    customer_id = None
    email = None
    first_name = None
    last_name = None
    mobile = None
    payment_nonce = None
    verify_card: bool = False
    billing_address : Address = None

    def __init__(self, first_name: str, email: str):
        self.first_name = first_name
        self.email = email

    def _process_verify_card(self, map):
        credit_card = {}
        if "credit_card" in map:
            credit_card = map['credit_card']
        credit_card["options"] = {"verify_card": True}
        return credit_card

    def _process_billing_address(self, map):
        credit_card = {}
        if "credit_card" in map:
            credit_card = map['credit_card']
        credit_card["billing_address"] = self.billing_address.get_data()
        return credit_card

    def get_data(self):
        map = {}
        for name, value in self.__dict__.items():
            if name == "payment_nonce":
                name = "payment_method_nonce"
            elif name == "customer_id":
                name = "id"
            elif name == "verify_card":
                name = "credit_card"
                value = self._process_verify_card(map)
            elif name == "billing_address":
                name = "credit_card"
                value = self._process_billing_address(map)
            map[name] = value
        return map
