import tkinter as tk
import math

# ------------------------
# 버튼 입력
# ------------------------
def click(value):
    entry.insert(tk.END, value)

# ------------------------
# 계산
# ------------------------
def calculate():
    expression = entry.get()

    try:
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))

        result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ------------------------
# 초기화
# ------------------------
def clear():
    entry.delete(0, tk.END)

# ------------------------
# 한 글자 삭제
# ------------------------
def backspace():
    text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, text[:-1])

# ------------------------
# 공학용 함수
# ------------------------
def scientific(func):

    try:
        value = float(entry.get())

        if func == "sin":
            result = math.sin(math.radians(value))

        elif func == "cos":
            result = math.cos(math.radians(value))

        elif func == "tan":
            result = math.tan(math.radians(value))

        elif func == "sqrt":
            result = math.sqrt(value)

        elif func == "square":
            result = value**2

        elif func == "log":
            result = math.log10(value)

        elif func == "ln":
            result = math.log(value)

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# ------------------------
# 창 생성
# ------------------------
window = tk.Tk()
window.title("반응형 공학용 계산기")
window.geometry("500x600")
window.minsize(350, 450)

# ------------------------
# Entry
# ------------------------
entry = tk.Entry(
    window,
    justify="right",
    font=("Arial", 22)
)

entry.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=5,
    pady=5
)

# ------------------------
# 일반 계산기 버튼
# ------------------------
buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
]

button_widgets = []

for text,row,col in buttons:

    if text=="=":
        btn=tk.Button(window,text=text,command=calculate)

    else:
        btn=tk.Button(
            window,
            text=text,
            command=lambda t=text:click(t)
        )

    btn.grid(
        row=row,
        column=col,
        sticky="nsew",
        padx=2,
        pady=2
    )

    button_widgets.append(btn)

# ------------------------
# Clear
# ------------------------
btn_clear=tk.Button(
    window,
    text="C",
    command=clear
)

btn_clear.grid(
    row=5,
    column=0,
    columnspan=2,
    sticky="nsew",
    padx=2,
    pady=2
)

button_widgets.append(btn_clear)

# ------------------------
# BackSpace
# ------------------------
btn_back=tk.Button(
    window,
    text="←",
    command=backspace
)

btn_back.grid(
    row=5,
    column=2,
    columnspan=2,
    sticky="nsew",
    padx=2,
    pady=2
)

button_widgets.append(btn_back)

# ------------------------
# 공학용 프레임
# ------------------------
scientific_frame=tk.Frame(window)

science_buttons=[
    ("sin",lambda:scientific("sin")),
    ("cos",lambda:scientific("cos")),
    ("tan",lambda:scientific("tan")),
    ("√",lambda:scientific("sqrt")),
    ("x²",lambda:scientific("square")),
    ("log",lambda:scientific("log")),
    ("ln",lambda:scientific("ln")),
    ("π",lambda:click("π")),
    ("e",lambda:click("e")),
]

science_widgets=[]

for i,(text,cmd) in enumerate(science_buttons):

    btn=tk.Button(
        scientific_frame,
        text=text,
        command=cmd
    )

    btn.grid(
        row=i//3,
        column=i%3,
        sticky="nsew",
        padx=2,
        pady=2
    )

    science_widgets.append(btn)

for i in range(3):
    scientific_frame.grid_columnconfigure(i,weight=1)

for i in range(3):
    scientific_frame.grid_rowconfigure(i,weight=1)
    
    
scientific_frame.grid(
    row=0,
    column=4,
    rowspan=6,
    sticky="nsew",
    padx=5,
    pady=5
)

window.grid_columnconfigure(4, weight=1)

# ------------------------
# 창 크기 변화
# ------------------------
def resize(event):
    

    size=max(12,event.width//28)

    entry.config(font=("Arial",size+6))

    for b in button_widgets:
        b.config(font=("Arial",size))

    for b in science_widgets:
        b.config(font=("Arial",size-1))

    

window.bind("<Configure>",resize)

# ------------------------
# 반응형 Grid
# ------------------------
for i in range(6):
    window.grid_rowconfigure(i,weight=1)

for i in range(4):
    window.grid_columnconfigure(i,weight=1)

# ------------------------
# 실행
# ------------------------
window.mainloop()