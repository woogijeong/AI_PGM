"""
status_bar.py

Smart Note Pro
상태바

담당 기능
-------------------------
- 현재 줄(Line)
- 현재 열(Column)
- 문자 수
- 단어 수
- 인코딩
- 저장 상태
- 확대 비율
"""

import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, parent , app_state):
        super().__init__(parent, height=30)

        
        self.parent = parent
        self.state = app_state
        self.grid_columnconfigure(0, weight=1)

        self.status_text = ctk.StringVar()
        self.status_text.set(
            "Ln 1 | Col 1 | UTF-8 | 저장됨 | 0자 | 0단어 | 100%"
        )

        self.label = ctk.CTkLabel(
            self,
            textvariable=self.status_text,
            anchor="w"
        )

        self.label.pack(fill="x", padx=10)

    # ------------------------------
    # 상태 갱신
    # ------------------------------

    def update_status(
        self,
        line,
        column,
        characters,
        words,
        saved=True,
        zoom=100
    ):

        save_state = "저장됨" if saved else "수정됨"

        text = (
            f"Ln {line} | "
            f"Col {column} | "
            f"UTF-8 | "
            f"{save_state} | "
            f"{characters}자 | "
            f"{words}단어 | "
            f"{zoom}%"
        )

        self.status_text.set(text)
        
def refresh(self, editor, is_saved):

    text = editor.get_text()

    chars = len(text)
    words = len(text.split())

    line, col = editor.get_cursor_position()

    save_state = "저장됨" if is_saved else "수정됨"

    self.status_text.set(
        f"Ln {line} | Col {col} | UTF-8 | {save_state} | {chars}자 | {words}단어"
    )