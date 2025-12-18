from fastapi import FastAPI, Query, HTTPException
from app.magento import search_products
from app.models import Product, ProductSearchResponse, Price
from app.utils import strip_html

app = FastAPI(
    title="CMI Store Product Search API",
    description="ChatGPT Action API to search products from CMI E-Store",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/search-products", response_model=ProductSearchResponse)
def search(q: str = Query(..., min_length=2)):
    try:
        data = search_products(q)
        products = data.get("data", {}).get("products", {})

        items = []
        for p in products.get("items", []):
            price = p["price_range"]["minimum_price"]["final_price"]

            items.append(
                Product(
                    name=p["name"],
                    sku=p["sku"],
                    price=Price(
                        value=price["value"],
                        currency=price["currency"],
                    ),
                    image=p.get("small_image", {}).get("url"),
                    url=f"https://cmiestore.com/{p['url_key']}{p['url_suffix']}",
                    description=strip_html(p["description"]["html"]),
                )
            )

        return ProductSearchResponse(
            total=products.get("total_count", 0),
            items=items,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
