# 🧪 Selenium Automation Testing - Login Feature

## 📌 Project Overview
Project ini merupakan automation testing untuk fitur login menggunakan Selenium dan Pytest.  
Pengujian dilakukan untuk memastikan sistem dapat menangani login valid dan invalid secara benar.

---

## 🎯 Objective
- Menguji fungsi login secara otomatis  
- Memastikan validasi input berjalan dengan baik  
- Mengurangi error pada manual testing  

---

## 🧪 Test Scenarios
- ✅ Login dengan data valid → berhasil masuk  
- ❌ Login dengan data invalid → muncul error message  

---

## ⚙️ Tech Stack
- Python  
- Selenium WebDriver  
- Pytest  
- Pytest HTML Report  

---

## 📂 Project Structure
```bash
selenium-testing/
│
├── test_login.py
├── conftest.py
├── report.html
└── README.md
```

---

## ▶️ How to Run

### Install dependencies
```bash
pip install selenium pytest pytest-html
```

### Run Testing
```bash
pytest -v --html=report.html
```

---

## 📊 Result
- Total test: 2  
- Status: PASSED ✅  
- Report: HTML report generated  

---

## 💡 Key Insight
Menggunakan explicit wait untuk menangani dynamic element sehingga meningkatkan stabilitas automation testing.

---

## 🚀 Future Improvement
- Integrasi CI/CD (GitHub Actions)  
- Data-driven testing  
- Cross-browser testing  

---

## 👩‍💻 Author
Fitria Rozi  
LinkedIn: https://www.linkedin.com/in/fitria-rozi
