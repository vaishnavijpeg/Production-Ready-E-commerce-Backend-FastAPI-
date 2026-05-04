from fastapi import FastAPI
from app.api.routes import auth, users, products, cart, orders

app = FastAPI(title="FastAPI E-commerce Backend")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])


@app.get("/")
def health_check():
    return {"status": "Ecommerce backend running"}
