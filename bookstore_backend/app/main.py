from fastapi import FastAPI
from app.routes import book
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Update with your frontend origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(book.router, prefix="/api/v1")

# Additional route to generate OpenAPI schema
@app.get("/openapi.json")
async def get_open_api_endpoint():
    return JSONResponse(content=get_openapi(title="Your Bookstore API", version="1.0.0", routes=app.routes))