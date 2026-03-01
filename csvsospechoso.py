import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# --- RESOLUCIÓN DEL CONFLICTO ---
# Se elige la versión de Sofía (600) para pruebas rápidas, 
# pero mantenemos la lógica de Jesús disponible si se requiere más volumen.
n_registros = 600  # SOFIA CORONEL 28/02/26 Modifica el numero de registros a 600
# n_registros = 99999 # JESUSV: Descomentar para pruebas de carga masiva

n_sospechosos = 50  # SOFIA CORONEL 28/02/26

def generar_datos(n, sospechosos):
    data = []
    tipos_op = ["Transferencia", "Retiro Cajero", "Pago Servicio", "Compra POS"]

    for i in range(n):
        # SOFIA CORONEL 26/02/26 Datos base
        id_transaccion = f"TRX-{15000 + i}"
        
        fecha = datetime(2023, 1, 1) + timedelta(
            days=random.randint(0, 365), hours=random.randint(0, 23)
        )
        
        monto = round(random.uniform(10, 2000), 2)
        
        # CORRECCIÓN DE ERROR DE SINTAXIS: decía 'tipos_oPP'
        tipo = random.choice(tipos_op) 

        # Lógica de sospecha
        es_sospechosa = 0 

        # SOFIA CORONEL 26/02/26 Insertar operaciones sospechosas
        if i < sospechosos:
            es_sospechosa = 1  # SOFIA CORONEL 28/02/26 Marcaje claro
            # Patrón sospechoso: Montos altos y hora inusual
            monto = round(random.uniform(10000, 50000), 2)
            tipo = "Transferencia Internacional NO AUTORIZADA"
            fecha = fecha.replace(hour=random.randint(2, 4)) # Madrugada

        data.append([id_transaccion, fecha, monto, tipo, es_sospechosa])

    # Mezclar los datos
    random.shuffle(data)
    return data

# Crear DataFrame
columnas = [
    "ID_Transaccion",
    "Fecha_Hora_EXACTA",
    "Monto_USD",
    "Tipo_Operacion",
    "Es_Sospechosa",
]

# CORRECCIÓN DE ERROR DE SINTAXIS: Se eliminó el doble llamado ()(...)
df = pd.DataFrame(
    generar_datos(n_registros, n_sospechosos),
    columns=columnas,
)

# Guardar a CSV
df.to_csv("operaciones_bancarias.csv", index=False)
print(f"Archivo 'operaciones_bancarias.csv' generado con éxito con {n_registros} registros.")