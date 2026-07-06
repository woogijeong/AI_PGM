"""
side_bar.py

Smart Note Pro
좌측 사이드바

담당 기능
------------------------
- 최근 파일 UI
- 프로젝트 탐색 UI (추후)
- 빠른 문서 접근
"""

import customtkinter as ctk


class SideBar(ctk.CTkFrame):

    def __init__(self, parent, app_state):
        super().__init__(parent, width=200)

        self.parent = parent
        self.state = app_state
        
        self.configure(corner_radius=0)

        self.grid_propagate(False)

        # =========================
        # 타이틀
        # =========================

        self.title = ctk.CTkLabel(
            self,
            text="📁 Documents",
            font=("Arial", 14, "bold")
        )
        self.title.pack(pady=10)

        # =========================
        # 최근 파일 영역
        # =========================

        self.recent_label = ctk.CTkLabel(
            self,
            text="최근 파일",
            anchor="w"
        )
        self.recent_label.pack(fill="x", padx=10)

        # 임시 버튼들 (데모용)
        self.file1 = ctk.CTkButton(self, text="file1.txt", anchor="w")
        self.file2 = ctk.CTkButton(self, text="file2.txt", anchor="w")
        self.file3 = ctk.CTkButton(self, text="file3.txt", anchor="w")

        self.file1.pack(fill="x", padx=10, pady=2)
        self.file2.pack(fill="x", padx=10, pady=2)
        self.file3.pack(fill="x", padx=10, pady=2)

        # =========================
        # 구분선
        # =========================

        self.divider = ctk.CTkLabel(self, text="----------------")
        self.divider.pack(pady=10)

        # =========================
        # 새 문서 버튼
        # =========================

        self.new_btn = ctk.CTkButton(
            self,
            text="➕ 새 문서"
        )
        self.new_btn.pack(padx=10, pady=10, fill="x")

        # =========================
        # 이벤트 연결
        # =========================

        self.bind_events()

    # =========================
    # 이벤트
    # =========================

    def bind_events(self):
        self.new_btn.configure(command=self.new_file)

        self.file1.configure(command=lambda: self.open_dummy("file1.txt"))
        self.file2.configure(command=lambda: self.open_dummy("file2.txt"))
        self.file3.configure(command=lambda: self.open_dummy("file3.txt"))

    # =========================
    # 기능 (임시)
    # =========================

    def new_file(self):
        """새 문서 생성"""
        self.parent.editor.clear()

    def open_dummy(self, name):
        """임시 파일 열기 (나중에 실제 파일 연결)"""
        self.parent.editor.set_text(f"{name} 내용입니다.")