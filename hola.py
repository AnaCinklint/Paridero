from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QSlider, QStackedWidget, QFrame
)
from PyQt6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def init(self):
        super().init()
        self.setWindowTitle("Interfaz de Control")
        self.setGeometry(100, 100, 600, 400)
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        self.main_screen = QWidget()
        self.main_layout = QVBoxLayout()
        
        self.encender_button = QPushButton("Encender")
        self.encender_button.clicked.connect(self.go_to_control_screen)
        self.apagar_button = QPushButton("Apagar")
        self.apagar_button.clicked.connect(self.close)
        
        self.main_layout.addWidget(self.encender_button)
        self.main_layout.addWidget(self.apagar_button)
        self.main_screen.setLayout(self.main_layout)
        
        self.control_screen = QWidget()
        self.control_layout = QVBoxLayout()
        
        self.focos_frame = QFrame()
        self.focos_frame.setFrameShape(QFrame.Shape.Box)
        self.focos_frame.setFixedHeight(80)
        self.control_layout.addWidget(self.focos_frame)
        
        self.foco_layout = QHBoxLayout()
        
        self.foco1 = QLabel("Foco 1")
        self.foco2 = QLabel("Foco 2")
        self.foco_layout.addWidget(self.foco1)
        self.foco_layout.addWidget(self.foco2)
        
        self.control_layout.addLayout(self.foco_layout)
        
        self.temperatura_label = QLabel("Temperatura:")
        self.temperatura_slider = QSlider(Qt.Orientation.Horizontal)
        self.temperatura_slider.setRange(0, 100)
        self.temperatura_slider.valueChanged.connect(self.update_temperature_display)
        
        self.temperature_display = QLabel("0Â°C")
        self.temperature_display.setFrameShape(QFrame.Shape.Box)
        self.temperature_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_display.setFixedSize(60, 30)
        
        self.temp_layout = QHBoxLayout()
        self.temp_layout.addWidget(self.temperatura_label)
        self.temp_layout.addWidget(self.temperatura_slider)
        self.temp_layout.addWidget(self.temperature_display)
        
        self.control_layout.addLayout(self.temp_layout)
        
        self.imagenes_layout = QHBoxLayout()
        
        self.imagen1_frame = QFrame()
        self.imagen1_frame.setFrameShape(QFrame.Shape.Box)
        self.imagen1_frame.setFixedSize(100, 100)
        
        self.imagen2_frame = QFrame()
        self.imagen2_frame.setFrameShape(QFrame.Shape.Box)
        self.imagen2_frame.setFixedSize(100, 100)
        
        self.imagenes_layout.addWidget(self.imagen1_frame)
        self.imagenes_layout.addWidget(self.imagen2_frame)
        
        self.control_layout.addLayout(self.imagenes_layout)
        self.control_screen.setLayout(self.control_layout)
        
        self.stack.addWidget(self.main_screen)
        self.stack.addWidget(self.control_screen)
    
    def go_to_control_screen(self):
        self.stack.setCurrentWidget(self.control_screen)
    
    def update_temperature_display(self, value):
        self.temperature_display.setText(f"{value}Â°C")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
