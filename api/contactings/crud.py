from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Body, HTTPException, status, Depends
from core.models import Contacting
from .schemas import ConCreateSchema
from sqlalchemy import select


async def create_contacting(session: AsyncSession, con_in: ConCreateSchema) -> dict:
    if not con_in.text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Empty text field"
        )
    else:
        contacting = Contacting(**con_in.model_dump())
        session.add(contacting)
        await session.commit()



        return {
            "status": status.HTTP_201_CREATED,
            "message": f"Обращение {len(contacting.text)} создано"
        }
    
async def contactings(session: AsyncSession, user_id: int) -> list:
    st = await session.execute(select(Contacting).filter(Contacting.user_id == user_id))
    contgs = st.scalars().all()


    return list(contgs)