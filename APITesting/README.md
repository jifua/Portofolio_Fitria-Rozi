# API Automation Testing - REST API

## 📌 Project Overview

Project ini merupakan automation testing untuk REST API menggunakan **Pytest** dan **Requests**.
Pengujian dilakukan untuk memastikan endpoint API dapat berjalan dengan baik melalui validasi status code dan response body.

---

## 🎯 Objective

* Menguji endpoint API secara otomatis
* Memastikan response sesuai dengan expected result
* Memvalidasi status code dan data response
* Mengurangi error pada manual API testing

---

## 🧪 Test Scenarios

*  GET data (list posts) → berhasil mengambil data
*  GET single data → data sesuai ID
*  POST data → berhasil membuat data baru
*  DELETE data → berhasil menghapus data

---

## ⚙️ Tech Stack

* Python
* Pytest
* Requests
* Pytest HTML Report

---

## 📂 Project Structure

```
PTF_APITesting/
│
├── test_api.py
├── conftest.py
├── report.html
└── README.md
```

---

## ▶️ How to Run

### Install dependencies

```bash
pip install pytest requests pytest-html
```

### Run testing

```bash
pytest -v --html=report.html
```

---

## 📊 Result

* Total test: 4
* Status: PASSED ✅
* Report: HTML report generated

---

## 💡 Key Insight

Menggunakan public API (JSONPlaceholder) untuk memastikan stabilitas testing.
Melakukan validasi pada status code serta response body untuk memastikan endpoint bekerja sesuai ekspektasi.

---

## 🔗 API Endpoint

```
https://jsonplaceholder.typicode.com
```

---

## 🚀 Future Improvement

* Menambahkan response time validation
* Implementasi data-driven testing
* Integrasi CI/CD (GitHub Actions)
* Negative testing lebih kompleks

---

## 👩‍💻 Author

**Fitria Rozi** 

🔗 LinkedIn: www.linkedin.com/in/fitria-rozi-6a344a1b1
