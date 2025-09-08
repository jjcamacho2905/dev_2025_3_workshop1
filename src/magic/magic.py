class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        fib_sequence = []
        for i in range(n):
            fib_sequence.append(self.fibonacci(i))
        return fib_sequence
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        return [i for i in range(2, n + 1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n < 2:
            return False
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        tri_pascal = []  
        for i in range(filas):
           fila = [1] * (i + 1)  # siempre empieza y termina en 1
           for j in range(1, i):  # los valores intermedios
                fila[j] = tri_pascal[i - 1][j - 1] + tri_pascal[i - 1][j]  
           tri_pascal.append(fila)  
        return tri_pascal
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n == 0 or n == 1:
          return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b:
            a, b = b, a % b
        return a

    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        return abs(a * b) // self.mcd(a, b) if a and b else 0
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        num_str = str(abs(n))
        potencia = len(num_str)
        suma = sum(int(d) ** potencia for d in num_str)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).

        Args:
            matriz (list of list of int): matriz cuadrada
        Returns:
            bool: True si es cuadrado mágico, False en caso contrario
        """
        n = len(matriz)
        if n == 0:
            return False

        # Verificar si todas las filas tienen la misma longitud
        for fila in matriz:
            if len(fila) != n:
                # Cobertura línea 200
                return False

        suma_objetivo = sum(matriz[0])

        # Diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False

        # Diagonal inversa
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False

        # Verificar filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                # Cobertura línea 208
                return False

        # Verificar columnas
        for col in range(n):
            if sum(matriz[i][col] for i in range(n)) != suma_objetivo:
                return False

        return True