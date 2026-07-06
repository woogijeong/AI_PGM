import customtkinter as ctk


class Editor(ctk.CTkFrame):

    def __init__(self, parent, state):
        super().__init__(parent)

        self.parent = parent  # ⭐ 이거 반드시 있어야 함
        self.state = state
        
        self.font_name = "맑은 고딕"
        self.font_size = 14

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ===============================
        # Textbox 생성
        # ===============================

        self.textbox = ctk.CTkTextbox(
            self,
            undo=True,
            wrap="word",
            font=(self.font_name, self.font_size)
        )

        # ⭐ UI 배치는 여기서 한 번만
        self.textbox.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # 이벤트 연결
        self.textbox.bind("<KeyRelease>", self.on_change)

    # ===============================
    # 변경 감지
    # ===============================

    def on_change(self, event=None):
        self.parent.is_saved = False

    # ==========================================
    # 기본 기능
    # ==========================================

    def get_text(self):
        return self.textbox.get("1.0", "end")

    def set_text(self, text):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)

    def clear(self):
        self.textbox.delete("1.0", "end")

    # ==========================================
    # 글꼴
    # ==========================================

    def set_font(self, font_name, font_size):
        self.font_name = font_name
        self.font_size = font_size

        self.textbox.configure(
            font=(font_name, font_size)
        )

    # ==========================================
    # Undo / Redo
    # ==========================================

    def undo(self):
        try:
            self.textbox.edit_undo()
        except:
            pass

    def redo(self):
        try:
            self.textbox.edit_redo()
        except:
            pass

    # ==========================================
    # Clipboard
    # ==========================================

    def cut(self):
        self.textbox.event_generate("<<Cut>>")

    def copy(self):
        self.textbox.event_generate("<<Copy>>")

    def paste(self):
        self.textbox.event_generate("<<Paste>>")

    # ==========================================
    # Cursor
    # ==========================================

    def get_cursor_position(self):
        index = self.textbox.index("insert")
        line, column = index.split(".")
        return int(line), int(column)