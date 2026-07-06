import tkinter as tk
from tkinter import filedialog, messagebox


class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python 메모장")
        self.root.geometry("800x600")

        self.filename = None

        # ===== 텍스트 영역 =====
        self.text = tk.Text(root, undo=True, font=("맑은 고딕", 11))
        self.text.pack(fill="both", expand=True)

        # ===== 메뉴 =====
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        edit_menu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="파일", menu=file_menu)
        menubar.add_cascade(label="편집", menu=edit_menu)

        # 파일 메뉴
        file_menu.add_command(label="새로 만들기", command=self.new_file)
        file_menu.add_command(label="열기", command=self.open_file)
        file_menu.add_command(label="저장", command=self.save_file)
        file_menu.add_command(label="다른 이름으로 저장", command=self.save_as)

        file_menu.add_separator()

        file_menu.add_command(label="종료", command=root.quit)

        # 편집 메뉴
        edit_menu.add_command(label="실행 취소", command=lambda: self.text.event_generate("<<Undo>>"))
        edit_menu.add_command(label="다시 실행", command=lambda: self.text.event_generate("<<Redo>>"))

        edit_menu.add_separator()

        edit_menu.add_command(label="잘라내기", command=lambda: self.text.event_generate("<<Cut>>"))
        edit_menu.add_command(label="복사", command=lambda: self.text.event_generate("<<Copy>>"))
        edit_menu.add_command(label="붙여넣기", command=lambda: self.text.event_generate("<<Paste>>"))

    # ========================
    # 새 파일
    # ========================
    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.filename = None
        self.root.title("새 문서 - 메모장")

    # ========================
    # 파일 열기
    # ========================
    def open_file(self):
        file = filedialog.askopenfilename(
            filetypes=[("텍스트 파일", "*.txt"),
                       ("모든 파일", "*.*")]
        )

        if file:
            with open(file, "r", encoding="utf-8") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, f.read())

            self.filename = file
            self.root.title(file)

    # ========================
    # 저장
    # ========================
    def save_file(self):
        if self.filename is None:
            self.save_as()
        else:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))

            messagebox.showinfo("저장", "저장되었습니다.")

    # ========================
    # 다른 이름으로 저장
    # ========================
    def save_as(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("텍스트 파일", "*.txt")]
        )

        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))

            self.filename = file
            self.root.title(file)
            messagebox.showinfo("저장", "저장되었습니다.")


root = tk.Tk()
Notepad(root)
root.mainloop()