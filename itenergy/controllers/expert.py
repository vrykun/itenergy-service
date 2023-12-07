from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from itenergy.controllers.models.incoming import Forecast
from itenergy.db.engine import engine
from itenergy.repositories import forecasts
from itenergy.repositories.forecasts import ForecastSwitch

router = APIRouter(
    prefix='/expert/forecast_switch',
    tags=['Expert']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def post_forecast(request: Forecast) -> ForecastSwitch:
    with engine.begin() as conn:
        forecast_switch = forecasts.new(
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

    return forecast_switch


@router.get('/', response_model=list[ForecastSwitch], status_code=status.HTTP_200_OK)
def get_all_forecasts() -> list[ForecastSwitch]:
    with engine.begin() as conn:
        forecast_switch = forecasts.get_forecasts(conn=conn)

    return forecast_switch


@router.get('/{id}', response_model=ForecastSwitch, status_code=status.HTTP_200_OK)
def get_forecast(forecast_id: int) -> ForecastSwitch:
    with engine.begin() as conn:
        forecast_switch = forecasts.get_forecast(forecast_id=forecast_id, conn=conn)

    return forecast_switch


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_forecast(forecast_id: int) -> Response:
    with engine.begin() as conn:
        forecasts.delete(forecast_id=forecast_id, conn=conn)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
