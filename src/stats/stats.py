

class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La media aritmética de los números
            
        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        return sum(numeros) / len(numeros) if numeros else 0.0
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
            
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        if not numeros:  # lista vacía
           return 0.0

        numeros = sorted(numeros)
        n = len(numeros)
        mid = n // 2

        if n % 2 == 0:  # número par de elementos
           return float((numeros[mid - 1] + numeros[mid]) / 2)
        else:  # número impar
           return float(numeros[mid])
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        if not numeros:  # manejar lista vacía
            return None  # o raise ValueError("Lista vacía, no se puede calcular la moda")

        from collections import Counter
        conteo = Counter(numeros)
        max_frecuencia = max(conteo.values())
        for num in conteo:
            if conteo[num] == max_frecuencia:
                return num
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        n = len(numeros)
        if n == 0:
            return 0.0
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / n
        return varianza ** 0.5
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        n = len(numeros)
        if n == 0:
            return 0.0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / n
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        return max(numeros) - min(numeros) if numeros else 0