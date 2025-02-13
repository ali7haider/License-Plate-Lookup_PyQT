from main_ui import Ui_MainWindow  # Import the generated UI class
import sys
import requests
import traceback
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView,QInputDialog, QLineEdit
)

from api_handler import get_plate_info,get_phone_info,get_zip_info  # Import API function
import json
CONFIG_FILE = "config.json"  # File to store business name
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

from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

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

            self.load_business_name()
            # Set default underlined button

            self.set_active_button(self.btnLicensePlate)

            # Connect buttons to respective functions
            self.state_dropdown.addItems(sorted(STATES.keys()))  
            self.btnLicensePlate.clicked.connect(lambda: self.change_page(0, self.btnLicensePlate))
            self.btnPhoneLookup.clicked.connect(lambda: self.change_page(1, self.btnPhoneLookup))
            self.btnZipLookup.clicked.connect(lambda: self.change_page(2, self.btnZipLookup))

            self.search_button.clicked.connect(self.fetch_plate_info)
            self.search_button_2.clicked.connect(self.fetch_phone_info)
            self.search_button_3.clicked.connect(self.fetch_zip_info)

            self.actionExit.triggered.connect(self.close)
            # Connect menu action to change business name
            self.actionChange_Business_Name.triggered.connect(self.change_business_name)

            # ✅ Apply Validators for Input Restrictions
            self.apply_input_validators()

    
        except Exception as e:
            self.show_error("Initialization Error", str(e))


    from PyQt5.QtWidgets import QInputDialog, QLineEdit

    def change_business_name(self):
        """Open styled input dialog to change business name, pre-fill with current title, and update UI."""
        
        current_name = self.lblTitle.text()  # Get current title

        # Create a styled input dialog
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Change Business Name")
        dialog.setLabelText("Enter new business name:")
        dialog.setTextValue(current_name)  # Pre-fill with current name
        dialog.setTextEchoMode(QLineEdit.Normal)
        dialog.resize(400, 150)  # Width x Height

        # Apply stylesheet for styling the input box & buttons
        dialog.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                border-radius: 5px;
                border: 1px solid gray;
                padding-left: 5px;
                selection-color: #fff;
                selection-background-color: #1159A8;
            }
            QLineEdit:hover {
                border: 2px solid gray;
            }
            QLineEdit:focus {
                border: 2px solid gray;
            }
            QPushButton {
                background-color: #1159A8;
                color: white;
                border-radius: 5px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #146CD0;
            }
            QPushButton:pressed {
                background-color: #146CD0;
            }
        """)

        # Execute dialog and get input
        if dialog.exec_():
            new_name = dialog.textValue().strip()
            if new_name:
                self.lblTitle.setText(new_name)  # Update label
                self.setWindowTitle(new_name)  # Update app title

                self.save_business_name(new_name)  # Save to JSON




    def save_business_name(self, name):
        """Save business name to config file."""
        with open(CONFIG_FILE, "w") as file:
            json.dump({"business_name": name}, file)
    def load_business_name(self):
        """Load business name from config file if available."""
        try:
            with open(CONFIG_FILE, "r") as file:
                data = json.load(file)
                business_name = data.get("business_name", "Big R Ranch Security")
                self.lblTitle.setText(business_name)
                self.setWindowTitle(business_name)  # Update app title

        except (FileNotFoundError, json.JSONDecodeError):
            self.lblTitle.setText("Big R Ranch Security")  # Fallback if config is missing or corrupted
            self.setWindowTitle("Big R Ranch Security")  # Update app title

    
    def apply_input_validators(self):
        """Apply validators to restrict input format."""

        # 1️⃣ Only Allow Digits in zip_entry and phone_entry (Using RegExp)
        digit_validator = QRegExpValidator(QRegExp("^[0-9]+$"), self)
        self.zip_entry.setValidator(digit_validator)
        self.phone_entry.setValidator(digit_validator)

        # 2️⃣ Allow lowercase letters but convert to uppercase in plate_entry
        plate_validator = QRegExpValidator(QRegExp("^[a-zA-Z0-9\\-\\s]+$"), self)  # Allow A-Z, a-z, 0-9, -, and spaces
        self.plate_entry.setValidator(plate_validator)

        # Convert input to uppercase dynamically
        self.plate_entry.textChanged.connect(self.convert_plate_to_uppercase)

    def convert_plate_to_uppercase(self):
        """Convert plate_entry text to uppercase dynamically."""
        text = self.plate_entry.text()
        self.plate_entry.setText(text.upper())

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
                self.result_listbox.clear()  
                self.vinTable.setRowCount(0)  
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
                self.phoneList.clear()
                self.phoneTable.setRowCount(0)
                QMessageBox.critical(self, "API Error", "Failed to fetch phone number details.")
        except Exception as e:
            self.show_error("Fetch Phone Info Error", str(e))

    def update_phone_results(self, data):
        """Update UI with fetched phone number results."""
        try:
            self.phoneList.clear()
            self.phoneTable.setRowCount(0)

            print("Raw data:", data)  # Debugging step

            # Extract the actual content
            content = data.get("content", {})
            print("Extracted content:", content)  # Debugging step

            caller_info = content.get("caller_name", {}) or {}  # Ensure it's a dict
            carrier_info = content.get("carrier", {}) or {}  # Ensure it's a dict

            print("Caller Info:", caller_info)  # Debugging step
            print("Carrier Info:", carrier_info)  # Debugging step

            # Function to replace None values with "NA"
            def safe_get(value):
                return str(value).strip() if value not in (None, "None") else "NA"

            # Details for phoneList
            details = {
                "Caller Name": safe_get(caller_info.get("caller_name")),
                "Caller Type": safe_get(caller_info.get("caller_type")),
                "Country Code": safe_get(content.get("country_code")),
                "National Format": safe_get(content.get("national_format")),
                "Phone Number": safe_get(content.get("phone_number")),
            }

            # Populate phoneList
            for key, value in details.items():
                self.phoneList.addItem(f"{key}: {value}")

            # Details for phoneTable
            table_data = {
                "Mobile Country Code": safe_get(carrier_info.get("mobile_country_code")),
                "Mobile Network Code": safe_get(carrier_info.get("mobile_network_code")),
                "Name": safe_get(carrier_info.get("name")),
                "Type": safe_get(carrier_info.get("type")),
            }

            # Populate phoneTable
            self.phoneTable.setRowCount(len(table_data))
            self.phoneTable.setColumnCount(2)
            self.phoneTable.setHorizontalHeaderLabels(["Key", "Value"])

            for row, (key, value) in enumerate(table_data.items()):
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
            print(response_data)
            if response_data:
                self.update_zip_results(response_data)
            else:
                self.zipList.clear()
                self.zipTable.setRowCount(0)         
                QMessageBox.critical(self, "API Error", "Failed to fetch ZIP code details.")

        except Exception as e:
            self.show_error("Fetch ZIP Code Info Error", str(e))

    def update_zip_results(self, data):
        """Update UI with fetched ZIP code results."""
        try:
            self.zipList.clear()
            self.zipTable.setRowCount(0)

            print("Raw data:", data)  # Debugging step

            # Extract the first entry from "Data" list
            zip_info_list = data.get("Data", [])
            if not zip_info_list:
                self.show_error("ZIP Code Lookup Error", "No data available.")
                return

            zip_info = zip_info_list[0]  # Assuming only one ZIP code entry is returned
            print("Extracted ZIP Info:", zip_info)  # Debugging step

            # Details for zipList
            details = {
                "City": zip_info.get("City", ""),
                "County": zip_info.get("County", ""),
                "State": zip_info.get("State", ""),
                "ZipLatitude": zip_info.get("ZipLatitude", ""),
                "ZipLongitude": zip_info.get("ZipLongitude", ""),
            }

            # Populate zipList
            for key, value in details.items():
                if value.strip():
                    self.zipList.addItem(f"{key}: {value}")

            # Details for zipTable
            table_data = {
                "CountyFIPS": zip_info.get("CountyFIPS", ""),
                "StateFIPS": zip_info.get("StateFIPS", ""),
                "Timezone": zip_info.get("TimeZone", ""),
                "DayLightSavings": zip_info.get("DayLightSavings", ""),
            }

            # Filter out empty values
            filtered_table_data = {key: value for key, value in table_data.items() if value.strip()}

            # Populate zipTable
            self.zipTable.setRowCount(len(filtered_table_data))
            self.zipTable.setColumnCount(2)
            self.zipTable.setHorizontalHeaderLabels(["Key", "Value"])

            for row, (key, value) in enumerate(filtered_table_data.items()):
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
        QMessageBox.critical(self, title, f"{message}\n\n")
    
   

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LicensePlate()
    window.show()
    sys.exit(app.exec_())
