import tkinter as tk

root = tk.Tk()
root.title("Login UI")
root.geometry("520x720")
root.configure(bg="#f2f4f7")

border = tk.Frame(root, bg="#4a90e2")
border.place(relx=0.5, rely=0.5, anchor="center", width=392, height=572)


card = tk.Frame(root, bg="white", bd=2, relief="groove")
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=560)

border.lower(card)

content = tk.Frame(card, bg="white")
content.place(x=28, y=28, width=324, height=504)

title = tk.Label(content, text="LOGIN", bg="white", fg="#333",
                 font=("Arial", 16, "bold"))
title.pack(anchor="w", pady=(0, 18))

def labeled_entry(parent, label_text, show=None):
    lbl = tk.Label(parent, text=label_text, bg="white", fg="#444",
                   font=("Arial", 11))
    lbl.pack(anchor="w")

    entry = tk.Entry(parent, bd=1, relief="solid", font=("Arial", 11),
                     highlightthickness=1, highlightbackground="#d9d9d9",
                     highlightcolor="#4a90e2", show=show)
    entry.pack(fill="x", ipady=8, pady=(6, 16))
    return entry

email_entry = labeled_entry(content, "Email")
pass_entry  = labeled_entry(content, "Password", show="*")

remember_var = tk.BooleanVar(value=True)
remember_row = tk.Frame(content, bg="white")
remember_row.pack(fill="x", pady=(0, 18))

remember_cb = tk.Checkbutton(
    remember_row,
    text="Remember me?",
    variable=remember_var,
    bg="white",
    fg="#444",
    activebackground="white",
    font=("Arial", 10)
)
remember_cb.pack(anchor="w")

login_btn = tk.Button(
    content,
    text="LOGIN",
    bg="#f05a8a",
    fg="white",
    activebackground="#e84f80",
    activeforeground="white",
    bd=0,
    font=("Arial", 11, "bold"),
    height=2
)
login_btn.pack(fill="x", pady=(0, 10))

forgot = tk.Label(content, text="Forgot Password?", bg="white",
                  fg="#888", font=("Arial", 10))
forgot.pack(anchor="e", pady=(0, 18))

sep = tk.Frame(content, bg="white")
sep.pack(fill="x", pady=(6, 16))

line1 = tk.Frame(sep, bg="#d9d9d9", height=1)
line1.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=10)

or_box = tk.Label(sep, text="OR", bg="white", fg="#888",
                  font=("Arial", 9), bd=1, relief="solid", padx=8, pady=2)
or_box.pack(side="left")

line2 = tk.Frame(sep, bg="#d9d9d9", height=1)
line2.pack(side="left", fill="x", expand=True, padx=(10, 0), pady=10)

icons = tk.Frame(content, bg="white")
icons.pack(pady=(4, 20))

def circle_icon(parent, text, outline, fg):
    c = tk.Canvas(parent, width=44, height=44, bg="white",
                  highlightthickness=0)
    c.create_oval(6, 6, 38, 38, outline=outline, width=2, fill="white")
    c.create_text(22, 22, text=text, fill=fg, font=("Arial", 12, "bold"))
    return c

g_icon  = circle_icon(icons, "G", outline="#e74c3c", fg="#e74c3c")
fb_icon = circle_icon(icons, "f", outline="#3b5998", fg="#3b5998")
in_icon = circle_icon(icons, "in", outline="#0077b5", fg="#0077b5")

g_icon.pack(side="left", padx=12)
fb_icon.pack(side="left", padx=12)
in_icon.pack(side="left", padx=12)

bottom = tk.Frame(content, bg="white")
bottom.pack(side="bottom", pady=(10, 0))

need = tk.Label(bottom, text="Need an account?", bg="white",
                fg="#666", font=("Arial", 10))
need.pack(side="left")

signup = tk.Label(bottom, text=" SIGN UP", bg="white",
                  fg="#333", font=("Arial", 10, "bold"))
signup.pack(side="left")

root.mainloop()
