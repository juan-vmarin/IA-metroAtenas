from util import resource_path
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(553, 322)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutWindow.sizePolicy().hasHeightForWidth())
        AboutWindow.setSizePolicy(sizePolicy)
        AboutWindow.setMinimumSize(QtCore.QSize(553, 322))
        AboutWindow.setMaximumSize(QtCore.QSize(553, 322))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        AboutWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(resource_path("image/1200px-Athens_Metro_Logo.svg.png")),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AboutWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.fondo = QtWidgets.QFrame(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 661, 381))
        self.fondo.setMaximumSize(QtCore.QSize(661, 16777215))
        self.fondo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo.setObjectName("fondo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.fondo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(48, 15, 452, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grupo = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(26)
        self.grupo.setFont(font)
        self.grupo.setTextFormat(QtCore.Qt.AutoText)
        self.grupo.setAlignment(QtCore.Qt.AlignCenter)
        self.grupo.setObjectName("grupo")
        self.verticalLayout.addWidget(self.grupo)
        self.aaron = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.aaron.setFont(font)
        self.aaron.setObjectName("aaron")
        self.verticalLayout.addWidget(self.aaron)
        self.sergio = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.sergio.setFont(font)
        self.sergio.setObjectName("sergio")
        self.verticalLayout.addWidget(self.sergio)
        self.daniel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.daniel.setFont(font)
        self.daniel.setObjectName("daniel")
        self.verticalLayout.addWidget(self.daniel)
        self.juan = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.juan.setFont(font)
        self.juan.setObjectName("juan")
        self.verticalLayout.addWidget(self.juan)
        self.xiao = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        self.xiao.setFont(font)
        self.xiao.setObjectName("xiao")
        self.verticalLayout.addWidget(self.xiao)
        AboutWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "Sobre nosotros"))
        self.grupo.setText(_translate("AboutWindow", "Grupo 57"))
        self.aaron.setText(_translate("AboutWindow", "Aarón Cabero Blanco"))
        self.sergio.setText(_translate("AboutWindow", "Sergio Sánchez-Carvajales Francoy"))
        self.daniel.setText(_translate("AboutWindow", "Daniel Tomás Sánchez"))
        self.juan.setText(_translate("AboutWindow", "Juan Diego Valencia Marín"))
        self.xiao.setText(_translate("AboutWindow", "Xiao Peng Ye"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())