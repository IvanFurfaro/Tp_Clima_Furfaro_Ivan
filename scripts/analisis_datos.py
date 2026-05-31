import pandas as pd
import matplotlib.pyplot as plt
import os

#==============================================================================
#FASE 1: GENERACIÓN DE DATOS HISTÓRICOS (Simulación de Open Data Climático)
#Generamos un dataset para que el proyecto sea 100% ejecutable sin dependencias externas.
#==============================================================================
def generar_dataset_climatico():
    #Simulamos registros mensuales de temperatura (°C) y precipitaciones (mm)
    datos_clima = {
        'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        'Temperatura_Min': [18.5, 17.0, 15.2, 12.0, 8.5, 5.0, 4.2, 6.1, 9.5, 12.1, 14.8, 17.2],
        'Temperatura_Max': [31.2, 29.8, 27.5, 23.0, 18.2, 14.5, 13.8, 16.0, 19.5, 22.8, 26.5, 29.5],
        'Precipitaciones': [110.5, 95.2, 120.0, 75.4, 45.1, 25.0, 30.2, 35.8, 55.0, 80.3, 90.1, 105.4]
    }
    
    df = pd.DataFrame(datos_clima)
    
    #Calculamos la temperatura media mensual para el análisis posterior
    df['Temperatura_Media'] = (df['Temperatura_Min'] + df['Temperatura_Max']) / 2
    
    #Nos aseguramos de que exista la carpeta /datos y guardamos el archivo
    os.makedirs('datos', exist_ok=True)
    df.to_csv('datos/registro_climatico.csv', index=False)
    print("[INFO] Dataset de registros climáticos guardado exitosamente en 'datos/registro_climatico.csv'")

#==============================================================================
#FASE 2: PROCESAMIENTO Y CÁLCULO DE INDICADORES METEOROLÓGICOS
#==============================================================================
def analizar_datos_climaticos():
    #Cargamos el archivo utilizando rutas relativas para asegurar la reproducibilidad
    if not os.path.exists('datos/registro_climatico.csv'):
        raise FileNotFoundError("No se encontró el archivo de datos climáticos.")
        
    df = pd.read_csv('datos/registro_climatico.csv')
    
    #1. Indicador: Temperatura Promedio Anual (a partir de las medias mensuales)
    temp_promedio_anual = df['Temperatura_Media'].mean()
    
    #2. Indicadores: Temperaturas Extremas (Máxima y Mínima absolutas observadas)
    temp_maxima_absoluta = df['Temperatura_Max'].max()
    temp_minima_absoluta = df['Temperatura_Min'].min()
    
    #Obtener los meses correspondientes a dichos extremos para enriquecer el reporte
    mes_max = df.loc[df['Temperatura_Max'].idxmax(), 'Mes']
    mes_min = df.loc[df['Temperatura_Min'].idxmin(), 'Mes']
    
    #3. Indicador: Promedio de Precipitaciones Mensuales
    precipitacion_promedio = df['Precipitaciones'].mean()
    
    #Imprimir reporte técnico en la consola de ejecución
    print("\n" + "="*45)
    print("      REPORTE DE INDICADORES CLIMÁTICOS      ")
    print("="*45)
    print(f"Temperatura Media Anual:      {temp_promedio_anual:.2f} °C")
    print(f"Temperatura Máxima Absoluta:  {temp_maxima_absoluta:.1f} °C ({mes_max})")
    print(f"Temperatura Mínima Absoluta:  {temp_minima_absoluta:.1f} °C ({mes_min})")
    print(f"Precipitación Mensual Promedio: {precipitacion_promedio:.2f} mm")
    print("="*45 + "\n")
    
    #Guardamos un resumen de texto en /resultados para que quede documentado físicamente
    os.makedirs('resultados', exist_ok=True)
    with open('resultados/reporte_indicadores.txt', 'w') as f:
        f.write("REPORTE DE INDICADORES CLIMÁTICOS ANUALES\n")
        f.write(f"Temp. Media Anual: {temp_promedio_anual:.2f} C\n")
        f.write(f"Temp. Max: {temp_maxima_absoluta:.1f} C ({mes_max})\n")
        f.write(f"Temp. Min: {temp_minima_absoluta:.1f} C ({mes_min})\n")
        f.write(f"Precipitacion Promedio: {precipitacion_promedio:.2f} mm\n")

    #==============================================================================
    #FASE 3: GENERACIÓN Y EXPORTACIÓN DEL GRÁFICO CLIMÁTICO
    #==============================================================================
    fig, ax1 = plt.subplots(figsize=(10, 6))

    #Graficar la evolución de la temperatura (Línea con marcadores)
    color = 'tab:red'
    ax1.set_xlabel('Meses del Año')
    ax1.set_ylabel('Temperatura (°C)', color=color)
    linea_temp = ax1.plot(df['Mes'], df['Temperatura_Media'], color=color, marker='o', linewidth=2.5, label='Temp. Media')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.5)

    #Crear un segundo eje y para representar las precipitaciones en el mismo gráfico (Barras)
    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Precipitaciones (mm)', color=color)
    barras_precip = ax2.bar(df['Mes'], df['Precipitaciones'], color=color, alpha=0.3, width=0.4, label='Precipitaciones')
    ax2.tick_params(axis='y', labelcolor=color)

    #Estética general del gráfico
    plt.title('Evolución de Temperatura y Precipitaciones a lo Largo del Año')
    fig.tight_layout()  
    
    #Guardar gráfico final usando ruta relativa
    plt.savefig('resultados/grafico_temperatura.png', dpi=150)
    plt.close()
    print("[INFO] Gráfico climático multieje guardado exitosamente en 'resultados/grafico_temperatura.png'")

if __name__ == "__main__":
    generar_dataset_climatico()
    analizar_datos_climaticos()
