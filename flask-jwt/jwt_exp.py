import jwt

secret_key = "very_secret"
encoded = jwt.encode({"key": "value"}, secret_key, algorithm="HS256")
print(encoded)

