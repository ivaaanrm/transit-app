from pydantic import BaseModel, Field
from dataclasses import asdict, dataclass, field

@dataclass(frozen=True)
class Incidencia:
    causa: str
    nivel: str
    via: str
    km_inicio_fin: str
    longitud: str
    demarcacion: str
    tramo: str
    direccion: str
    inicio: str
    observaciones: str
    
    def to_dict(self):
        return asdict(self)


