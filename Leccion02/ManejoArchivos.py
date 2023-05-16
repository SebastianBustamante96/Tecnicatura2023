class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        # Encapsulamos el codigo dentro del metodo
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()  # cerramos el archivo
