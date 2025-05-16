'''
6. Sistema Académico Universitario
En una universidad existen personas con distintos roles: estudiantes, profesores y personal administrativo. Todos comparten datos comunes, pero tienen responsabilidades y acciones distintas. El sistema debe permitir registrar a cualquier persona como 'miembro universitario', y ejecutar acciones como recibir mensajes o consultar información personalizada según su tipo.
'''

from abc import ABC, abstractmethod

class MiembroUniversitario(ABC):
  def __init__(self, nombre, edad, correo):
    self.nombre = nombre
    self.edad = edad
    self.correo = correo

  @abstractmethod
  def consultar_informacion(self):
    pass

  def recibir_mensaje(self, mensaje):
    print(f"{self.nombre} ha recibido un mensaje: {mensaje}")

class Estudiante(MiembroUniversitario):
  def __init__(self, nombre, edad, correo, carrera):
    super().__init__(nombre, edad, correo)
    self.carrera = carrera

  def consultar_informacion(self):
    print(f"Estudiante: {self.nombre}, Carrera: {self.carrera}")

  def anotar_clase(self):
    print(f"El estudiante {self.nombre} está anotando la clase")

class Profesor(MiembroUniversitario):
  def __init__(self, nombre, edad, correo, materia):
    super().__init__(nombre, edad, correo)
    self.materia = materia

  def consultar_informacion(self):
    print(f"Profesor: {self.nombre}, Materia: {self.materia}")

  def impartir_clase(self):
    print(f"El profesor {self.nombre} está impartiendo clases")

class Administrativo(MiembroUniversitario):
  def __init__(self, nombre, edad, correo, departamento):
    super().__init__(nombre, edad, correo)
    self.departamento = departamento

  def consultar_informacion(self):
    print(f"Personal Administrativo: {self.nombre}, Departamento: {self.departamento}")

  def gestionar_documentos(self):
    print(f"El personal administrativo {self.nombre} está gestionando documentos en el departamento de {self.departamento}.")

estudiante = Estudiante("Miguel", 22, "miguel@email.com", "Ingeniería de Sistemas")
profesor = Profesor("Dr. López", 45, "lopez@email.com", "Informática")
administrativo = Administrativo("Ana", 35, "ana@email.com", "Recursos Humanos")

estudiante.consultar_informacion()
profesor.consultar_informacion()
administrativo.consultar_informacion()

estudiante.recibir_mensaje("Tienes una nueva tarea pendiente.")
profesor.recibir_mensaje("Revisión de exámenes programada.")
administrativo.recibir_mensaje("Reunión administrativa el viernes.")

estudiante.anotar_clase()
profesor.impartir_clase()
administrativo.gestionar_documentos()

