from fastapi import FastAPI
from config import Settings
from functions import table_controller
from models.finder_models import PayloadModel

app = FastAPI()
settings = Settings()


@app.post("/get-table-data")
async def get_table_data(payload: PayloadModel):
    payload = payload.dict()
    data = table_controller.fetch_table_data(settings.MONGO_URI, payload)
    return {"data": data, "success": True}
