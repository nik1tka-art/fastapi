from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def root() -> dict[str, str]:
    return {"msg":"Hello world"}

@router.get("/items/{item_id}")
def read_item(item_id:int) -> dict[str, int]:
    return {"item_id": item_id}