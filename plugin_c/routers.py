from fastapi import APIRouter

router = APIRouter()

@router.get("/plugin_c")
async def read_plugin_c():
    return {"message": "This is Plugin C"}
