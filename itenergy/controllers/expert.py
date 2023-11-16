from fastapi import APIRouter

router = APIRouter(
    prefix='/expert/forecast_switch',
    tags=['Expert']
)


@router.patch('/{id}')
def update_forecast() -> None:
    return
