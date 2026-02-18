class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating instance...")
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)

"""
🧠 ¿Por qué usamos __new__ y no __init__?

__init__ se ejecuta cada vez que llamas la clase.

__new__ controla la creación real del objeto.

Si quieres controlar instancias, debes interceptar la creación.
"""

"""
❌ Problemas del Singleton

Introduce estado global (difícil de testear).

Oculta dependencias.

Rompe Dependency Injection.

Puede causar problemas en entornos multi-thread.

Hace el código menos predecible.
"""