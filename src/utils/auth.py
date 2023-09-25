from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from jose import jwt, JWTError
from config.core import Setting
from starlette import status
from typing import Dict

api_key_header = APIKeyHeader(name="bearer", scheme_name="Bearer")


def create_access_token(params: Dict[str, str]) -> str:
    encode = {
        "wallet_address": params["wallet_address"],
        "user_id": params["user_id"],
    }
    to_encode = encode.copy()
    expire_time = datetime.utcnow() + timedelta(
        minutes=int(Setting.JWT_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire_time})
    try:
        encoded_jwt = jwt.encode(
            to_encode,
            Setting.JWT_SECRET_KEY,
            algorithm=Setting.JWT_ALGORITHM,
        )
        return encoded_jwt
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create access token",
        )


async def get_current_user(token: Annotated[str, Depends(api_key_header)]):
    try:
        payload = jwt.decode(
            token, Setting.JWT_SECRET_KEY, algorithms=[Setting.JWT_ALGORITHM]
        )
        wallet_address: str = payload.get("wallet_address")
        user_id: int = payload.get("user_id")
        if wallet_address is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
        return {"wallet_address": wallet_address, "user_id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
