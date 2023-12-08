import sys
import os
import hashlib
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
import subprocess
from duplicadosUI import*


import tkinter as tk
from tkinter.filedialog import askdirectory

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        # loadUi('ptqt6_duplicados.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tvResultado.setColumnWidth(0, 150)
        self.ui.tvResultado.setColumnWidth(1, 500)
        self.ui.tvResultado.setColumnWidth(2, 100)
        self.ui.tvResultado.verticalHeader().hide()
        # self.setStyleSheet("QMainWindow::title { background-color: #aaaa7f; }")

        self.ui.btnSeleccionar.clicked.connect(self.seleccionarDirectorio)
        self.ui.btnBuscarDuplicados.clicked.connect(self.buscarDuplicados)
        self.ui.tvResultado.cellClicked.connect(self.clickTabla)

        self.tabla_ficheros = []
        self.contador_archivos = 0


    def seleccionarDirectorio(self):
        directory_path = tk.filedialog.askdirectory()
        self.inicializar_objetos()
        self.ui.directorioActual.setText(directory_path)

    def proteger_elementos(self, estado):
        self.ui.directorioActual.setEnabled(estado)
        self.ui.btnSeleccionar.setEnabled(estado)
        self.ui.btnBuscarDuplicados.setEnabled(estado)
        self.ui.tvResultado.setEnabled(estado)

    def inicializar_objetos(self):
        self.ui.lb_contador_archivos.setText(str(0))
        self.ui.lb_contador_duplicados.setText(str(0))
        self.ui.tvResultado.setRowCount(0)

#----------------------------------------------------------------------------------------
    def buscarDuplicados(self):
        QApplication.setOverrideCursor(QCursor(Qt.CursorShape.BusyCursor))
        self.proteger_elementos(False)

        self.leer_ficheros(self.ui.directorioActual.text())
        duplicados = {}
        duplicados1 = []

        for fila in self.tabla_ficheros:
            valor = fila[2]
            if valor in duplicados:
                duplicados[valor].append(fila)
            else:
                duplicados[valor] = [fila]

        for valor, filas in duplicados.items():
            if len(filas) > 1:
                for i in range(len(filas)):
                    duplicados1.append((str(filas[i][0]), str(filas[i][1]), str(filas[i][2])))
        self.llenar_QTableWidget(duplicados1)
        self.proteger_elementos(True)
        QApplication.restoreOverrideCursor()

#----------------------------------------------------------------------------------------
    def leer_ficheros(self, directorio):
        self.tabla_ficheros = []
        self.contador_archivos = 0
        self.inicializar_objetos()

        for ruta_actual, directorios, archivos in os.walk(directorio):
            for nombre_archivo in archivos:
                ruta_completa = os.path.join(ruta_actual, nombre_archivo)
                valor_hash = self.calcular_hash(ruta_completa)
                self.tabla_ficheros.append((str(nombre_archivo), str(ruta_actual), str(valor_hash)))
                self.contador_archivos += 1
                total = format(self.contador_archivos, ',d')
                total = total.replace(",", ".")
                self.ui.lb_contador_archivos.setText(str(total))
                QApplication.processEvents()

    def calcular_hash(self, ruta_archivo, algoritmo='sha256'):
        hash_calculado = hashlib.new(algoritmo)
        with open(ruta_archivo, 'rb') as archivo:
            for bloque in iter(lambda: archivo.read(4096), b""):
                hash_calculado.update(bloque)
        return hash_calculado.hexdigest()

#----------------------------------------------------------------------------------------
    def llenar_QTableWidget(self, tabla):
        self.ui.tvResultado.clearContents()
        self.ui.tvResultado.setRowCount(0)
        for fila in tabla:
            row_position = self.ui.tvResultado.rowCount()
            self.ui.tvResultado.insertRow(row_position)

            for col, valor in enumerate(fila):
                item = QTableWidgetItem(valor)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.ui.tvResultado.setItem(row_position, col, item)

        self.ui.lb_contador_duplicados.setText(str(len(tabla)))
        total = format(len(tabla), ',d')
        total = total.replace(",", ".")
        self.ui.lb_contador_duplicados.setText(str(total))

#----------------------------------------------------------------------------------------
    def clickTabla(self, fila, columna):
        # Obtener los valores de la fila clicada
        valores_fila = []
        for col in range(self.ui.tvResultado.columnCount()):
            item = self.ui.tvResultado.item(fila, col)
            if item is not None:
                valores_fila.append(item.text())

        ruta_completa = os.path.normpath(os.path.join(valores_fila[1],valores_fila[0]))
        print("fichero: ", ruta_completa) 

        # Leer el contenido del archivo y mostrarlo en el QTextEdit
        # with open(ruta_completa, "r") as file:
        #     contenido = file.read()
        #     self.text_edit.setPlainText(contenido)  

        # # Utilizar subprocess para abrir el archivo con el programa predeterminado
        try:
            subprocess.run(["xdg-open", ruta_completa])  # Linux
        except FileNotFoundError:
            try:
                subprocess.run(["open", ruta_completa])  # macOS
            except FileNotFoundError:
                try:
                    subprocess.run(["start", "", ruta_completa], shell=True)  # Windows
                except FileNotFoundError:
                    print("No se pudo abrir el archivo. Asegúrate de que el comando 'xdg-open', 'open' o 'start' esté disponible en tu sistema.")
#----------------------------------------------------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
