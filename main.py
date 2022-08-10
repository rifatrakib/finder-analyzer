from fastapi import FastAPI
from models.finder_models import PayloadModel
from config import Settings

app = FastAPI()
settings = Settings()


@app.post('/get-table-data/{section_name}')
async def get_table_data(section_name: str, payload: PayloadModel):
    payload = payload.dict()
    return {'param': section_name, 'payload': payload}
