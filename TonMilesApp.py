from functions import *
from tkinter import *
from datetime import *
from tkinter import messagebox
import pandas as pd

# -----------GLOBAL VARIABLES ------------
drilling_miles_total = 0
tripping_miles_total = 0
casing_miles_total = 0
liner_miles_total = 0
jarring_miles_total = 0
total_miles_result = 0
FORMATTED_DATE = 0
COMMENTS = ''


# -------------------------SUBMIT CONFIRM WARNING BOX ---------------------
def submit_warning():
    if date_bottom_value.cget('text') != FORMATTED_DATE:
        messagebox.showwarning("Date Not Committed!", "Please Commit the Date on top by clicking 'Submit'.")
        return
    confirm = messagebox.askokcancel('Confirm!', 'You are about to enter the ton-miles '
                                                 'for the day to the CSV file. Continue?')
    if confirm:
        store_ton_miles_data()
    else:
        return


# ---------------------------SEND DATA TO CSV FILE---------------------------------------
def store_ton_miles_data():
    global FORMATTED_DATE, drilling_miles_total, tripping_miles_total, casing_miles_total, liner_miles_total, \
        jarring_miles_total, total_miles_result, COMMENTS
    COMMENTS = comments_box.get('1.0', END)
    rig_name_entered = rig_name_entry.get()
    get_total_miles()
    new_entry = [rig_name_entered, FORMATTED_DATE, f'{drilling_miles_total:.2f}', f'{tripping_miles_total:.2f}', f'{casing_miles_total:.2f}',
                 f'{liner_miles_total:.2f}', f'{jarring_miles_total:.2f}', total_miles_result, COMMENTS]

    data = pd.read_csv('ton_miles_record.csv')
    if data['Date'].values.any() == FORMATTED_DATE:
        duplicate = messagebox.askyesnocancel('Oops! An Entry for this Date Already Exists!',
                                              'To go back & check the date you have entered, press CANCEL. '
                                              'If you wish to replace the previous entry, press YES. If you wish '
                                              'to create an extra entry with the same date, press NO.')

        if duplicate:
            location = data[data['Date'] == FORMATTED_DATE].index.values[0]
            data.loc[
                location, ['RigName', 'Date', 'DrillingMiles', 'TrippingMiles', 'CasingMiles', 'LinerMiles', 'JarringMiles',
                           'TotalMiles', 'Comments']
            ] = new_entry
            data.to_csv('ton_miles_record.csv', index=False, mode='w', header='column_names')
            return
        if duplicate is False:
            pass
        if duplicate is None:
            return
    try:
        last_index = [data.index[-1]]
        new_index = last_index[0] + 1
    except IndexError:
        new_index = 1
    new_entry = [new_entry]
    new_data = pd.DataFrame(new_entry, index=[new_index])
    new_data.to_csv('ton_miles_record.csv', index=True, mode='a', header=False)



# ----------------------TON MILES TOTAL---------------------------------------
def get_total_miles():
    global total_miles_result
    drill_result = float(drilling_miles_result_value.cget('text'))
    trip_result = float(tripping_miles_result_value.cget('text'))
    csg_result = float(casing_miles_result_value.cget('text'))
    liner_result = float(liner_miles_result_value.cget('text'))
    jarring_result = float(jarring_miles_result_value.cget('text'))
    total_miles_result = drill_result + trip_result + csg_result + liner_result + jarring_result
    total_miles_result_value.config(text=total_miles_result)


# -----------CLEAR FRAME FUNCTION----------------------------------------
def clear_btm_frame():
    for widget in bottom_frame.winfo_children():
        widget.destroy()


def clear_canvas_frame():
    # destroy all widgets from frame
    for widget in canvas_frame.winfo_children():
        widget.destroy()




# -----------DATE SUBMIT FUNCTION-------------------------------------------
def submit_date():
    global dd, mm, yyyy, FORMATTED_DATE
    try:
        dd = int(dd_entry.get().strip())
        mm = int(mm_entry.get().strip())
        yyyy = int(yy_entry.get().strip())
        FORMATTED_DATE = date(day=dd, month=mm, year=yyyy).strftime('%d %B %Y')
        top_entry_confirm.config(text=f"Rig: {rig_name_entry.get()} | Choose the options below"
                                      f" to enter data for: {FORMATTED_DATE}.")
        date_bottom_value.config(text=FORMATTED_DATE)

    except ValueError:
        messagebox.showerror(title="Invalid Input!", message="Please enter only numbers in DD, MM, YYYY format.")


# ----------------------CHANGE BUTTON COLORS DEPENDING ON USER CHOICE ---------------------------------------------
def change_button_colors(active_button, button2, button3, button4, button5):
    active_button.config(bg='#3EDBF0')
    button2.config(bg='#77ACF1')
    button3.config(bg='#77ACF1')
    button4.config(bg='#77ACF1')
    button5.config(bg='#77ACF1')


