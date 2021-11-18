import datetime
import jwt


class JWTUtil:
    ALGORITHMS: str = "HS256"
    JWT_ACCESS_TOKEN_VALIDITY_MIN = 1
    JWT_REFRESH_TOKEN_VALIDITY_MIN = 60
    SECRET = "SECRET____KEY"

    def get_token(self, exp: datetime, payload: dict = None, iss=None):
        if not payload:
            payload = {}
        payload["exp"] = exp
        if iss:
            payload["iss"] = iss
        return jwt.encode(payload, self.SECRET, algorithm=self.ALGORITHMS)

    def get_access_token(self, payload: dict = None, iss=None):
        validity = self.get_access_token_validity()
        return self.get_token(validity, payload=payload, iss=iss)

    def get_refresh_token(self, payload: dict = None, iss=None):
        validity = self.get_refresh_token_validity()
        return self.get_token(validity, payload=payload, iss=iss)

    def validate_token(self, token: str):
        try:
            return jwt.decode(token, self.SECRET, algorithms=[self.ALGORITHMS])
        except jwt.ExpiredSignatureError:
            return None

    def get_access_token_validity(self, minutes=None):
        if not minutes:
            minutes = self.JWT_ACCESS_TOKEN_VALIDITY_MIN
        return self.get_token_validity(minutes)

    def get_refresh_token_validity(self, minutes=None):
        if not minutes:
            minutes = self.JWT_REFRESH_TOKEN_VALIDITY_MIN
        return self.get_token_validity(minutes)

    def get_token_validity(self, minutes):
        return datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=minutes)


if __name__ == "__main__":
    jwt_util = JWTUtil()
    _validity = jwt_util.get_access_token_validity()
    print(_validity)
    print(jwt_util.get_access_token())
    response = jwt_util.validate_token("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzcyMzg1NTJ9.jCDlzb89Pyyc36BCV2JUcLTIB_OnKmnc-VSx4oXPdB8")
    print(response)
