from pydantic import BaseModel, ConfigDict


class AlergenoRead(BaseModel):
    alergeno_id: int
    nombre: str

    model_config = ConfigDict(from_attributes=True)
