class PasswordManager:
    def __init__(self):
        self.default_password = "1111"
        self.entered_password = ""

    def submit_password(self):
        if self.entered_password == self.default_password:
            print("Password correct!")
        else:
            print("Password incorrect!")

    def button_click(self, button_number):
        self.entered_password += str(button_number)
        print("Entered password:", self.entered_password)
class Check_pass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.button_image_1 = PhotoImage(
        file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.submit_password,
            relief="flat"
        )
        self.button_1.place(
            x=56.0,
            y=271.0,
            width=62.0,
            height=55.0
        )