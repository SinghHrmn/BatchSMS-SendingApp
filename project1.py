import tkinter
import tkinter.ttk
import tkinter.messagebox
import http.client


class form1:
    def add(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "":
            tkinter.messagebox.showinfo("", "ALL FIELDS ARE MANDATORY")
        else:
            obj = open(".\\group_record.txt", "a")
            grp = self.textbox1.get()
            desc = self.textbox2.get()
            obj.write(grp)
            obj.write("\n")
            obj.write(desc)
            obj.write("\n*************\n")
            obj.close()
            tkinter.messagebox.showinfo("", "GROUP ADDED SUCCESSFULLY")

    def __init__(self):
        self.win1 = tkinter.Tk()
        self.label1 = tkinter.Label(self.win1, text="ENTER GROUP NAME")
        self.textbox1 = tkinter.Entry(self.win1)
        self.label2 = tkinter.Label(self.win1, text="DESCRIPTION")
        self.textbox2 = tkinter.Entry(self.win1)
        self.bt1 = tkinter.Button(self.win1, text="SUBMIT", command=self.add)
        # this code is for placing
        self.label1.grid(row=0, column=0)
        self.textbox1.grid(row=0, column=1)
        self.label2.grid(row=1, column=0)
        self.textbox2.grid(row=1, column=1)
        self.bt1.grid(row=2, column=1)

        self.win1.mainloop()


# -------------------------------------------------------------
def test():
    x = form1()


# -------------------------------------------------------------
def view():
    win2 = tkinter.Tk()
    t = tkinter.ttk.Treeview(win2, columns=("grpname", "desc"))
    t.heading("grpname", text="GROUP NAME")
    t.heading("desc", text="DESCRIPTION")
    rd = open(".\\group_record.txt", "r")
    i = 0
    while True:
        grp = rd.readline()
        if grp == "":
            break
        des = rd.readline()
        sep = rd.readline()
        t.insert("", i, values=(grp, des))
        i = i + 1
    t.pack()
    win2.mainloop()


# --------------------------------------------------------------
class form3:
    def insert(self):
        if self.textbox2.get() == "":
            tkinter.messagebox.showinfo("", "Number cannot be empty")
        if self.textbox2.get() != int:
            tkinter.messagebox.showinfo("","Number must contain digits only")

        if len(self.textbox2.get()) != 10:
            tkinter.messagebox.showinfo("", "Number must be of 10 digits")
        else:
            wr = open(".\\phones.txt", "a")
            wr.write(self.cb1.get())
            wr.write(self.textbox2.get())
            wr.write("\n*****\n")
            wr.close()
            tkinter.messagebox.showinfo("", "Member Added Sucessfully")

    def __init__(self):
        self.win = tkinter.Tk()

        self.lb1 = tkinter.Label(self.win, text="Enter Group Name")

        list1 = []

        fileopen = open(".\\group_record.txt", "r")

        i = 0

        while True:
            line = fileopen.readline()
            if line == "":
                break
            line1 = fileopen.readline()
            line2 = fileopen.readline()
            list1.insert(i, line)
            i = i + 1
        fileopen.close()

        self.cb1 = tkinter.ttk.Combobox(self.win, values=tuple(list1))

        self.lb2 = tkinter.Label(self.win, text="Enter Mobile Number")
        self.textbox2 = tkinter.Entry(self.win)

        self.bt1 = tkinter.Button(self.win, text="Add New Member", command=self.insert)

        self.lb1.grid(row=0, column=0)
        self.cb1.grid(row=0, column=1)

        self.lb2.grid(row=1, column=0)
        self.textbox2.grid(row=1, column=1)

        self.bt1.grid(row=2, column=1)

        self.win.mainloop()


# --------------------------------------------------------------
class form4:
    def send(self):

        n = self.messagebox1.get()
        list1 = n.split(" ")
        ans = ""
        for x in list1:
            ans = ans + x + "%20"

        for child in self.tree.get_children():
            temp = self.tree.item(child)["values"]
            num = str(temp[2])
            print(num)
            conn = http.client.HTTPConnection("server1.vmm.education")
            conn.request('GET', "/VMMCloudMessaging/AWS_SMS_Sender?username=dhk_py&password=GNEP0QCE&message=" + ans + "&phone_numbers=" + num + "")
            response = conn.getresponse()
            print(response.read())

    def insert(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        rd = open(".\\phones.txt", "r")
        i = 0
        while True:
            line = rd.readline()
            if line == "":
                break
            line2 = rd.readline()
            line3 = rd.readline()
            if line == self.cb1.get():
                self.tree.insert("", i, values=((i + 1), line, line2))
                i = i + 1

    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry("800x800")

        self.frame1 = tkinter.Frame(self.win)

        self.lb1 = tkinter.Label(self.frame1, text="Enter Group Name")

        list1 = []

        fileopen = open(".\\group_record.txt", "r")

        i = 0

        while True:
            line = fileopen.readline()
            if line == "":
                break
            line1 = fileopen.readline()
            line2 = fileopen.readline()
            list1.insert(i, line)
            i = i + 1
        fileopen.close()

        self.cb1 = tkinter.ttk.Combobox(self.frame1, values=tuple(list1))

        self.bt1 = tkinter.Button(self.frame1, text="Add New Member", command=self.insert)

        self.lb1.grid(row=0, column=0)
        self.cb1.grid(row=0, column=1)

        self.bt1.grid(row=0, column=3)

        self.frame1.pack()
        self.lb1 = tkinter.Label(self.win, text="Enter the Message")
        self.messagebox1 = tkinter.Entry(self.win)
        self.bt1 = tkinter.Button(self.win, text="Send Message", command=self.send)

        self.tree = tkinter.ttk.Treeview(self.win, columns=("srno", "groupname", "members"))
        self.tree.heading("srno", text="Serial Number")
        self.tree.heading("groupname", text="Group Name")
        self.tree.heading("members", text="Mobile Number")
        self.tree.pack()
        self.lb1.pack()
        self.messagebox1.pack()
        self.bt1.pack()

        self.win.mainloop()


# --------------------------------------------------------------
def show_phones():
    x = form4()


# -----------------------


def show_insert_data():
    x = form3()


root = tkinter.Tk()
mymenu = tkinter.Menu(root)
root.config(menu=mymenu)
submenu1 = tkinter.Menu(mymenu, tearoff=False)
mymenu.add_cascade(label="GROUP MANAGEMENT", menu=submenu1)
submenu1.add_command(label="ADD GROUP", command=test)
submenu1.add_command(label="VIEW GROUPS", command=view)
submenu1.add_command(label="Add Contacts", command=show_insert_data)
submenu1.add_command(label="View Contacts", command=show_phones)

root.mainloop()
