from dotenv import load_dotenv

from data.customer_data import CustomerData
from gateway import generate_client_token, gateway


class BraintreeService:

    def __init__(self):
        load_dotenv()

    def get_client_token(self):
        return generate_client_token()

    def _create_update_customer(self,
                                action: str,
                                email: str,
                                first_name: str,
                                last_name: str = None,
                                mobile: str = None,
                                id: str = None,
                                payment_nonce: str = None,
                                ):
        request = {"email": email, "first_name": first_name}
        if last_name:
            request["last_name"] = last_name
        if mobile:
            request["mobile"] = mobile
        if payment_nonce:
            request["payment_method_nonce"] = payment_nonce
        if id and action == "create":
            request["id"] = id
        if action == "update" and id:
            return gateway.customer.update(id, request)
        elif action == "create":
            return gateway.customer.create(request)
        return None

    def create_customer(self, data: CustomerData):
        return gateway.customer.create(data.get_data())

    def update_customer(self, id: str, data: CustomerData):
        return gateway.customer.update(id, data.get_data())

    def get_customer_by_id(self, id):
        gateway.customer.find(id)

    def delete_customer_by_id(self, id):
        gateway.customer.delete(id)
