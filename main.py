import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6 import QtWidgets, uic
import csv_handler

class giaoDienDangNhap(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giao_dien_dang_nhap.ui", self)
        self.commandLinkButtonSignUp.clicked.connect(self.chuyenGiaoDienDangKy)
        self.pushButtonDangNhap.clicked.connect(self.dangNhap)

        # Load and apply CSS
        with open('style.css', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)

    def chuyenGiaoDienDangKy(self):
        self.window = giaoDienDangKy()
        self.window.show()
        self.hide()
    
    def chuyenGiaoDienChinh(self):
        self.window = giaoDienChinh()
        self.window.show()
        self.hide()

    def dangNhap(self):
        tai_khoan = self.lineEditTaiKhoan.text()
        mat_khau = self.lineEditMatKhau.text()

        data = csv_handler.read_data_from_csv()
        for row in data:
            if row[0] == tai_khoan:
                if row[1] == mat_khau:
                    QMessageBox.information(self, "Thông báo", "Đăng nhập thành công")
                    self.chuyenGiaoDienChinh()
                    return
                else:
                    QMessageBox.warning(self, "Thông báo", "Bạn nhập sai mật khẩu")
                    return

        QMessageBox.warning(self, "Thông báo", "Tài khoản vừa nhập không tồn tại")

class giaoDienDangKy(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giao_dien_dang_ky.ui", self)
        self.commandLinkButtonBackToLogin.clicked.connect(self.chuyenGiaoDienDangNhap)
        self.pushButtonDangKy.clicked.connect(self.dangKy)

        # Load and apply CSS
        with open('style.css', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)

    def chuyenGiaoDienDangNhap(self):
        self.window = giaoDienDangNhap()
        self.window.show()
        self.hide()

    def dangKy(self):
        tai_khoan = self.lineEditTaiKhoan.text()
        mat_khau = self.lineEditMatKhau.text()
        mat_khau_xac_nhan = self.lineEditMatKhauXacNhan.text()

        # Kiểm tra xem mật khẩu có trùng khớp không
        if mat_khau != mat_khau_xac_nhan:
            QMessageBox.warning(self, "Thông báo", "Mật khẩu không khớp. Hãy thử lại.")
            return
        
        # Kiểm tra xem tài khoản đã tồn tại chưa
        data = csv_handler.read_data_from_csv()
        for row in data:
            if row[0] == tai_khoan:
                QMessageBox.warning(self, "Thông báo", "Tài khoản đã tồn tại trước đó. Hãy thử lại.")
                return

        #Ghi dữ liệu vào CSV
        data = [tai_khoan, mat_khau]
        csv_handler.write_data_to_csv(data)
        QMessageBox.information(self, "Thông báo", "Đăng ký thành công")

        #Chuyển sang giao diện đăng nhập
        self.chuyenGiaoDienDangNhap()
    
class giaoDienChinh(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giao_dien_chinh.ui", self)
        self.pushButtonDangXuat.clicked.connect(self.dangXuat)

    def dangXuat(self):
        self.window = giaoDienDangNhap()
        self.window.show()
        self.hide()

khoiChayHeThong = QApplication(sys.argv)
phanMem = giaoDienDangNhap()
phanMem.show()
chayPhanMem = khoiChayHeThong.exec()
sys.exit(chayPhanMem)