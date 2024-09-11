from fastapi import APIRouter
from .auth.views import router as authRouter
from .contactings.views import router as conRouter

router = APIRouter(prefix="/api")
router.include_router(router=authRouter)
router.include_router(router=conRouter)