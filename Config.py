import os

# Get the environment status
ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    
    # Ensure SQLAlchemy compatibility
    if DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  
    
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN and MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]  # Remove '@' from MUST_JOIN
else:
    # Fill in the values directly for local testing
    API_ID = 20787644
    API_HASH = "9dada820698e8a5fdd5e6cc78fac8567"
    BOT_TOKEN = "7939164806:AAFM_IcYWxPqVVbKGbdlEThnXLQ4qHS1AYA"
    DATABASE_URL = "mongodb+srv://abc:abc@music.dlua0.mongodb.net/yukk
i?retryWrites=true&w=majority"
    
    # Ensure SQLAlchemy compatibility
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  
    MUST_JOIN = "@Coding"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]  # Remove '@' from MUST_JOIN

# Debug print to check the values
print(f"API_ID: {API_ID}, API_HASH: {API_HASH}, BOT_TOKEN: {BOT_TOKEN}, DATABASE_URL: {DATABASE_URL}, MUST_JOIN: {MUST_JOIN}")

# Continue with your application logic...
