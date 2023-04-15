import time

import jwt

from core.config import settings


JWT_SECRET = settings.jwt_secret
JWT_ALGORITHM = settings.jwt_algorithm

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}