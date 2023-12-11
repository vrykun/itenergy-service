from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from itenergy.controllers.models.incoming import EquipmentRequest
from itenergy.db.engine import engine
from itenergy.repositories import equipments
from itenergy.repositories.equipments import Equipment

router = APIRouter(
    prefix='/expert/equipment',
    tags=['Expert']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def post_equipment(request: EquipmentRequest) -> Equipment:
    print(request)
    with engine.begin() as conn:
        equipment = equipments.new(
            id=request.id,
            voltage_deviation=request.voltage_deviation,
            phase_voltage_ua=request.phase_voltage_ua,
            phase_voltage_ub=request.phase_voltage_ub,
            phase_voltage_uc=request.phase_voltage_uc,
            interphase_voltage_uab=request.interphase_voltage_uab,
            interphase_voltage_uac=request.interphase_voltage_uac,
            interphase_voltage_ubc=request.interphase_voltage_ubc,
            asymmetry_coefficient_k2u=request.asymmetry_coefficient_k2u,
            asymmetry_coefficient_k0u=request.asymmetry_coefficient_k0u,
            capacity_battery_pb=request.capacity_battery_pb,
            current_solar_power=request.current_solar_power,
            current_wind_power=request.current_wind_power,
            capacity=request.capacity,
            solar_battery_power=request.solar_battery_power,
            wind_power=request.wind_power,
            power_consumption=request.power_consumption,
            conn=conn)

    return equipment


@router.patch('/', status_code=status.HTTP_200_OK)
def patch_equipment(request: EquipmentRequest) -> Equipment:
    with engine.begin() as conn:
        equipment = equipments.new(
            id=request.id,
            voltage_deviation=request.voltage_deviation,
            phase_voltage_ua=request. phase_voltage_ua,
            phase_voltage_ub=request. phase_voltage_ub,
            phase_voltage_uc=request.phase_voltage_uc,
            interphase_voltage_uab=request.interphase_voltage_uab,
            interphase_voltage_uac=request.interphase_voltage_uac,
            interphase_voltage_ubc=request.interphase_voltage_ubc,
            asymmetry_coefficient_k2u=request.asymmetry_coefficient_k2u,
            asymmetry_coefficient_k0u=request.asymmetry_coefficient_k0u,
            capacity_battery_pb=request.capacity_battery_pb,
            current_solar_power=request.current_solar_power,
            current_wind_power=request.current_wind_power,
            capacity=request.capacity,
            solar_battery_power=request.solar_battery_power,
            wind_power=request.wind_power,
            power_consumption=request.power_consumption,
            conn=conn)

    return equipment


@router.get('/', response_model=list[Equipment], status_code=status.HTTP_200_OK)
def get_all_equipments() -> list[Equipment]:
    with engine.begin() as conn:
        equipment = equipments.get_equipments(conn=conn)

    return equipment


@router.get('/{id}', response_model=Equipment, status_code=status.HTTP_200_OK)
def get_equipment(id: int) -> Equipment:
    with engine.begin() as conn:
        equipment = equipments.get_equipment(id=id, conn=conn)

    return equipment


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_equipment(id: int) -> Response:
    with engine.begin() as conn:
        equipments.delete(id=id, conn=conn)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