# ----------------DRILLING TON MILES BUTTON FUNCTION --------------------------------------------------------------
def drilling_ton_miles_ui():
    clear_canvas_frame()
    change_button_colors(drilling_button, tripping_button, casing_button, liner_button, jarring_button)

    # ----------------- TAKE DATA AND PUT IT INSIDE CALCULATE FUNCTION IN FUNCTION.PY------------------------
    def drill_miles_data():
        global BF, BLOCK_WT, drilling_miles_total
        BLOCK_WT = float(block_wt_label_entry.get().strip()) / 2000
        MUD_WT = float(mud_wt_label_entry.get().strip())
        BF = (65.44 - MUD_WT) / 65.44
        start_depth = float(drilling_text1.get().strip())
        end_depth = float(drilling_text2.get().strip())
        drilled_depth = end_depth - start_depth

        dc1_length = float(bha_text_dc1.get().strip())
        dc1_ppf = float(dc1_weight_text.get().strip())
        dc1_bw = calculate_boyed_weight(dc1_length, dc1_ppf, BF)

        dc2_length = float(bha_text_dc2.get().strip())
        dc2_ppf = float(dc2_weight_text.get().strip())
        dc2_bw = calculate_boyed_weight(dc2_length, dc2_ppf, BF)

        hwdp_length = float(bha_text_hwdp.get().strip())
        hwdp_ppf = float(hwdp_weight_text.get().strip())
        hwdp_bw = calculate_boyed_weight(hwdp_length, hwdp_ppf, BF)

        dp1_length = float(bha_text_dp1.get().strip())
        dp1_ppf = float(dp1_weight_text.get().strip())
        dp1_bw = calculate_boyed_weight(dp1_length, dp1_ppf, BF)

        dp2_length_start = (start_depth - dc1_length - dc2_length - hwdp_length - dp1_length)
        dp2_ppf = float(dp2_weight_text.get().strip())
        # -------------- AUTO-FILL SECOND STRING OF DRILL-PIPE BASED ON DEPTH ENTERED ----------------
        if dp2_length_start > 0:
            bha_dp2_value.config(text=dp2_length_start)
            dp2_bw_start = calculate_boyed_weight(dp2_length_start, dp2_ppf, BF)
        else:
            bha_dp2_value.config(text=0)
            dp2_bw_start = 0
        dp2_length_end = (end_depth - dc1_length - dc2_length - hwdp_length - dp1_length)

        if dp2_length_end > 0:
            bha_dp2_value_end.config(text=dp2_length_end)
            dp2_bw_end = calculate_boyed_weight(dp2_length_end, dp2_ppf, BF)
        else:
            bha_dp2_value_end.config(text=0)
            dp2_bw_end = 0
        # ______________________________________________________

        total_str_wt_depth1 = cal_total_wt(dc1_bw, dc2_bw, hwdp_bw, dp1_bw, dp2_bw_start)
        total_str_wt_depth2 = cal_total_wt(dc1_bw, dc2_bw, hwdp_bw, dp1_bw, dp2_bw_end)
        total_str_wt_avg_tons = (total_str_wt_depth1 + total_str_wt_depth2) / 2
        ream = float(drilling_text4.get().strip())
        drilling_miles_total = calculate_drill_miles(drilled_depth, BLOCK_WT, total_str_wt_avg_tons, ream)

        # ______________________ RESULT LABELS _________________________________
        drilling_miles_result_value.config(text=f'{drilling_miles_total:.2f}')  # ---> SEND DATA TO BTM FRAME
        get_total_miles()  # ----------ADDING MILES TO TOTAL MILES

    # ------------------------------DRILLING UI ELEMENTS----------------------------------------------------
    drilling_label1 = Label(canvas_frame, text="Drill From: ", fg='black', bg='#9BA4B4')
    drilling_label1.grid(row=3, column=0, sticky='e', padx=5)
    drilling_text1 = Entry(canvas_frame, foreground='black')
    drilling_text1.insert(END, string=0)
    drilling_text1.grid(row=3, column=1, sticky='w', padx=5)

    drilling_label2 = Label(canvas_frame, text="To: ", fg='black', bg='#9BA4B4')
    drilling_label2.grid(row=3, column=2, sticky='e', padx=5)
    drilling_text2 = Entry(canvas_frame, foreground='black')
    drilling_text2.insert(END, string=0)
    drilling_text2.grid(row=3, column=3, sticky='w', padx=5)

    drilling_label3 = Label(canvas_frame, text="No. of times reamed stand: ", fg='black', bg='#9BA4B4')
    drilling_label3.grid(row=3, column=4, sticky='ew', padx=5, columnspan=4)
    drilling_text4 = Entry(canvas_frame, foreground='black', width=6)
    drilling_text4.insert(END, string=0)
    drilling_text4.grid(row=3, column=5, sticky='ew', padx=10, columnspan=5)

    # ---------DRILLING BHA Elements--------------------
    bha_title = Label(canvas_frame, text="BHA Details: ", fg='#0A1931', bg='#9BA4B4', font=('serif', 14, 'bold'))
    bha_title.grid(row=4, column=0, pady=10)
    # ----DC1---------------------
    bha_label_dc1 = Label(canvas_frame, text="DC#1 (Bottom): ", fg='black', bg='#9BA4B4')
    bha_label_dc1.grid(row=5, column=0, sticky='w', padx=5)
    bha_text_dc1 = Entry(canvas_frame, foreground='black')
    bha_text_dc1.insert(END, string=0)
    bha_text_dc1.grid(row=5, column=1, sticky='w', padx=5)

    dc1_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dc1_weight_label.grid(row=5, column=2, sticky='e', padx=5)

    dc1_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dc1_weight_text.insert(END, string=0)
    dc1_weight_text.grid(row=5, column=3, sticky='w')
    # ----DC2---------------------
    bha_label_dc2 = Label(canvas_frame, text="DC#2 (Top): ", fg='black', bg='#9BA4B4')
    bha_label_dc2.grid(row=6, column=0, sticky='w', padx=5)
    bha_text_dc2 = Entry(canvas_frame, foreground='black')
    bha_text_dc2.insert(END, string=0)
    bha_text_dc2.grid(row=6, column=1, sticky='w', padx=5)

    dc2_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dc2_weight_label.grid(row=6, column=2, sticky='e', padx=5)

    dc2_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dc2_weight_text.insert(END, string=0)
    dc2_weight_text.grid(row=6, column=3, sticky='w')
    # ---------HWDP--------------
    bha_label_hwdp = Label(canvas_frame, text="HWDP: ", fg='black', bg='#9BA4B4')
    bha_label_hwdp.grid(row=7, column=0, sticky='w', padx=5)
    bha_text_hwdp = Entry(canvas_frame, foreground='black')
    bha_text_hwdp.insert(END, string=0)
    bha_text_hwdp.grid(row=7, column=1, sticky='w', padx=5)
    hwdp_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    hwdp_weight_label.grid(row=7, column=2, sticky='e', padx=5)
    hwdp_weight_text = Entry(canvas_frame, foreground='black', width=5)
    hwdp_weight_text.insert(END, string=0)
    hwdp_weight_text.grid(row=7, column=3, sticky='w')
    # ---------DP1 (Bottom)--------------
    bha_label_dp1 = Label(canvas_frame, text="Drill Pipe (Bottom): ", fg='black', bg='#9BA4B4')
    bha_label_dp1.grid(row=8, column=0, sticky='w', padx=5)
    bha_text_dp1 = Entry(canvas_frame, foreground='black')
    bha_text_dp1.insert(END, string=0)
    bha_text_dp1.grid(row=8, column=1, sticky='w', padx=5)
    dp1_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dp1_weight_label.grid(row=8, column=2, sticky='e', padx=5)
    dp1_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dp1_weight_text.insert(END, string=0)
    dp1_weight_text.grid(row=8, column=3, sticky='w')
    # ---------DP2 (Top)START--------------
    bha_label_dp2 = Label(canvas_frame, text="Drill Pipe (Top) @ start of section: ", fg='black', bg='#9BA4B4')
    bha_label_dp2.grid(row=9, column=0, sticky='w', padx=5)
    bha_dp2_value = Label(canvas_frame, text="0", fg='#0A1931', bg='#77ACF1')
    bha_dp2_value.grid(row=9, column=1, sticky='w', padx=5)
    dp2_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dp2_weight_label.grid(row=9, column=2, sticky='e', padx=5)
    dp2_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dp2_weight_text.insert(END, string=0)
    dp2_weight_text.grid(row=9, column=3, sticky='w')
    dp2_warning_label = Label(canvas_frame, text="(Enter only if you're using 2 types of Drill Pipe in string)",
                              fg='black', bg='#9BA4B4')
    dp2_warning_label.grid(row=9, column=4, sticky='w', padx=5)
    # -----------DP2 (TOP)END-----------------------
    bha_label_dp2_end = Label(canvas_frame, text="Drill Pipe (Top) @ end of section: ", fg='black', bg='#9BA4B4')
    bha_label_dp2_end.grid(row=10, column=0, sticky='w', padx=5)
    bha_dp2_value_end = Label(canvas_frame, text="0", fg='#0A1931', bg='#77ACF1')
    bha_dp2_value_end.grid(row=10, column=1, sticky='w', padx=5)
    # ----------COMPUTE BUTTON TO CALCULATE DATA & SEND DATA TO BOTTOM FRAME---------------
    compute_button = Button(canvas_frame, text='Compute Drilling Miles', bg='#77ACF1', width=30,
                            command=drill_miles_data)
    compute_button.grid(row=10, column=2, sticky='w', pady=10, columnspan=3)


