# Basic Pyside Main Window

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QFrame

from widget.bar_chart import BarChart


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 800, 600)
        lightgrid_info_chart_1 = BarChart(title_str="Lightgrid Status", labels=["F", "O", "D", "U"], bar_names=["Free", "Occupied", "Defect", "Unavailable"])
        lightgrid_info_chart_1.setFixedWidth(200)
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        lightgrid_info_chart_2 = BarChart(title_str="Lightgrid Status", labels=["F", "O", "D", "U"], bar_names=["Free", "Occupied", "Defect", "Unavailable"])
        lightgrid_info_chart_2.setFixedWidth(200)
        lightgrid_info_chart_3 = BarChart(title_str="Lightgrid Status", labels=["F", "O", "D", "U"], bar_names=["Free", "Occupied", "Defect", "Unavailable"])
        lightgrid_info_chart_3.setFixedWidth(200)
        # set stylesheed id
        lightgrid_info_chart_1.setObjectName("BarChartLightgrids")
        lightgrid_info_chart_2.setObjectName("BarChartLightgrids")
        lightgrid_info_chart_3.setObjectName("BarChartLightgrids")
        button = QPushButton("Click me")
        left_layout = QVBoxLayout()
        empty_placeholder = QWidget()
        empty_placeholder.setFixedWidth(600)
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        vlayout.addWidget(lightgrid_info_chart_1)
        vlayout.addWidget(hline)
        vlayout.addWidget(lightgrid_info_chart_2)
        vlayout.addWidget(hline)
        vlayout.addWidget(lightgrid_info_chart_3)
        left_layout.addWidget(empty_placeholder)
        left_layout.addWidget(button)
        hlayout.addLayout(left_layout)
        hlayout.addLayout(vlayout)
        widget = QWidget()
        widget.setLayout(hlayout)
        # add stylesheet from file

        self.setStyleSheet(open("resource/stylesheet.qss", "r").read())
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

# Run the script
# You should see a window with the title "My App" and dimensions 800x600.
# The window should be positioned at 100, 100 on your screen.
# Press the red "X" button to close the window and exit the application.
