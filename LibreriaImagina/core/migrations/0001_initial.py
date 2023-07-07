# Generated by Django 3.2.3 on 2023-07-07 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatgLibro',
            fields=[
                ('id_catg', models.AutoField(primary_key=True, serialize=False)),
                ('catg_libro', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'catg_libro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cli', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre_cli', models.CharField(max_length=30)),
                ('ap_paterno_cli', models.CharField(blank=True, max_length=30, null=True)),
                ('correo_cli', models.CharField(max_length=50)),
                ('telefono_cli', models.IntegerField()),
                ('usuario_cli', models.CharField(max_length=30)),
                ('contrasenia_cli', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id_despc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_despc', models.CharField(max_length=30)),
                ('precio_despc', models.IntegerField()),
            ],
            options={
                'db_table': 'despacho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut_emp', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nombre_emp', models.CharField(max_length=20)),
                ('ap_paterno_emp', models.CharField(max_length=30)),
                ('correo_emp', models.CharField(max_length=40)),
                ('telefono_emp', models.IntegerField()),
                ('usuario_emp', models.CharField(max_length=15)),
                ('contrasenia_emp', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_est', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estado', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_libro', models.CharField(max_length=40)),
                ('autor_libro', models.CharField(max_length=40)),
                ('sinopsis_libro', models.CharField(blank=True, max_length=250, null=True)),
                ('precio_libro', models.IntegerField()),
                ('stock_libro', models.IntegerField()),
                ('imagen', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'libro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id_compra', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_or_compra', models.DateField()),
                ('total_final_or', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orden_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_serv', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_serv', models.CharField(max_length=50)),
                ('dscrp_serv', models.CharField(blank=True, max_length=250, null=True)),
                ('precio_serv', models.IntegerField()),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id_tp_cli', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tp_cli', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id_tp_emp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tp_emp', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tipo_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_tp_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tp_pago', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenDespacho',
            fields=[
                ('fecha_despc', models.DateField()),
                ('direccion_despc', models.CharField(max_length=100)),
                ('indicaciones_despc', models.CharField(blank=True, max_length=250, null=True)),
                ('id_despc', models.OneToOneField(db_column='id_despc', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.despacho')),
            ],
            options={
                'db_table': 'orden_despacho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenLibro',
            fields=[
                ('total_detalle_libro', models.IntegerField()),
                ('cant_libro', models.IntegerField()),
                ('id_libro', models.OneToOneField(db_column='id_libro', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.libro')),
            ],
            options={
                'db_table': 'orden_libro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenServicio',
            fields=[
                ('total_detalle_serv', models.IntegerField()),
                ('cant_serv', models.IntegerField()),
                ('fecha_serv', models.DateField(blank=True, null=True)),
                ('confirm_serv', models.FloatField(blank=True, null=True)),
                ('id_serv', models.OneToOneField(db_column='id_serv', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.servicio')),
            ],
            options={
                'db_table': 'orden_servicio',
                'managed': False,
            },
        ),
    ]
