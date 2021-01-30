from tkinter import Button, Entry, Frame, StringVar, messagebox
from tkinter.constants import GROOVE


class Window:
    def __init__(self, root, database_manager) -> None:
        self.root = root
        self.root.title("Авторизация")
        self.root.geometry("400x200+0+0")
        self.database_manager = database_manager

    def main_page_init(self):
        print("yeah")

    def login_page_init(self) -> None:
        self.Frame = Frame(self.root, bg="black")
        self.Frame.place(x=0, y=0)
        self.username = StringVar()
        self.password = StringVar()

        login_input = Entry(
            self.Frame, textvariable=self.username, bd=5, relief=GROOVE, font=("", 15),
        ).grid(row=1, column=1, padx=20)
        password_input = Entry(
            self.Frame, textvariable=self.password, bd=5, relief=GROOVE, font=("", 15),
        ).grid(row=2, column=1, padx=20)

        auth_button = Button(
            self.Frame,
            command=self.auth,
            text="Login",
            width=15,
            font=("times new roman", 14, "bold"),
            bg="yellow",
            fg="red",
        ).grid(row=3, column=1, pady=10)

    def auth(self):
        login, password = self.username.get(), self.password.get()

        is_sign_in = self.database_manager.sign_in(login, password)

        if is_sign_in:
            # * Очистка фрейма, мусорных атрибутов
            self.Frame.destroy()
            del self.Frame
            del self.username
            del self.password

            # * Инициализация основной страницы
            self.main_page_init()

            messagebox.showinfo("Авторизация", "Успешно!")
            return True

        messagebox.showerror("Авторизация", "Логин и/или пароль неверны!")
        return False
