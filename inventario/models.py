from django.db import models

# Create your models here.

# Models me permite crear la estructura de la base de datos.
# Todo cambio que realice dentro de model impacta sobre la base de datos, por lo que es necesario hacer un makemigrations y luego un migrate.
# el str es quien me permite ver los campos en el ADMIN DJANGO

# ********************************************************************

# SAP_COD_CLASE

class Clase(models.Model): 
    cod_clase = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self): # ------------------------------------------->>>> el str define como se mostrara el objeto o que se vera en el Admin de Django.
        return f'{self.cod_clase} - {self.nombre}'

# ********************************************************************

# SAP_COD_MARCA

class Marca(models.Model): 
    cod_marca = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.cod_marca} - {self.nombre}'

# ********************************************************************

# LPM_CODIGOS_POLARIS_TIPO_VEH (la parte de modelo).
# codificacion de modelos 
# Cada descripcion del modelo se construye con cod_clase /cod_marca/ cod_modelo

# models.ForeignKey: establece la relacion entre tablas en base a un campo
# on_delete=models.PROTECT : si alguien intenta borrar una Clase que tiene Elementos asociados, Django no permitira borrarla (Proteccion)
# related_name='modelos': permite acceder desde una instancia de Clase a todos sus elementos con clase.elementos.all()

class Modelo(models.Model):
    cod_modelo = models.CharField(max_length=20)
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT, related_name='modelos') 
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='modelos')
    descripcion = models.CharField(max_length=200, blank=True)
    cod_veh = models.CharField(max_length=20, primary_key=True)
    
    def __str__(self):
        return f'{self.cod_modelo} - {self.descripcion or 'Sin desc.'}'

# ********************************************************************

# SAP_PARTES (puerta, faro, paragolpes…)

class Parte(models.Model):
    cod_parte = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.cod_parte} - {self.nombre}'


# ********************************************************************

# SAP_ELEMENTOS (granularidad debajo de Parte)

class Elemento(models.Model):  
    cod_elemento = models.CharField(max_length=20, primary_key=True)
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT, related_name="elementos")
    parte = models.ForeignKey(Parte, on_delete=models.PROTECT, related_name="elementos")
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.cod_elemento} - {self.nombre}"


# ********************************************************************

# Esta tabla modela SAP_BRAN: une Clase + Marca + Modelo + Parte + Elemento y lo junta con `nro_pieza` y `precio`

class Estructura(models.Model):
        clase = models.ForeignKey(Clase, on_delete=models.PROTECT, related_name="estructuras")
        marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="estructuras")
        modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="estructuras")
        parte = models.ForeignKey(Parte, on_delete=models.PROTECT, related_name="estructuras")
        elemento = models.ForeignKey(Elemento, on_delete=models.PROTECT, related_name="estructuras")
        
        nro_pieza = models.CharField(max_length=50, blank=True, null=True)  ##
        precio = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True) ##

        def __str__(self):
            return f"{self.modelo} | {self.parte} | {self.elemento} | pieza={self.nro_pieza or '-'}"