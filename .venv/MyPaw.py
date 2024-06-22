import matplotlib.pyplot as plt
import pandas as pd

# Datos del cronograma
data = {
    "Actividad": [
        "Reunión inicial y definición de requerimientos",
        "Diseño de la arquitectura del sistema",
        "Diseño de la interfaz de usuario (UI/UX)",
        "Configuración del entorno de desarrollo",
        "Desarrollo del backend",
        "Desarrollo del frontend",
        "Integración y pruebas unitarias",
        "Pruebas de integración",
        "Pruebas de aceptación del usuario (UAT)",
        "Preparación del entorno de producción",
        "Despliegue inicial",
        "Pruebas en producción",
        "Monitoreo y mantenimiento",
        "Recolección de retroalimentación del usuario", "Implementación de mejoras y nuevas funcionalidades"
    ],
    "Inicio": [
        "2024-07-01", "2024-07-08", "2024-07-15",
        "2024-08-01", "2024-08-15", "2024-09-01",
        "2024-10-01", "2024-11-01", "2024-11-15",
        "2024-12-01", "2024-12-15", "2024-12-20",
        "2025-01-01", "2025-02-01", "2025-03-01"
    ],
    "Fin": [
        "2024-07-07", "2024-07-14", "2024-07-31",
        "2024-08-14", "2024-08-31", "2024-09-30",
        "2024-10-31", "2024-11-14", "2024-11-30",
        "2024-12-14", "2024-12-19", "2024-12-31",
        "2025-01-31", "2025-02-28", "2025-03-31"
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Convertir fechas a datetime
df["Inicio"] = pd.to_datetime(df["Inicio"])
df["Fin"] = pd.to_datetime(df["Fin"])

# Calcular la duración en días
df["Duración"] = (df["Fin"] - df["Inicio"]).dt.days

# Verificar datos
print(df)

# Crear diagrama de Gantt
plt.figure(figsize=(12, 8)) 
plt.barh(df["Actividad"], df["Duración"], left=df["Inicio"].map(pd.Timestamp.toordinal), color='skyblue')
plt.xlabel("Fecha")
plt.ylabel("Actividad")
plt.title("Diagrama de Gantt del Proyecto My Paw")
plt.grid(axis='x')

# Configurar el eje x para mostrar fechas y rotar etiquetas
ax = plt.gca()
ax.set_xticks(df["Inicio"].map(pd.Timestamp.toordinal))
ax.set_xticklabels(df["Inicio"].dt.strftime('%Y-%m-%d'), rotation=45, ha='right')

# Guardar el diagrama como JPG
plt.tight_layout()
plt.savefig("/mnt/data/diagrama_gantt_my_paw.jpg", format='jpg')
plt.show()
