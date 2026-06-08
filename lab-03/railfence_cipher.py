import sys
import requests

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)

from ui.railfence import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        key = self.ui.txt_key.text().strip()

        if not plain_text:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Vui lòng nhập bản rõ!"
            )
            return

        if not key:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Vui lòng nhập khóa!"
            )
            return

        if not key.isdigit():
            QMessageBox.warning(
                self,
                "Lỗi",
                "Khóa Rail Fence phải là số nguyên!"
            )
            return

        if int(key) < 2:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Khóa Rail Fence phải lớn hơn hoặc bằng 2!"
            )
            return

        url = "http://127.0.0.1:5000/api/railfence/encrypt"

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_cipher_text.setPlainText(
                    data["encrypted_text"]
                )

                QMessageBox.information(
                    self,
                    "Thành công",
                    "Mã hóa Rail Fence thành công!"
                )

            else:
                QMessageBox.warning(
                    self,
                    "Lỗi API",
                    f"Mã lỗi: {response.status_code}\n\n{response.text}"
                )

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(
                self,
                "Lỗi kết nối",
                str(e)
            )

    def call_api_decrypt(self):
        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key = self.ui.txt_key.text().strip()

        if not cipher_text:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Vui lòng nhập bản mã!"
            )
            return

        if not key:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Vui lòng nhập khóa!"
            )
            return

        if not key.isdigit():
            QMessageBox.warning(
                self,
                "Lỗi",
                "Khóa Rail Fence phải là số nguyên!"
            )
            return

        if int(key) < 2:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Khóa Rail Fence phải lớn hơn hoặc bằng 2!"
            )
            return

        url = "http://127.0.0.1:5000/api/railfence/decrypt"

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_plain_text.setPlainText(
                    data["decrypted_text"]
                )

                QMessageBox.information(
                    self,
                    "Thành công",
                    "Giải mã Rail Fence thành công!"
                )

            else:
                QMessageBox.warning(
                    self,
                    "Lỗi API",
                    f"Mã lỗi: {response.status_code}\n\n{response.text}"
                )

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(
                self,
                "Lỗi kết nối",
                str(e)
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    sys.exit(app.exec_())