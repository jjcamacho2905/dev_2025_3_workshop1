import pytest
from src.magic.magic import Magic

class TestMagic:
    def setup_method(self):
        self.magic = Magic()
    
    def test_fibonacci(self):
        # Test para los primeros números de Fibonacci
        assert self.magic.fibonacci(0) == 0
        assert self.magic.fibonacci(1) == 1
        assert self.magic.fibonacci(2) == 1
        assert self.magic.fibonacci(3) == 2
        assert self.magic.fibonacci(10) == 55
        assert self.magic.fibonacci(10) != 35
    
    def test_secuencia_fibonacci(self):
        # Test para generar secuencia de Fibonacci
        assert self.magic.secuencia_fibonacci(1) == [0]
        assert self.magic.secuencia_fibonacci(2) == [0, 1]
        assert self.magic.secuencia_fibonacci(5) == [0, 1, 1, 2, 3]
        assert self.magic.secuencia_fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    
    def test_es_primo(self):
        # Test para números primos
        assert self.magic.es_primo(2) == True
        assert self.magic.es_primo(7) == True
        assert self.magic.es_primo(17) == True
        # Test para números no primos
        assert self.magic.es_primo(1) == False
        assert self.magic.es_primo(4) == False
        assert self.magic.es_primo(15) == False
        # Test para números negativos
        assert self.magic.es_primo(-5) == False
    
    def test_generar_primos(self):
        # Test para generar números primos hasta n
        assert self.magic.generar_primos(10) == [2, 3, 5, 7]
        assert self.magic.generar_primos(20) == [2, 3, 5, 7, 11, 13, 17, 19]
        # Test para n < 2
        assert self.magic.generar_primos(1) == []
    
    def test_es_numero_perfecto(self):
        # Test para números perfectos
        assert self.magic.es_numero_perfecto(6) == True  # 1 + 2 + 3 = 6
        assert self.magic.es_numero_perfecto(28) == True  # 1 + 2 + 4 + 7 + 14 = 28
        # Test para números no perfectos
        assert self.magic.es_numero_perfecto(10) == False
        assert self.magic.es_numero_perfecto(15) == False
        # Test para 0 y 1
        assert self.magic.es_numero_perfecto(0) == False
        assert self.magic.es_numero_perfecto(1) == False
    
    def test_triangulo_pascal(self):
        # Test para 1 fila
        assert self.magic.triangulo_pascal(1) == [[1]]
        # Test para 3 filas
        assert self.magic.triangulo_pascal(3) == [[1], [1, 1], [1, 2, 1]]
        # Test para 5 filas
        assert self.magic.triangulo_pascal(5) == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    
    def test_factorial(self):
        # Test para factorial
        assert self.magic.factorial(0) == 1
        assert self.magic.factorial(1) == 1
        assert self.magic.factorial(5) == 120
        assert self.magic.factorial(10) == 3628800
    
    def test_mcd(self):
        # Test para máximo común divisor
        assert self.magic.mcd(48, 18) == 6
        assert self.magic.mcd(15, 25) == 5
        assert self.magic.mcd(7, 13) == 1  # Primos entre sí
        assert self.magic.mcd(0, 5) == 5
    
    def test_mcm(self):
        # Test para mínimo común múltiplo
        assert self.magic.mcm(4, 6) == 12
        assert self.magic.mcm(15, 25) == 75
        assert self.magic.mcm(7, 13) == 91
        assert self.magic.mcm(5, 0) == 0
    
    def test_suma_digitos(self):
        # Test para suma de dígitos
        assert self.magic.suma_digitos(123) == 6
        assert self.magic.suma_digitos(9999) == 36
        assert self.magic.suma_digitos(0) == 0
        assert self.magic.suma_digitos(7) == 7
    
    def test_es_numero_armstrong(self):
        # Test para números de Armstrong
        assert self.magic.es_numero_armstrong(153) == True  # 1^3 + 5^3 + 3^3 = 153
        assert self.magic.es_numero_armstrong(370) == True  # 3^3 + 7^3 + 0^3 = 370
        assert self.magic.es_numero_armstrong(371) == True  # 3^3 + 7^3 + 1^3 = 371
        # Test para números que no son de Armstrong
        assert self.magic.es_numero_armstrong(123) == False
        assert self.magic.es_numero_armstrong(100) == False
    
    def test_es_cuadrado_magico_completo(self):
        # 1. Matriz no cuadrada
        no_cuadrada = [
            [1, 2, 3],
            [4, 5]  # fila más corta
        ]
        assert self.magic.es_cuadrado_magico(no_cuadrada) is False

        # 2. Fila con suma distinta
        fila_distinta = [
            [2, 7, 6],
            [9, 5, 1],
            [4, 3, 9]  # suma diferente en la última fila
        ]
        assert self.magic.es_cuadrado_magico(fila_distinta) is False

        # 3. Columna con suma distinta
        columna_distinta = [
            [2, 7, 6],
            [9, 5, 1],
            [4, 4, 8]  # columna 2 suma distinta
        ]
        assert self.magic.es_cuadrado_magico(columna_distinta) is False

        # 4. Diagonal principal distinta
        diagonal_distinta = [
            [2, 7, 6],
            [9, 1, 5],
            [4, 3, 8]  # diagonal suma distinta
        ]
        assert self.magic.es_cuadrado_magico(diagonal_distinta) is False

        # 5. Diagonal inversa distinta
        diagonal_inversa_distinta = [
            [2, 7, 6],
            [9, 5, 1],
            [8, 3, 4]
        ]
        assert self.magic.es_cuadrado_magico(diagonal_inversa_distinta) is False

        # 6. Cuadrado mágico válido
        cuadrado_magico = [
            [2, 7, 6],
            [9, 5, 1],
            [4, 3, 8]
        ]
        assert self.magic.es_cuadrado_magico(cuadrado_magico) is True

    def test_cobertura_lineas_200_208(self):
        # Línea 200: matriz no cuadrada
        matriz_no_cuadrada = [
            [1, 2, 3],
            [4, 5]  # fila más corta
        ]
        assert self.magic.es_cuadrado_magico(matriz_no_cuadrada) is False

        # Línea 208: fila con suma distinta
        matriz_fila_distinta = [
            [2, 7, 6],
            [9, 5, 1],
            [4, 3, 10]  # suma diferente (15 != 17)
        ]
        assert self.magic.es_cuadrado_magico(matriz_fila_distinta) is False

    def test_es_cuadrado_magico_vacio(self):
        # Cobertura del caso n == 0 (matriz vacía)
        assert self.magic.es_cuadrado_magico([]) is False

    def test_es_cuadrado_magico_fila_falla_despues_de_diagonales(self):
        # Diagonales correctas (suman 15), pero una fila no suma 15
        matriz = [
            [8, 1, 6],   # suma 15 => suma_objetivo
            [9, 5, 7],   # suma 21 => falla en verificación de filas
            [4, 10, 2],  # suma 16
        ]
        assert self.magic.es_cuadrado_magico(matriz) is False

    def test_es_cuadrado_magico_columna_falla_despues_de_filas_y_diagonales(self):
        # Diagonales correctas y todas las filas suman 15, pero columnas no
        matriz = [
            [8, 1, 6],
            [2, 5, 8],
            [4, 9, 2],
        ]
        # Columnas: col0=14, col1=15, col2=16 => debe fallar en verificación de columnas
        assert self.magic.es_cuadrado_magico(matriz) is False

    def test_es_cuadrado_magico_diagonal_inversa_falla_tras_principal_ok(self):
        # La diagonal principal suma correctamente (15), pero la diagonal inversa no
        # Ajustamos la primera fila para mantener suma_objetivo=15 y romper la diagonal inversa
        matriz = [
            [2, 6, 7],  # 2+6+7=15 (suma_objetivo); principal 2+5+8=15; inversa 7+5+4=16
            [9, 5, 1],
            [4, 3, 8],
        ]
        # Principal: 2+5+8=15 (ok). Inversa: 7+5+4=16 (falla)
        assert self.magic.es_cuadrado_magico(matriz) is False