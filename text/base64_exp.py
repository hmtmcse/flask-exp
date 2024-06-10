import base64


def base64_encode(text, altchars=None):
    if not text:
        return None
    bytes_string = text.encode('utf-8')
    base64_bytes = base64.b64encode(bytes_string, altchars=altchars)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


def base64_decode(base64_text, altchars=None):
    if not base64_text:
        return None
    bytes_string = base64_text.encode('utf-8')
    base64_bytes = base64.b64decode(bytes_string, altchars=altchars)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


base64_string = base64_encode("বিসমিল্লাহ")
print(base64_string)
print(base64_decode(base64_string))
