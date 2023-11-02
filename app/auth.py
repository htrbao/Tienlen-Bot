from fastapi import Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from .config import Settings, get_settings

api_key_header = APIKeyHeader(name="api_key", auto_error=False)


async def require_api_key(settings: Settings = Depends(get_settings), api_key: str = Security(api_key_header)):
    if settings.api_keys is not None and api_key not in settings.api_keys:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Could not validate API KEY"
        )
