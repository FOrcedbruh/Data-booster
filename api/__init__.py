from fastapi import APIRouter
from .auth.views import router as authRouter

router = APIRouter(prefix="/api")
router.include_router(router=authRouter)