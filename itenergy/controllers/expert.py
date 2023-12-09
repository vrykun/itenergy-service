from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from itenergy.controllers.models.incoming import Forecast
from itenergy.db.engine import engine
from itenergy.repositories import forecasts
from itenergy.repositories.forecasts import EquipmentData

router = APIRouter(
    prefix='/expert/forecast_switch',
    tags=['Expert']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def post_forecast(request: Forecast) -> EquipmentData:
    with engine.begin() as conn:
        forecast_switch = forecasts.new(
            id=request.id,
            current_solar_power=request.current_solar_power,
            current_wind_power=request.current_wind_power,
            capacity=request.capacity,
            solar_battery_power=request.solar_battery_power,
            wind_power=request.wind_power,
            power_consumption=request.power_consumption,
            conn=conn)

    return forecast_switch


@router.get('/aaa', response_model=list[EquipmentData], status_code=status.HTTP_200_OK)
def get_all_forecasts() -> list[EquipmentData]:
    with engine.begin() as conn:
        forecast_switch = forecasts.get_forecasts(conn=conn)

    return forecast_switch


@router.get('/{id}', response_model=EquipmentData, status_code=status.HTTP_200_OK)
def get_forecast(id: int) -> EquipmentData:
    # breakpoint()
    with engine.begin() as conn:
        forecast_switch = forecasts.get_forecast(id=id, conn=conn)

    return forecast_switch


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_forecast(id: int) -> Response:
    with engine.begin() as conn:
        forecasts.delete(id=id, conn=conn)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
