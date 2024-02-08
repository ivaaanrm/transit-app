from django.db import models

class Incidencia(models.Model):
    causa = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    via = models.CharField(max_length=100)
    km_inicio_fin = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    demarcacion = models.CharField(max_length=50)
    tramo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    inicio = models.TimeField()
    observaciones = models.TextField()
    tiempo_registro = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)



    def __str__(self):
        return f"Incidencia: {self.causa} - {self.via} ({self.km_inicio_fin})"
    


class Log(models.Model):
    log_time = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Log: {self.tipo} - {self.log_time.strftime('%Y-%m-%d %H:%M:%S')}"
