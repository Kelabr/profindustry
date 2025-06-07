from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from ..core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def createAccessToken(data:dict):
    toEncode = data.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    toEncode.update({'exp':expire})
    encodedJwt = encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodedJwt

