from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from no_ui_main import *
import datetime
import json

today = datetime.date.today()
current_year = today.year + 1


# defining
# controls rd entry, makes it so you can't input text and write more than 4 digits
def validate_rd(P):
    if len(P) == 0:
        return True
    elif len(P) < 5 and P.isdigit():
        return True
    else:
        return False


def validate_age(P):
    if len(P) == 0:
        return True
    elif len(P) < 3 and P.isdigit():
        return True
    else:
        return False


# controls date entry, makes it so you can't write a wrong date
def validate_dt(P):
    if not P == "DD/MM/YYYY":
        if len(P) == 0:
            return True
        elif len(P) < 3:
            try:
                if int(P[0:2]) < 32:
                    return True
                else:
                    return False
            except:
                return False
        elif len(P) > 2 and len(P) < 6 and P[2] == "/":
            try:
                if len(P) > 3:
                    if int(P[3:5]) < 13:
                        return True
                    else:
                        return False
                else:
                    return True
            except:
                return False
        elif len(P) > 5 and len(P) < 11 and P[2] == "/" and P[5] == "/":
            if len(P) == 10:
                try:
                    if int(P[6:11]) < current_year and int(P[6:11]) > 1999:
                        return True
                    else:
                        return False
                except:
                    return False
            else:
                return True
        else:
            return False
    else:
        return True


# controls time entry, makes it so you can't write an invalid time
def validate_tm(P):
    if not P == "HH:MM":
        if len(P) == 0:
            return True
        elif len(P) < 3:
            try:
                if int(P[0:2]) < 24:
                    return True
                else:
                    return False
            except:
                return False
        elif len(P) > 2 and len(P) < 6 and P[2] == ":":
            if len(P) == 5:
                try:
                    if int(P[3:5]) < 60:
                        return True
                    else:
                        return False
                except:
                    return False
            else:
                return True
        else:
            return False
    else:
        return True


# --- MAIN --- #
def main():
    # inner functions
    # removes temp text in the time entry
    def c_temp_time(e):
        if time_entry.get() == "HH:MM":
            time_entry.delete(0, END)

    # adds temp text in the time entry
    def a_temp_time(e):
        print(len(time_entry.get()))
        if time_entry.get() == "":
            time_entry.insert(0, "HH:MM")
        elif len(time_entry.get()) < 5:
            time_entry.delete(0, END)
            time_entry.insert(0, "HH:MM")

    # removes temp text in the date entry
    def c_temp_date(e):
        if date_entry.get() == "DD/MM/YYYY":
            date_entry.delete(0, END)

    # adds temp text in the date entry
    def a_temp_date(e):
        print(len(date_entry.get()))
        if date_entry.get() == "":
            date_entry.insert(0, "DD/MM/YYYY")
        elif len(date_entry.get()) < 10:
            date_entry.delete(0, END)
            date_entry.insert(0, "DD/MM/YYYY")

    # takes all the stuff from the entries/comboboxes and generates the template
    def submit():
        to_fill_in["DIVISION"] = selected_div.get()
        to_fill_in["DR"] = dr
        to_fill_in["FULL_NAME"] = fn_entry.get()
        to_fill_in["SEX"] = selected_sex.get()
        to_fill_in["AGE"] = age_entry.get()
        to_fill_in["LOCATION"] = lc_entry.get()
        to_fill_in["RD"] = rd_entry.get()
        to_fill_in["ETHNICITY"] = eth_entry.get()
        to_fill_in["HAIR"] = hair_entry.get()
        to_fill_in["TIME"] = time_entry.get()
        to_fill_in["DATE"] = date_entry.get()
        to_fill_in["OFFENSE"] = of_entry.get().upper()
        to_fill_in["WEAPONS"] = wp_entry.get()
        to_fill_in["DESCRIPTION"] = dsc_text.get("1.0", END)
        to_fill_in["DIVISION_CAPS"] = to_fill_in["DIVISION"].upper()
        # print(json.dumps(to_fill_in, sort_keys=True, indent=4))
        passed = False
        for k in to_fill_in:
            if to_fill_in[k] == "" or to_fill_in[k] == "\n" or to_fill_in[k] == "null" or to_fill_in[k] == "HH:MM" or to_fill_in[k] == "DD/MM/YYYY":
                messagebox.showerror("Incorrect input", f"Please fill in the {k} field.")
                passed = False
                break
            else:
                passed = True
        if passed:
            full_name = to_fill_in["FULL_NAME"]
            full_name_mugshot = full_name.lower().replace(" ", "_")
            mugshot = save_file()
            if not mugshot:
                messagebox.showwarning("No mugshot", f"Mugshot {full_name_mugshot}.png/jpg/jpeg was not found in mugshot/.")
            messagebox.showinfo("Complete", f"Wanted poster for {full_name} is complete.")
            

    # root
    root = Tk()
    root.title("WANTED!")
    root.resizable(False, False)
    root.minsize(250, 450)

    # icon
    icon = PhotoImage(file="icon.png")
    root.iconphoto(True, icon)

    # frame
    main_frame = Frame(root)

    # --- ROW 0 -- #
    r0_frame = Frame(main_frame)
    # division (label + combobox)
    selected_div = StringVar()
    divisions = [
        "Central",
        "South",
        "Valley",
        "West",
    ]
    div_label = Label(r0_frame, text="Division:", pady=7)
    div_label.grid(row=0, column=0, padx=(0, 7))
    div_dropdown = ttk.Combobox(
        r0_frame, values=divisions, width=7, textvariable=selected_div
    )
    div_dropdown["state"] = "readonly"
    div_dropdown.grid(row=0, column=1, pady=7)

    # rd (label + stringvar)
    temp_frame = Frame(r0_frame, width=20).grid(row=0, column=2)
    dr = create_dr()
    dr_label = Label(r0_frame, text=f"DR: {dr}")
    dr_label.grid(row=0, column=3)
    # --- ROW 0 END --- #
    r0_frame.grid(row=0, column=0)

    # --- ROW 1 -- #
    r1_frame = Frame(main_frame)
    # full name (label + entry)
    fn_label = Label(r1_frame, text="Full name:  ")
    fn_label.grid(row=0, column=0)
    fn_entry = Entry(r1_frame)
    fn_entry.config(width=27)
    fn_entry.grid(row=0, column=1)
    # --- ROW 1 END --- #
    r1_frame.grid(row=1, column=0)

    # --- ROW 2 --- #
    r2_frame = Frame(main_frame)
    # sex (label + combobox)
    sex_label = Label(r2_frame, text="Sex: ", padx=7).grid(row=0, column=0)
    sexes = [
        "Male",
        "Female",
        "Unknown",
    ]
    selected_sex = StringVar()
    sex_dropdown = ttk.Combobox(
        r2_frame, values=sexes, textvariable=selected_sex, width=9
    ).grid(row=0, column=1, pady=7)

    # age (label + entry)
    temp_frame2 = Frame(r2_frame, width=50).grid(row=0, column=2)
    age_label = Label(r2_frame, text="Age:").grid(row=0, column=3, padx=(5, 0))
    vcmd_age = (root.register(validate_age), "%P")
    age_entry = Entry(r2_frame, width=4, validate="key", validatecommand=vcmd_age)
    age_entry.grid(row=0, column=4, padx=7)
    # --- ROW 2 END --- #
    r2_frame.grid(row=2, column=0)

    # --- ROW 3 --- #
    r3_frame = Frame(main_frame)
    # location (label + entry)
    lc_label = Label(r3_frame, text="Location: ").grid(row=0, column=0)
    lc_entry = Entry(r3_frame, width=18)
    lc_entry.grid(row=0, column=1)

    # rd (label + entry)
    rd_label = Label(r3_frame, text="RD#: ").grid(row=0, column=2)
    vcmd_rd = (root.register(validate_rd), "%P")
    rd_entry = Entry(r3_frame, width=4, validate="key", validatecommand=vcmd_rd)
    rd_entry.grid(row=0, column=3)
    # --- ROW 3 END --- #
    r3_frame.grid(row=3, column=0)

    # --- ROW 4 --- #
    r4_frame = Frame(main_frame)
    # ethnicity (label + entry)
    eth_label = Label(r4_frame, text="Ethnicity: ").grid(row=0, column=0)
    eth_entry = Entry(r4_frame, width=11)
    eth_entry.grid(row=0, column=1)

    # hair (label + entry)
    hair_label = Label(r4_frame, text="Hair: ").grid(row=0, column=2)
    hair_entry = Entry(r4_frame, width=11)
    hair_entry.grid(row=0, column=3, pady=7)
    # --- ROW 4 END --- #
    r4_frame.grid(row=4, column=0)

    # --- ROW 5 --- #
    r5_frame = Frame(main_frame)
    temp_frame3 = Frame(r5_frame, width=30).grid(row=0, column=2)
    # time (label + entry)
    time_label = Label(r5_frame, text="Time: ").grid(row=0, column=0)
    vcmd_tm = (root.register(validate_tm), "%P")
    time_entry = Entry(r5_frame, width=7, validate="key", validatecommand=vcmd_tm)
    time_entry.insert(0, "HH:MM")
    time_entry.bind("<FocusIn>", c_temp_time)
    time_entry.bind("<FocusOut>", a_temp_time)
    time_entry.grid(row=0, column=1)
    # date (label + entry)
    date_label = Label(r5_frame, text="Date: ").grid(row=0, column=3)
    vcmd_dt = (root.register(validate_dt), "%P")
    date_entry = Entry(r5_frame, width=13, validate="key", validatecommand=vcmd_dt)
    date_entry.insert(0, "DD/MM/YYYY")
    date_entry.bind("<FocusIn>", c_temp_date)
    date_entry.bind("<FocusOut>", a_temp_date)
    date_entry.grid(row=0, column=4)
    # --- ROW 5 END --- #
    r5_frame.grid(row=5, column=0)

    # --- ROW 6 --- #
    r6_frame = Frame(main_frame)
    # offense (label + entry)
    of_label = Label(r6_frame, text="Offense: ").grid(row=0, column=0)
    of_entry = Entry(r6_frame, width=29)
    of_entry.grid(row=0, column=1, pady=(7,0))
    # --- ROW 6 END --- #
    r6_frame.grid(row=6, column=0)

    # --- ROW 7 --- #
    r7_frame = Frame(main_frame)
    # weapons (label + entry)
    wp_label = Label(r7_frame, text="Weapon(s): ").grid(row=0, column=0, pady=(0,7))
    wp_entry = Entry(r7_frame, width=26)
    wp_entry.grid(row=0, column=1)
    # --- ROW 7 END --- #
    r7_frame.grid(row=7, column=0)

    # --- ROW 8 --- #
    r8_frame = Frame(main_frame)
    # description (label + text + button)
    dsc_label = Label(r8_frame, text="Description: ").pack(side=TOP, anchor=NW)
    dsc_text = Text(r8_frame, width=38, height=12, wrap=WORD)
    dsc_text.config(font="Calibri 9")
    dsc_text.pack(side=TOP)
    dsc_button = Button(r8_frame, text="Generate!", command=submit).pack(
        side=TOP, pady=7
    )
    # --- ROW 8 END --- #
    r8_frame.grid(row=8, column=0)

    # frame end
    main_frame.grid(row=0, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()


# ---------------------------------------------- #
#  Division: (dropdown) DR: (checkbox if random, if not - entry)
#  Full name: | (entry)                         |#
#  Sex: (dropdown) Age: |(entry)|                #
#  Location: |(entry)             | RD: |(entry)|#
#  Ethnicity: |(entry)    | Hair: |(entry)      |#
#  Time: |(entry)|       Date: |(entry)         |#
#  Offense: |(entry)                            |#
#  Weapons: |(entry)                            |#
#  Description:                                  #
# |(entry)                                      |#
# |                                             |#
# |                                             |#
# |                                             |#
# |                                             |#
# |                                             |#
# ---------------------------------------------- #
#               (button submit)                  #
# ---------------------------------------------- #
