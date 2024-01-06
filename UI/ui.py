# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mark.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slice_controller = QtWidgets.QGroupBox(self.centralwidget)
        self.slice_controller.setGeometry(QtCore.QRect(50, 630, 331, 141))
        self.slice_controller.setTitle("")
        self.slice_controller.setObjectName("slice_controller")
        self.z_plus_1 = QtWidgets.QPushButton(self.slice_controller)
        self.z_plus_1.setGeometry(QtCore.QRect(280, 100, 41, 30))
        self.z_plus_1.setObjectName("z_plus_1")
        self.z_slice_slider = QtWidgets.QSlider(self.slice_controller)
        self.z_slice_slider.setGeometry(QtCore.QRect(60, 100, 211, 30))
        self.z_slice_slider.setOrientation(QtCore.Qt.Horizontal)
        self.z_slice_slider.setObjectName("z_slice_slider")
        self.x_minus_1 = QtWidgets.QPushButton(self.slice_controller)
        self.x_minus_1.setGeometry(QtCore.QRect(10, 20, 41, 30))
        self.x_minus_1.setObjectName("x_minus_1")
        self.y_minus_1 = QtWidgets.QPushButton(self.slice_controller)
        self.y_minus_1.setGeometry(QtCore.QRect(10, 60, 41, 30))
        self.y_minus_1.setObjectName("y_minus_1")
        self.z_minus_1 = QtWidgets.QPushButton(self.slice_controller)
        self.z_minus_1.setGeometry(QtCore.QRect(10, 100, 41, 30))
        self.z_minus_1.setObjectName("z_minus_1")
        self.y_plus_1 = QtWidgets.QPushButton(self.slice_controller)
        self.y_plus_1.setGeometry(QtCore.QRect(280, 60, 41, 30))
        self.y_plus_1.setObjectName("y_plus_1")
        self.x_slice_slider = QtWidgets.QSlider(self.slice_controller)
        self.x_slice_slider.setGeometry(QtCore.QRect(60, 20, 211, 30))
        self.x_slice_slider.setOrientation(QtCore.Qt.Horizontal)
        self.x_slice_slider.setObjectName("x_slice_slider")
        self.y_slice_slider = QtWidgets.QSlider(self.slice_controller)
        self.y_slice_slider.setGeometry(QtCore.QRect(60, 60, 211, 30))
        self.y_slice_slider.setOrientation(QtCore.Qt.Horizontal)
        self.y_slice_slider.setObjectName("y_slice_slider")
        self.x_plus_1 = QtWidgets.QPushButton(self.slice_controller)
        self.x_plus_1.setGeometry(QtCore.QRect(280, 20, 41, 30))
        self.x_plus_1.setObjectName("x_plus_1")
        self.main_view = QtWidgets.QGroupBox(self.centralwidget)
        self.main_view.setGeometry(QtCore.QRect(30, 50, 571, 581))
        self.main_view.setObjectName("main_view")
        self.y_view = QtWidgets.QGraphicsView(self.main_view)
        self.y_view.setGeometry(QtCore.QRect(290, 20, 250, 300))
        self.y_view.setObjectName("y_view")
        self.z_view = QtWidgets.QGraphicsView(self.main_view)
        self.z_view.setGeometry(QtCore.QRect(290, 330, 250, 250))
        self.z_view.setObjectName("z_view")
        self.x_view = QtWidgets.QGraphicsView(self.main_view)
        self.x_view.setGeometry(QtCore.QRect(21, 20, 250, 300))
        self.x_view.setObjectName("x_view")
        self.main_view_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.main_view_2.setGeometry(QtCore.QRect(620, 50, 681, 231))
        self.main_view_2.setObjectName("main_view_2")
        self.y_view_focus = QtWidgets.QGraphicsView(self.main_view_2)
        self.y_view_focus.setGeometry(QtCore.QRect(240, 20, 200, 200))
        self.y_view_focus.setObjectName("y_view_focus")
        self.z_view_focus = QtWidgets.QGraphicsView(self.main_view_2)
        self.z_view_focus.setGeometry(QtCore.QRect(460, 20, 200, 200))
        self.z_view_focus.setObjectName("z_view_focus")
        self.x_view_focus = QtWidgets.QGraphicsView(self.main_view_2)
        self.x_view_focus.setGeometry(QtCore.QRect(20, 20, 200, 200))
        self.x_view_focus.setObjectName("x_view_focus")
        self.record_coord = QtWidgets.QPushButton(self.centralwidget)
        self.record_coord.setGeometry(QtCore.QRect(480, 640, 93, 28))
        self.record_coord.setObjectName("record_coord")
        self.select_folder = QtWidgets.QPushButton(self.centralwidget)
        self.select_folder.setGeometry(QtCore.QRect(30, 10, 93, 28))
        self.select_folder.setObjectName("select_folder")
        self.save_to_csv = QtWidgets.QPushButton(self.centralwidget)
        self.save_to_csv.setGeometry(QtCore.QRect(130, 10, 93, 28))
        self.save_to_csv.setObjectName("save_to_csv")
        self.coord_list = QtWidgets.QListWidget(self.centralwidget)
        self.coord_list.setGeometry(QtCore.QRect(620, 290, 256, 341))
        self.coord_list.setObjectName("coord_list")
        self.file_list = QtWidgets.QListWidget(self.centralwidget)
        self.file_list.setGeometry(QtCore.QRect(900, 290, 256, 341))
        self.file_list.setObjectName("file_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.z_plus_1.setText(_translate("MainWindow", ">"))
        self.x_minus_1.setText(_translate("MainWindow", "<"))
        self.y_minus_1.setText(_translate("MainWindow", "<"))
        self.z_minus_1.setText(_translate("MainWindow", "<"))
        self.y_plus_1.setText(_translate("MainWindow", ">"))
        self.x_plus_1.setText(_translate("MainWindow", ">"))
        self.main_view.setTitle(_translate("MainWindow", "View"))
        self.main_view_2.setTitle(_translate("MainWindow", "Focus View"))
        self.record_coord.setText(_translate("MainWindow", "Record Coord"))
        self.select_folder.setText(_translate("MainWindow", "Select Folder"))
        self.save_to_csv.setText(_translate("MainWindow", "Save to CSV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
