import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QListWidget, QFileDialog, QGraphicsView, QGraphicsScene
)
from PyQt5.QtGui import QIcon

class VTTMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Tabletop")
        self.setGeometry(100, 100, 1000, 700)
        self.init_ui()

    def init_ui(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QHBoxLayout()
        sidebar_layout = QVBoxLayout()
        map_layout = QVBoxLayout()

        # Sidebar: Character list and buttons
        self.char_list = QListWidget()
        add_char_btn = QPushButton("Add Character")
        add_char_btn.clicked.connect(self.add_character)

        sidebar_layout.addWidget(QLabel("Characters"))
        sidebar_layout.addWidget(self.char_list)
        sidebar_layout.addWidget(add_char_btn)
        sidebar_layout.addStretch()

        # Map area: Placeholder using QGraphicsView
        self.scene = QGraphicsScene()
        self.map_view = QGraphicsView(self.scene)
        self.map_view.setMinimumSize(600, 600)
        map_layout.addWidget(QLabel("Map Area"))
        map_layout.addWidget(self.map_view)

        # Combine layouts
        main_layout.addLayout(sidebar_layout, 1)
        main_layout.addLayout(map_layout, 3)
        central_widget.setLayout(main_layout)

    def add_character(self):
        # Simple placeholder for adding a character
        self.char_list.addItem("New Character")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VTTMainWindow()
    window.show()
    sys.exit(app.exec_())