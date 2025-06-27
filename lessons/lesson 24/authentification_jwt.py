# pip install pyjwt
import jwt

from datetime import datetime, timedelta

# >>> import uuid
# >>> uuid.uuid4()
# UUID('ca4fa2e8-7f88-4b31-a108-cf767634937d')
SECRET = 'ca4fa2e8-7f88-4b31-a108-cf767634937d'
ALGORITHM = "HS256" # os.environ()

payload = {
    # sub = subject = той, хто запитує
    "sub": "fluffy",
    # exp = expire = коли токен перестане діяти
    "exp": datetime.utcnow() + timedelta(seconds=4)
}

token = jwt.encode( payload, SECRET, ALGORITHM )
print(token)

decoded_token = jwt.decode( token, SECRET, ALGORITHM )
print(decoded_token)
