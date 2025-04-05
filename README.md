# 🛒 Selenium Shopping Cart Test Automation Framework

This project demonstrates an end-to-end test automation framework for testing shopping cart functionality using **Selenium WebDriver with Python**. It follows the **Page Object Model (POM)** design pattern and uses **pytest** as the testing framework.

---

## 🚀 Features

- 🔍 Search for products
- ➕ Add items to the cart
- 💸 Apply promo codes
- ✅ Validate total cart value
- 📦 Place orders with selected country
- 🧪 Automated with `pytest` and structured for maintainability

---

## 🧱 Project Structure

```
shopping-cart-automation/
│
├── tests/
│   └── test_shopping_cart.py         # Main test script
│
├── pages/
│   ├── base_page.py                  # Common Selenium utilities
│   ├── home_page.py                  # Home page actions
│   ├── cart_page.py                  # Cart-related actions
│   └── checkout_page.py              # Checkout actions
│
├── conftest.py                       # Pytest setup/teardown
├── requirements.txt                  # Project dependencies
├── test_log.log                      # Log file from test runs
└── README.md                         # Project documentation
```

---

## 🛠 Key Highlights

- ✅ **Explicit Waits**: Replaces `time.sleep()` with smart waits for better stability.
- 🔁 **Retry Mechanisms**: Handles stale DOM elements using `safe_find_element()` methods.
- 🔍 **Dynamic Locator Handling**: Prevents locator mismatches and improves test reliability.
- 📄 **Logging**: Each test step and result is logged to console and a `.log` file.
- 🧼 **Clean Architecture**: Uses Page Object Model (POM) to ensure separation of concerns and easy maintenance.

---

## ⚙️ Installation & Setup

### ✅ Prerequisites
- Python 3.7+
- Google Chrome (latest)
- ChromeDriver (matching your Chrome version)

### 📦 Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ezegeorgechukwuma/shopping-cart-automation.git
   cd shopping-cart-automation
   ```

2. **(Optional) Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scriptsctivate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Running the Tests

Make sure ChromeDriver is in your system’s PATH.

Run the test suite using:
```bash
pytest tests/test_shopping_cart.py --capture=no
```

📝 Test logs will be saved in `test_log.log`.

---

## 🧩 Challenges Overcome

- **Locator Overmatch**: Fixed excessive matches by refining locators (e.g., limiting “Add to Cart” buttons).
- **Selenium Deprecations**: Replaced deprecated methods like `find_element_by_class_name` with the updated `By.CLASS_NAME` syntax.
- **StaleElementReferenceException**: Solved using retry wrappers with smart exception handling.

---

## 🧰 Technologies Used

- Python 3.7+
- Selenium WebDriver
- Pytest
- Git & GitHub

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Create a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

**George Chukwuma Eze**  
📧 Email: ezegeorgechukwuma@gmail.com  
🔗 GitHub: [@ezegeorgechukwuma](https://github.com/ezegeorgechukwuma)

---
