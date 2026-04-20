from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router as chat_router

app = FastAPI(title="ChatFastapi", docs_url="/api/chat/docs", redoc_url="/api/chat/redoc", openapi_url="/api/chat/openapi.json")

#por ahora dejarlo asi
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(chat_router, prefix="/api/chat")