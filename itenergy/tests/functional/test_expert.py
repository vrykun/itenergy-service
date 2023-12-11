import random

from fastapi.testclient import TestClient


def test_equipment(test_client: TestClient) -> None:
    equipment_id = random.randint(0, 9)
    equipment_body = dict(
        id=equipment_id,
        voltage_deviation=random.uniform(1, 200),
        phase_voltage_ua=random.uniform(1, 200),
        phase_voltage_ub=random.uniform(1, 200),
        phase_voltage_uc=random.uniform(1, 200),
        interphase_voltage_uab=random.uniform(1, 200),
        interphase_voltage_uac=random.uniform(1, 200),
        interphase_voltage_ubc=random.uniform(1, 200),
        asymmetry_coefficient_k2u=random.uniform(1, 200),
        asymmetry_coefficient_k0u=random.uniform(1, 200),
        capacity_battery_pb=random.uniform(1, 200),
        current_solar_power=random.uniform(1, 200),
        current_wind_power=random.uniform(1, 200),
        capacity=random.uniform(1, 200),
        solar_battery_power=random.uniform(1,200),
        wind_power=random.uniform(1, 200),
        power_consumption=random.uniform(1, 200))

    with test_client:
        # test POST
        create_equipment = test_client.post(
            url='/expert/equipment/',
            json=equipment_body)

        assert create_equipment.status_code == 201

        # test DELETE
        create_equipment = test_client.delete(url=f'/expert/equipment/{equipment_id}')

        assert create_equipment.status_code == 204
