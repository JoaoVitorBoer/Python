import pytest
#pytest on bash or python3 -m pytest
# python3 -m pytest -v -> more info
# python3 -m pytest filename -> execution of specified file
# python3 -m pytest -m markername -> execution of specified marker(pytest.ini)

def calcular_faturamento():
    vendas = [1000, 2000, 3000, 4000, 5000]
    faturamento = sum(vendas)
    return faturamento
    
def calcular_lucro(faturamento, custo):
    lucro = faturamento - custo
    return lucro

def calcular_custo(cotacao):
    custo = 1000 * cotacao
    return custo

