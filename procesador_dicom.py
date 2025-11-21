import os
from pydicom import dcmread
from pydicom.data import get_testdata_files
from pydicom.errors import InvalidDicomError
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


class ProcesadorDICOM:
    def __init__(self, directorio="datos_ejemplo"):
        self.directorio = os.path.normpath(directorio)
        self.df = None  

    def _valor_seguro(self, ds, keyword, default="Desconocido"):
        try:
            valor = ds.get(keyword, default)
            if valor in ("", None, [], (), {}):
                return default
            return str(valor) if keyword == "PatientName" else valor
        except:
            return default

    def cargar_dicom(self):
        archivos = []

        if not os.path.exists(self.directorio) or not os.listdir(self.directorio):
            print("Carpeta vacía: Se usará datos de prueba de pydicom\n")
            for archivo in get_testdata_files("*.dcm")[:20]:
                try:
                    ds = dcmread(archivo, force=True)
                    archivos.append((os.path.basename(archivo), ds))
                except:
                    pass
            return archivos

        for raiz, _, files in os.walk(self.directorio):
            for f in files:
                ruta_completa = os.path.join(raiz, f)
                try:
                    ds = dcmread(ruta_completa, force=True)
                    archivos.append((f, ds))
                except:
                    pass
        return archivos

    def procesar(self):
        print(f"\n=== Iniciando procesamiento de: {self.directorio} ===\n")

        lista = self.cargar_dicom()
        total = len(lista)

        if total == 0:
            print("No se encontraron archivos DICOM válidos.")
            return

        print(f"Archivos DICOM encontrados: {total}")
        print("Procesando metadatos e intensidades...")

        datos = []
        for nombre, ds in lista:
            fila = {
                "Archivo": nombre,
                "PatientID": self._valor_seguro(ds, "PatientID"),
                "PatientName": self._valor_seguro(ds, "PatientName"),
                "StudyInstanceUID": self._valor_seguro(ds, "StudyInstanceUID"),
                "StudyDescription": self._valor_seguro(ds, "StudyDescription", "Sin descripción"),
                "StudyDate": self._valor_seguro(ds, "StudyDate"),
                "Modality": self._valor_seguro(ds, "Modality"),
                "Rows": int(self._valor_seguro(ds, "Rows", 0)),
                "Columns": int(self._valor_seguro(ds, "Columns", 0)),
            }

            try:
                fila["IntensidadPromdio"] = float(np.mean(ds.pixel_array))
            except:
                fila["IntensidadPromdio"] = None

            datos.append(fila)

        self.df = pd.DataFrame(datos)

        # Guardar CSV en la carpeta donde se ejecuta el script
        ruta_csv = os.path.join(os.getcwd(), "metadatos_dicom.csv")
        contador = 1
        while os.path.exists(ruta_csv):
            ruta_csv = os.path.join(os.getcwd(), f"metadatos_dicom_{contador}.csv")
            contador += 1

        self.df.to_csv(ruta_csv, index=False, encoding="utf-8")
        print(f"CSV guardado como: {os.path.basename(ruta_csv)}")
        print("-"*60)
        print("\nPrimeras filas del CSV generado:")
        print(self.df.head().to_string(index=False))


if __name__ == "__main__":
    import sys
    carpeta = sys.argv[1] if len(sys.argv) > 1 else "datos_ejemplo"
    ProcesadorDICOM(carpeta).procesar()

