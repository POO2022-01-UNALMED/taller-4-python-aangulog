from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        
    def __str__(self):
        texto="Grupo de estudiantes: "+self._grupo
        return texto

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas is None:
            lista = []
            for x in kwargs.values():
                lista.append(Asignatura(x))
                self._asignaturas=lista
        else:
            for x in kwargs.values():
                self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, bree=None):
        if(self.listadoAlumnos is None):
            if isinstance(bree, list):
                bree.append(alumno)
                self.listadoAlumnos = bree
                return
            lista=[]
            lista.append(alumno)
            self.listadoAlumnos = lista
        else:
            self.listadoAlumnos.append(alumno)

# =============================================================================
#     @ classmethod
#     def asignarNombre(cls, nombre="Grado 10"):
#         cls.grado = nombre
# =============================================================================

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre


# =============================================================================
#     @ classmethod
#     def asignarNombre(cls, nombre="Grado 4"):
#         cls.grado = nombre
# =============================================================================



