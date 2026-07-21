"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibe una lista y retorna el total de ventas."""
    return sum(ventas)
def calcular_porcentaje_logro(total, venta):
    """calcula el procentaje de cumplimiento de un meta"""
    procentaje = total / meta * 100
    return procentaje

def calcular_clasificacion(porcentaje):
    if porcentaje >= 100:
        mensaje="Meta alcanzada, felicitaciones..!"
    elif porcentaje >= 90:
        mensaje = "ADVERTENCIA: meta no lograda."
    else:
        mensaje = "URGENTE: meta no alcanzada, revisar perdidas"
    return mensaje

def imprimir_reporte(datos_reporte):
    """Imprime el reporte final de ventas por emprendimiento"""
    #Encabezado
    print("\nREPORTE FINAL")
    print("-" * 60)

    for fila in datos_reporte:
        print(f"sede: {fila["provincia"]}")
        print(f"provincia: {fila["tipo"]}")
        print(f"tipo: {fila["tipo"]}")

    print(f"Total ventas semanal: ₡{fila["total"]:,.2f}")
    print(f"cumplimiento de meta:{fila["porcentaje"]:.2f}")
    print(f"promeio diario: ₡{fila["total"]/5:,.2f}")
    print(fila['clasificacion'])

    print("-" * 60)
    
    
    
reporte = []
for emprendimiento in sedes:

    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]
    nombre = emprendimiento["nombre"]

    total_ventas = calcular_total(ventas)
    porcentaje_emprendimiento = calcular_porcentaje_logro(total_ventas, meta)
    clasificacion = calcular_clasificacion(porcentaje_emprendimiento)
    
    reporte.append(
        {
            "nombre" : emprendimiento["nombre"],
            "provincia" : emprendimiento["provincia"],
            "tipo": emprendimiento["tipo"],
            "total": total_ventas,
            "porcentaje": porcentaje_emprendimiento,
            "clasificacio": clasificacion
        }
    )
    
imprimir_reporte(reporte)