from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud, utils
from core.db_conn import db_conn

router = APIRouter(prefix="/contactings", tags=["Contacting"])


@router.post("/create")
async def create(session: AsyncSession = Depends(db_conn.session_creation), con_in = Depends(utils.ConForm)):
    return await crud.create_contacting(session=session, con_in=con_in)

@router.post("/")
async def get_con(user_id: int = Body(), session: AsyncSession = Depends(db_conn.session_creation)):
    return await crud.contactings(session=session, user_id=user_id)