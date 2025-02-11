from main_ui import Ui_MainWindow  # Import the generated UI class
import sys
import requests
import traceback
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
)
from api_handler import get_plate_info,get_phone_info,get_zip_info  # Import API function

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
        try:
            super(LicensePlate, self).__init__()
            self.setupUi(self)  # Initialize UI

            # List of buttons for navigation
            self.nav_buttons = [
                self.btnLicensePlate,
                self.btnPhoneLookup,
                self.btnZipLookup,
            ]

            # Set default underlined button
            self.set_active_button(self.btnLicensePlate)

            # Connect buttons to respective functions
            self.state_dropdown.addItems(sorted(STATES.keys()))  
            self.btnLicensePlate.clicked.connect(lambda: self.change_page(0, self.btnLicensePlate))
            self.btnPhoneLookup.clicked.connect(lambda: self.change_page(1, self.btnPhoneLookup))
            self.btnZipLookup.clicked.connect(lambda: self.change_page(2, self.btnZipLookup))
            # self.btnBlank3.clicked.connect(lambda: self.change_page(3, self.btnBlank3))

            self.search_button.clicked.connect(self.fetch_plate_info)
            self.search_button_2.clicked.connect(self.fetch_phone_info)  # New phone search button

        except Exception as e:
            self.show_error("Initialization Error", str(e))
    def change_page(self, index, clicked_button):
        """Change the stacked widget page and update active button styling."""
        try:
            self.stackedWidget.setCurrentIndex(index)
            self.set_active_button(clicked_button)
        except Exception as e:
            self.show_error("Page Change Error", str(e))

    def set_active_button(self, active_button):
        """Apply underline to the active button and remove from others."""
        try:
            for button in self.nav_buttons:
                button.setStyleSheet("color:black;")  # Remove underline
            
            active_button.setStyleSheet("color:#1159A8")  # Apply underline
        except Exception as e:
            self.show_error("Button Styling Error", str(e))

    def fetch_plate_info(self):
        """Fetch license plate details from API."""
        try:
            plate = self.plate_entry.text().upper()  # Get plate number
            state = self.state_dropdown.currentText()  # Get selected state
            
            if not plate or not state:
                QMessageBox.warning(self, "Input Error", "Please enter a plate number and select a state.")
                return

            response_data = get_plate_info(plate, state)
            if response_data:
                self.update_results(response_data)
            else:
                QMessageBox.critical(self, "API Error", "Failed to fetch license plate details.")

        except Exception as e:
            self.show_error("Fetch Plate Info Error", str(e))

    def update_results(self, data):
        """Update UI with fetched results."""
        try:
            self.result_listbox.clear()  
            self.vinTable.setRowCount(0)  

            details = ["Make", "Model", "Year", "Plate", "State", "Country", "VIN"]

            # Populate result_listbox
            for key in details:
                value = data.get(key.lower(), "").strip()
                if value:
                    entry = f"{key}: {value}"
                    self.result_listbox.addItem(entry)

            # Populate vinTable
            vin_data = data.get("vin_data", {})
            filtered_vin_data = {key: value for key, value in vin_data.items() if value.strip()}

            self.vinTable.setRowCount(len(filtered_vin_data))
            self.vinTable.setColumnCount(2)
            self.vinTable.setHorizontalHeaderLabels(["Key", "Value"])

            for row, (key, value) in enumerate(filtered_vin_data.items()):
                self.vinTable.setItem(row, 0, QTableWidgetItem(key))
                self.vinTable.setItem(row, 1, QTableWidgetItem(value))

            self.vinTable.resizeColumnsToContents()
            self.vinTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        except Exception as e:
            self.show_error("Update Results Error", str(e))

    def fetch_phone_info(self):
        """Fetch phone number details from API."""
        try:
            phone = self.phone_entry.text().strip()  # Get phone number

            if not phone:
                QMessageBox.warning(self, "Input Error", "Please enter a phone number.")
                return

            response_data = get_phone_info(phone)
            if response_data:
                self.update_phone_results(response_data)
            else:
                QMessageBox.critical(self, "API Error", "Failed to fetch phone number details.")

        except Exception as e:
            self.show_error("Fetch Phone Info Error", str(e))

    def update_phone_results(self, data):
        """Update UI with fetched phone number results."""
        try:
            self.phoneList.clear()  
            self.phoneTable.setRowCount(0)  

            details = ["Carrier", "Line Type", "Location", "Timezone", "Risk Score"]

            # Populate phoneList
            for key in details:
                value = data.get(key.lower(), "").strip()
                if value:
                    entry = f"{key}: {value}"
                    self.phoneList.addItem(entry)

            # Populate phoneTable
            phone_data = data.get("details", {})
            filtered_phone_data = {key: value for key, value in phone_data.items() if value.strip()}

            self.phoneTable.setRowCount(len(filtered_phone_data))
            self.phoneTable.setColumnCount(2)
            self.phoneTable.setHorizontalHeaderLabels(["Key", "Value"])

            for row, (key, value) in enumerate(filtered_phone_data.items()):
                self.phoneTable.setItem(row, 0, QTableWidgetItem(key))
                self.phoneTable.setItem(row, 1, QTableWidgetItem(value))

            self.phoneTable.resizeColumnsToContents()
            self.phoneTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        except Exception as e:
            self.show_error("Update Phone Results Error", str(e))
    def fetch_zip_info(self):
        """Fetch ZIP code details from API."""
        try:
            zip_code = self.zip_entry.text().strip()  # Get ZIP code

            if not zip_code:
                QMessageBox.warning(self, "Input Error", "Please enter a ZIP code.")
                return

            response_data = get_zip_info(zip_code)
            if response_data:
                self.update_zip_results(response_data)
            else:
                QMessageBox.critical(self, "API Error", "Failed to fetch ZIP code details.")

        except Exception as e:
            self.show_error("Fetch ZIP Code Info Error", str(e))

    def update_zip_results(self, data):
        """Update UI with fetched ZIP code results."""
        try:
            self.zipList.clear()  
            self.zipTable.setRowCount(0)  

            details = ["City", "State", "County", "Latitude", "Longitude", "Timezone"]

            # Populate zipList
            for key in details:
                value = data.get(key.lower(), "").strip()
                if value:
                    entry = f"{key}: {value}"
                    self.zipList.addItem(entry)

            # Populate zipTable
            zip_data = data.get("details", {})
            filtered_zip_data = {key: value for key, value in zip_data.items() if value.strip()}

            self.zipTable.setRowCount(len(filtered_zip_data))
            self.zipTable.setColumnCount(2)
            self.zipTable.setHorizontalHeaderLabels(["Key", "Value"])

            for row, (key, value) in enumerate(filtered_zip_data.items()):
                self.zipTable.setItem(row, 0, QTableWidgetItem(key))
                self.zipTable.setItem(row, 1, QTableWidgetItem(value))

            self.zipTable.resizeColumnsToContents()
            self.zipTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        except Exception as e:
            self.show_error("Update ZIP Code Results Error", str(e))

        
    
    def show_error(self, title, message):
        """Display an error message."""
        error_details = traceback.format_exc()
        print(f"ERROR: {message}\n{error_details}")  # Log error details
        QMessageBox.critical(self, title, f"{message}\n\nCheck console for details.")
    
   

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LicensePlate()
    window.show()
    sys.exit(app.exec_())
