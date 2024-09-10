from fastapi import FastAPI
import uvicorn
from api import router as ApiRouter

app = FastAPI()
app.include_router(router=ApiRouter)