# ------------------------------------------------------------------------------------------------------------------


# --------------TRIPPING TON MILES BUTTON FUNCTION------------------------------------------------------------------
def tripping_ton_miles_ui():
    clear_canvas_frame()
    change_button_colors(tripping_button, drilling_button, casing_button, liner_button, jarring_button)

    # _______________________CALCULATE TRIPPING TON MILES________________________
    def trip_miles_data():
        global BF, BLOCK_WT, tripping_miles_total
        BLOCK_WT = float(block_wt_label_entry.get().strip()) / 2000
        MUD_WT = float(mud_wt_label_entry.get().strip())
        BF = (65.44 - MUD_WT) / 65.44
        start_depth = float(tripping_text1.get().strip())
        end_depth = float(tripping_text2.get().strip())
        total_depth = end_depth - start_depth

        dc1_trip_length = float(bha_text_dc1.get().strip())
        dc1_trip_ppf = float(dc1_weight_text.get().strip())
        dc1_trip_bw = calculate_boyed_weight(dc1_trip_length, dc1_trip_ppf, BF)

        dc2_trip_length = float(bha_text_dc2.get().strip())
        dc2_trip_ppf = float(dc2_weight_text.get().strip())
        dc2_trip_bw = calculate_boyed_weight(dc2_trip_length, dc2_trip_ppf, BF)

        hwdp_trip_length = float(bha_text_hwdp.get().strip())
        hwdp_trip_ppf = float(hwdp_weight_text.get().strip())
        hwdp_trip_bw = calculate_boyed_weight(hwdp_trip_length, hwdp_trip_ppf, BF)

        dp1_trip_length = float(bha_text_dp1.get().strip())
        dp1_trip_ppf = float(dp1_weight_text.get().strip())
        dp1_trip_bw = calculate_boyed_weight(dp1_trip_length, dp1_trip_ppf, BF)

        dp2_trip_length = (total_depth - dc1_trip_length - dc2_trip_length - hwdp_trip_length - dp1_trip_length)
        dp2_trip_ppf = float(dp2_weight_text.get().strip())

        # -------------- AUTO-FILL SECOND STRING OF DRILL-PIPE BASED ON DEPTH ENTERED ----------------
        if dp2_trip_length > 0:
            bha_dp2_value.config(text=dp2_trip_length)
            dp2_trip_bw = calculate_boyed_weight(dp2_trip_length, dp2_trip_ppf, BF)
        else:
            bha_dp2_value.config(text=0)
            dp2_trip_bw = 0
        bha_wt = cal_total_wt(dc1_trip_bw, dc2_trip_bw, hwdp_trip_bw)
        tripping_miles_total = calculate_trip_miles(dc1_trip_length, dc2_trip_length, hwdp_trip_length, bha_wt,
                                                    dp1_trip_length, dp2_trip_length, dp2_trip_bw, dp1_trip_bw,
                                                    total_depth, BLOCK_WT)
        # ______________________ RESULT LABELS _________________________________
        if radio_state.get() == 1:
            tripping_miles_result_value.config(text=f'{tripping_miles_total:.2f}')  # ---> SEND DATA TO BTM FRAME
            get_total_miles()  # ----------ADDING MILES TO TOTAL MILES
        elif radio_state.get() == 2:
            tripping_miles_total *= 2
            tripping_miles_result_value.config(text=f'{tripping_miles_total:.2f}')  # ---> SEND DATA TO BTM FRAME
            get_total_miles()  # ----------ADDING MILES TO TOTAL MILES
        else:
            messagebox.showerror(title="Radio Button Unchecked!", message="Please select Single or Round Trip.")

    # ------------------------UI ELEMENTS------------------------------------
    tripping_label1 = Label(canvas_frame, text="Trip From (depth#1): ", fg='black', bg='#9BA4B4')
    tripping_label1.grid(row=3, column=0, sticky='w', padx=5)
    tripping_text1 = Entry(canvas_frame, foreground='black')
    tripping_text1.insert(END, string=0)
    tripping_text1.grid(row=3, column=1, sticky='e', padx=5)

    tripping_label2 = Label(canvas_frame, text="To (depth#2): ", fg='black', bg='#9BA4B4')
    tripping_label2.grid(row=3, column=2, sticky='e', padx=5)
    tripping_text2 = Entry(canvas_frame, foreground='black')
    tripping_text2.insert(END, string=0)
    tripping_text2.grid(row=3, column=3, sticky='e', padx=5)

    radio_state = IntVar()
    radiobutton1 = Radiobutton(canvas_frame, text="Single Trip", value=1, variable=radio_state, bg='#9BA4B4')
    radiobutton2 = Radiobutton(canvas_frame, text="Round Trip", value=2, variable=radio_state, bg='#9BA4B4')
    radiobutton1.grid(row=3, column=4, sticky='w')
    radiobutton2.grid(row=4, column=4, sticky='w')

    # ---------BHA Elements--------------------
    bha_title = Label(canvas_frame, text="BHA Details: ", fg='#0A1931', bg='#9BA4B4', font=('serif', 14, 'bold'))
    bha_title.grid(row=4, column=0, pady=10)
    # ----DC1---------------------
    bha_label_dc1 = Label(canvas_frame, text="DC#1 (Bottom): ", fg='black', bg='#9BA4B4')
    bha_label_dc1.grid(row=5, column=0, sticky='w', padx=5)
    bha_text_dc1 = Entry(canvas_frame, foreground='black')
    bha_text_dc1.insert(END, string=0)
    bha_text_dc1.grid(row=5, column=1, sticky='w', padx=5)

    dc1_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dc1_weight_label.grid(row=5, column=2, sticky='e', padx=5)

    dc1_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dc1_weight_text.insert(END, string=0)
    dc1_weight_text.grid(row=5, column=3, sticky='w')
    # ----DC2---------------------
    bha_label_dc2 = Label(canvas_frame, text="DC#2 (Top): ", fg='black', bg='#9BA4B4')
    bha_label_dc2.grid(row=6, column=0, sticky='w', padx=5)
    bha_text_dc2 = Entry(canvas_frame, foreground='black')
    bha_text_dc2.insert(END, string=0)
    bha_text_dc2.grid(row=6, column=1, sticky='w', padx=5)

    dc2_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dc2_weight_label.grid(row=6, column=2, sticky='e', padx=5)

    dc2_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dc2_weight_text.insert(END, string=0)
    dc2_weight_text.grid(row=6, column=3, sticky='w')
    # ---------HWDP--------------
    bha_label_hwdp = Label(canvas_frame, text="HWDP: ", fg='black', bg='#9BA4B4')
    bha_label_hwdp.grid(row=7, column=0, sticky='w', padx=5)
    bha_text_hwdp = Entry(canvas_frame, foreground='black')
    bha_text_hwdp.insert(END, string=0)
    bha_text_hwdp.grid(row=7, column=1, sticky='w', padx=5)
    hwdp_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    hwdp_weight_label.grid(row=7, column=2, sticky='e', padx=5)
    hwdp_weight_text = Entry(canvas_frame, foreground='black', width=5)
    hwdp_weight_text.insert(END, string=0)
    hwdp_weight_text.grid(row=7, column=3, sticky='w')
    # ---------DP1 (Bottom)--------------
    bha_label_dp1 = Label(canvas_frame, text="Drill Pipe (Bottom): ", fg='black', bg='#9BA4B4')
    bha_label_dp1.grid(row=8, column=0, sticky='w', padx=5)
    bha_text_dp1 = Entry(canvas_frame, foreground='black')
    bha_text_dp1.insert(END, string=0)
    bha_text_dp1.grid(row=8, column=1, sticky='w', padx=5)
    dp1_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dp1_weight_label.grid(row=8, column=2, sticky='e', padx=5)
    dp1_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dp1_weight_text.insert(END, string=0)
    dp1_weight_text.grid(row=8, column=3, sticky='w')
    # ---------DP2 (Top)START--------------
    bha_label_dp2 = Label(canvas_frame, text="Drill Pipe (At the Top): ", fg='black', bg='#9BA4B4')
    bha_label_dp2.grid(row=9, column=0, sticky='w', padx=5)
    bha_dp2_value = Label(canvas_frame, text="0", fg='#0A1931', bg='#77ACF1')
    bha_dp2_value.grid(row=9, column=1, sticky='w', padx=5)
    dp2_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    dp2_weight_label.grid(row=9, column=2, sticky='e', padx=5)
    dp2_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dp2_weight_text.insert(END, string=0)
    dp2_weight_text.grid(row=9, column=3, sticky='w')
    dp2_warning_label = Label(canvas_frame, text="(Enter only if you're using 2 types of Drill Pipe in string)",
                              fg='black', bg='#9BA4B4')
    dp2_warning_label.grid(row=9, column=4, sticky='w', padx=5)
    # ---------------COMPUTE TRIPPING MILES AND SEND DATA TO BTM FRAME-------------------------------------------
    compute_button = Button(canvas_frame, text='Compute Tripping Miles', bg='#77ACF1', width=30,
                            command=trip_miles_data)
    compute_button.grid(row=10, column=2, sticky='w', pady=10, columnspan=3)
    # ---------------------------------------------------------------


