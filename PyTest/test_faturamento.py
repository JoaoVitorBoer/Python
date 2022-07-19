from main import calcular_lucro, calcular_faturamento
import pytest

# faturamento
@pytest.mark.faturamento
def test_calcular_faturamento():
    assert type(calcular_faturamento()) == int