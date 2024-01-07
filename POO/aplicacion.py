import datetime
import time

class Empleado:
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora = 20):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.sueldo_hora = sueldo_hora
        # Estados
        self.fichajes = []
        self.transporte = 0
        self.trabajando = False
        self.ubicacion = "Rentería"
        # Balance de trabajo
        self.tiempo_trabajado = 0
        self.dinero_ganado = 0
        self.vacaciones_acumuladas = 0

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        self.trabajando = not self.trabajando
        self.fichajes.append(datetime.datetime.now())
        self.transporte += 1
        if not self.trabajando:
            self.tiempo_trabajado = self.__calcula_trabajo()
            self.dinero_ganado= self.__calcula_sueldo()
            self.vacaciones_acumuladas = self.__calcula_vacaciones()

    def muestra_fichajes(self):
        print(self.fichajes)

    def __calcula_trabajo(self):
        delta_acum = datetime.timedelta(0)
        jornada = 0
        for entrada, salida in zip(self.fichajes[::2], self.fichajes[1::2]):
            delta = salida - entrada
            jornada +=1
            delta_acum += delta
            # print(f'Jornada {jornada}: Duración {delta}. Duración acumulada {delta_acum}')

        return delta_acum

    def __calcula_sueldo(self):
        tiempo_trabajo = self.__calcula_trabajo().seconds/3600
        return tiempo_trabajo*self.sueldo_hora + self.transporte

    def __calcula_vacaciones(self):
        return self.__calcula_trabajo()/5
    
class Directivo(Empleado):
    def __init__(self, nombre, apellido1, apellido2, coche, sueldo_hora = 30):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.coche = coche
        self.dietas = 0

    def viaja(self, nueva_ubicacion):
        super().viaja(nueva_ubicacion)
        self.dietas += 100

    def calcula_sueldo(self):
        return super().calcula_sueldo() + self.dietas
    
    def en_activo(self):
        print("Cuadro un balance")
        time.sleep(3)
        print("Despido un empleado")
        time.sleep(3)
        print("Me tomo un café")

class Oficinista(Empleado):
    def __init__(self, nombre, apellido1, apellido2, hijos = 0, sueldo_hora = 20):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.bonus_familiar = 0
        self.hijos = hijos

    def calcula_bonus(self):
        self.bonus_familiar = self.hijos*100

    def en_activo(self):
        print("Saco una fotocopia")
        time.sleep(3)
        print("Despido un peón")
        time.sleep(3)
        print("Me tomo un café")

class Peon(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora = 15):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.guardias = 0

CEO = Directivo("John", "Harrison", "Johnson", coche = "Mercedes Maybach", sueldo_hora=40)
CEO.en_activo()
CEO.viaja("Toledo")

secretario = Oficinista(nombre = "James", apellido1 = "Taft", apellido2 = "Johnson", sueldo_hora = 25)

CEO.ficha()
CEO.muestra_fichajes()
CEO.ficha()
CEO.trabajando