import json

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from itenergy.controllers.models.rule_base import RuleBaseRequest
from itenergy.db.engine import engine
from itenergy.repositories import rule_base
from itenergy.repositories.rule_base import RuleBase

router = APIRouter(
    prefix='/rule_base',
    tags=['Rule base']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def post_rule_base(request: RuleBaseRequest) -> RuleBase:
    with engine.begin() as conn:
        rulebase = rule_base.new(
            id=request.id,
            input=request.input,
            switch=request.switch,
            conn=conn)

    return rulebase


@router.get('/{id}', response_model=RuleBase, status_code=status.HTTP_200_OK)
def get_rule_base(id: int) -> RuleBase:
    with engine.begin() as conn:
        rulebase = rule_base.get_rule_base(id=id, conn=conn)

    return rulebase


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_rule_base(id: int) -> Response:
    with engine.begin() as conn:
        rule_base.delete(id=id, conn=conn)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
