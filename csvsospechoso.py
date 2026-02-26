import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


n_registros = 500
n_sospechosos = 15 # SOFIA CORONEL 26/02/26 Generamos un poco más de 10 de registros sospechosos

def generar_datos(n, sospechosos):
    data = []
    tipos_op = ['Transferencia', 'Retiro Cajero', 'Pago Servicio', 'Compra POS']
    
    for i in range(n):
        # SOFIA CORONEL 26/02/26 Datos base
        id_transaccion = f"TRX-{1000 + i}"
        fecha = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))
        monto = round(random.uniform(10, 2000), 2)
        tipo = random.choice(tipos_op)
        es_sospechosa = 0
        
        # SOFIA CORONEL 26/02/26 Insertar operaciones sospechosas 
        if i < sospechosos:
            es_sospechosa = 1
            # SOFIA CORONEL 26/02/26 Patrón sospechoso: Montos inusualmente altos o transferencias a las 3 AM
            monto = round(random.uniform(10000, 50000), 2) 
            tipo = 'Transferencia Internacional'
            fecha = fecha.replace(hour=random.randint(2, 4)) # Operaciones en la madrugada
        
        data.append([id_transaccion, fecha, monto, tipo, es_sospechosa])
    
    # SOFIA CORONEL 26/02/26 Mezclar los datos para que las sospechosas no estén todas al principio
    random.shuffle(data)
    return data

# SOFIA CORONEL 26/02/26 Crear DataFrame
columnas = ['ID_Transaccion', 'Fecha_Hora', 'Monto_USD', 'Tipo_Operacion', 'Es_Sospechosa']
df = pd.DataFrame(generar_datos(n_registros, n_sospechosos), columns=columnas)

# SOFIA CORONEL 26/02/26  Guardar a CSV
df.to_csv('operaciones_bancarias.csv', index=False)
print("Archivo 'operaciones_bancarias.csv' generado con éxito.")