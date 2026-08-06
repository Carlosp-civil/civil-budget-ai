import subprocess
import sys

import pandas as pd


def test_cli_execution(tmp_path):
    csv_file = tmp_path / "budget.csv"

    dataframe = pd.DataFrame(
        {
            "codigo": ["001"],
            "descripcion": ["Concreto"],
            "unidad": ["m3"],
            "cantidad": [10],
            "precio_unitario": [250],
        }
    )

    dataframe.to_csv(
        csv_file,
        index=False,
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.cli.main",
            str(csv_file),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

    output = result.stdout

    assert "Civil Budget AI" in output
    assert "Resumen" in output
    assert "2500" in output
    assert "Items" in output
    assert "Calculados" in output
