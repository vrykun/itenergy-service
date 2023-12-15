from dataclasses import dataclass
from typing import Any

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Connection

from itenergy.db.schema import indicator_data


@dataclass
class RuleBase:
    id: int
    input: Any
    switch: Any


def new(id: int, input: Any, switch: Any, conn: Connection) -> RuleBase:
    set_fields = dict(id=id, input=input, switch=switch)
    stmt = (insert(indicator_data).values(
        set_fields,
    ).on_conflict_do_update(constraint='indicator_pkey', set_=set_fields).returning(indicator_data))
    return RuleBase(**conn.execute(stmt).mappings().one())


def get_rule_base(id: int, conn: Connection) -> RuleBase:
    indicator = conn.execute(indicator_data.select().where(
        indicator_data.c.id == id)).mappings().one()

    return RuleBase(**indicator)


def delete(id: int, conn: Connection) -> None:
    conn.execute(indicator_data.delete().where(indicator_data.c.id == id))
