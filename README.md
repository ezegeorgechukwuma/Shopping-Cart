Selenium Shopping Cart Test Automation
This project demonstrates an end-to-end test automation framework for a shopping cart functionality using Selenium WebDriver with Python. It is structured using the Page Object Model (POM) for maintainability and uses pytest as the testing framework.

Features
Automated Testing:
Search for products
Add items to the shopping cart
Apply promo codes
Validate total cart value
Place orders with a selected country
Refactored Code:
Follows best practices with explicit waits and dynamic locators
Improved robustness with retry mechanisms to handle dynamic DOM changes
Logging:
Logs test steps and outcomes to both console and log files for better debugging.
POM Architecture:
Clean separation of concerns using the Page Object Model (POM).
Project Structure
plaintext
Copy code
.
├── tests/
│   └── test_shopping_cart.py       # Main test script
├── pages/
│   ├── base_page.py                # Base class for common Selenium utilities
│   ├── home_page.py                # Page class for home page actions
│   ├── cart_page.py                # Page class for shopping cart actions
│   └── checkout_page.py            # Page class for checkout actions
├── conftest.py                     # Pytest fixtures for setup and teardown
├── requirements.txt                # Project dependencies
├── test_log.log                    # Log file generated during test execution
└── README.md                       # Project documentation
Getting Started
Prerequisites
Ensure the following tools are installed on your system:

Python (3.7 or higher)
Google Chrome (latest version)
ChromeDriver (compatible with your Chrome version)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/shopping-cart-automation.git
cd shopping-cart-automation
Set Up a Virtual Environment (Optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Dependencies
The project uses the following Python libraries:

selenium
pytest
These are listed in the requirements.txt file and can be installed with the above command.

Usage
Running the Tests
Ensure ChromeDriver is in your system's PATH.
Execute the tests using pytest:
bash
Copy code
pytest tests/test_shopping_cart.py --capture=no
Logs
All test logs are saved in the test_log.log file. Logs include details of actions performed, errors encountered, and test outcomes.

Key Highlights
Challenges Faced During Refactoring
Locator Overmatch: Initial locators retrieved incorrect elements, such as 30 "Add to Cart" buttons instead of 3. This was debugged and fixed by refining locators.
Deprecated Methods: Replaced find_element_by_class_name with find_element(By.CLASS_NAME) to align with Selenium 4 standards.
StaleElementReferenceException: Implemented retry mechanisms in safe_find_element and safe_find_elements to handle dynamic DOM changes robustly.
Key Features of the Refactored Code
Explicit Waits: Eliminates brittle time.sleep statements, making the test faster and more reliable.
Dynamic Locator Handling: Prevents locator mismatches and stale element exceptions.
Logging: Provides detailed insights into the execution of each step.
Contributing
Contributions are welcome! Follow these steps to contribute:

Fork this repository.
Create a feature branch: git checkout -b feature-name.
Commit changes: git commit -m "Add a new feature".
Push to the branch: git push origin feature-name.
Create a pull request.
License
This project is licensed under the MIT License.

Contact
For questions or feedback, reach out at:

Email: ezegeorgechukwuma@gmail.com
GitHub:https://github.com/ezegeorgechukwuma