# ---------------------------CASING TON MILES BUTTON FUNCTION -----------------------------------------------------
def casing_ton_miles_ui():
    clear_canvas_frame()
    change_button_colors(casing_button, tripping_button, drilling_button, liner_button, jarring_button)

    # -------------------CALCULATE CASING TON MILES------------------------------------------
    def casing_miles_data():
        global BF, BLOCK_WT, casing_miles_total
        BLOCK_WT = float(block_wt_label_entry.get().strip()) / 2000
        MUD_WT = float(mud_wt_label_entry.get().strip())
        BF = (65.44 - MUD_WT) / 65.44
        shoe_depth = float(depth_text1.get().strip())
        lower_csg_length = float(bha_text_lower_csg.get().strip())
        lower_csg_ppf = float(lower_csg_weight_text.get().strip())
        lower_csg_bw = calculate_boyed_weight(lower_csg_length, lower_csg_ppf, BF)

        mid_csg_length = float(bha_text_mid_csg.get().strip())
        mid_csg_ppf = float(mid_csg_weight_text.get().strip())
        mid_csg_bw = calculate_boyed_weight(mid_csg_length, mid_csg_ppf, BF)

        top_csg_length = shoe_depth - lower_csg_length - mid_csg_length
        top_csg_ppf = float(mid_csg_weight_text.get().strip())

        if top_csg_length > 0:
            bha_value_top_csg.config(text=f'{top_csg_length}')
            top_csg_bw = calculate_boyed_weight(top_csg_length, top_csg_ppf, BF)
        else:
            bha_value_top_csg.config(text=f'{0}')
            top_csg_bw = 0

        casing_miles_total = calculate_casing_miles(lower_csg_length, mid_csg_length, top_csg_length, lower_csg_bw,
                                                    mid_csg_bw, top_csg_bw, shoe_depth, BLOCK_WT)

        casing_miles_result_value.config(text=f'{casing_miles_total:.2f}')  # ---> SEND DATA TO BTM FRAME
        get_total_miles()  # ----------ADDING MILES TO TOTAL MILES

    # __________________________________UI ELEMENTS FOR CASING ------------------------------------------
    note_label1 = Label(canvas_frame, text="Note: 1. If you are running casing on DP use 'Top Casing' "
                                           "as your DP string.", fg='black', bg='#9BA4B4', wraplength=600)
    note_label1.grid(row=2, column=0, sticky='w', padx=5, columnspan=6)

    note_label2 = Label(canvas_frame,
                        text="2. If only one casing string is being run all the way, only enter shoe depth"
                             " and weight for 'Top Casing'.", fg='black', bg='#9BA4B4', wraplength=600)
    note_label2.grid(row=3, column=0, sticky='e', padx=35, columnspan=6)
    depth_label1 = Label(canvas_frame, text="Shoe Setting Depth: ", fg='black', bg='#9BA4B4')
    depth_label1.grid(row=4, column=0, sticky='w', padx=5)
    depth_text1 = Entry(canvas_frame, foreground='black')
    depth_text1.insert(END, string=0)
    depth_text1.grid(row=4, column=1, sticky='w', padx=5)

    # ---------BHA Elements--------------------
    bha_title = Label(canvas_frame, text="BHA Details: ", fg='#0A1931', bg='#9BA4B4', font=('serif', 14, 'bold'))
    bha_title.grid(row=5, column=0, pady=10)
    # ----LOWER CSG---------------------
    bha_label_lower_csg = Label(canvas_frame, text="Lower Casing String: ", fg='black', bg='#9BA4B4')
    bha_label_lower_csg.grid(row=6, column=0, sticky='w', padx=5)
    bha_text_lower_csg = Entry(canvas_frame, foreground='black')
    bha_text_lower_csg.insert(END, string=0)
    bha_text_lower_csg.grid(row=6, column=1, sticky='w', padx=5)
    lower_csg_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    lower_csg_weight_label.grid(row=6, column=2, sticky='e', padx=5)
    lower_csg_weight_text = Entry(canvas_frame, foreground='black', width=5)
    lower_csg_weight_text.insert(END, string=0)
    lower_csg_weight_text.grid(row=6, column=3, sticky='w')
    # --------- MID CSG ----------------
    bha_label_mid_csg = Label(canvas_frame, text="Mid Casing String: ", fg='black', bg='#9BA4B4')
    bha_label_mid_csg.grid(row=7, column=0, sticky='w', padx=5)
    bha_text_mid_csg = Entry(canvas_frame, foreground='black')
    bha_text_mid_csg.insert(END, string=0)
    bha_text_mid_csg.grid(row=7, column=1, sticky='w', padx=5)
    mid_csg_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    mid_csg_weight_label.grid(row=7, column=2, sticky='e', padx=5)
    mid_csg_weight_text = Entry(canvas_frame, foreground='black', width=5)
    mid_csg_weight_text.insert(END, string=0)
    mid_csg_weight_text.grid(row=7, column=3, sticky='w')
    # --------- TOP CSG -----------------
    bha_label_top_csg = Label(canvas_frame, text="Top Casing/Landing String: ", fg='black', bg='#9BA4B4')
    bha_label_top_csg.grid(row=8, column=0, sticky='w', padx=5)
    bha_value_top_csg = Label(canvas_frame, text="0", fg='#0A1931', bg='#77ACF1')
    bha_value_top_csg.grid(row=8, column=1, sticky='w', padx=5)
    top_csg_weight_label = Label(canvas_frame, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
    top_csg_weight_label.grid(row=8, column=2, sticky='e', padx=5)
    top_csg_weight_text = Entry(canvas_frame, foreground='black', width=5)
    top_csg_weight_text.insert(END, string=0)
    top_csg_weight_text.grid(row=8, column=3, sticky='w')
    # ---------------------------------------------------------------
    compute_button = Button(canvas_frame, text='Compute Casing Miles', bg='#77ACF1', width=30,
                            command=casing_miles_data)
    compute_button.grid(row=9, column=2, sticky='w', pady=10, columnspan=3)
    # ---------------------------------------------------------------
    # -----------------JARRING UI -----------------------------------------------------------------------


def jarring_tonmiles_ui():
    clear_canvas_frame()
    change_button_colors(jarring_button, casing_button, tripping_button, drilling_button, liner_button)

    def jarring_ton_miles_data():
        global jarring_miles_total
        top_reading = float(top_reading_text.get().strip())
        btm_reading = float(btm_reading_text.get().strip())
        dist_trav = float(distance_text.get().strip())
        strokes_per_hr = float(number_text.get().strip())
        hrs_jarring = float(hours_text.get().strip())
        weight_tons = ((top_reading + btm_reading) / 2) / 2000
        jarring_miles_total = jarring_miles(dist_trav, weight_tons, strokes_per_hr, hrs_jarring)

        jarring_miles_result_value.config(text=f'{jarring_miles_total:.2f}')
        get_total_miles()  # ----------ADDING MILES TO TOTAL MILES

    jar_title = Label(canvas_frame, text="Jarring Details: ", fg='#0A1931', bg='#9BA4B4', font=('serif', 14, 'bold'))
    jar_title.grid(row=1, column=0, pady=10)

    top_reading_label = Label(canvas_frame, text="Weight Indicator Reading @ Top of Up-Stroke: ", fg='black',
                              bg='#9BA4B4')
    top_reading_label.grid(row=2, column=0, sticky='w', padx=5)
    top_reading_text = Entry(canvas_frame, foreground='black')
    top_reading_text.insert(END, string=0)
    top_reading_text.grid(row=2, column=1, sticky='w', padx=5)

    btm_reading_label = Label(canvas_frame, text="Weight Indicator Reading @ Btm of Down-Stroke: ", fg='black',
                              bg='#9BA4B4')
    btm_reading_label.grid(row=3, column=0, sticky='w', padx=5)
    btm_reading_text = Entry(canvas_frame, foreground='black')
    btm_reading_text.insert(END, string=0)
    btm_reading_text.grid(row=3, column=1, sticky='w', padx=5)

    distance_label = Label(canvas_frame, text="Distance Travelled Between Top & Btm of Each Stroke: ", fg='black',
                           bg='#9BA4B4')
    distance_label.grid(row=4, column=0, sticky='w', padx=5)
    distance_text = Entry(canvas_frame, foreground='black')
    distance_text.insert(END, string=0)
    distance_text.grid(row=4, column=1, sticky='w', padx=5)

    number_label = Label(canvas_frame, text="Number of Strokes/Hour: ", fg='black', bg='#9BA4B4')
    number_label.grid(row=5, column=0, sticky='w', padx=5)
    number_text = Entry(canvas_frame, foreground='black')
    number_text.insert(END, string=0)
    number_text.grid(row=5, column=1, sticky='w', padx=5)

    hours_label = Label(canvas_frame, text="Number of Hours Jarring: ", fg='black', bg='#9BA4B4')
    hours_label.grid(row=6, column=0, sticky='w', padx=5)
    hours_text = Entry(canvas_frame, foreground='black')
    hours_text.insert(END, string=0)
    hours_text.grid(row=6, column=1, sticky='w', padx=5)
    # ---------------------------------------------------------------
    compute_button = Button(canvas_frame, text='Compute Jarring Miles', bg='#77ACF1', width=30,
                            command=jarring_ton_miles_data)
    compute_button.grid(row=7, column=2, sticky='w', pady=10, columnspan=3)
    # ___________________________________________________________________________________________________________


def liner_tonmiles_ui():
    clear_canvas_frame()
    change_button_colors(liner_button, jarring_button, casing_button, tripping_button, drilling_button)

    # --------------------------CREATE CSV FILE AND STORE DATA -----------------------
    def liner_tonmiles_data():
        global BF, BLOCK_WT, liner_miles_total
        BLOCK_WT = float(block_wt_label_entry.get().strip()) / 2000
        MUD_WT = float(mud_wt_label_entry.get().strip())
        BF = (65.44 - MUD_WT) / 65.44
        shoe_depth = float(depth_text1.get().strip())
        liner_length = float(liner_length_text.get().strip())
        liner_ppf = float(liner_weight_text.get().strip())
        liner_bw = calculate_boyed_weight(liner_length, liner_ppf, BF)

        dp_length = shoe_depth - liner_length
        dp_ppf = float(dp_weight_text.get().strip())

        if dp_length > 0:
            dp_value.config(text=f'{dp_length}')
            dp_bw = calculate_boyed_weight(dp_length, dp_ppf, BF)
            note_label = Label(canvas_frame, text="Note: Total includes miles gained during POOH DP. ", fg='#14274E',
                               bg='#9BA4B4')
            note_label.grid(row=4, column=0, columnspan=3, sticky='w', padx=5, pady=10)
        else:
            dp_value.config(text=f'{0}')
            dp_bw = 0

        liner_miles_total = liner_miles(dp_length, dp_bw, liner_length, liner_bw, shoe_depth, BLOCK_WT)
        liner_miles_result_value.config(text=f'{liner_miles_total:.2f}')
        get_total_miles()  # ----------ADDING MILES TO TOTAL MILES

    # --------------------------LINER TON MILES UI ELEMENTS-------------------------------------
    depth_label1 = Label(canvas_frame, text="Liner Shoe Setting Depth: ", fg='black', bg='#9BA4B4')
    depth_label1.grid(row=1, column=0, sticky='w', padx=5)
    depth_text1 = Entry(canvas_frame, foreground='black')
    depth_text1.insert(END, string=0)
    depth_text1.grid(row=1, column=1, sticky='w', padx=5)

    liner_length_label = Label(canvas_frame, text="Liner String Length: ", fg='black', bg='#9BA4B4')
    liner_length_label.grid(row=2, column=0, sticky='w', padx=5)
    liner_length_text = Entry(canvas_frame, foreground='black')
    liner_length_text.insert(END, string=0)
    liner_length_text.grid(row=2, column=1, sticky='w', padx=5)
    liner_weight_label = Label(canvas_frame, text="Liner Weight in ppf: ", fg='black', bg='#9BA4B4')
    liner_weight_label.grid(row=2, column=2, sticky='e', padx=5)
    liner_weight_text = Entry(canvas_frame, foreground='black', width=5)
    liner_weight_text.insert(END, string=0)
    liner_weight_text.grid(row=2, column=3, sticky='w')

    label_dp = Label(canvas_frame, text="Drill Pipe Length: ", fg='black', bg='#9BA4B4')
    label_dp.grid(row=3, column=0, sticky='w', padx=5, pady=10)
    dp_value = Label(canvas_frame, text="0", fg='#0A1931', bg='#77ACF1')
    dp_value.grid(row=3, column=1, sticky='w', padx=5, pady=10)
    dp_weight_label = Label(canvas_frame, text="Weight of DP in ppf: ", fg='black', bg='#9BA4B4')
    dp_weight_label.grid(row=3, column=2, sticky='e', padx=5, pady=10)
    dp_weight_text = Entry(canvas_frame, foreground='black', width=5)
    dp_weight_text.insert(END, string=0)
    dp_weight_text.grid(row=3, column=3, sticky='w', pady=10)

    # ---------------------------------------------------------------
    compute_button = Button(canvas_frame, text='Compute Liner Ton Miles', bg='#77ACF1', width=30,
                            command=liner_tonmiles_data)
    compute_button.grid(row=5, column=2, sticky='w', pady=10, columnspan=3)
    # -------------------------------------------------------------------------------------------------------


# ______________MAIN FRAME___________________________________________________________________________
window = Tk()
window.title(f"{datetime.now():%a, %b %d %Y} | Ton Miles Calculator | Developer: madon.zubin@gmail.com")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("+%d+%d" % (200, 100))
window.config(background='#394867')
top_frame = Frame(window, height=100, bg='#14274E')
top_frame.grid(row=0, sticky='ew')
mid_frame = Frame(window, width=1000, height=100, bg='#9BA4B4')
mid_frame.grid(row=1, sticky='ew')
canvas_frame = Frame(window, width=1000, height=300, bg='#9BA4B4')
canvas_frame.grid(row=3, sticky='ew')
bottom_frame = Frame(window, width=1000, height=500, bg='#394867')
bottom_frame.grid(row=4, sticky='ew')
icon_photo = PhotoImage(file='images/icon.png')
window.iconphoto(False, icon_photo)

# -----------Date Elements-----------
date_label = Label(top_frame, text="Enter Date: ", bg='#14274E', fg='#9BA4B4')
date_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
dd_entry = Entry(top_frame, width=5, foreground='grey')
mm_entry = Entry(top_frame, width=5, foreground='grey')
yy_entry = Entry(top_frame, width=10, foreground='grey')
dd_entry.insert(END, string="DD")
mm_entry.insert(END, string="MM")
yy_entry.insert(END, string="YYYY")
dd_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
dd_entry.focus()
mm_entry.grid(row=0, column=2, padx=5, pady=5, sticky='w')
yy_entry.grid(row=0, column=3, padx=5, sticky='ew')
rig_name = Label(top_frame, text=f"Rig Name: ",
                     bg='#14274E', fg='#9BA4B4')
rig_name.grid(row=0, column=4, padx=5, pady=5, sticky='w')
rig_name_entry = Entry(top_frame, width=15)
rig_name_entry.grid(row=0, column=5, padx=5, pady=5, sticky='ew')
# ---------------------COMMIT DATE & RIG NAME-------------------
submit_top = Button(top_frame, text='Submit', command=submit_date, bg='#77ACF1')
submit_top.grid(row=0, column=6, pady=5, sticky='e', padx=10)
top_entry_confirm = Label(top_frame, text=f"Rig: Choose the options below to enter data for: ", bg='#14274E', fg='#9BA4B4')
top_entry_confirm.grid(row=1, column=0, padx=5, sticky='w', columnspan = 7)

# ----------Block Weight & Mud Weight ---------------
block_wt_label = Label(top_frame, text="Empty Block Weight (lbs): ", bg='#14274E', fg='#9BA4B4')
mud_wt_label = Label(top_frame, text="Mud Weight (ppg): ", bg='#14274E', fg='#9BA4B4')
block_wt_label_entry = Entry(top_frame, width=20, foreground='grey')
mud_wt_label_entry = Entry(top_frame, width=20, foreground='grey')
mud_wt_label_entry.insert(END, string=0)
block_wt_label_entry.insert(END, string=0)
block_wt_label.grid(row=1, column=7, padx=5, pady=10, sticky='e')
block_wt_label_entry.grid(row=1, column=8, padx=5, pady=10, sticky='w')
mud_wt_label.grid(row=1, column=9, padx=5, pady=10, sticky='e')
mud_wt_label_entry.grid(row=1, column=10, padx=10, pady=10, sticky='w')
top_note_label = Label(top_frame, text="Note: Enter all weights in pounds (1kips = 1000 pounds). "
                                       "All lengths & depths in feet. Leave '0' "
                                       "for empty fields.", bg='#14274E', fg='#DA7F8F', font=('serif', 10, 'bold'))
top_note_label.grid(row=2, column=0, padx=5, pady=5, sticky='w', columnspan= 10)


# ---------------TON MILE CALC ELEMENTS-------------------
drilling_button = Button(mid_frame, text='Drilling', command=drilling_ton_miles_ui, bg='#77ACF1')
tripping_button = Button(mid_frame, text='Tripping', bg='#77ACF1', command=tripping_ton_miles_ui)
casing_button = Button(mid_frame, text='Ran Casing', bg='#77ACF1', command=casing_ton_miles_ui)
liner_button = Button(mid_frame, text='Ran Liner', bg='#77ACF1', command=liner_tonmiles_ui)
jarring_button = Button(mid_frame, text='Jarring', bg='#77ACF1', command=jarring_tonmiles_ui)

drilling_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')
tripping_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')
casing_button.grid(row=2, column=2, padx=10, pady=10, sticky='w')
liner_button.grid(row=2, column=3, padx=10, pady=10, sticky='w')
jarring_button.grid(row=2, column=4, padx=10, pady=10, sticky='w')

# _____________BOTTOM FRAME RESULT WIDGETS___________________________________________________
date_bottom_label = Label(bottom_frame, text=f'Compiled Miles for the Date:',
                          bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
date_bottom_label.grid(row=0, column=0, sticky='w', padx=10)
date_bottom_value = Label(bottom_frame, text=f'DD:MM:YYYY',
                          bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
date_bottom_value.grid(row=0, column=1, sticky='w', padx=10)

drilling_miles_result_label = Label(bottom_frame, text=f'Drilling Ton Miles: ',
                                    bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
drilling_miles_result_label.grid(row=1, column=0, sticky='w', padx=10)
drilling_miles_result_value = Label(bottom_frame, text=f'{0}',
                                    bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
drilling_miles_result_value.grid(row=1, column=1, sticky='w', padx=10)

tripping_miles_result_label = Label(bottom_frame, text=f'Tripping Ton Miles: ',
                                    bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
tripping_miles_result_label.grid(row=2, column=0, sticky='w', padx=10)
tripping_miles_result_value = Label(bottom_frame, text=f'{0}',
                                    bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
tripping_miles_result_value.grid(row=2, column=1, sticky='w', padx=10)

casing_miles_result_label = Label(bottom_frame, text=f'Casing Run Ton Miles: ',
                                  bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))

casing_miles_result_label.grid(row=3, column=0, sticky='w', padx=10)

casing_miles_result_value = Label(bottom_frame, text=f'{0}',
                                  bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
casing_miles_result_value.grid(row=3, column=1, sticky='w', padx=10)
liner_miles_result_label = Label(bottom_frame, text=f'Liner Run Ton Miles: ',
                                 bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
liner_miles_result_label.grid(row=4, column=0, sticky='w', padx=10)
liner_miles_result_value = Label(bottom_frame, text=f'{0}',
                                 bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
liner_miles_result_value.grid(row=4, column=1, sticky='w', padx=10)
jarring_miles_result_label = Label(bottom_frame, text=f'Jarring Ton Miles: ',
                                   bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
jarring_miles_result_label.grid(row=5, column=0, sticky='w', padx=10)
jarring_miles_result_value = Label(bottom_frame, text=f'{0}',
                                   bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
jarring_miles_result_value.grid(row=5, column=1, sticky='w', padx=10)

total_miles_result_label = Label(bottom_frame, text=f'Total Ton Miles: ',
                                 bg='#394867', fg='#DA7F8F', font=('serif', 12, 'bold'))
total_miles_result_label.grid(row=6, column=0, sticky='w', padx=10)
total_miles_result_value = Label(bottom_frame, text=f'{total_miles_result}', bg='#394867', fg='#DA7F8F',
                                 font=('serif', 12, 'bold'))
total_miles_result_value.grid(row=6, column=1, sticky='w', padx=10)
comments_box = Text(bottom_frame, height=3, width=60)
comments_box.insert(END, "Enter Ops Details Before Clicking Submit")
comments_box.grid(row=7, column=0, sticky='w', pady=10, columnspan=6, padx=10)
submit_day_data = Button(bottom_frame, text="Commit Day's Data to CSV File", bg='#77ACF1', width=30,
                         command=submit_warning)
submit_day_data.grid(row=10, column=0, sticky='w', pady=10, padx=10, columnspan=5)
# --------------------------------------------------------------------------------------


window.mainloop()
