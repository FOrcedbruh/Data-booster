from fastapi import APIRouter, Depends, Response, HTTPException, status
from . import utils
from .schemas import UserSchema, UserCreateSchema, UserLoginSchema
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_conn import db_conn
from core.models import User
from .actions import create_access_token



router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registration")
async def reg(response: Response, user_in: UserCreateSchema = Depends(utils.RegForm), session: AsyncSession = Depends(db_conn.session_creation)):
    st = await session.execute(select(User).filter(User.email == user_in.email))
    candidate = st.scalars().first()

    if candidate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с такой почтой уже существует"
        )
    else:
        user_in.password = utils.hash_password(password=user_in.password)
        user = User(**user_in.model_dump())

        session.add(user)
        await session.commit()

        access_token = create_access_token(user=user_in)

        response.set_cookie(key="access_token", value=access_token)

        return {
            "status": status.HTTP_201_CREATED,
            "user": user
        }
    
@router.post("/login")
async def log(response: Response, session: AsyncSession = Depends(db_conn.session_creation), user_in: UserLoginSchema = Depends(utils.LogForm)):
    st = await session.execute(select(User).filter(User.email == user_in.email))
    user = st.scalars().first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователя не существует"
        )
    else:
        isValid_password: bool = utils.validation_password(hashed_password=user.password, password=user_in.password)
        if isValid_password == False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Неправильный пароль"
            )
        else:
            access_token = create_access_token(user=user_in)

            response.set_cookie(key="access_token", value=access_token)

        
            return {
                "status": status.HTTP_200_OK,
                "user": user
            }