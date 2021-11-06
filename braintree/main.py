from braintree_pay.braintree_service import BraintreeService
from data.customer_data import CustomerData


def bismillah():
    braintree_service = BraintreeService()

    customer_data = CustomerData(first_name="Touhid", email="email")
    print(customer_data.get_data())

    # customer = braintree_service.create_customer(email="hmtmcse.office@gmail.com", first_name="Mia")
    # print(customer)


if __name__ == '__main__':
    bismillah()
