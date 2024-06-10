# Expenses Tracker

<img src="https://img.shields.io/badge/Made_With-Python-blue" width="150px" alt="Made with Python" />

A simple Expenses Tracker application built using Python and Tkinter to help you manage and keep track of your daily expenses.

## Project as Part of the "Programming Fundamentals with Python" Track
This project is part of the graduation project for the "Programming Fundamentals with Python" track on Almdrasa platform. You can find the track via the following link: [Programming Fundamentals with Python](https://almdrasa.com/products/tracks/programming-fundamentals-python)

## Features

- Add expenses with details such as amount, currency, category, payment method, and date.
- View all added expenses in a table format.
- Total amount calculation in USD.
- Persistent data storage using an Excel file (`myExpenses.xlsx`).
- Currency conversion using the Fixer API.
- Date picker for easy date selection.

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/expenses-tracker.git
   cd expenses-tracker
   ```
3. Install the required dependencies:
   ```bash
   pip install tkcalendar openpyxl requests
   ```
## Usage

1. Run the application:
   
   ```bash
   python app.py
   ```
3. The application window will open, allowing you to enter and manage your expenses.

## How it Works

- **Data Storage:** An Excel file (myExpenses.xlsx) is automatically created in the project directory the first time you enter data. This file stores all expense entries persistently.
- **Data Restoration:** Upon running the program, any previously entered data is restored from the Excel file, ensuring that your expense history is always available.

## Dependencies

- **tkinter**: Standard Python interface to the Tk GUI toolkit.
- **tkcalendar**: A Tkinter calendar and date picker module.
- **openpyxl**: A Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
- **requests**: A simple HTTP library for Python.

### API Usage

The application uses the [Fixer API](https://apilayer.com/marketplace/fixer-api) to fetch currency symbols and conversion rates. Ensure you have a valid API key and replace the placeholder in the script:

```python
headers= {"apikey": "your_api_key"}
```
## Project as Part of the "Programming Fundamentals with Python" Track
This project is part of the graduation project for the "Programming Fundamentals with Python" track on Almdrasa platform. You can find the track via the following link: [Programming Fundamentals with Python](https://almdrasa.com/products/tracks/programming-fundamentals-python)

## Contributing
Feel free to submit issues or pull requests if you have any improvements or fixes. Contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
