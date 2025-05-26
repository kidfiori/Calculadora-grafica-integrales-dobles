Manual de Usuario – Calculadora Gráfica de Planos Tangentes
1. Introducción
Esta aplicación permite graficar funciones de dos variables (x, y) en 3D y calcular el plano tangente en un punto específico (x0, y0). Está diseñada para estudiantes y usuarios que deseen visualizar funciones matemáticas y sus derivadas parciales de forma interactiva.
2. Ingreso de la función
La función debe ingresarse usando la sintaxis de Python y SymPy. Por ejemplo, para ingresar una parábola, escribe:
x**2 + y**2
3. Formato de expresiones matemáticas
A continuación, se indican las conversiones más comunes:
- Potencias: usa '**' en lugar de '^'. Ej: x^2 → x**2
- Multiplicación explícita: escribe x*y, no xy
- Funciones trigonométricas: usa sin(x), cos(x), tan(x)
- Raíz cuadrada: sqrt(x)
- Número pi: pi (sin comillas)
- Exponencial: exp(x) para e^x
- Logaritmo natural: log(x)
- Constante e: E
4. Ingreso de coordenadas
Debes ingresar los valores de x0 y y0 donde deseas calcular el plano tangente. Asegúrate de que estén dentro del dominio de la función ingresada.
5. Errores comunes
- No usar doble asterisco para potencias
- Olvidar paréntesis en funciones como sin(x + y)
- Dejar campos vacíos
- Ingresar texto no reconocido por SymPy
6. Funcionalidad de los botones
- Continuar (pantalla de carga): cierra la pantalla de bienvenida
- Mostrar Gráfico 3D: genera la gráfica de la función ingresada
- Borrar Gráfica: elimina el gráfico actual de la ventana
7. Ejemplo práctico
Función: sin(x) + cos(y)
Coordenadas: x0 = 0, y0 = 0
Esto genera la gráfica de la función y muestra el plano tangente en el punto (0, 0).
