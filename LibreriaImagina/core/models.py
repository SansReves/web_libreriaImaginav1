# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class CatgLibro(models.Model):
    id_catg = models.AutoField(primary_key=True)
    catg_libro = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'catg_libro'


class Cliente(models.Model):
    rut_cli = models.CharField(primary_key=True, max_length=9)
    nombre_cli = models.CharField(max_length=30)
    ap_paterno_cli = models.CharField(max_length=30, blank=True, null=True)
    correo_cli = models.CharField(max_length=50)
    telefono_cli = models.IntegerField()
    usuario_cli = models.CharField(max_length=30)
    contrasenia_cli = models.CharField(max_length=30)
    id_tp_cli = models.ForeignKey('TipoCliente', models.DO_NOTHING, db_column='id_tp_cli')

    class Meta:
        managed = False
        db_table = 'cliente'


class Despacho(models.Model):
    id_despc = models.AutoField(primary_key=True)
    nombre_despc = models.CharField(max_length=30)
    precio_despc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'despacho'

class Empleado(models.Model):
    rut_emp = models.CharField(primary_key=True, max_length=9)
    nombre_emp = models.CharField(max_length=20)
    ap_paterno_emp = models.CharField(max_length=30)
    correo_emp = models.CharField(max_length=40)
    telefono_emp = models.IntegerField()
    usuario_emp = models.CharField(max_length=15)
    contrasenia_emp = models.CharField(max_length=20)
    id_tp_emp = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='id_tp_emp')

    class Meta:
        managed = False
        db_table = 'empleado'


class Estado(models.Model):
    id_est = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'estado'


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    nombre_libro = models.CharField(max_length=40)
    autor_libro = models.CharField(max_length=40)
    sinopsis_libro = models.CharField(max_length=250, blank=True, null=True)
    precio_libro = models.IntegerField()
    stock_libro = models.IntegerField()
    imagen = models.ImageField(upload_to="libros", blank=True, null=True)
    id_catg = models.ForeignKey(CatgLibro, models.DO_NOTHING, db_column='id_catg')

    class Meta:
        managed = False
        db_table = 'libro'


class OrdenCompra(models.Model):
    id_compra = models.BigAutoField(primary_key=True)
    fecha_or_compra = models.DateField()
    total_final_or = models.IntegerField(blank=True, null=True)
    rut_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='rut_emp')
    id_est = models.ForeignKey(Estado, models.DO_NOTHING, db_column='id_est')
    id_tp_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tp_pago')
    rut_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cli')

    class Meta:
        managed = False
        db_table = 'orden_compra'


class OrdenDespacho(models.Model):
    fecha_despc = models.DateField()
    direccion_despc = models.CharField(max_length=100)
    indicaciones_despc = models.CharField(max_length=250, blank=True, null=True)
    id_despc = models.OneToOneField(Despacho, models.DO_NOTHING, db_column='id_despc', primary_key=True)
    id_compra = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'orden_despacho'
        unique_together = (('id_despc', 'id_compra'),)


class OrdenLibro(models.Model):
    total_detalle_libro = models.IntegerField()
    cant_libro = models.IntegerField()
    id_libro = models.OneToOneField(Libro, models.DO_NOTHING, db_column='id_libro', primary_key=True)
    id_compra = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'orden_libro'
        unique_together = (('id_libro', 'id_compra'),)


class OrdenServicio(models.Model):
    total_detalle_serv = models.IntegerField()
    cant_serv = models.IntegerField()
    fecha_serv = models.DateField(blank=True, null=True)
    confirm_serv = models.FloatField(blank=True, null=True)
    id_serv = models.OneToOneField('Servicio', models.DO_NOTHING, db_column='id_serv', primary_key=True)
    id_compra = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_compra')

    class Meta:
        managed = False
        db_table = 'orden_servicio'
        unique_together = (('id_serv', 'id_compra'),)


class Servicio(models.Model):
    id_serv = models.AutoField(primary_key=True)
    nombre_serv = models.CharField(max_length=50)
    dscrp_serv = models.CharField(max_length=250, blank=True, null=True)
    precio_serv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoCliente(models.Model):
    id_tp_cli = models.AutoField(primary_key=True)
    nombre_tp_cli = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoEmpleado(models.Model):
    id_tp_emp = models.AutoField(primary_key=True)
    nombre_tp_emp = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'


class TipoPago(models.Model):
    id_tp_pago = models.AutoField(primary_key=True)
    nombre_tp_pago = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_pago'
