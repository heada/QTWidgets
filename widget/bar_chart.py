from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGraphicsDropShadowEffect


# Create a custom widget that displays a bar chart
# The bar chart is drawn using QPainter

class BarChart(QWidget):
    def __init__(self, title_str, labels, bar_names, object_name="BarChartLightgrids"):
        super().__init__()
        # set mouse move event
        self.title_str = title_str
        self.labels = labels
        self.bar_names = bar_names
        self.object_name = object_name
        # Create a layout
        self.init_data()
        self.init_layout()
        self.set_behavior()


    def init_data(self):
        self.data = {
            label: int(100/len(self.labels))
            for label in self.labels
        }
        self.set_data(self.data)
    def init_layout(self):
        layout = QVBoxLayout()
        # add a Title
        self.title = QLabel(self.title_str)
        layout.setObjectName("BarChartLightgrids")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.width()
        layout.addStretch(0)
        layout.addWidget(self. title)
        self.bars = Bars(width=100, bar_names=self.bar_names)
        self.bars.set_data(self.data)
        layout.addWidget(self.bars)
        self.setLayout(layout)

    def set_behavior(self):
        self.setToolTipDuration(100)


    def set_data(self, data):
        self.data = data

        self.update()
    def setObjectName(self, name):
        super().setObjectName(name)
        self.title.setObjectName(name)
        self.bars.setObjectName(name)
        self.update()
class Bars(QWidget):

    def __init__(self, width, bar_names):
        super().__init__()

        # Create a layout
        layout = QVBoxLayout()
        self.setMinimumWidth(width)
        self.setMinimumHeight(100)
        # add a Title
        self.setMouseTracking(True)
        self.bar_names = bar_names

        # Set the layout
        self.setLayout(layout)
    def set_data(self, data):
        self.data = data
        # sum of all values
        self.total = sum(data.values())
        self.update()
    def paintEvent(self, event):

        # draw the bar chart with the data provided, the data is a dictionary with the key as the label and the value as the height of the bar
        # the height of the bar is calculated as the value divided by the total sum of all values the display value is the percentage of the value
        # add spacing between the bars
        # labes are displayed underneat the bars and centered
        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)
        # defin bar colors as a list of colors
        # generate 4 meaningfulness colors to represent the bars Free, occuopied defect and blocked
        pastel_colors = [
            QColor(51, 160, 44),
            QColor(31, 120, 180),
            QColor(168, 86, 97),
            QColor(138, 138, 138),
        ]
        bar_width = self.width() / len(self.data)
        spacing = 10
        for i, (label, value) in enumerate(self.data.items()):
            painter.setPen(Qt.NoPen)
            painter.setBrush(pastel_colors[i % len(pastel_colors)])
            bar_height = value / self.total * self.height()
            painter.drawRoundedRect(i * bar_width+spacing, self.height() - bar_height, bar_width- spacing, bar_height, 2, 2)
            # draw the label withing the center bar of the bar
            painter.setPen(Qt.white)
            painter.drawText(i * bar_width, self.height(), bar_width + 10, -20, Qt.AlignCenter, f"{label}")

        painter.end()
    def mouseMoveEvent(self, event):
        # show the lable if the mouse is over the bar
        # get the bar index
        bar_index = int(event.pos().x() // (self.width() / len(self.data)))
        # get the label
        label = list(self.bar_names)[bar_index]
        # get the value
        value = list(self.data.values())[bar_index]
        # set the tool tip
        self.setToolTip(f"{label}: {value}")

        # update the widget
        self.update()

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    chart = BarChart(title="Lightgrid Status", labels=["F", "O", "D", "B"], bar_names=["Free", "Occupied", "Defect", "Unavailable"])
    chart.set_data({
        "F": 100,
        "O": 0,
        "D": 0,
        "U": 0,
    })
    chart.show()
    sys.exit(app.exec())
    # Usage
