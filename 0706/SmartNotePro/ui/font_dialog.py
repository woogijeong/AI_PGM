"""
font_dialog.py

Smart Note Pro
글꼴 설정 다이얼로그

기능
----------------------
- 글꼴 선택
- 글자 크기 선택
- 적용 버튼
"""

import customtkinter as ctk
from tkinter import font


class FontDialog(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.title("글꼴 설정")
        self.geometry("400x300")
        self.resizable(False, False)

        # =========================
        # 시스템 글꼴 목록
        # =========================

        self.font_list = list(font.families())
        self.font_list.sort()

        # =========================
        # 현재 값
        # =========================

        self.selected_font = ctk.StringVar(value="맑은 고딕")
        self.selected_size = ctk.IntVar(value=14)

        # =========================
        # UI
        # =========================

        self.create_widgets()

    # -------------------------
    # UI 구성
    # -------------------------

    def create_widgets(self):

        # 글꼴 선택
        self.font_box = ctk.CTkComboBox(
            self,
            values=self.font_list,
            variable=self.selected_font,
            width=300
        )
        self.font_box.pack(pady=10)

        # 크기 선택
        self.size_box = ctk.CTkComboBox(
            self,
            values=[str(i) for i in range(8, 40)],
            variable=self.selected_size,
            width=100
        )
        self.size_box.pack(pady=10)

        # 적용 버튼
        self.apply_btn = ctk.CTkButton(
            self,
            text="적용",
            command=self.apply_font
        )
        self.apply_btn.pack(pady=20)

    # -------------------------
    # 적용
    # -------------------------

    def apply_font(self):

        font_name = self.selected_font.get()
        font_size = int(self.selected_size.get())

        # Editor에 적용
        self.parent.editor.set_font(font_name, font_size)

        # 상태 저장
        self.parent.current_font = font_name
        self.parent.current_size = font_size

        self.destroy()