from fastapi import APIRouter
from starlette import status

from itenergy.controllers.models.incoming import Forecast
from itenergy.db.engine import engine
from itenergy.repositories import forecasts
from itenergy.repositories.forecasts import ForecastSwitch

router = APIRouter(
    prefix='/expert/forecast_switch',
    tags=['Expert']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_forecast(request: Forecast) -> ForecastSwitch:
    with engine.begin() as conn:
        forecast = forecasts.new(
            forecast_id=request.forecast_id,
            v1_state=request.v1_state,
            v2_state=request.v2_state,
            v3_state=request.v3_state,
            v4_state=request.v4_state,
            v5_state=request.v5_state,
            v6_state=request.v6_state,
            v7_state=request.v7_state,
            user_id=request.user_id,
            conn=conn)

    return forecast
