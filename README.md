
# Katalon Cura Demo Web Application Automation Testing

This project contains automation tests designed to verify various functionalities of the Katalon Cura Demo web application. The tests are written using Python and Selenium, covering menu, login, appointment booking, page verification, footer, and logout functionalities.

## Project Structure

- `main.py`: The main file that initiates the tests and manages the overall test flow.
- `MenuTest.py`: Tests for the clickability of menu items and header verification.
- `LoginTest.py`: Tests for verifying the user login functionality.
- `AppointmentTest.py`: Tests for verifying the appointment booking process.
- `HistoryTest.py`: Tests for verifying the clickability of the History page and its correctness.
- `ProfileTest.py`: Tests for verifying the clickability and correctness of the Profile page.
- `FooterTest.py`: Tests for verifying the footer elements and links.

`tests/`: A folder that contains the test files.

## Requirements

This project is written using Python and Selenium WebDriver. To install the required dependencies, follow these steps:

1. Ensure that Python 3.x is installed.
2. Open the terminal and run the following command to install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Test Flow

The following tests are performed:

1. **Menu Test**
   - Verifies the clickability of the menu button.
   - Verifies that the correct header is displayed when the menu is opened.

2. **Login Test**
   - Verifies that the login functionality works correctly.
   - Ensures the user is redirected to the correct page after logging in.

3. **Appointment Booking Test**
   - Verifies the entire process of booking an appointment.
   - Ensures correct redirection and page content.

4. **History Button Test**
   - Verifies the clickability of the History button.
   - Ensures the correct History page opens.

5. **Profile Button Test**
   - Verifies the clickability of the Profile button.
   - Ensures correct redirection to the Profile page.

6. **Logout Test**
   - Verifies the logout functionality.

7. **Footer Test**
   - Verifies the correctness of footer links.


