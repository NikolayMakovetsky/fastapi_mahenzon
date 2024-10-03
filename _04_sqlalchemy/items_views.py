from typing import Annotated  # Annotated позволяет комбинировать различные правила
from fastapi import APIRouter, Path  # Path необходим, чтобы дополнять параметры пути

router = APIRouter(prefix="/items", tags=["Items"])



@router.get("/")
def list_items():
    return {
        "item_901",
        "item_902",
        "item_903",
    }


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": 0, "name": "latest"}}


# Комбинирование аннотаций типов с дополнительными параметрами
@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "id": item_id
    }