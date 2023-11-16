from fastapi import APIRouter

router = APIRouter(
    prefix='/expert',
    tags=['Expert']
)


@router.get('/{id}')
def get_user_by_id() -> None:
    return
