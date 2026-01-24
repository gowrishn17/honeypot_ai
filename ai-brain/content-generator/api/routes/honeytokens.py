"""Honeytoken routes."""

from typing import Optional

from fastapi import APIRouter, Depends, Query

from api.dependencies import get_honeytoken_store
from api.schemas.requests import HoneytokenCheckRequest
from api.schemas.responses import HoneytokenCheckResponse, HoneytokenResponse
from storage.honeytoken_store import HoneytokenStore

router = APIRouter(prefix="/api/v1/honeytokens", tags=["honeytokens"])


@router.get("/", response_model=list[HoneytokenResponse])
async def list_honeytokens(
    honeypot_id: Optional[str] = Query(None),
    token_type: Optional[str] = Query(None),
    active_only: bool = Query(True),
    limit: int = Query(100, ge=1, le=1000),
    store: HoneytokenStore = Depends(get_honeytoken_store),
):
    """List honeytokens with filters."""
    tokens = store.list_honeytokens(
        honeypot_id=honeypot_id,
        token_type=token_type,
        active_only=active_only,
        limit=limit,
    )
    return tokens


@router.get("/{token_id}", response_model=HoneytokenResponse)
async def get_honeytoken(
    token_id: str,
    store: HoneytokenStore = Depends(get_honeytoken_store),
):
    """Get honeytoken by ID."""
    token = store.get_honeytoken(token_id)
    if not token:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Honeytoken not found")
    return token


@router.post("/check", response_model=HoneytokenCheckResponse)
async def check_honeytoken(
    request: HoneytokenCheckRequest,
    store: HoneytokenStore = Depends(get_honeytoken_store),
):
    """Check if token value is a honeytoken."""
    token = store.check_honeytoken(request.token_value)
    
    if token:
        return HoneytokenCheckResponse(
            is_honeytoken=True,
            token_info=token,
            message="ALERT: Honeytoken accessed!",
        )
    else:
        return HoneytokenCheckResponse(
            is_honeytoken=False,
            message="Not a known honeytoken",
        )


@router.delete("/{token_id}")
async def deactivate_honeytoken(
    token_id: str,
    store: HoneytokenStore = Depends(get_honeytoken_store),
):
    """Deactivate a honeytoken."""
    success = store.deactivate_honeytoken(token_id)
    if not success:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Honeytoken not found")
    return {"message": "Honeytoken deactivated", "token_id": token_id}
