"""
bold_italic_underline.py

Smart Note Pro

텍스트 서식 기능 모듈
- Bold
- Italic
- Underline
"""

import customtkinter as ctk
import tkinter.font as tkfont


class TextStyle:

    def __init__(self, editor):
        self.editor = editor

    def toggle_bold(self):
        self._apply_style(weight="bold")

    def toggle_italic(self):
        self._apply_style(slant="italic")

    def toggle_underline(self):
        self._apply_style(underline=1)

    def _apply_style(self, weight=None, slant=None, underline=None):

        try:
            current_font = tkfont.Font(font=self.editor.textbox.cget("font"))

            tags = self.editor.textbox.tag_names("sel.first")

            new_font = tkfont.Font(
                family=current_font.actual("family"),
                size=current_font.actual("size"),
                weight=weight if weight else current_font.actual("weight"),
                slant=slant if slant else current_font.actual("slant"),
                underline=underline if underline is not None else current_font.actual("underline")
            )

            self.editor.textbox.tag_configure("style", font=new_font)
            self.editor.textbox.tag_add("style", "sel.first", "sel.last")

        except:
            pass