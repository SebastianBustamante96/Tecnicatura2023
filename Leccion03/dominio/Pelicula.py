class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'


@property  # Metodo Get
def nombre(self):
    return self.nombre


@nombre.setter  # Metodo set
def nombre(self, nombre):
    self._nombre = nombre
