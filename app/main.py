from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .startup import init_db
from .routers import router

app = FastAPI(title="Career Guidance Prototype")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok", "service": "career-guidance-prototype"}


@app.on_event("startup")
def on_startup():
    init_db()
    app.include_router(router)


