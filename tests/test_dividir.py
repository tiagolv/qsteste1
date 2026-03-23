from functions.dividir import dividir

def test_dividir_simples():
    assert dividir(10, 2) == 5

def test_dividir_com_float():
    assert dividir(9, 3) == 3

def test_dividir_resultado_decimal():
    assert dividir(7, 2) == 3.5

def test_dividir_por_zero():
    # este teste vai falhar porque a função não trata divisão por zero
    assert dividir(5, 0) == 0