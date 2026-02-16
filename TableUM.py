import time
from tkinter import Tk, LabelFrame, Label, Button, CENTER, BOTH, N, S, IntVar, messagebox, ttk
import random

def finish(app):
    app.after_cancel(app.id_after)
    for i in app.winfo_children():
        i.destroy()

    label_up = Label(app)
    label_down = Label(app)
    list_labels = [label_up, label_down]
    label_up.pack(fill=BOTH, expand=True, anchor=N)
    label_down.pack(fill=BOTH, expand=True, anchor=S)

    if app.sec_count == 0:
        for i in list_labels:
            i.configure(bg="red")
        label_up.configure(text=f"Ошибок = {app.error_count}", font=("Arial", 60, "bold"))
        label_down.configure(text="Время вышло", font=("Arial", 60, "bold"))
    if len(app.list_counts) == 0 and app.run:
        label_up.configure(text=f"Ошибок = {app.error_count}", font=("Arial", 60, "bold"))
        label_down.configure(text="Проверка завершена", font=("Arial", 60, "bold"))
        if app.error_count != 0:
            col = "orrange"
        else:
            col = "green"
        for i in list_labels:
            i.configure(bg=col)

    app.run = False



def update(app):
    if app.run:
        app.sec_count-=1
        app.time_label.configure(text=f"{app.sec_count} сек")
        if app.sec_count!=0:
            app.after(1000, update, app)
        else:
            finish(app)


def button_name(app):

    rand_but = random.randint(0, len(app.but_list)-1)  #  0..9
    des_val = app.list_of_num[app.index_task][0]*app.list_of_num[app.index_task][1]
    list_val = [des_val]

    for i in range(0,len(app.but_list)): # i in 0..9
        if i != rand_but:
            val = random.randint(1, 10) * random.randint(1, 10)
            while val in list_val:
                val = random.randint(1, 10) * random.randint(1, 10)
        else:
            val = des_val
        app.but_list[i].configure(text=val, command=lambda v=val: check(v, app))
        list_val.append(val)


def check(val, app):
    rez = app.list_of_num[app.index_task][0] * app.list_of_num[app.index_task][1]
    # print("*", val, rez, val==rez)

    if len(app.list_counts) == 0 and app.run:
        finish(app)

    if val==rez and app.run:
        app.sec_count = app.max_time
        app.time_label.configure(text=f"{app.sec_count} сек")
        app.index_task = random.choice(app.list_counts)
        try:
            app.list_counts.remove(app.index_task)
        except ValueError:
            print(app.list_counts)
            print(app.index_task)
        # print(app.list_of_num[app.index_task])
        try:
            app.ex_label.configure(text = f"{app.list_of_num[app.index_task][0]} X {app.list_of_num[app.index_task][1]}")
        except IndexError:
            print(app.list_of_num)
            print(app.index_task)
        button_name(app)
        app.count_task.set(app.count_task.get()+1)


    elif app.run:
        app.error_count+=1
        print("YOU WRONG!!! Error count =", app.error_count)



def init_APP(list_of_num, list_counts):




    app = Tk()
    app.title("TableUM")
    app.geometry("940x405")
    app.len_list_of_num = len(list_of_num)
    app.count_task = IntVar()
    app.count_task.set(1)
    app.list_of_num = list_of_num
    app.list_counts = list_counts
    app.max_time = 3
    app.sec_count = app.max_time
    app.error_count = 0
    app.run = True

    app.index_task = random.choice(app.list_counts)
    app.list_counts.pop(app.index_task)
    # print(app.list_of_num[app.index_task])

    ex_label_fr = LabelFrame(app, background="yellow")
    ex_label_fr.grid(row=0, column=0,  padx=10, pady=10)

    app.but_fr = LabelFrame(app)
    app.but_fr.grid(row=0, column=1)

    app.progr_bar = ttk.Progressbar(app, length=900, variable=app.count_task)
    app.progr_bar.grid(row=1, column=0, columnspan=2, )

    but1 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but2 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but3 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but4 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but5 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but6 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but7 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but8 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but9 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)
    but10 = Button(app.but_fr, font=("Arial", 25, "bold"), width=4)

    app.but_list = [but1, but2, but3, but4, but5, but6, but7, but8, but9, but10]

    button_name(app)

    but1.grid(row=0, column=0)
    but2.grid(row=1, column=0)
    but3.grid(row=2, column=0)
    but4.grid(row=3, column=0)
    but5.grid(row=4, column=0)
    but6.grid(row=0, column=1)
    but7.grid(row=1, column=1)
    but8.grid(row=2, column=1)
    but9.grid(row=3, column=1)
    but10.grid(row=4, column=1)

    app.ex_label = Label(ex_label_fr,
                     font=("Arial", 145, "bold"),
                     background="yellow",
                     width=6,
                     anchor=CENTER
                     )
    app.ex_label.pack()

    app.time_label = Label(ex_label_fr,
                     text=f"{app.sec_count} сек.",
                     font=("Arial", 75, "bold"),
                     background = "yellow"
                     )
    app.time_label.pack()

    app.list_bg_changes = [app.time_label, app.ex_label, ex_label_fr]

    messagebox.showinfo(title="Проверка знания таблицы умножения", message="ПОГНАЛИ???")

    app.ex_label.configure(text = f"{app.list_of_num[app.index_task][0]} X {app.list_of_num[app.index_task][1]}")

    app.id_after = app.after(1000, update, app)

    app.mainloop()


def run():
    # list_of_num = [[i, j] for i in range(1,11) for j in range(1,11)]
    list_of_num = [[i, j] for i in range(1, 3) for j in range(1, 3)]
    list_counts = [i for i in range(0,len(list_of_num))]

    # print(list_counts)
    init_APP(list_of_num, list_counts)

if __name__ == "__main__":
    run()