# Form implementation generated from reading ui file 'plot_complex.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PlotComplex(object):
    def setupUi(self, PlotComplex):
        PlotComplex.setObjectName("PlotComplex")
        PlotComplex.resize(640, 480)
        self.widget = MPLWidget(parent=PlotComplex)
        self.widget.setGeometry(QtCore.QRect(110, 40, 511, 401))
        self.widget.setObjectName("widget")
        self.pushButtonSaveComplex = QtWidgets.QPushButton(parent=PlotComplex)
        self.pushButtonSaveComplex.setGeometry(QtCore.QRect(300, 450, 131, 21))
        self.pushButtonSaveComplex.setObjectName("pushButtonSaveComplex")
        self.listWidgetComplex = QtWidgets.QListWidget(parent=PlotComplex)
        self.listWidgetComplex.setGeometry(QtCore.QRect(10, 10, 91, 461))
        self.listWidgetComplex.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.listWidgetComplex.setObjectName("listWidgetComplex")
        self.pushButtonPlotComplex = QtWidgets.QPushButton(parent=PlotComplex)
        self.pushButtonPlotComplex.setGeometry(QtCore.QRect(440, 10, 80, 23))
        self.pushButtonPlotComplex.setObjectName("pushButtonPlotComplex")
        self.pushButtonPlotComplexStoi = QtWidgets.QPushButton(parent=PlotComplex)
        self.pushButtonPlotComplexStoi.setGeometry(QtCore.QRect(190, 10, 151, 23))
        self.pushButtonPlotComplexStoi.setObjectName("pushButtonPlotComplexStoi")

        self.retranslateUi(PlotComplex)
        QtCore.QMetaObject.connectSlotsByName(PlotComplex)

    def retranslateUi(self, PlotComplex):
        _translate = QtCore.QCoreApplication.translate
        PlotComplex.setWindowTitle(_translate("PlotComplex", "Plot Complex"))
        self.pushButtonSaveComplex.setText(_translate("PlotComplex", "Save to CSV"))
        self.pushButtonPlotComplex.setText(_translate("PlotComplex", "Plot"))
        self.pushButtonPlotComplexStoi.setText(_translate("PlotComplex", "Stoichiometry"))
from .mplwidget import MPLWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotComplex = QtWidgets.QWidget()
    ui = Ui_PlotComplex()
    ui.setupUi(PlotComplex)
    PlotComplex.show()
    sys.exit(app.exec())
