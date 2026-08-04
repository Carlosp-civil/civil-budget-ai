import copy
import json
from pathlib import Path

DEFAULT_KNOWLEDGE_BASE = {
    "codigo": {
        "high_confidence": [
            "codigo",
            "cod",
            "id",
            "numero",
            "nro",
            "no."
        ],
        "low_confidence": [
            "item"
        ]
    },

    "descripcion": {
        "high_confidence": [
            "descripcion",
            "descripcion del item",
            "detalle",
            "detalle del item",
            "actividad",
            "concepto"
        ],
        "low_confidence": [
            "item"
        ]
    },

    "unidad": {
        "high_confidence": [
            "unidad",
            "und",
            "u.m.",
            "um",
            "medida"
        ],
        "low_confidence": []
    },

    "cantidad": {
        "high_confidence": [
            "cantidad",
            "cant",
            "volumen",
            "vol",
            "cant."
        ],
        "low_confidence": []
    },

    "precio_unitario": {
        "high_confidence": [
            "precio_unitario",
            "valor_unitario",
            "vr_unitario",
            "p.u."
        ],
        "low_confidence": [
            "precio",
            "valor"
        ]
    }
}


class KnowledgeManager:
    """
    Gestiona la base de conocimiento del proyecto.
    """

    def __init__(self, storage_path):
        self.storage_path = Path(storage_path)
        self._knowledge_base = {}

    def load(self) -> None:
        """
        Carga la base de conocimiento.

        Si el archivo no existe:
        - crea la carpeta necesaria;
        - genera una base inicial;
        - guarda el archivo en disco.
        """

        if not self.storage_path.exists():

            print(
                f"⚠️ No se encontró {self.storage_path}. "
                "Creando base de conocimiento inicial..."
            )

            self.storage_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            self._knowledge_base = copy.deepcopy(
                DEFAULT_KNOWLEDGE_BASE
            )

            self._save_to_disk()

        else:

            with open(
                self.storage_path,
                encoding="utf-8"
            ) as file:

                self._knowledge_base = json.load(file)

    def _save_to_disk(self) -> None:
        """
        Guarda la base de conocimiento actual en formato JSON.
        """

        with open(
            self.storage_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self._knowledge_base,
                file,
                indent=4,
                ensure_ascii=False
            )