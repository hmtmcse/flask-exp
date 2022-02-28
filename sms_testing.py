import requests

message = "প্রিয় গ্রাহক"
message = message.encode('utf-16-be').hex().upper()
data = {
    "user": "",
    "pass": "",
    "sid": "",
    "sms[0][0]": "",
    # "sms[0][0]": "",
    "sms[0][1]": message,
    "sms[0][2]": "98765",
}
# thread = Thread(target=threaded_function, args=(10,))
# thread.start()
# thread.join()
r = requests.post("http://sms.sslwireless.com/pushapi/dynamic/server.php", data=data)
print("-----")
if r.status_code == 200:
    print("Success")
    print(r.content)
