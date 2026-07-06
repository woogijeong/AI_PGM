import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

# Pillow가 설치되어 있으면 저장 기능 사용
try:
    from PIL import ImageGrab
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Python 그림판")
        self.root.geometry("900x600")

        self.color = "black"
        self.brush_size = 3

        # ===== 상단 메뉴 =====
        top = tk.Frame(root)
        top.pack(fill="x")

        tk.Button(top, text="색상", command=self.choose_color).pack(side="left", padx=5)

        tk.Button(top, text="지우기", command=self.clear_canvas).pack(side="left", padx=5)

        tk.Button(top, text="저장", command=self.save_image).pack(side="left", padx=5)

        tk.Label(top, text="굵기").pack(side="left", padx=(20, 5))

        self.size = tk.Scale(top,
                             from_=1,
                             to=20,
                             orient="horizontal",
                             command=self.change_size)
        self.size.set(3)
        self.size.pack(side="left")

        # ===== 캔버스 =====
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.old_x = None
        self.old_y = None

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def change_size(self, value):
        self.brush_size = int(value)

    def start_draw(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def draw(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(
                self.old_x,
                self.old_y,
                event.x,
                event.y,
                fill=self.color,
                width=self.brush_size,
                capstyle=tk.ROUND,
                smooth=True
            )

        self.old_x = event.x
        self.old_y = event.y

    def stop_draw(self, event):
        self.old_x = None
        self.old_y = None

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_image(self):
        if not PIL_AVAILABLE:
            messagebox.showinfo(
                "안내",
                "저장 기능을 사용하려면 Pillow를 설치하세요.\n\npip install pillow"
            )
            return

        file = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png")]
        )

        if not file:
            return

        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()

        ImageGrab.grab((x, y, x1, y1)).save(file)

        messagebox.showinfo("저장 완료", "이미지가 저장되었습니다.")


root = tk.Tk()
Paint(root)
root.mainloop()