from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QFormLayout,
    QSpacerItem,
    QSizePolicy,
    QComboBox,
    QFileDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QIntValidator


class EmployeeAddPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employee")

        # Enable drag-and-drop for the entire widget
        self.setAcceptDrops(True)

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Add a spacer at the top
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Header label in the center
        self.header_label = QLabel("Add Employee")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(self.header_label)

        # Add another spacer below the header
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Input fields with labels
        form_container = QVBoxLayout()
        form_container.setContentsMargins(180, 0, 180, 0)

        form_layout = QFormLayout()

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter name")
        form_layout.addRow(self.name_label, self.name_input)

        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter age")
        # allow only numbers
        self.age_input.setValidator(QIntValidator())
        form_layout.addRow(self.age_label, self.age_input)

        self.address_label = QLabel("Address:")
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter address")
        form_layout.addRow(self.address_label, self.address_input)

        self.position_label = QLabel("Position:")
        self.position_input = QLineEdit()
        self.position_input.setPlaceholderText("Enter position")
        form_layout.addRow(self.position_label, self.position_input)

        self.department_label = QLabel("Department:")
        self.department_input = QComboBox()
        form_layout.addRow(self.department_label, self.department_input)

        self.permission_label = QLabel("Permission ID:")
        self.permission_input = QComboBox()
        form_layout.addRow(self.permission_label, self.permission_input)

        self.image_label = QLabel("Profile Image:")

        # Image path input and button
        image_path_layout = QHBoxLayout()
        self.image_input = QLineEdit()
        self.image_input.setPlaceholderText("Enter image path or click 'Browse'")
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.open_file_explorer)
        image_path_layout.addWidget(self.image_input)
        image_path_layout.addWidget(self.browse_button)

    
        form_layout.addRow(self.image_label, image_path_layout)

        form_container.addLayout(form_layout)
        form_container.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(form_container)

        # Add another spacer below the form
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Buttons layout
        button_container = QHBoxLayout()
        button_container.setContentsMargins(200, 0, 200, 0)
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        button_container.addWidget(self.save_button)
        button_container.addWidget(self.cancel_button)
        main_layout.addLayout(button_container)

        # Add a spacer at the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Connect buttons to their respective methods
        self.save_button.clicked.connect(self.on_save_clicked)
        self.cancel_button.clicked.connect(lambda: self.presenter.open_list_view())

    def dragEnterEvent(self, event: QDragEnterEvent):
        """Accept drag events if the data contains image files."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        """Handle dropping an image file."""
        urls = event.mimeData().urls()
        if urls and urls[0].isLocalFile():
            file_path = urls[0].toLocalFile()
            self.set_image(file_path)

    def open_file_explorer(self, event):
        """Open file explorer to select an image."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Profile Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            self.image_input.setText(file_path)

    def set_image(self, file_path):
        """Display the selected or dropped image in the QLabel."""
        pixmap = QPixmap(file_path)
        self.image_input.setPixmap(pixmap.scaled(self.image_input.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def set_presenter(self, presenter):
        """Set the presenter for interaction."""
        self.presenter = presenter

    def on_save_clicked(self):
        """Save employee details."""
        name = self.name_input.text()
        age = self.age_input.text()
        address = self.address_input.text()
        position = self.position_input.text()
        dept = self.department_input.currentData().id
        permission = self.permission_input.currentData().id
        file_path = self.image_input.text()
        # Include logic to save the image file path if needed
        self.presenter.add_employee(name, age, address, position, dept, permission, file_path)
