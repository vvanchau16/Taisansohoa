import tkinter as tk
from tkinter import ttk, messagebox

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Trang Chủ")
        self.root.geometry("1000x600")  # Kích thước cửa sổ

        # Tạo Frame chứa cả cột tùy chọn và bảng thông tin
        main_frame = ttk.Frame(root, style="TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Tạo cột tùy chọn
        self.create_option_column(main_frame)

        # Tạo bảng thông tin
        self.create_info_table(main_frame)

        # Tạo nút và chức năng
        self.create_function_buttons(root)

    def create_info_table(self, parent_frame):
        # Tạo bảng thông tin với 4 hàng và 4 cột
        tree = ttk.Treeview(parent_frame, columns=("ID", "Tên", "Chức Vụ", "Lương"), show="headings", style="Treeview")
        tree.heading("ID", text="ID", anchor=tk.CENTER)
        tree.heading("Tên", text="Tên", anchor=tk.CENTER)
        tree.heading("Chức Vụ", text="Chức Vụ", anchor=tk.CENTER)
        tree.heading("Lương", text="Lương", anchor=tk.CENTER)

        for i in range(4):
            tree.column(i, width=150, anchor=tk.CENTER)

        # Sample data for the table
        data = [
            ("1", "Người 1", "Quản lý", "$5000"),
            ("2", "Người 2", "Nhân viên", "$3000"),
            ("3", "Người 3", "Nhân viên", "$3500"),
            ("4", "Người 4", "Quản lý", "$4800"),
        ]

        for row in data:
            tree.insert("", "end", values=row)

        # Set up vertical scrollbar
        scroll_y = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree.pack(side=tk.LEFT, padx=10, pady=10)
        tree.configure(yscrollcommand=scroll_y.set)

    def create_option_column(self, parent_frame):
        options_frame = ttk.Frame(parent_frame, width=200, style="Options.TFrame")
        options_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))  # Thêm padding bên phải

        parent_frame.grid_columnconfigure(0, weight=0)  # Để cột 0 không coi trọng trọng lượng
        parent_frame.grid_columnconfigure(1, weight=1)  # Để cột 1 coi trọng trọng lượng

        options = [
            ("Thông tin tổ chức", []),
            ("+ Phòng ban", []),
            ("+ Nhân viên", []),
            ("Thông tin đối tượng", [
                ("+ Khách hàng", []),
                ("+ Nhà cung cấp", []),
                ("+ Đơn hàng", [])
            ]),
            ("Tài liệu", [
                ("+ Hợp đồng", []),
                ("+ Tài liệu", []),
                ("+ Báo cáo", []),
                ("+ Văn bản pháp quy", [])
            ]),
            ("Tài sản", [
                ("+ Sản phẩm", []),
                ("+ Nguyên vật liệu", []),
                ("+ TSCD", []),
                ("+ CCDC", [])
            ])
        ]

        tree = ttk.Treeview(options_frame, columns=("Options",), show="headings", style="Options.Treeview")
        tree.heading("Options", text="Tùy chọn")
        tree.pack(pady=20)

        self.insert_options(tree, options)

    def insert_options(self, tree, options):
        for option, sub_options in options:
            item = tree.insert("", "end", values=(option,))
            if sub_options:
                self.insert_options(tree, sub_options)
                tree.item(item, open=True)

    def create_function_buttons(self, parent_frame):
        function_buttons_frame = ttk.Frame(parent_frame)
        function_buttons_frame.pack(side=tk.BOTTOM, pady=10)

        button_add = tk.Button(function_buttons_frame, text="Thêm", command=self.add, font=("Arial", 14), bg="#5f6f79", fg="white")
        button_add.pack(side=tk.LEFT, padx=10)

        button_edit = tk.Button(function_buttons_frame, text="Sửa", command=self.edit, font=("Arial", 14), bg="#5f6f79", fg="white")
        button_edit.pack(side=tk.LEFT, padx=10)

        button_delete = tk.Button(function_buttons_frame, text="Xóa", command=self.delete, font=("Arial", 14), bg="#5f6f79", fg="white")
        button_delete.pack(side=tk.LEFT, padx=10)

        button_logout = tk.Button(function_buttons_frame, text="Đăng Xuất", command=self.logout, font=("Arial", 14), bg="#5f6f79", fg="white")
        button_logout.pack(side=tk.LEFT, padx=10)

    def add(self):
        messagebox.showinfo("Thông báo", "Chức năng Thêm")

    def edit(self):
        messagebox.showinfo("Thông báo", "Chức năng Sửa")

    def delete(self):
        messagebox.showinfo("Thông báo", "Chức năng Xóa")

    def logout(self):
        # Quay lại màn hình đăng nhập
        self.root.destroy()
        login_root = tk.Tk()
        login_form = AuthenticationApp(login_root)
        login_root.mainloop()


class AuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Đăng Nhập")
        self.root.geometry("600x500")  # Kích thước cửa sổ

        # Tạo Notebook (Tab)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=20, padx=20)

        # Tạo các tab cho Đăng nhập và Đăng ký
        self.login_tab = ttk.Frame(self.notebook)
        self.register_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.login_tab, text="Đăng Nhập")
        self.notebook.add(self.register_tab, text="Đăng Ký")

        # Tạo giao diện cho mỗi tab
        self.create_login_tab()
        self.create_register_tab()

    def create_login_tab(self):
        login_frame = ttk.Frame(self.login_tab, padding=(40, 20), style="TFrame")
        login_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(login_frame, text="Tên đăng nhập:", style="TLabel").grid(row=0, column=0, sticky="e")
        login_username_entry = ttk.Entry(login_frame)
        login_username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(login_frame, text="Mật khẩu:", style="TLabel").grid(row=1, column=0, sticky="e")
        login_password_entry = ttk.Entry(login_frame, show="*")
        login_password_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(login_frame, text="Đăng Nhập", command=lambda: self.login(login_username_entry.get(), login_password_entry.get()), style="TButton").grid(row=2, column=1, pady=20)

        # Use Label instead of ttk.Label for the link label
        link_label = tk.Label(login_frame, text="Chưa có tài khoản? Đăng ký ngay!", cursor="hand2", foreground="blue", font=("Arial", 12, "underline"))
        link_label.grid(row=3, column=1, pady=10, sticky="w")
        link_label.bind("<Button-1>", lambda event: self.notebook.select(self.register_tab))

    def create_register_tab(self):
        register_frame = ttk.Frame(self.register_tab, padding=(40, 20), style="TFrame")
        register_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(register_frame, text="Tên đăng ký:", style="TLabel").grid(row=0, column=0, sticky="e")
        register_username_entry = ttk.Entry(register_frame)
        register_username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(register_frame, text="Mật khẩu:", style="TLabel").grid(row=1, column=0, sticky="e")
        register_password_entry = ttk.Entry(register_frame, show="*")
        register_password_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(register_frame, text="Đăng Ký", command=lambda: self.register(register_username_entry.get(), register_password_entry.get()), style="TButton").grid(row=2, column=1, pady=20)

        # Use Label instead of ttk.Label for the link label
        link_label = tk.Label(register_frame, text="Đã có tài khoản? Đăng nhập ngay!", cursor="hand2", foreground="blue", font=("Arial", 12, "underline"))
        link_label.grid(row=3, column=1, pady=10, sticky="w")
        link_label.bind("<Button-1>", lambda event: self.notebook.select(self.login_tab))

    def login(self, username, password):
        print(f"Đăng nhập:\nTên đăng nhập: {username}\nMật khẩu: {password}")
        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")

        # Chuyển đến trang chủ sau khi đăng nhập
        self.root.destroy()
        home_root = tk.Tk()
        home_page = HomePage(home_root)
        home_root.mainloop()

    def register(self, username, password):
        print(f"Đã đăng ký:\nTên đăng ký: {username}\nMật khẩu: {password}")
        messagebox.showinfo("Thông báo", "Đăng ký thành công!")


if __name__ == "__main__":
    root = tk.Tk()

    # Thêm các style cho giao diện
    style = ttk.Style()
    style.configure("TFrame", background="#e1d8b9")
    style.configure("TLabel", background="#e1d8b9", font=("Arial", 14))
    style.configure("TButton", background="#5f6f79", foreground="white", font=("Arial", 14))
    style.configure("TLinkLabel.TLabel", background="#e1d8b9", font=("Arial", 12, "underline"), foreground="blue")

    style.configure("Options.TFrame", background="#a0cfe6")
    style.configure("Options.Treeview", background="#a0cfe6")
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))  # Đặt font cho tiêu đề của Treeview

    app = AuthenticationApp(root)
    root.mainloop()
