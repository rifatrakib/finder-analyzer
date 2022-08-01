from fastapi import FastAPI
from models.finder_models import PayloadModel

app = FastAPI()


@app.post('/get-table-data/{section_name}')
def get_table_data(section_name: str, payload: PayloadModel):
    payload = payload.dict()
    return {'param': section_name, 'payload': payload}
