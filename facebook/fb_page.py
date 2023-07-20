import json
import requests

ACCESS_TOKEN = ""
PAGE_ID = ""


def send_to_fb(url_postfix, method="get", data=None, json=None, files=None, params=None):
    if params is None:
        params = {}

    url = f"https://graph.facebook.com/{PAGE_ID}/{url_postfix}"
    params["access_token"] = ACCESS_TOKEN
    response = None
    if method == "get":
        response = requests.get(url=url)
    else:
        response = requests.post(url=url, params=params, data=data, json=json, files=files)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Reason: {response.reason}")
        print(f"Error: {response.reason}")
        return None
    return response


def post_content(content):
    response = send_to_fb("feed", json={"message": content}, method="post")
    return response


def post_image_and_content(content, image_file_path, is_publish=True):
    data = {"message": content, "published": is_publish}
    files = {"source": open(image_file_path, 'rb')}
    response = send_to_fb("photos", data=data, files=files, method="post")
    return response


def post_multiple_image_and_content(content, image_and_content: list):
    image_ids = []
    for data in image_and_content:
        single_response = post_image_and_content(data["content"], data["file"], is_publish=False)
        if single_response:
            json_data = json.loads(single_response)
            if json_data and "id" in json_data:
                image_ids.append({"media_fbid": json_data["id"]})
    json_request_content = {
        "message": content,
    }

    if image_ids:
        json_request_content["attached_media"] = image_ids

    response = send_to_fb("feed", json=json_request_content, method="post")
    print(response)


# print("Create text post")
# post_content("Post from Python application")

# print("Create text & Image post")
# post_image_and_content("Post from Python application with image", "resource/bg.png")


print("Upload Multiple Image")
image_and_content_input = [
    {"content": "Image 1", "file": "resource/bg.png"},
    {"content": "Image 2", "file": "resource/internship.jpg"},
    {"content": "Image 3", "file": "resource/watermark.png"},
]
post_multiple_image_and_content("Multiple Image post from App", image_and_content=image_and_content_input)
