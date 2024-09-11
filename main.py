from fastapi import FastAPI
import uvicorn
from api import router as ApiRouter
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000"
]

app = FastAPI()
app.include_router(router=ApiRouter)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=int(8000), reload=True)

