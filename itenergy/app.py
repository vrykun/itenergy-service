from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from itenergy.controllers import expert, rule_base

app = FastAPI(title='IT Energy service', version='0.0.1')
app.include_router(expert.router)
app.include_router(rule_base.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
