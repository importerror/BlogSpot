import os
import base64
KEY=base64.b64encode(os.urandom(32))

CSRF_ENABLE = True
SECRET_KEY=KEY
