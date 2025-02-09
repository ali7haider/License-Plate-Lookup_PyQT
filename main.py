from main_ui import Ui_MainWindow  # Import the generated UI class
import sys
import requests

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
)

# State dictionary
STATES = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

class LicensePlate(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LicensePlate, self).__init__()
        self.setupUi(self)  # Initialize UI

        # List of buttons for navigation
        self.nav_buttons = [
            self.btnLicensePlate,
            self.btnBlank1,
            self.btnBlank2,
            self.btnBlank3
        ]

        # Set default underlined button
        self.set_active_button(self.btnLicensePlate)

        # Connect buttons to respective functions
        self.state_dropdown.addItems(sorted(STATES.keys()))  
        self.search_button.clicked.connect(self.fetch_plate_info)
        self.btnLicensePlate.clicked.connect(lambda: self.change_page(0, self.btnLicensePlate))
        self.btnBlank1.clicked.connect(lambda: self.change_page(1, self.btnBlank1))
        self.btnBlank2.clicked.connect(lambda: self.change_page(2, self.btnBlank2))
        self.btnBlank3.clicked.connect(lambda: self.change_page(3, self.btnBlank3))

    def change_page(self, index, clicked_button):
        """Change the stacked widget page and update active button styling."""
        self.stackedWidget.setCurrentIndex(index)
        self.set_active_button(clicked_button)

    def set_active_button(self, active_button):
        """Apply underline to the active button and remove from others."""
        for button in self.nav_buttons:
            button.setStyleSheet("color:black;")  # Remove underline
        
        # Set underline for the active button
        active_button.setStyleSheet("color:#1159A8")  # Apply underline

   

    def fetch_plate_info(self):
        """Fetch license plate details from API."""
        plate = self.plate_entry.text().upper()  # Get plate number
        state = self.state_dropdown.currentText()  # Get selected state
        
        if not plate or not state:
            QMessageBox.warning(self, "Input Error", "Please enter a plate number and select a state.")
            return
        
        api_url = f"https://api.licenselookup.org/license-plate-search?plate={plate}&state={state}&format=json&request_type=web&access_token=5b13d1c13f8a04d0ffe80b725866843f"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            if "content" not in data:
                QMessageBox.critical(self, "Invalid Plate", "The entered plate is not valid or not found.")
                return

            self.update_results(data["content"])  # Update UI with results
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {str(e)}")

    def update_results(self, data):
        """Update UI with fetched results in vinTable, skipping empty values."""
        self.result_listbox.clear()  # Clear previous results
        self.vinTable.setRowCount(0)  # Clear previous table entries

        details = ["Make", "Model", "Year", "Plate", "State", "Country", "VIN"]
        text_content = []  # Store text for plainTextEdit

        # Populate result_listbox with key details
        for key in details:
            value = data.get(key.lower(), "").strip()
            if value:  # Avoid inserting empty values
                entry = f"{key}: {value}"
                self.result_listbox.addItem(entry)
                text_content.append(entry)
        print(f"Result Listbox Height: {self.result_listbox.height()}")

        # self.textEdit.setPlainText("\n".join(text_content))  # Convert list to string
    # Set text in plainTextEdit
        # Adjust listbox size based on entries
        # self.resize_listbox()

        # Populate vinTable with VIN data (Skipping empty values)
        vin_data = data.get("vin_data", {})
        filtered_vin_data = {key: value for key, value in vin_data.items() if value.strip()}  # Remove empty values

        self.vinTable.setRowCount(len(filtered_vin_data))  # Set row count based on non-empty vin_data
        self.vinTable.setColumnCount(2)  # Ensure at least 2 columns exist
        self.vinTable.setHorizontalHeaderLabels(["Key", "Value"])  # Set column headers

        for row, (key, value) in enumerate(filtered_vin_data.items()):
            self.vinTable.setItem(row, 0, QTableWidgetItem(key))
            self.vinTable.setItem(row, 1, QTableWidgetItem(value))

        # Auto-resize columns for better visibility
        self.vinTable.resizeColumnsToContents()
        self.vinTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Adjust column widths

    def resize_listbox(self):
        """Dynamically resize the list box based on the number of items."""
        item_count = self.result_listbox.count()
        item_height = 20  # Approximate height per item
        max_height = 200  # Set a maximum height

        new_height = min(item_count * item_height, max_height)
        self.result_listbox.setFixedHeight(new_height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LicensePlate()
    window.show()
    sys.exit(app.exec_())
