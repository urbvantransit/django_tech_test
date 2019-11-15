# coding: utf8
from datetime import datetime
from uuid import uuid4


# función para crear un ID de manera aleatoria
# utilizando datetime y F-String, una nueva y 
# mejorada manera de dar formato a las String en Python
def create_id(identifier):


    now = datetime.utcnow()
    uid = str(uuid4())[:8]
    return (
        f"{identifier}"
        f"{now.year}"
        f"{now.month}"
        f"{now.day}"
        f"{now.hour}"
        f"{now.minute}"
        f"{now.second}"
        f"{uid}"
    ) 
