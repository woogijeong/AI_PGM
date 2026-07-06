"""
menu_bar.py

Smart Note Pro
메뉴바

담당 기능
-------------------------
- 파일 관리
- 편집 기능
- 단축키 연결 (추후 확장)
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox


class MenuBar(ctk.CTkFrame):

    def __init__(self, parent ,app_state):
        super().__init__(parent, height=30)

        self.parent = parent
        self.state = app_state

        # =========================
        # 메뉴 버튼
        # =========================

        self.file_btn = ctk.CTkButton(self, text="파일")
        self.edit_btn = ctk.CTkButton(self, text="편집")
        self.help_btn = ctk.CTkButton(self, text="도움말")

        self.file_btn.pack(side="left", padx=5, pady=5)
        self.edit_btn.pack(side="left", padx=5, pady=5)
        self.help_btn.pack(side="left", padx=5, pady=5)

        # 이벤트 연결
        self.bind_events()

    # =========================
    # 이벤트
    # =========================

    def bind_events(self):
        self.file_btn.configure(command=self.show_file_menu)
        self.edit_btn.configure(command=self.show_edit_menu)
        self.help_btn.configure(command=self.show_help)

    # =========================
    # 파일 메뉴
    # =========================

    def show_file_menu(self):
        menu = ctk.CTkToplevel(self)
        menu.title("파일")
        menu.geometry("200x200")

        ctk.CTkButton(menu, text="새 파일", command=self.new_file).pack(pady=5)
        ctk.CTkButton(menu, text="열기", command=self.open_file).pack(pady=5)
        ctk.CTkButton(menu, text="저장", command=self.save_file).pack(pady=5)
        ctk.CTkButton(menu, text="다른 이름으로 저장", command=self.save_as).pack(pady=5)
        ctk.CTkButton(menu, text="종료", command=self.parent.destroy).pack(pady=5)

    # =========================
    # 편집 메뉴
    # =========================

    def show_edit_menu(self):
        menu = ctk.CTkToplevel(self)
        menu.title("편집")
        menu.geometry("200x200")

        ctk.CTkButton(menu, text="실행취소", command=self.undo).pack(pady=5)
        ctk.CTkButton(menu, text="다시실행", command=self.redo).pack(pady=5)
        ctk.CTkButton(menu, text="잘라내기", command=self.cut).pack(pady=5)
        ctk.CTkButton(menu, text="복사", command=self.copy).pack(pady=5)
        ctk.CTkButton(menu, text="붙여넣기", command=self.paste).pack(pady=5)

    # =========================
    # 도움말
    # =========================

    def show_help(self):
        messagebox.showinfo(
            "Smart Note Pro",
            "Python + CustomTkinter 기반 메모장 프로젝트\nv0.1"
        )

    # =========================
    # 파일 기능 (임시 연결)
    # =========================

    def new_file(self):
        editor = self.parent.editor
        editor.clear()

    def open_file(self):
        file = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file:
            with open(file, "r", encoding="utf-8") as f:
                self.parent.editor.set_text(f.read())

    def save_file(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.parent.editor.get_text())

    def save_as(self):
        self.save_file()

    # =========================
    # 편집 기능 연결
    # =========================

    def undo(self):
        self.parent.editor.undo()

    def redo(self):
        self.parent.editor.redo()

    def cut(self):
        self.parent.editor.cut()

    def copy(self):
        self.parent.editor.copy()

    def paste(self):
        self.parent.editor.paste()
        
    def new_file(self):
        self.parent.editor.clear()
        self.parent.current_file = None
        self.parent.is_saved = True
        self.parent.status_bar.update_status(1, 1, 0, 0, True)
        
    
    def open_file(self):
        file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

        if file:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

            self.parent.editor.set_text(content)
            self.parent.current_file = file
            self.parent.is_saved = True
            
    def save_file(self):
        if not self.parent.current_file:
            return self.save_as()

        with open(self.parent.current_file, "w", encoding="utf-8") as f:
            f.write(self.parent.editor.get_text())

        self.parent.is_saved = True
        
        
    def save_as(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
    )

        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.parent.editor.get_text())

            self.parent.current_file = file
            self.parent.is_saved = True