from fastapi import FastAPI

from itenergy.controllers import expert

app = FastAPI(title='IT Energy service', version='0.0.1')
app.include_router(expert.router)
