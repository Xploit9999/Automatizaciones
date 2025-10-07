import sys
import os

def convertir_a_html(archivo_dat):
    # Verifica si el archivo .dat existe
    if not os.path.isfile(archivo_dat):
        print(f"El archivo {archivo_dat} no existe.")
        return

    # Generar el nombre de archivo de salida
    nombre_salida = os.path.splitext(archivo_dat)[0] + ".html"

    try:
        with open(archivo_dat, 'r') as f_in:
            contenido = f_in.readlines()

        with open(nombre_salida, 'w') as f_out:
            f_out.write("""
<html>
<head>
    <title>Reporte Lynis</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
        }
        h1 {
            margin: 0;
        }
        table {
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        th, td {
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #ddd;
        }
        footer {
            text-align: center;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Reporte Lynis - Análisis de Sistema</h1>
    </header>
    <table>
        <tr><th>Información</th><th>Descripción</th></tr>
""")

            # Procesa cada línea para extraer la clave y el valor
            for linea in contenido:
                linea = linea.strip()
                if "=" in linea:  # Solo procesa líneas con formato clave=valor
                    clave, valor = linea.split("=", 1)
                    f_out.write(f"<tr><td><strong>{clave}</strong></td><td>{valor}</td></tr>\n")

            f_out.write("""
    </table>
    <footer>
        <p>Generado con Lynis</p>
    </footer>
</body>
</html>
""")

        print(f"Reporte convertido exitosamente a {nombre_salida}")
    
    except Exception as e:
        print(f"Hubo un error al convertir el archivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporciona el archivo .dat como argumento.")
    else:
        archivo_dat = sys.argv[1]
        convertir_a_html(archivo_dat)
