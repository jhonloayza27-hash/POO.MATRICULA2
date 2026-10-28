class Matricula:
    def __init__(self, costo_base=60.00):
        self._costo_base = costo_base

    def calcular_costo(self):
        return self._costo_base


class MatriculaExtemporanea(Matricula):
    def calcular_costo(self):
        return super().calcular_costo() + 15.00


class IndiceDesaprobatorio(Matricula):
    def calcular_costo(self):
        return super().calcular_costo() + 15.00


class Beca(Matricula):
    def calcular_costo(self):
        return super().calcular_costo() / 2


class MatriculaCombinada1(
    Beca,
    IndiceDesaprobatorio,
    MatriculaExtemporanea
):
    pass


class MatriculaCombinada2(
    IndiceDesaprobatorio,
    MatriculaExtemporanea,
    Beca
):
    pass


class Estudiante:
    def __init__(self, nombre, tipo_matricula):
        self.__nombre = nombre
        self.__tipo_matricula = tipo_matricula

    def mostrar_informacion(self):
        print("Estudiante:", self.__nombre)
        print(
            f"Costo de matrícula: "
            f"S/ {self.__tipo_matricula.calcular_costo():.2f}"
        )


luis = Estudiante(
    "Luis Huamani Cardenas",
    MatriculaCombinada1()
)

rosa = Estudiante(
    "Rosa Ccahuana Prado",
    MatriculaCombinada2()
)



print("SISTEMA DE MATRÍCULA")


print("\nPRIMERA VERSION")
luis.mostrar_informacion()

print("\nSEGUNDA VERSION")
rosa.mostrar_informacion()


print("ORDEN DE RESOLUCION DE METODOS (MRO)")

print("\nMatriculaCombinada1:")
for clase in MatriculaCombinada1.__mro__:
    print("->", clase.__name__)

print(MatriculaCombinada1.mro())

print("\nMatriculaCombinada2:")
for clase in MatriculaCombinada2.__mro__:
    print("->", clase.__name__)
print(MatriculaCombinada2.mro())


# Comparar los costos
costo_luis = luis._Estudiante__tipo_matricula.calcular_costo()
costo_rosa = rosa._Estudiante__tipo_matricula.calcular_costo()
print("COMPARACION DE COSTOS")

print(f"Costo de Luis: S/ {costo_luis:.2f}")
print(f"Costo de Rosa: S/ {costo_rosa:.2f}")
print(f"Diferencia: S/ {abs(costo_luis - costo_rosa):.2f}")

if costo_luis < costo_rosa:
    print("Luis paga menos en esta version.")
elif costo_rosa < costo_luis:
    print("Rosa paga menos en esta version.")
else:
    print("Ambos pagan el mismo monto.")
