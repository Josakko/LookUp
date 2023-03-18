from tkinter import *
import whois


root = Tk()

window_width = 500
window_hight = 550

monitor_width = root.winfo_screenwidth()
monitor_hight = root.winfo_screenheight()

x = (monitor_width / 2) - (window_width / 2)
y = (monitor_hight / 2) - (window_hight / 2)

root.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')
root.title("Domain Lookup")
root.iconbitmap("JK.ico")
root.configure(bg="#dbdbdb")
root.resizable(False, False)


def lookup():
	text_box.delete(1.0, END)

	domain = entry.get()
	domain_info = whois.whois(domain)

	for key, value in domain_info.items():
		text_box.insert(1.0, f'{key} : {value}' + '\n\n')


input_frame = LabelFrame(root, text="Lookup Domain Name", bg="#dbdbdb")
input_frame.pack(pady=20)

entry = Entry(input_frame, width=24, font=("Arial", 14))
entry.grid(row=0, column=0, pady=10, padx=10)

button = Button(input_frame, text="Lookup Domain", font=("Arial", 9), command=lookup)
button.grid(row=0, column=1, padx=10)

text_box = Text(root, width=50, font=("Arial", 11))
text_box.pack()


root.mainloop()