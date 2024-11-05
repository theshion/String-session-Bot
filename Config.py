import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Ensure SQLAlchemy compatibility.
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill in the Values directly for local testing
    API_ID = 20787644
    API_HASH = "9dada820698e8a5fdd5e6cc78fac8567"
    BOT_TOKEN = "7939164806:AAFM_IcYWxPqVVbKGbdlEThnXLQ4qHS1AYA"
    DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Ensure SQLAlchemy compatibility.
    MUST_JOIN = "@Coding"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
