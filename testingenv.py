# Source - https://stackoverflow.com/a/61029741
# Posted by ParisNakitaKejser, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-04, License - CC BY-SA 4.0

import os
from dotenv import load_dotenv

load_dotenv()

REDIRECT = os.getenv('REDIRECT_URI')
SECRET = os.getenv('CLIENT_SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')

print(REDIRECT)
print(SECRET)
print(CLIENT_ID)
