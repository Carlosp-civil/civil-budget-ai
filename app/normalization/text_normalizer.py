import re
import unicodedata


class TextNormalizer:
    """
    Realiza normalización básica de texto.

    Este componente no conoce reglas del dominio.
    Solo aplica limpieza general.
    """

    TECHNICAL_CHARACTERS = {
        "'",
        "=",
        "/",
        "²",
        "³",
        "Ø",
        "%"
    }


    def normalize(
        self,
        text: str,
        preserve_special_chars: bool = False
    ) -> str:
        """
        Normaliza texto.

        Args:
            text:
                Texto original.

            preserve_special_chars:
                Conserva caracteres técnicos.
        """

        if not text:
            return ""


        text = text.strip()

        text = text.lower()


        text = self._remove_accents(
            text
        )


        if preserve_special_chars:
            text = self._clean_preserving_technical_chars(
                text
            )

        else:
            text = self._remove_special_characters(
                text
            )


        text = self._remove_extra_spaces(
            text
        )


        return text



    def _remove_accents(
        self,
        text: str
    ) -> str:
        """
        Elimina tildes.

        Ejemplo:
        descripción -> descripcion
        """

        normalized = unicodedata.normalize(
            "NFD",
            text
        )

        return "".join(
            char
            for char in normalized
            if unicodedata.category(char) != "Mn"
        )



    def _remove_special_characters(
        self,
        text: str
    ) -> str:
        """
        Elimina símbolos no alfanuméricos.

        Mantiene letras, números y espacios.
        """

        return re.sub(
            r"[^a-z0-9\s]",
            "",
            text
        )



    def _clean_preserving_technical_chars(
        self,
        text: str
    ) -> str:
        """
        Elimina ruido pero conserva
        caracteres técnicos importantes.
        """

        allowed = (
            r"[^a-z0-9\s"
            + "".join(
                re.escape(char)
                for char in self.TECHNICAL_CHARACTERS
            )
            + "]"
        )


        return re.sub(
            allowed,
            "",
            text
        )



    def _remove_extra_spaces(
        self,
        text: str
    ) -> str:
        """
        Reduce espacios múltiples.
        """

        return re.sub(
            r"\s+",
            " ",
            text
        )