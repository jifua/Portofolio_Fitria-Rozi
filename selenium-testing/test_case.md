## 🧪 Test Case - Login Feature

Test case berikut digunakan untuk memvalidasi fitur login menggunakan pendekatan manual testing dan diimplementasikan pada automation testing menggunakan Selenium & Pytest.

| ID            | Scenario                  | Expected Result          | Type      | Priority |
|--------------|--------------------------|--------------------------|----------|----------|
| TC-LOGIN-001 | Login dengan data valid  | Berhasil masuk           | Positive | High     |
| TC-LOGIN-002 | Login password salah     | Muncul error message     | Negative | High     |
| TC-LOGIN-003 | Login tanpa input        | Validasi muncul          | Negative | Medium   |

## 🔗 Mapping Test Case to Automation

| Test Case ID | Automation Function      |
|--------------|--------------------------|
| TC-LOGIN-001 | test_login_success       |
| TC-LOGIN-002 | test_login_invalid       |
| TC-LOGIN-003 | (belum di-automate)      |

💡 Automation coverage saat ini: 2/3 test case telah diotomatisasi.
