from app.analysis.models import (
    BudgetItem,
    NormalizedBudget
)

from app.ingestion.models import (
    BudgetDocument,
    ColumnMapping
)


class BudgetNormalizer:
    """
    Transforms a BudgetDocument into a NormalizedBudget.

    Responsibilities:
    - extract mapped columns;
    - convert numeric values;
    - ignore completely empty rows;
    - preserve missing values.
    """


    def normalize(
        self,
        document: BudgetDocument,
        mapping: ColumnMapping
    ) -> NormalizedBudget:

        items = []


        for _, row in document.data.iterrows():

            if self._is_empty_row(row):
                continue


            item = BudgetItem(
                code=self._get_value(
                    row,
                    mapping.codigo
                ),

                description=self._get_value(
                    row,
                    mapping.descripcion
                ),

                unit=self._get_value(
                    row,
                    mapping.unidad
                ),

                quantity=self._convert_number(
                    self._get_value(
                        row,
                        mapping.cantidad
                    )
                ),

                unit_price=self._convert_number(
                    self._get_value(
                        row,
                        mapping.precio_unitario
                    )
                )
            )


            items.append(item)


        return NormalizedBudget(
            items=items,
            source_filename=document.filename
        )


    def _get_value(
        self,
        row,
        column_name: str | None
    ):
        """
        Gets a value from a row safely.

        Missing columns return None.
        """

        if column_name is None:
            return None


        if column_name not in row:
            return None


        value = row[column_name]


        if value != value:  # NaN check
            return None


        return value



    def _convert_number(
        self,
        value
    ) -> float | None:
        """
        Converts external numeric formats
        into float values.
        """

        if value is None:
            return None


        if isinstance(value, str):

            value = value.replace(
                ",",
                ""
            )


        try:
            return float(value)

        except (ValueError, TypeError):
            return None



    def _is_empty_row(
        self,
        row
    ) -> bool:
        """
        Detects rows without any meaningful data.
        """

        for value in row:

            if value == value and value not in ("", None):
                return False


        return True