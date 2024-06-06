from PySide6.QtCore import Qt, QPropertyAnimation, QRect
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QGridLayout, QFrame, QPushButton, QScrollArea, \
    QLineEdit, QCompleter
from PySide6.scripts.metaobjectdump import Signal


class CustomListItem(QWidget):
    def __init__(self,id , name, length, labels):
        super().__init__()
        self.layout = QVBoxLayout()

        # Create a QHBoxLayout for the name and length
        upper_layout = QHBoxLayout()
        upper_layout.addWidget(QLabel(str(id)))
        upper_layout.addWidget(QLabel(name))
        upper_layout.addWidget(QLabel(str(length)))


        # Add the QHBoxLayout to the main layout
        self.layout.addLayout(upper_layout)

        # Create a QGridLayout for the labels
        self.label_layout = QGridLayout()
        cols = 3
        for num, label in enumerate(labels):
            self.label_layout.addWidget(QLabel(label), num // cols, num % cols)

        # Add horizonatal line to the main layout

        self.layout.addLayout(self.label_layout)
        # add a button to hide and show the labels

        self.toggle_labels_button = QPushButton("\u2193")

        self.toggle_labels_button.setStyleSheet("background-color: #333; color: white; border: 1px solid gray; padding: 5px; border-radius: 5px;"
                                                'hover {background-color: #444;}')

        self.toggle_labels_button.setFixedWidth(20)
        self.toggle_labels_button.setFixedHeight(20)

        self.toggle_labels_button.clicked.connect(self.toggle_labels)
        expand_button_layout = QHBoxLayout()
        expand_button_layout.addWidget(self.toggle_labels_button)
        upper_layout.addLayout(expand_button_layout)
        # expand_button_layout.addStretch(1)
        self.setLayout(self.layout)
        self.hide_labels()
        # style the widget
        self.setStyleSheet("border: 0px solid white;"
                            "radius: 5px;"
                            "padding: 5px;"
                            "margin: 0px;" 
                            "color: white; background-color: #333;")
        # animate the lable show and hide action
        # different ways to style the widget

    def toggle_labels(self):
        # Hide or show the labels
        if self.toggle_labels_button.text() == "\u2193":
            self.show_labels()
        else:
            self.hide_labels()
    def hide_labels(self):
        for i in range(self.label_layout.count()):
            widget = self.label_layout.itemAt(i).widget()
            widget.setVisible(False)
        self.toggle_labels_button.setText("\u2193")

    def show_labels(self):
        for i in range(self.label_layout.count()):
            widget = self.label_layout.itemAt(i).widget()
            widget.setVisible(True)
        self.toggle_labels_button.setText("\u2191")
class DataListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # Create a QScrollArea
        self.scroll_area = QScrollArea(self)
        # Enable vertical scrollbar
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # Set widget resizable
        self.scroll_area.setWidgetResizable(True)

        # Create a QWidget for the scroll area content
        self.scroll_content = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_content.setStyleSheet("background-color: #333;"
                                          "border: 0px solid white;"
                                          "radius: 5px;"
                                          "padding: 0px;"
                                          "margin: 0px;"
                                          "color: white; background-color: #333;")
        # Create a QVBoxLayout for the scroll area content
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        # Add the scroll area to the main layout
        upper_layout = QHBoxLayout()
        upper_layout.addWidget(QLabel('Id'))
        upper_layout.addWidget(QLabel("Name"))
        upper_layout.addWidget(QLabel("Length"))
        self.layout.addLayout(upper_layout)
        self.layout.addWidget(self.scroll_area)


    def insertItem(self, item_id,  name, length, labels):
        item = CustomListItem(item_id, name, length, labels)
        self.scroll_layout.addWidget(item)
        # self.list_layout.addWidget(item)

class FilterWidget(QWidget):
    # filter_sig = Signal(str)
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        # Textinput for filtering
        self.filter_input = QLineEdit()
        self.filter_button = QPushButton("Filter")
        # add suggestions to the input
        self.filter_input.setPlaceholderText("Filter by label")
        # add suggestions to the input as dropdown

        self.layout.addWidget(self.filter_button)
        self.layout.addWidget(self.filter_input)
        self.setLayout(self.layout)
        self.filter_button.clicked.connect(self.filter_data)
    def filter_data(self):
        pass

    def set_filter_completer(self, completion_list):
        completer = QCompleter(completion_list)
        self.filter_input.setCompleter(completer)
class DatasetWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.item_list = []
        self.label_list = []
        self.layout = QVBoxLayout(self)
        self.filter_widget = FilterWidget()
        self.list_widget = DataListWidget()
        self.layout.addWidget(self.filter_widget)
        self.layout.addWidget(self.list_widget)

        self.setLayout(self.layout)

    def insertItem(self, item_id, name, length, labels):
        self.list_widget.insertItem(item_id, name, length, labels)
        for label in labels:
            if label not in self.label_list:
                self.label_list.append(label)
    def update_filter_completer(self):
        self.filter_widget.set_filter_completer(self.label_list)
    def update_list_widget(self, item_list):
        for args in item_list:
            self.list_widget.insertItem(*args)