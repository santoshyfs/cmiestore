import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from app.config import MAGENTO_GRAPHQL_URL, REQUEST_TIMEOUT


GRAPHQL_QUERY = """
query ($search: String!) {
  products(search: $search, pageSize: 5) {
    total_count
    items {
      name
      sku
      url_key
      url_suffix
      description {
        html
      }
      small_image {
        url
        label
      }
      price_range {
        minimum_price {
          final_price {
            value
            currency
          }
        }
      }
    }
  }
}
"""


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def search_products(search: str) -> dict:
    response = requests.post(
        MAGENTO_GRAPHQL_URL,
        json={
            "query": GRAPHQL_QUERY,
            "variables": {"search": search},
        },
        headers={"Content-Type": "application/json"},
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()
    return response.json()
