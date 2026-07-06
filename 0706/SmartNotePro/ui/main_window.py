import customtkinter as ctk

from ui.menu_bar import MenuBar
from ui.tool_bar import ToolBar
from ui.side_bar import SideBar
from editor.editor import Editor
from ui.status_bar import StatusBar
from core.app_state import AppState


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # =========================
        # 기본 설정
        # =========================

        self.title("Smart Note Pro")
        self.geometry("1400x900")
        self.minsize(1000, 700)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # =========================
        # 상태 관리 (핵심)
        # =========================

        self.app_state = AppState()

        # =========================
        # UI 생성 (state 기반 통일)
        # =========================
        
        
        self.editor = Editor(self, self.app_state)
        self.menu_bar = MenuBar(self, self.app_state)
        self.tool_bar = ToolBar(self, self.app_state)
        self.side_bar = SideBar(self, self.app_state)
        
        self.status_bar = StatusBar(self, self.app_state)

        # =========================
        # 레이아웃
        # =========================

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.menu_bar.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.tool_bar.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.side_bar.grid(row=2, column=0, sticky="ns")

        self.editor.grid(row=2, column=1, sticky="nsew")

        self.status_bar.grid(row=3, column=0, columnspan=2, sticky="ew")

        # =========================
        # 단축키
        # =========================

        self.bind_hotkeys()

    # =========================
    # 단축키
    # =========================

    def bind_hotkeys(self):

        self.bind("<Control-n>", lambda e: self.menu_bar.new_file())
        self.bind("<Control-o>", lambda e: self.menu_bar.open_file())
        self.bind("<Control-s>", lambda e: self.menu_bar.save_file())