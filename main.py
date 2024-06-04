# Basic Pyside Main Window

import sys
from random import random, randint

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QFrame, \
    QScrollArea

from widget.bar_chart import BarChart
import os
import sys

from widget.custom_list_widget import DataListWidget, DatasetWidget

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_yml = os.path.abspath(os.path.join(bundle_dir, 'config.yml'))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 800, 600)
        self.lightgrid_info_chart_1 = BarChart(title_str="Lightgrid Status", labels=["F", "O", "D", "U"], bar_names=["Free", "Occupied", "Defect", "Unavailable"])
        self.lightgrid_info_chart_1.setFixedWidth(200)
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        lightgrid_info_chart_2 = BarChart(title_str="Lightgrid Status", labels=["F", "O", "D", "U"], bar_names=["Free", "Occupied", "Defect", "Unavailable"])
        lightgrid_info_chart_2.setFixedWidth(200)
        lightgrid_info_chart_3 = BarChart(title_str="Lightgrid Status", labels=["F", "O", "D", "U"], bar_names=["Free", "Occupied", "Defect", "Unavailable"])
        lightgrid_info_chart_3.setFixedWidth(200)
        # set stylesheed id
        self.lightgrid_info_chart_1.setObjectName("BarChartLightgrids")
        lightgrid_info_chart_2.setObjectName("BarChartLightgrids")
        lightgrid_info_chart_3.setObjectName("BarChartLightgrids")
        button = QPushButton("Click me")
        button.clicked.connect(self.toggle_data)
        left_layout = QVBoxLayout()
        empty_placeholder = QWidget()
        empty_placeholder.setFixedWidth(600)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        vlayout.addWidget(self.lightgrid_info_chart_1)
        vlayout.addWidget(hline)
        vlayout.addWidget(lightgrid_info_chart_2)
        vlayout.addWidget(hline)
        vlayout.addWidget(lightgrid_info_chart_3)
        left_layout.addWidget(empty_placeholder)
        left_layout.addWidget(button)
        list_widget = DatasetWidget()
        # list_widget.setObjectName(f"DataListItem")
        list_widget.insertItem(0, "name", 50,["Label 1", "Label 2", "Label 3", "Label 2_1", "Label 2_2"])
        list_widget.insertItem(1, "name2", 150, ["Label 4", "Label 5", "Label 6"])
        list_widget.insertItem(2, "name3", 250, ["Label 7", "Label 8", "Label 9"])
        list_widget.insertItem(3, "name", 50,["Label 1", "Label 2", "Label 3", "Label 2_1", "Label 2_2"])
        list_widget.insertItem(4, "name2", 150, ["Label 4", "Label 5", "Label 6"])
        list_widget.insertItem(5, "name3", 250, ["Label 7", "Label 8", "Label 9"])
        list_widget.insertItem(6, "name", 50,["Label 1", "Label 2", "Label 3", "Label 2_1", "Label 2_2"])
        list_widget.insertItem(7, "name2", 150, ["Label 4", "Label 5", "Label 6"])
        list_widget.insertItem(8, "name3", 250, ["Label 7", "Label 8", "Label 9"])
        list_widget.insertItem(9, "name", 50, ["Label 1", "Label 2", "Label 3", "Label 2_1", "Label 2_2"])
        list_widget.insertItem(10, "name2", 150, ["Label 4", "Label 5", "Label 6"])
        list_widget.insertItem(11, "name3", 250, ["Label 7", "Label 8", "Label 9"])
        list_widget.insertItem(12, "name", 50, ["Label 1", "Label 2", "Label 3", "Label 2_1", "Label 2_2"])
        list_widget.insertItem(13, "name2", 150, ["Label 4", "Label 5", "Label 6"])
        list_widget.insertItem(14, "name3", 250, ["Label 7", "Label 8", "Label 9"])
        list_widget.update_filter_completer()
        hlayout.addLayout(left_layout)
        hlayout.addWidget(list_widget)

        hlayout.addLayout(vlayout)
        widget = QWidget()
        widget.setLayout(hlayout)
        # add stylesheet from file

        # self.setStyleSheet(open("resources/stylesheet.qss", "r").read())
        self.setCentralWidget(widget)
    def toggle_data(self):
        self.lightgrid_info_chart_1.set_data({
            "F": randint(0, 100),
            "O": randint(0, 100),
            "D": randint(0, 100),
            "U": randint(0, 100)
        })
        print("Button clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

# Run the script
# You should see a window with the title "My App" and dimensions 800x600.
# The window should be positioned at 100, 100 on your screen.
# Press the red "X" button to close the window and exit the application.
