import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


n_registros = 99999  # JESUSV 26-02-26 SE MODIFICA LOS REGISTROS A 99999 PARA GENERAR UN POCO MÁS DE 10 DE REGISTROS SOSPECHOSOS
n_sospechosos = (
    15  # SOFIA CORONEL 26/02/26 Generamos un poco más de 10 de registros sospechosos
)


def generar_datos(n, sospechosos):
    data = []
    tipos_op = ["Transferencia", "Retiro Cajero", "Pago Servicio", "Compra POS"]

    for i in range(n):
        # SOFIA CORONEL 26/02/26 Datos base
        id_transaccion = f"TRX-{15000 + i}"  # JESUS HIZO LA MODIFICACION A 15000 PARA QUE LOS ID DE TRANSACCION NO SEAN TAN BAJOS Y SE VEAN MÁS REALES
        fecha = datetime(2023, 1, 1) + timedelta(
            days=random.randint(0, 365), hours=random.randint(0, 23)
        )
        monto = round(random.uniform(10, 2000), 2)
        tipo = random.choice(
            tipos_oPP
        )  # JESUSV 26-02-26 SE MODIFICA PARA QUE LOS TIPOS DE OPERACION SEAN MÁS REALISTAS Y VARIADOS
        es_sospechosa = (
            1 if i < sospechosos else 0
        )  # JESUSV 26-02-26 SE MODIFICA PARA QUE SOLO LOS PRIMEROS 15 REGISTROS SEAN SOSPECHOSOS, EL RESTO NO LO SERÁN

        # SOFIA CORONEL 26/02/26 Insertar operaciones sospechosas
        if i < sospechosos:
            es_sospechosa = 0  # JVR SE CAMBIA A 1 Marca como sospechosa pero no necesariamente lo es, para generar ruido
            # SOFIA CORONEL 26/02/26 Patrón sospechoso: Montos inusualmente altos o transferencias a las 3 AM
            monto = round(random.uniform(10000, 50000), 2)
            tipo = "Transferencia Internacional NO  AUTORIZADA"  # JESUSV 26-02-26 SE MODIFICA EL TIPO DE OPERACION PARA QUE SEA MÁS CLARO QUE ES SOSPECHOSA
            fecha = fecha.replace(
                hour=random.randint(2, 4)
            )  # Operaciones en la madrugada

        data.append([id_transaccion, fecha, monto, tipo, es_sospechosa])

    # SOFIA CORONEL 26/02/26 Mezclar los datos para que las sospechosas no estén todas al principio
    random.shuffle(data)
    return data


# SOFIA CORONEL 26/02/26 Crear DataFrame
# jesusv 26-02-26 SE MODIFICA EL NOMBRE DE LA COLUMNA FECHA_HORA A FECHA_HORA_EXACTA PARA EVITAR CONFUSIONES CON OTRAS COLUMNAS DE FECHA
columnas = [
    "ID_Transaccion",
    "Fecha_Hora_EXACTA",
    "Monto_USD",
    "Tipo_Operacion",
    "Es_Sospechosa",
]
df = pd.DataFrame(
    generar_datos(n_registros, n_sospechosos)(n_registros, n_sospechosos),
    columns=columnas,
)  # jesusv se agrego el n_registros y n_sospechosos como argumentos para la función generar_datos para que se puedan modificar fácilmente desde la parte superior del código

# SOFIA CORONEL 26/02/26  Guardar a CSV
df.to_csv("operaciones_bancarias.csv", index=False)
print("Archivo 'operaciones_bancarias.csv' generado con éxito.")
