import os
from dotenv import load_dotenv

load_dotenv()

MAGENTO_GRAPHQL_URL = os.getenv(
    "MAGENTO_GRAPHQL_URL",
    "https://cmiestore.com/graphql"
)

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
