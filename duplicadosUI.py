# Form implementation generated from reading ui file 'duplicados.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 589)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(172, 197, 224);\n"
"} \n"
"\n"
"QLabel {\n"
"    background-color: rgb(220, 220, 220);\n"
"}\n"
"\n"
" QLineEdit1 {\n"
"     border: 2px solid gray;\n"
"     border-radius: 10px;\n"
"     padding: 0 8px;\n"
"    background-color: darkgray;\n"
" }")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("font: 12pt \"Segoe UI\";\n"
"background-color: rgb(88, 179, 152);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_superior = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_superior.setAutoFillBackground(False)
        self.frame_superior.setStyleSheet("font: 12pt \"Verdana\";")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_superior.setLineWidth(3)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.frame_superior)
        self.frame.setMaximumSize(QtCore.QSize(200, 80))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnSeleccionar = QtWidgets.QPushButton(parent=self.frame)
        self.btnSeleccionar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnSeleccionar.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.btnSeleccionar.setObjectName("btnSeleccionar")
        self.verticalLayout_2.addWidget(self.btnSeleccionar)
        self.btnBuscarDuplicados = QtWidgets.QPushButton(parent=self.frame)
        self.btnBuscarDuplicados.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnBuscarDuplicados.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.btnBuscarDuplicados.setObjectName("btnBuscarDuplicados")
        self.verticalLayout_2.addWidget(self.btnBuscarDuplicados)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_superior)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.directorioActual = QtWidgets.QLineEdit(parent=self.frame_2)
        self.directorioActual.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-radius: 10px;")
        self.directorioActual.setText("")
        self.directorioActual.setObjectName("directorioActual")
        self.verticalLayout_3.addWidget(self.directorioActual)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lb_contador_archivos = QtWidgets.QLabel(parent=self.frame_3)
        self.lb_contador_archivos.setGeometry(QtCore.QRect(60, 10, 100, 21))
        self.lb_contador_archivos.setMinimumSize(QtCore.QSize(0, 20))
        self.lb_contador_archivos.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.lb_contador_archivos.setFont(font)
        self.lb_contador_archivos.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lb_contador_archivos.setAutoFillBackground(False)
        self.lb_contador_archivos.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"")
        self.lb_contador_archivos.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lb_contador_archivos.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_contador_archivos.setWordWrap(False)
        self.lb_contador_archivos.setObjectName("lb_contador_archivos")
        self.lb_contador_duplicados = QtWidgets.QLabel(parent=self.frame_3)
        self.lb_contador_duplicados.setGeometry(QtCore.QRect(290, 10, 100, 20))
        self.lb_contador_duplicados.setMinimumSize(QtCore.QSize(0, 20))
        self.lb_contador_duplicados.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.lb_contador_duplicados.setFont(font)
        self.lb_contador_duplicados.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lb_contador_duplicados.setAutoFillBackground(False)
        self.lb_contador_duplicados.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"")
        self.lb_contador_duplicados.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.lb_contador_duplicados.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_contador_duplicados.setWordWrap(False)
        self.lb_contador_duplicados.setObjectName("lb_contador_duplicados")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 10, 56, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 90, 21))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_superior)
        self.frame_abajo = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_abajo.setStyleSheet("background-color: rgb(245, 207, 147);")
        self.frame_abajo.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_abajo.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_abajo.setObjectName("frame_abajo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_abajo)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tvResultado = QtWidgets.QTableWidget(parent=self.frame_abajo)
        self.tvResultado.setMinimumSize(QtCore.QSize(800, 0))
        self.tvResultado.setBaseSize(QtCore.QSize(2, 4))
        self.tvResultado.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tvResultado.setAutoFillBackground(False)
        self.tvResultado.setStyleSheet("QWitget {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section { \n"
"    background-color: #aaaa7f;\n"
"    padding: 2px;\n"
"    border: 1px solid #000000;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableWitget {\n"
"    gridline-color: #ff00ff;\n"
"    font-size: 12pt;\n"
"}")
        self.tvResultado.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tvResultado.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.tvResultado.setLineWidth(1)
        self.tvResultado.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.tvResultado.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked)
        self.tvResultado.setGridStyle(QtCore.Qt.PenStyle.DashLine)
        self.tvResultado.setObjectName("tvResultado")
        self.tvResultado.setColumnCount(3)
        self.tvResultado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tvResultado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tvResultado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tvResultado.setHorizontalHeaderItem(2, item)
        self.tvResultado.horizontalHeader().setVisible(True)
        self.tvResultado.horizontalHeader().setCascadingSectionResizes(False)
        self.tvResultado.horizontalHeader().setSortIndicatorShown(True)
        self.tvResultado.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tvResultado)
        self.verticalLayout.addWidget(self.frame_abajo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Buscar Duplicados"))
        self.btnSeleccionar.setToolTip(_translate("MainWindow", "<html><head/><body><p>ToolTip de pulsar boton</p></body></html>"))
        self.btnSeleccionar.setText(_translate("MainWindow", "Directorio"))
        self.btnBuscarDuplicados.setToolTip(_translate("MainWindow", "<html><head/><body><p>ToolTip de pulsar boton</p></body></html>"))
        self.btnBuscarDuplicados.setText(_translate("MainWindow", "Buscar Duplicados"))
        self.lb_contador_archivos.setText(_translate("MainWindow", "0"))
        self.lb_contador_duplicados.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Leídos"))
        self.label_2.setText(_translate("MainWindow", "Duplicados"))
        item = self.tvResultado.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "FICHERO"))
        item = self.tvResultado.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DIRECTORIO"))
        item = self.tvResultado.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "HASH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())