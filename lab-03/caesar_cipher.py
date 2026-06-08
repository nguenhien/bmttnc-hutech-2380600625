import sys
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        plain_text = self.ui.txt_plain_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        # Kiểm tra dữ liệu
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
                "Khóa Caesar phải là số nguyên!"
            )
            return

        key = int(key)

        if key < 1 or key > 25:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Khóa Caesar phải nằm trong khoảng từ 1 đến 25!"
            )
            return

        url = "http://127.0.0.1:5000/api/caesar/encrypt"

        payload = {
            "plain_text": plain_text,
            "key": str(key)
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_cipher_text.setPlainText(
                    data["encrypted_message"]
                )

                QMessageBox.information(
                    self,
                    "Thành công",
                    "Mã hóa thành công!"
                )

            else:
                QMessageBox.warning(
                    self,
                    "Lỗi API",
                    f"Mã lỗi: {response.status_code}"
                )

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(
                self,
                "Lỗi kết nối",
                str(e)
            )

    def call_api_decrypt(self):
        cipher_text = self.ui.txt_cipher_text.toPlainText().strip()
        key = self.ui.txt_key.toPlainText().strip()

        # Kiểm tra dữ liệu
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
                "Khóa Caesar phải là số nguyên!"
            )
            return

        key = int(key)

        if key < 1 or key > 25:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Khóa Caesar phải nằm trong khoảng từ 1 đến 25!"
            )
            return

        url = "http://127.0.0.1:5000/api/caesar/decrypt"

        payload = {
            "cipher_text": cipher_text,
            "key": str(key)
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()

                self.ui.txt_plain_text.setPlainText(
                    data["decrypted_message"]
                )

                QMessageBox.information(
                    self,
                    "Thành công",
                    "Giải mã thành công!"
                )

            else:
                QMessageBox.warning(
                    self,
                    "Lỗi API",
                    f"Mã lỗi: {response.status_code}"
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