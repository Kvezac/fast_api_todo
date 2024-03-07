from fastapi import APIRouter

router = APIRouter()


@router.get("/lists")
async def get_lists():
    return


@router.post("/lists")
async def create_list():
    return


@router.delete("/lists/{list_id}")
async def delete_list():
    return
