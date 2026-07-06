import customtkinter as ctk


class ToolBar(ctk.CTkFrame):

    def __init__(self, parent, state=None):
        super().__init__(parent, height=50)

        self.parent = parent

        # =========================
        # Canvas + Scroll 구조
        # =========================

        self.canvas = ctk.CTkCanvas(self, height=50, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.button_frame = ctk.CTkFrame(self.canvas)

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.button_frame,
            anchor="nw"
        )

        # =========================
        # 버튼 생성 (여기에 붙임)
        # =========================

        self.buttons = []

        def add_btn(text, cmd=None):
            btn = ctk.CTkButton(self.button_frame, text=text, command=cmd)
            btn.pack(side="left", padx=3, pady=5)
            self.buttons.append(btn)
            return btn

        # 파일
        add_btn("새로", self.parent.menu_bar.new_file)
        add_btn("열기", self.parent.menu_bar.open_file)
        add_btn("저장", self.parent.menu_bar.save_file)

        # 편집
        add_btn("↩", self.parent.editor.undo)
        add_btn("↪", self.parent.editor.redo)

        # 스타일
        add_btn("B")
        add_btn("I")
        add_btn("U")

        # 기타
        add_btn("글꼴")
        add_btn("😊")

        # =========================
        # 크기 자동 조정
        # =========================

        self.button_frame.bind(
            "<Configure>",
            self.on_frame_configure
        )

        self.canvas.bind(
            "<Configure>",
            self.on_canvas_configure
        )

    # =========================
    # 스크롤/리사이즈 처리
    # =========================

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )