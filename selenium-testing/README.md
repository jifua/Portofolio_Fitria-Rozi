**Selenium Automation Testing - Login Feature**

📌 Project Overview
Project ini merupakan automation testing untuk fitur login menggunakan Selenium dan Pytest. Pengujian dilakukan untuk memastikan sistem dapat menangani login valid dan invalid secara benar.

🎯 Objective
1. Menguji fungsi login secara otomatis
2. Memastikan validasi input berjalan dengan baik
3. Mengurangi error manual testing

🧪 Test Scenarios
✅ Login dengan username & password valid → berhasil masuk
❌ Login dengan data invalid → muncul error message

⚙️ Tech Stack
1. Python
2. Selenium WebDriver
3. Pytest
4. Pytest HTML Report

▶️ How to Run
Install dependencies:
pip install selenium pytest pytest-html

Run test:
pytest -v --html=report.html

📊 Result
1. 2 test case berhasil dijalankan
2. Semua test PASSED
3. Report otomatis di-generate dalam bentuk HTML

💡 Key Insight
Menggunakan explicit wait untuk mengatasi dynamic element sehingga meningkatkan stabilitas automation testing.

🚀 Improvement
1. Integrasi CI/CD (GitHub Actions)
2. Data-driven testing
3. Cross-browser testing

👩‍💻 Author
Fitria Rozi
LinkedIn: https://www.linkedin.com/in/fitria-rozi-6a344a1b1/
