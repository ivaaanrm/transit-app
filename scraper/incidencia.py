from pydantic import BaseModel, Field
from dataclasses import asdict, dataclass, field

@dataclass(frozen=True)
class Incidencia:
    causa: str
    zona: str
    via: str
    km_inicio_fin: str
    longitud: str
    demarcacion: str
    tramo: str
    direccion: str
    inicio: str
    observaciones: str
    
    @property
    def nivel(self):
        return 1
    
    def to_dict(self):
        return asdict(self)


