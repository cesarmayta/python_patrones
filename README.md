# python_patrones
ejercicios de patrones de diseño con python
## Factory

Su propósito es centralizar la creación de objetos y evitar `if/elif` dispersos en el código, delegando la decisión de qué instancia crear a una función o clase especializada.  
Se usa cuando existen múltiples implementaciones de una misma interfaz (por ejemplo, distintos tipos de pago o exportadores) y quieres desacoplar el código cliente de clases concretas.

---

## Builder

Su propósito es construir objetos complejos paso a paso, especialmente cuando tienen muchos parámetros opcionales o requieren validaciones antes de crearse.  
Se usa cuando el constructor empieza a volverse ilegible o riesgoso, y necesitas mayor claridad, control y fluidez en la creación del objeto.

---

## Singleton

Su propósito es garantizar que solo exista una única instancia de una clase durante toda la ejecución del programa.  
Se usa únicamente cuando el recurso debe ser verdaderamente global (por ejemplo, configuración o métricas), pero debe evitarse en lógica de negocio porque introduce estado global y dificulta el testing.

---

## Dependency Injection (DI)

Su propósito es desacoplar clases haciendo que reciban sus dependencias desde afuera en lugar de crearlas internamente.  
Se usa para mejorar testabilidad, flexibilidad y mantenimiento del sistema, permitiendo cambiar implementaciones sin modificar la lógica principal.

