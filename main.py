import tkinter as tk
from tkinter import ttk


class MainAppAgain(tk.Tk):
    def __init__(self, counting):
        super().__init__()
        self.counting = counting
        self.create_widgets()

    def create_widgets(self):
        self.button_quit = tk.Button(self, text='QUIT', bg='red', fg='white', font=('Arial', 20, 'bold'),
                                     command=self.quit_app)
        self.button_quit.pack(side='left')
        self.button_again = tk.Button(self, text='AGAIN', bg='orange', fg='white', font=('Arial', 20, 'bold'),
                                      command=self.again)
        self.button_again.pack(side='right')

    def quit_app(self):
        self.destroy()

    def again(self):
        self.destroy()
        new_window = MainApp(self.counting)
        new_window.mainloop()


class MainApp(tk.Tk):
    def __init__(self, counting):
        super().__init__()
        self.canvas = tk.Canvas(master=self)
        self.canvas.pack()
        self.ready_label = tk.Label(master=self.canvas, text='Ready to write?', font=('Arial', 30))
        self.ready_label.pack()
        self.button = tk.Button(master=self.canvas, text='Ready', fg='orange', bg='red', font=('Arial', 15, 'bold'),
                                command=self.start)
        self.button.pack()
        self.label = tk.Label(master=self.canvas, font=('Arial', 15, 'bold'), bg='orange', fg='white',
                              text='You will write here:')
        self.label.pack_forget()
        self.text = tk.Text(master=self.canvas)
        self.text.pack_forget()

        self.previous_content = ''
        self.counting = counting

    def check_text(self):
        content = self.text.get('1.0', tk.END).strip()
        if content != self.previous_content:
            self.previous_content = content
        else:
            self.counting += 1
            if self.counting > 1:
                print("You have not typed")
                counting = 0
                MainAppAgain(counting)
                self.destroy()
        self.after(5000, self.check_text)

    def start(self):
        self.ready_label.pack_forget()
        self.button.pack_forget()
        self.label.pack()
        self.text.pack()
        self.text.focus_set()
        self.check_text()


count = 0
app = MainApp(count)
app.mainloop()
