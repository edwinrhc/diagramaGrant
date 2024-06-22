import matplotlib.pyplot as plt
import pandas as pd

# Datos del cronograma
data = {
    "Actividad": [
        "Revisión de literatura", "Diseño de instrumentos", "Recolección de datos (Pretest)",
        "Implementación de la plataforma", "Recolección de datos (Postest)", "Análisis de datos",
        "Redacción del informe", "Revisión y ajustes", "Presentación de resultados"
    ],
    "Inicio": [
        "2024-05-01", "2024-06-01", "2024-07-01", "2024-08-01", "2024-10-01", "2024-11-01", "2025-01-01", "2025-03-01", "2025-04-01"
    ],
    "Fin": [
        "2024-05-31", "2024-06-30", "2024-07-31", "2024-09-30", "2024-10-31", "2024-12-31", "2025-02-28", "2025-03-31", "2025-04-30"
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir fechas
df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"] = pd.to_datetime(df["Fin"])

# Calcular la duración en días
df["Duración"] = (df["Fin"] - df["Inicio"]).dt.days

# Crear diagrama de Gantt
plt.figure(figsize=(12, 8))
plt.barh(df["Actividad"], df["Duración"], left=df["Inicio"].map(pd.Timestamp.toordinal), color='skyblue')
plt.xlabel("Fecha")
plt.ylabel("Actividad")
plt.title("Diagrama de Gantt del Proyecto de Investigación")
plt.grid(axis='x')

# Configurar el eje x para mostrar fechas
ax = plt.gca()
ax.set_xticks(df["Inicio"].map(pd.Timestamp.toordinal))
ax.set_xticklabels(df["Inicio"].dt.strftime('%Y-%m-%d'))

# Mostrar el diagrama
plt.tight_layout()
plt.show()
