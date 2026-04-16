import sys
from PyQt6.QtWidgets import *
import mathang, khachhang, donhang

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QUẢN LÝ BÁN HÀNG")
        self.resize(1000, 650)

        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab_mh = QWidget()
        self.tab_kh = QWidget()
        self.tab_dh = QWidget()

        self.tabs.addTab(self.tab_mh, "Mặt hàng")
        self.tabs.addTab(self.tab_kh, "Khách hàng")
        self.tabs.addTab(self.tab_dh, "Đơn hàng")

        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        self.ui_mathang()
        self.ui_khachhang()
        self.ui_donhang()

    # ================= MẶT HÀNG =================
    def ui_mathang(self):
        layout = QVBoxLayout()

        self.txtSearchMH = QLineEdit()
        self.txtSearchMH.setPlaceholderText("Tìm kiếm mặt hàng...")
        self.txtSearchMH.textChanged.connect(self.search_mh)

        self.tblMH = QTableWidget()
        self.tblMH.setColumnCount(4)
        self.tblMH.setHorizontalHeaderLabels(["Mã", "Tên", "Nguồn", "Giá"])

        btnAdd = QPushButton("Thêm")
        btnEdit = QPushButton("Sửa")
        btnDelete = QPushButton("Xóa")

        btnAdd.clicked.connect(self.add_mh)
        btnEdit.clicked.connect(self.edit_mh)
        btnDelete.clicked.connect(self.delete_mh)

        layout.addWidget(self.txtSearchMH)
        layout.addWidget(self.tblMH)
        layout.addWidget(btnAdd)
        layout.addWidget(btnEdit)
        layout.addWidget(btnDelete)

        self.tab_mh.setLayout(layout)
        self.load_mh()

    def load_mh(self):
        data = mathang.get_all()
        self.tblMH.setRowCount(len(data))
        for i, r in enumerate(data):
            self.tblMH.setItem(i,0,QTableWidgetItem(str(r["MaHang"])))
            self.tblMH.setItem(i,1,QTableWidgetItem(r["TenHang"]))
            self.tblMH.setItem(i,2,QTableWidgetItem(r["NguonGoc"]))
            self.tblMH.setItem(i,3,QTableWidgetItem(str(r["DonGia"])))

    def search_mh(self):
        data = mathang.search(self.txtSearchMH.text())
        self.tblMH.setRowCount(len(data))
        for i, r in enumerate(data):
            self.tblMH.setItem(i,0,QTableWidgetItem(str(r["MaHang"])))
            self.tblMH.setItem(i,1,QTableWidgetItem(r["TenHang"]))
            self.tblMH.setItem(i,2,QTableWidgetItem(r["NguonGoc"]))
            self.tblMH.setItem(i,3,QTableWidgetItem(str(r["DonGia"])))

    def add_mh(self):
        ten, ok = QInputDialog.getText(self, "Tên hàng", "Nhập tên:")
        if ok:
            nguon, _ = QInputDialog.getText(self, "Nguồn", "Nhập nguồn:")
            gia, _ = QInputDialog.getInt(self, "Giá", "Nhập giá:")
            mathang.insert(ten, nguon, gia)
            self.load_mh()

    def edit_mh(self):
        row = self.tblMH.currentRow()
        if row >= 0:
            ma = int(self.tblMH.item(row,0).text())
            ten, _ = QInputDialog.getText(self, "Tên", "Nhập tên mới:")
            nguon, _ = QInputDialog.getText(self, "Nguồn", "Nhập nguồn:")
            gia, _ = QInputDialog.getInt(self, "Giá", "Nhập giá:")
            mathang.update(ma, ten, nguon, gia)
            self.load_mh()

    def delete_mh(self):
        row = self.tblMH.currentRow()
        if row >= 0:
            ma = int(self.tblMH.item(row,0).text())
            mathang.delete(ma)
            self.load_mh()

    # ================= KHÁCH HÀNG =================
    def ui_khachhang(self):
        layout = QVBoxLayout()

        self.txtSearchKH = QLineEdit()
        self.txtSearchKH.setPlaceholderText("Tìm kiếm khách hàng...")
        self.txtSearchKH.textChanged.connect(self.search_kh)

        self.tblKH = QTableWidget()
        self.tblKH.setColumnCount(4)
        self.tblKH.setHorizontalHeaderLabels(["Mã", "Tên", "Địa chỉ", "SĐT"])

        btnAdd = QPushButton("Thêm")
        btnEdit = QPushButton("Sửa")
        btnDelete = QPushButton("Xóa")

        btnAdd.clicked.connect(self.add_kh)
        btnEdit.clicked.connect(self.edit_kh)
        btnDelete.clicked.connect(self.delete_kh)

        layout.addWidget(self.txtSearchKH)
        layout.addWidget(self.tblKH)
        layout.addWidget(btnAdd)
        layout.addWidget(btnEdit)
        layout.addWidget(btnDelete)

        self.tab_kh.setLayout(layout)
        self.load_kh()

    def load_kh(self):
        data = khachhang.get_all()
        self.tblKH.setRowCount(len(data))
        for i, r in enumerate(data):
            self.tblKH.setItem(i,0,QTableWidgetItem(str(r["MaKH"])))
            self.tblKH.setItem(i,1,QTableWidgetItem(r["TenKH"]))
            self.tblKH.setItem(i,2,QTableWidgetItem(r["DiaChi"]))
            self.tblKH.setItem(i,3,QTableWidgetItem(r["SoDienThoai"]))

    def search_kh(self):
        data = khachhang.search(self.txtSearchKH.text())
        self.tblKH.setRowCount(len(data))
        for i, r in enumerate(data):
            self.tblKH.setItem(i,0,QTableWidgetItem(str(r["MaKH"])))
            self.tblKH.setItem(i,1,QTableWidgetItem(r["TenKH"]))
            self.tblKH.setItem(i,2,QTableWidgetItem(r["DiaChi"]))
            self.tblKH.setItem(i,3,QTableWidgetItem(r["SoDienThoai"]))

    def add_kh(self):
        ten, _ = QInputDialog.getText(self, "Tên", "")
        diachi, _ = QInputDialog.getText(self, "Địa chỉ", "")
        sdt, _ = QInputDialog.getText(self, "SĐT", "")
        khachhang.insert(ten, diachi, sdt)
        self.load_kh()

    def edit_kh(self):
        row = self.tblKH.currentRow()
        if row >= 0:
            ma = int(self.tblKH.item(row,0).text())
            ten, _ = QInputDialog.getText(self, "Tên", "")
            diachi, _ = QInputDialog.getText(self, "Địa chỉ", "")
            sdt, _ = QInputDialog.getText(self, "SĐT", "")
            khachhang.update(ma, ten, diachi, sdt)
            self.load_kh()

    def delete_kh(self):
        row = self.tblKH.currentRow()
        if row >= 0:
            ma = int(self.tblKH.item(row,0).text())
            khachhang.delete(ma)
            self.load_kh()

    # ================= ĐƠN HÀNG =================
    def ui_donhang(self):
        layout = QVBoxLayout()

        self.tblDH = QTableWidget()
        self.tblDH.setColumnCount(4)
        self.tblDH.setHorizontalHeaderLabels(["Mã", "Khách", "Ngày", "Tổng"])

        self.tblCT = QTableWidget()
        self.tblCT.setColumnCount(4)
        self.tblCT.setHorizontalHeaderLabels(["Tên hàng", "SL", "Giá", "Thành tiền"])

        btnAdd = QPushButton("Thêm đơn")

        btnAdd.clicked.connect(self.add_dh)
        self.tblDH.cellClicked.connect(self.show_ct)

        layout.addWidget(self.tblDH)
        layout.addWidget(btnAdd)
        layout.addWidget(QLabel("Chi tiết"))
        layout.addWidget(self.tblCT)

        self.tab_dh.setLayout(layout)
        self.load_dh()

    def load_dh(self):
        data = donhang.get_all()
        self.tblDH.setRowCount(len(data))
        for i, r in enumerate(data):
            self.tblDH.setItem(i,0,QTableWidgetItem(str(r["MaDon"])))
            self.tblDH.setItem(i,1,QTableWidgetItem(r["TenKH"]))
            self.tblDH.setItem(i,2,QTableWidgetItem(str(r["NgayLap"])))
            self.tblDH.setItem(i,3,QTableWidgetItem(str(r["TongTien"])))

    def add_dh(self):
        makh, _ = QInputDialog.getInt(self, "Mã KH", "Nhập mã KH:")
        ngay, _ = QInputDialog.getText(self, "Ngày", "YYYY-MM-DD:")
        madon = donhang.insert(makh, ngay)

        # thêm 1 sản phẩm demo
        donhang.insert_chitiet(madon, 1, 2, 10000)
        self.load_dh()

    def show_ct(self, row, col):
        madon = int(self.tblDH.item(row,0).text())
        data = donhang.get_chitiet(madon)

        self.tblCT.setRowCount(len(data))
        for i, r in enumerate(data):
            self.tblCT.setItem(i,0,QTableWidgetItem(r["TenHang"]))
            self.tblCT.setItem(i,1,QTableWidgetItem(str(r["SoLuong"])))
            self.tblCT.setItem(i,2,QTableWidgetItem(str(r["DonGia"])))
            self.tblCT.setItem(i,3,QTableWidgetItem(str(r["ThanhTien"])))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())