import sys
import requests

print("Initiating Request")

API_URL = ''
API_KEY = ''


def create_ticket(phone, subject_message="Missed called from", name_message="Missed called from", call_description=None):
    if not call_description:
        call_description = "Ticket for missed call"

    request_data = {
        "name": name_message + " " + phone,
        "phone": phone,
        "subject": subject_message + " " + phone,
        "priority": 1,
        "description": call_description,
        "status": 2
    }
    response = requests.post(API_URL + 'api/v2/tickets', auth=(API_KEY, 'X'), json=request_data)
    api_response = "Response Code: " + str(response.status_code) + "\n"
    api_response += "Response " + str(response.text) + "\n\n"
    print(api_response)


args_count = len(sys.argv)
if args_count <= 1:
    print("Please enter phone number")
else:
    phone = sys.argv[1]
    create_ticket(phone)


