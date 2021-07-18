from tkinter import *
from datetime import *
from tkinter import messagebox
import calculate_functions

window = Tk()
window.title(f"{datetime.now():%a, %b %d %Y} | Ton Miles Calculator | Developer: madon.zubin@gmail.com")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("+%d+%d" % (200, 100))
window.config(background='#394867')
icon_photo = PhotoImage(file='images/icon.png')
window.iconphoto(False, icon_photo)


class MainScreen():
    drilling_miles_total = 0
    tripping_miles_total = 0
    casing_miles_total = 0
    liner_miles_total = 0
    jarring_miles_total = 0
    total_miles_result = 0
    formatted_date = 0
    comments = ''

    def __init__(self, main):
        # -------------------------------FRAMES----------------------------------------------------------------
        self.top_frame = Frame(main, height=100, bg='#14274E')
        self.top_frame.grid(row=0, sticky='ew')
        self.mid_frame = Frame(main, width=1000, height=100, bg='#9BA4B4')
        self.mid_frame.grid(row=1, sticky='ew')
        self.canvas_frame = Frame(main, width=1000, height=300, bg='#9BA4B4')
        self.canvas_frame.grid(row=3, sticky='ew')
        self.bottom_frame = Frame(main, width=1000, height=300, bg='#394867')
        self.bottom_frame.grid(row=4, sticky='ew')
        self.canvas_frame_drill = Frame(main, width=1000, height=300, bg='#9BA4B4')
        self.canvas_frame_trip = Frame(main, width=1000, height=300, bg='#9BA4B4')
        self.canvas_frame_csg = Frame(main, width=1000, height=300, bg='#9BA4B4')
        self.canvas_frame_liner = Frame(main, width=1000, height=300, bg='#9BA4B4')
        self.canvas_frame_jarring = Frame(main, width=1000, height=300, bg='#9BA4B4')
        self.canvas_frame_drill.grid(row=3, sticky='ew')
        self.canvas_frame_trip.grid(row=3, sticky='ew')
        self.canvas_frame_csg.grid(row=3, sticky='ew')
        self.canvas_frame_liner.grid(row=3, sticky='ew')
        self.canvas_frame_jarring.grid(row=3, sticky='ew')
        # -----------------------DRILLING MILES WIDGETS------------------------------------------------
        self.compute_button = Button(self.canvas_frame_drill, text='Compute Drilling Miles', bg='#77ACF1',
                                     width=30, command=drilling_trigger.drill_miles_data)
        self.bha_dp2_value_end = Label(self.canvas_frame_drill, text="0", fg='#0A1931', bg='#77ACF1')
        self.bha_label_dp2_end = Label(self.canvas_frame_drill, text="Drill Pipe (Top) @ end of section: ", fg='black',
                                       bg='#9BA4B4')
        self.dp2_warning_label = Label(self.canvas_frame_drill,
                                       text="(Enter only if you're using 2 types of Drill Pipe in string)",
                                       fg='black', bg='#9BA4B4')
        self.dp2_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.dp2_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.bha_dp2_value = Label(self.canvas_frame_drill, text="0", fg='#0A1931', bg='#77ACF1')
        self.bha_label_dp2 = Label(self.canvas_frame_drill, text="Drill Pipe (Top) @ start of section: ", fg='black',
                                   bg='#9BA4B4')
        self.dp1_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.dp1_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.bha_text_dp1 = Entry(self.canvas_frame_drill, foreground='black')
        self.bha_label_dp1 = Label(self.canvas_frame_drill, text="Drill Pipe (Bottom): ", fg='black', bg='#9BA4B4')
        self.hwdp_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.hwdp_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.bha_text_hwdp = Entry(self.canvas_frame_drill, foreground='black')
        self.bha_label_hwdp = Label(self.canvas_frame_drill, text="HWDP: ", fg='black', bg='#9BA4B4')
        self.dc2_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.dc2_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.bha_text_dc2 = Entry(self.canvas_frame_drill, foreground='black')
        self.bha_label_dc2 = Label(self.canvas_frame_drill, text="DC#2 (Top): ", fg='black', bg='#9BA4B4')
        self.dc1_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.dc1_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.bha_text_dc1 = Entry(self.canvas_frame_drill, foreground='black')
        self.bha_label_dc1 = Label(self.canvas_frame_drill, text="DC#1 (Bottom): ", fg='black', bg='#9BA4B4')
        self.bha_title = Label(self.canvas_frame_drill, text="BHA Details: ", fg='#0A1931', bg='#9BA4B4',
                               font=('serif', 14, 'bold'))
        self.drilling_text4 = Entry(self.canvas_frame_drill, foreground='black', width=6)
        self.drilling_label3 = Label(self.canvas_frame_drill, text="No. of times reamed stand: ", fg='black',
                                     bg='#9BA4B4')
        self.drilling_text2 = Entry(self.canvas_frame_drill, foreground='black')
        self.drilling_label2 = Label(self.canvas_frame_drill, text="To: ", fg='black', bg='#9BA4B4')
        self.drilling_text1 = Entry(self.canvas_frame_drill, foreground='black')
        self.drilling_label1 = Label(self.canvas_frame_drill, text="Drill From: ", fg='black', bg='#9BA4B4')

        # -----------Date Elements-----------
        self.date_label = Label(self.top_frame, text="Enter Date: ", bg='#14274E', fg='#9BA4B4')
        self.date_label.grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.dd_entry = Entry(self.top_frame, width=5, foreground='grey')
        self.mm_entry = Entry(self.top_frame, width=5, foreground='grey')
        self.yy_entry = Entry(self.top_frame, width=10, foreground='grey')
        self.dd_entry.insert(END, string="DD")
        self.mm_entry.insert(END, string="MM")
        self.yy_entry.insert(END, string="YYYY")
        self.dd_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.dd_entry.focus()
        self.mm_entry.grid(row=0, column=2, padx=5, pady=5, sticky='w')
        self.yy_entry.grid(row=0, column=3, padx=5, sticky='ew')
        self.rig_name = Label(self.top_frame, text=f"Rig Name: ",
                              bg='#14274E', fg='#9BA4B4')
        self.rig_name.grid(row=0, column=4, padx=5, pady=5, sticky='w')
        self.rig_name_entry = Entry(self.top_frame, width=15)
        self.rig_name_entry.grid(row=0, column=5, padx=5, pady=5, sticky='ew')
        # ---------------------COMMIT DATE & RIG NAME-------------------
        self.submit_top = Button(self.top_frame, text='Submit', command=self.submit_date, bg='#77ACF1')
        self.submit_top.grid(row=0, column=6, pady=5, sticky='e', padx=10)
        self.top_entry_confirm = Label(self.top_frame, text=f"Rig: Choose the options below to enter data for: ",
                                       bg='#14274E',
                                       fg='#9BA4B4')
        self.top_entry_confirm.grid(row=1, column=0, padx=5, sticky='w', columnspan=7)
        # ----------Block Weight & Mud Weight ---------------
        self.block_wt_label = Label(self.top_frame, text="Empty Block Weight (lbs): ", bg='#14274E', fg='#9BA4B4')
        self.mud_wt_label = Label(self.top_frame, text="Mud Weight (ppg): ", bg='#14274E', fg='#9BA4B4')
        self.block_wt_label_entry = Entry(self.top_frame, width=20, foreground='grey')
        self.mud_wt_label_entry = Entry(self.top_frame, width=20, foreground='grey')
        self.mud_wt_label_entry.insert(END, string=0)
        self.block_wt_label_entry.insert(END, string=0)
        self.block_wt_label.grid(row=1, column=7, padx=5, pady=10, sticky='e')
        self.block_wt_label_entry.grid(row=1, column=8, padx=5, pady=10, sticky='w')
        self.mud_wt_label.grid(row=1, column=9, padx=5, pady=10, sticky='e')
        self.mud_wt_label_entry.grid(row=1, column=10, padx=10, pady=10, sticky='w')
        self.top_note_label = Label(self.top_frame, text="Note: Enter all weights in pounds (1kips = 1000 pounds). "
                                                         "All lengths & depths in feet. Leave '0' "
                                                         "for empty fields.", bg='#14274E', fg='#DA7F8F',
                                    font=('serif', 10, 'bold'))
        self.top_note_label.grid(row=2, column=0, padx=5, pady=5, sticky='w', columnspan=10)

        # ---------------TON MILE CALC ELEMENTS-------------------
        self.drilling_button = Button(self.mid_frame, text='Drilling', command=self.drilling_ui, bg='#77ACF1')
        self.tripping_button = Button(self.mid_frame, text='Tripping', bg='#77ACF1', command=self.tripping_ui)
        self.casing_button = Button(self.mid_frame, text='Ran Casing', bg='#77ACF1', command=self.casing_ui)
        self.liner_button = Button(self.mid_frame, text='Ran Liner', bg='#77ACF1', command=self.liner_ui)
        self.jarring_button = Button(self.mid_frame, text='Jarring', bg='#77ACF1', command=self.jarring_ui)
        self.drilling_button.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.tripping_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')
        self.casing_button.grid(row=2, column=2, padx=10, pady=10, sticky='w')
        self.liner_button.grid(row=2, column=3, padx=10, pady=10, sticky='w')
        self.jarring_button.grid(row=2, column=4, padx=10, pady=10, sticky='w')

        # _____________BOTTOM FRAME RESULT WIDGETS___________________________________________________
        self.date_bottom_label = Label(self.bottom_frame, text=f'Compiled Miles for the Date:',
                                       bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.date_bottom_label.grid(row=0, column=0, sticky='w', padx=10)
        self.date_bottom_value = Label(self.bottom_frame, text=f'DD:MM:YYYY',
                                       bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.date_bottom_value.grid(row=0, column=1, sticky='w', padx=10)

        self.drilling_miles_result_label = Label(self.bottom_frame, text=f'Drilling Ton Miles: ',
                                                 bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.drilling_miles_result_label.grid(row=1, column=0, sticky='w', padx=10)
        self.drilling_miles_result_value = Label(self.bottom_frame, text=f'{0}',
                                                 bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.drilling_miles_result_value.grid(row=1, column=1, sticky='w', padx=10)

        self.tripping_miles_result_label = Label(self.bottom_frame, text=f'Tripping Ton Miles: ',
                                                 bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.tripping_miles_result_label.grid(row=2, column=0, sticky='w', padx=10)
        self.tripping_miles_result_value = Label(self.bottom_frame, text=f'{0}',
                                                 bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.tripping_miles_result_value.grid(row=2, column=1, sticky='w', padx=10)

        self.casing_miles_result_label = Label(self.bottom_frame, text=f'Casing Run Ton Miles: ',
                                               bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))

        self.casing_miles_result_label.grid(row=3, column=0, sticky='w', padx=10)

        self.casing_miles_result_value = Label(self.bottom_frame, text=f'{0}',
                                               bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.casing_miles_result_value.grid(row=3, column=1, sticky='w', padx=10)
        self.liner_miles_result_label = Label(self.bottom_frame, text=f'Liner Run Ton Miles: ',
                                              bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.liner_miles_result_label.grid(row=4, column=0, sticky='w', padx=10)
        self.liner_miles_result_value = Label(self.bottom_frame, text=f'{0}',
                                              bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.liner_miles_result_value.grid(row=4, column=1, sticky='w', padx=10)
        self.jarring_miles_result_label = Label(self.bottom_frame, text=f'Jarring Ton Miles: ',
                                                bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.jarring_miles_result_label.grid(row=5, column=0, sticky='w', padx=10)
        self.jarring_miles_result_value = Label(self.bottom_frame, text=f'{0}',
                                                bg='#394867', fg='#9BA4B4', font=('serif', 10, 'bold'))
        self.jarring_miles_result_value.grid(row=5, column=1, sticky='w', padx=10)

        self.total_miles_result_label = Label(self.bottom_frame, text=f'Total Ton Miles: ',
                                              bg='#394867', fg='#DA7F8F', font=('serif', 12, 'bold'))
        self.total_miles_result_label.grid(row=6, column=0, sticky='w', padx=10)
        # self.total_miles_result_value = Label(self.bottom_frame, text=f'{total_miles_result}', bg='#394867',
        #                                      fg='#DA7F8F',
        #                                      font=('serif', 12, 'bold'))
        # self.total_miles_result_value.grid(row=6, column=1, sticky='w', padx=10)
        self.comments_box = Text(self.bottom_frame, height=3, width=60)
        self.comments_box.insert(END, "Enter Ops Details Before Clicking Submit")
        self.comments_box.grid(row=7, column=0, sticky='w', pady=10, columnspan=6, padx=10)
        # self.submit_day_data = Button(self.bottom_frame, text="Commit Day's Data to CSV File", bg='#77ACF1', width=30,
        #                              command=submit_warning)
        # self.submit_day_data.grid(row=10, column=0, sticky='w', pady=10, padx=10, columnspan=5)
        # ------------------------Useful Variables for Calculation----------------------------------------
        self.block_wt = float(self.block_wt_label_entry.get().strip()) / 2000
        self.mud_wt = float(self.mud_wt_label_entry.get().strip())
        self.bf = (65.44 - self.mud_wt) / 65.44

    # ------------------------------------------------------------------------------------------------------

    def change_button_colors(self, active_button, button2, button3, button4, button5):
        active_button.config(bg='#3EDBF0')
        button2.config(bg='#77ACF1')
        button3.config(bg='#77ACF1')
        button4.config(bg='#77ACF1')
        button5.config(bg='#77ACF1')

    def submit_date(self):
        try:
            dd = int(self.dd_entry.get().strip())
            mm = int(self.mm_entry.get().strip())
            yyyy = int(self.yy_entry.get().strip())
            formatted_date = date(day=dd, month=mm, year=yyyy).strftime('%d %B %Y')
            self.top_entry_confirm.config(text=f"Rig: {self.rig_name_entry.get()} | Choose the options below"
                                               f" to enter data for: {formatted_date}.")
            self.date_bottom_value.config(text=formatted_date)

        except ValueError:
            messagebox.showerror(title="Invalid Input!", message="Please enter only numbers in DD, MM, YYYY format.")

    def drilling_ui(self):
        self.canvas_frame.tkraise()  # ----Brings blank frame up first, so that widgets from other frames don't clash.
        self.canvas_frame_drill.tkraise()  # ----Raises the drilling frame to top and brings all its widgets up.
        self.change_button_colors(self.drilling_button, self.tripping_button, self.casing_button, self.liner_button,
                                  self.jarring_button)
        # ------------------------------DRILLING UI ELEMENTS----------------------------------------------------
        self.drilling_label1.grid(row=0, column=0, sticky='e', padx=5)
        self.drilling_text1.insert(END, string=0)
        self.drilling_text1.grid(row=0, column=1, sticky='w', padx=5)

        self.drilling_label2.grid(row=0, column=2, sticky='e', padx=5)
        self.drilling_text2.insert(END, string=0)
        self.drilling_text2.grid(row=0, column=3, sticky='w', padx=5)

        self.drilling_label3.grid(row=0, column=4, sticky='ew', padx=5, columnspan=4)
        self.drilling_text4.insert(END, string=0)
        self.drilling_text4.grid(row=0, column=5, sticky='ew', padx=10, columnspan=5)

        # ---------DRILLING BHA Elements--------------------
        self.bha_title.grid(row=1, column=0, pady=10)
        # ----DC1---------------------
        self.bha_label_dc1.grid(row=2, column=0, sticky='w', padx=5)
        self.bha_text_dc1.insert(END, string=0)
        self.bha_text_dc1.grid(row=2, column=1, sticky='w', padx=5)

        self.dc1_weight_label.grid(row=2, column=2, sticky='e', padx=5)

        self.dc1_weight_text.insert(END, string=0)
        self.dc1_weight_text.grid(row=2, column=3, sticky='w')
        # ----DC2---------------------
        self.bha_label_dc2.grid(row=3, column=0, sticky='w', padx=5)
        self.bha_text_dc2.insert(END, string=0)
        self.bha_text_dc2.grid(row=3, column=1, sticky='w', padx=5)
        self.dc2_weight_label.grid(row=3, column=2, sticky='e', padx=5)
        self.dc2_weight_text.insert(END, string=0)
        self.dc2_weight_text.grid(row=3, column=3, sticky='w')
        # ---------HWDP--------------
        self.bha_label_hwdp.grid(row=4, column=0, sticky='w', padx=5)
        self.bha_text_hwdp.insert(END, string=0)
        self.bha_text_hwdp.grid(row=4, column=1, sticky='w', padx=5)
        self.hwdp_weight_label.grid(row=4, column=2, sticky='e', padx=5)
        self.hwdp_weight_text.insert(END, string=0)
        self.hwdp_weight_text.grid(row=4, column=3, sticky='w')
        # ---------DP1 (Bottom)--------------
        self.bha_label_dp1.grid(row=5, column=0, sticky='w', padx=5)
        self.bha_text_dp1.insert(END, string=0)
        self.bha_text_dp1.grid(row=5, column=1, sticky='w', padx=5)
        self.dp1_weight_label.grid(row=5, column=2, sticky='e', padx=5)
        self.dp1_weight_text.insert(END, string=0)
        self.dp1_weight_text.grid(row=5, column=3, sticky='w')
        # ---------DP2 (Top)START--------------
        self.bha_label_dp2.grid(row=6, column=0, sticky='w', padx=5)
        self.bha_dp2_value.grid(row=6, column=1, sticky='w', padx=5)
        self.dp2_weight_label.grid(row=6, column=2, sticky='e', padx=5)
        self.dp2_weight_text.insert(END, string=0)
        self.dp2_weight_text.grid(row=6, column=3, sticky='w')
        self.dp2_warning_label.grid(row=6, column=4, sticky='w', padx=5)
        # -----------DP2 (TOP)END-----------------------
        self.bha_label_dp2_end.grid(row=7, column=0, sticky='w', padx=5)
        self.bha_dp2_value_end.grid(row=7, column=1, sticky='w', padx=5)
        # ----------COMPUTE BUTTON TO CALCULATE DATA & SEND DATA TO BOTTOM FRAME---------------
        self.compute_button.grid(row=7, column=2, sticky='w', pady=10, columnspan=3)

    def tripping_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_trip.tkraise()
        self.change_button_colors(self.tripping_button, self.drilling_button, self.casing_button, self.liner_button,
                                  self.jarring_button)
        # ------------------------UI ELEMENTS------------------------------------
        self.tripping_label1 = Label(self.canvas_frame_trip, text="Trip From (depth#1): ", fg='black', bg='#9BA4B4')
        self.tripping_label1.grid(row=3, column=0, sticky='w', padx=5)
        self.tripping_text1 = Entry(self.canvas_frame_trip, foreground='black')
        self.tripping_text1.insert(END, string=0)
        self.tripping_text1.grid(row=3, column=1, sticky='e', padx=5)
        self.tripping_label2 = Label(self.canvas_frame_trip, text="To (depth#2): ", fg='black', bg='#9BA4B4')
        self.tripping_label2.grid(row=3, column=2, sticky='e', padx=5)
        self.tripping_text2 = Entry(self.canvas_frame_trip, foreground='black')
        self.tripping_text2.insert(END, string=0)
        self.tripping_text2.grid(row=3, column=3, sticky='e', padx=5)
        self.radio_state = IntVar()
        self.radiobutton1 = Radiobutton(self.canvas_frame_trip, text="Single Trip", value=1, variable=self.radio_state,
                                        bg='#9BA4B4')
        self.radiobutton2 = Radiobutton(self.canvas_frame_trip, text="Round Trip", value=2, variable=self.radio_state,
                                        bg='#9BA4B4')
        self.radiobutton1.grid(row=3, column=4, sticky='w')
        self.radiobutton2.grid(row=4, column=4, sticky='w')
        # ---------BHA Elements--------------------
        self.bha_title = Label(self.canvas_frame_trip, text="BHA Details: ", fg='#0A1931', bg='#9BA4B4',
                               font=('serif', 14, 'bold'))
        self.bha_title.grid(row=4, column=0, pady=10)
        # ----DC1---------------------
        self.bha_label_dc1 = Label(self.canvas_frame_trip, text="DC#1 (Bottom): ", fg='black', bg='#9BA4B4')
        self.bha_label_dc1.grid(row=5, column=0, sticky='w', padx=5)
        self.bha_text_dc1 = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_text_dc1.insert(END, string=0)
        self.bha_text_dc1.grid(row=5, column=1, sticky='w', padx=5)
        self.dc1_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dc1_weight_label.grid(row=5, column=2, sticky='e', padx=5)
        self.dc1_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dc1_weight_text.insert(END, string=0)
        self.dc1_weight_text.grid(row=5, column=3, sticky='w')
        # ----DC2---------------------
        self.bha_label_dc2 = Label(self.canvas_frame_trip, text="DC#2 (Top): ", fg='black', bg='#9BA4B4')
        self.bha_label_dc2.grid(row=6, column=0, sticky='w', padx=5)
        self.bha_text_dc2 = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_text_dc2.insert(END, string=0)
        self.bha_text_dc2.grid(row=6, column=1, sticky='w', padx=5)
        self.dc2_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dc2_weight_label.grid(row=6, column=2, sticky='e', padx=5)
        self.dc2_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dc2_weight_text.insert(END, string=0)
        self.dc2_weight_text.grid(row=6, column=3, sticky='w')
        # ---------HWDP--------------
        self.bha_label_hwdp = Label(self.canvas_frame_trip, text="HWDP: ", fg='black', bg='#9BA4B4')
        self.bha_label_hwdp.grid(row=7, column=0, sticky='w', padx=5)
        self.bha_text_hwdp = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_text_hwdp.insert(END, string=0)
        self.bha_text_hwdp.grid(row=7, column=1, sticky='w', padx=5)
        self.hwdp_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.hwdp_weight_label.grid(row=7, column=2, sticky='e', padx=5)
        self.hwdp_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.hwdp_weight_text.insert(END, string=0)
        self.hwdp_weight_text.grid(row=7, column=3, sticky='w')
        # ---------DP1 (Bottom)--------------
        self.bha_label_dp1 = Label(self.canvas_frame_trip, text="Drill Pipe (Bottom): ", fg='black', bg='#9BA4B4')
        self.bha_label_dp1.grid(row=8, column=0, sticky='w', padx=5)
        self.bha_text_dp1 = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_text_dp1.insert(END, string=0)
        self.bha_text_dp1.grid(row=8, column=1, sticky='w', padx=5)
        self.dp1_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dp1_weight_label.grid(row=8, column=2, sticky='e', padx=5)
        self.dp1_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dp1_weight_text.insert(END, string=0)
        self.dp1_weight_text.grid(row=8, column=3, sticky='w')
        # ---------DP2 (Top)START--------------
        self.bha_label_dp2 = Label(self.canvas_frame_trip, text="Drill Pipe (At the Top): ", fg='black', bg='#9BA4B4')
        self.bha_label_dp2.grid(row=9, column=0, sticky='w', padx=5)
        self.bha_dp2_value = Label(self.canvas_frame_trip, text="0", fg='#0A1931', bg='#77ACF1')
        self.bha_dp2_value.grid(row=9, column=1, sticky='w', padx=5)
        self.dp2_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dp2_weight_label.grid(row=9, column=2, sticky='e', padx=5)
        self.dp2_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dp2_weight_text.insert(END, string=0)
        self.dp2_weight_text.grid(row=9, column=3, sticky='w')
        self.dp2_warning_label = Label(self.canvas_frame_trip,
                                       text="(Enter only if you're using 2 types of Drill Pipe in string)",
                                       fg='black', bg='#9BA4B4')
        self.dp2_warning_label.grid(row=9, column=4, sticky='w', padx=5)
        # ---------------COMPUTE TRIPPING MILES AND SEND DATA TO BTM FRAME-------------------------------------------
        self.compute_button = Button(self.canvas_frame_trip, text='Compute Tripping Miles', bg='#77ACF1', width=30)
        self.compute_button.grid(row=10, column=2, sticky='w', pady=10, columnspan=3)
        # ---------------------------------------------------------------

    def casing_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_csg.tkraise()
        self.change_button_colors(self.casing_button, self.tripping_button, self.drilling_button, self.liner_button,
                                  self.jarring_button)
        # __________________________________UI ELEMENTS FOR CASING ------------------------------------------
        self.note_label1 = Label(self.canvas_frame_csg,
                                 text="Note: 1. If you are running casing on DP use 'Top Casing' "
                                      "as your DP string.", fg='black', bg='#9BA4B4', wraplength=600)
        self.note_label1.grid(row=0, column=0, sticky='w', padx=5, columnspan=6)

        self.note_label2 = Label(self.canvas_frame_csg,
                                 text="2. If only one casing string is being run all the way, only enter shoe depth"
                                      " and weight for 'Top Casing'.", fg='black', bg='#9BA4B4', wraplength=600)
        self.note_label2.grid(row=1, column=0, sticky='e', padx=35, columnspan=6)
        self.depth_label1 = Label(self.canvas_frame_csg, text="Shoe Setting Depth: ", fg='black', bg='#9BA4B4')
        self.depth_label1.grid(row=2, column=0, sticky='w', padx=5)
        self.depth_text1 = Entry(self.canvas_frame_csg, foreground='black')
        self.depth_text1.insert(END, string=0)
        self.depth_text1.grid(row=2, column=1, sticky='w', padx=5)

        # ---------BHA Elements--------------------
        self.bha_title = Label(self.canvas_frame_csg, text="BHA Details: ", fg='#0A1931', bg='#9BA4B4',
                               font=('serif', 14, 'bold'))
        self.bha_title.grid(row=5, column=0, pady=10)
        # ----LOWER CSG---------------------
        self.bha_label_lower_csg = Label(self.canvas_frame_csg, text="Lower Casing String: ", fg='black', bg='#9BA4B4')
        self.bha_label_lower_csg.grid(row=6, column=0, sticky='w', padx=5)
        self.bha_text_lower_csg = Entry(self.canvas_frame_csg, foreground='black')
        self.bha_text_lower_csg.insert(END, string=0)
        self.bha_text_lower_csg.grid(row=6, column=1, sticky='w', padx=5)
        self.lower_csg_weight_label = Label(self.canvas_frame_csg, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.lower_csg_weight_label.grid(row=6, column=2, sticky='e', padx=5)
        self.lower_csg_weight_text = Entry(self.canvas_frame_csg, foreground='black', width=5)
        self.lower_csg_weight_text.insert(END, string=0)
        self.lower_csg_weight_text.grid(row=6, column=3, sticky='w')
        # --------- MID CSG ----------------
        self.bha_label_mid_csg = Label(self.canvas_frame_csg, text="Mid Casing String: ", fg='black', bg='#9BA4B4')
        self.bha_label_mid_csg.grid(row=7, column=0, sticky='w', padx=5)
        self.bha_text_mid_csg = Entry(self.canvas_frame_csg, foreground='black')
        self.bha_text_mid_csg.insert(END, string=0)
        self.bha_text_mid_csg.grid(row=7, column=1, sticky='w', padx=5)
        self.mid_csg_weight_label = Label(self.canvas_frame_csg, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.mid_csg_weight_label.grid(row=7, column=2, sticky='e', padx=5)
        self.mid_csg_weight_text = Entry(self.canvas_frame_csg, foreground='black', width=5)
        self.mid_csg_weight_text.insert(END, string=0)
        self.mid_csg_weight_text.grid(row=7, column=3, sticky='w')
        # --------- TOP CSG -----------------
        self.bha_label_top_csg = Label(self.canvas_frame_csg, text="Top Casing/Landing String: ", fg='black',
                                       bg='#9BA4B4')
        self.bha_label_top_csg.grid(row=8, column=0, sticky='w', padx=5)
        self.bha_value_top_csg = Label(self.canvas_frame_csg, text="0", fg='#0A1931', bg='#77ACF1')
        self.bha_value_top_csg.grid(row=8, column=1, sticky='w', padx=5)
        self.top_csg_weight_label = Label(self.canvas_frame_csg, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.top_csg_weight_label.grid(row=8, column=2, sticky='e', padx=5)
        self.top_csg_weight_text = Entry(self.canvas_frame_csg, foreground='black', width=5)
        self.top_csg_weight_text.insert(END, string=0)
        self.top_csg_weight_text.grid(row=8, column=3, sticky='w')
        # ---------------------------------------------------------------
        self.compute_button = Button(self.canvas_frame_csg, text='Compute Casing Miles', bg='#77ACF1', width=30)
        self.compute_button.grid(row=9, column=2, sticky='w', pady=10, columnspan=3)
        # ---------------------------------------------------------------

    def liner_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_liner.tkraise()
        self.change_button_colors(self.liner_button, self.casing_button, self.tripping_button, self.drilling_button,
                                  self.jarring_button)
        # --------------------------LINER TON MILES UI ELEMENTS-------------------------------------
        self.depth_label1 = Label(self.canvas_frame_liner, text="Liner Shoe Setting Depth: ", fg='black', bg='#9BA4B4')
        self.depth_label1.grid(row=1, column=0, sticky='w', padx=5)
        self.depth_text1 = Entry(self.canvas_frame_liner, foreground='black')
        self.depth_text1.insert(END, string=0)
        self.depth_text1.grid(row=1, column=1, sticky='w', padx=5)
        self.liner_length_label = Label(self.canvas_frame_liner, text="Liner String Length: ", fg='black', bg='#9BA4B4')
        self.liner_length_label.grid(row=2, column=0, sticky='w', padx=5)
        self.liner_length_text = Entry(self.canvas_frame_liner, foreground='black')
        self.liner_length_text.insert(END, string=0)
        self.liner_length_text.grid(row=2, column=1, sticky='w', padx=5)
        self.liner_weight_label = Label(self.canvas_frame_liner, text="Liner Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.liner_weight_label.grid(row=2, column=2, sticky='e', padx=5)
        self.liner_weight_text = Entry(self.canvas_frame_liner, foreground='black', width=5)
        self.liner_weight_text.insert(END, string=0)
        self.liner_weight_text.grid(row=2, column=3, sticky='w')
        self.label_dp = Label(self.canvas_frame_liner, text="Drill Pipe Length: ", fg='black', bg='#9BA4B4')
        self.label_dp.grid(row=3, column=0, sticky='w', padx=5, pady=10)
        self.dp_value = Label(self.canvas_frame_liner, text="0", fg='#0A1931', bg='#77ACF1')
        self.dp_value.grid(row=3, column=1, sticky='w', padx=5, pady=10)
        self.dp_weight_label = Label(self.canvas_frame_liner, text="Weight of DP in ppf: ", fg='black', bg='#9BA4B4')
        self.dp_weight_label.grid(row=3, column=2, sticky='e', padx=5, pady=10)
        self.dp_weight_text = Entry(self.canvas_frame_liner, foreground='black', width=5)
        self.dp_weight_text.insert(END, string=0)
        self.dp_weight_text.grid(row=3, column=3, sticky='w', pady=10)

        # ---------------------------------------------------------------
        self.compute_button = Button(self.canvas_frame_liner, text='Compute Liner Ton Miles', bg='#77ACF1', width=30)
        self.compute_button.grid(row=5, column=2, sticky='w', pady=10, columnspan=3)
        # -------------------------------------------------------------------------------------------------------

    def jarring_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_jarring.tkraise()
        self.change_button_colors(self.jarring_button, self.liner_button, self.casing_button,
                                  self.tripping_button, self.drilling_button)
        # --------------------------------------------------------------------------------------------------

        self.jar_title = Label(self.canvas_frame_jarring, text="Jarring Details: ", fg='#0A1931', bg='#9BA4B4',
                               font=('serif', 14, 'bold'))
        self.jar_title.grid(row=1, column=0, pady=10)

        self.top_reading_label = Label(self.canvas_frame_jarring, text="Weight Indicator Reading @ Top of Up-Stroke: ",
                                       fg='black', bg='#9BA4B4')
        self.top_reading_label.grid(row=2, column=0, sticky='w', padx=5)
        self.top_reading_text = Entry(self.canvas_frame_jarring, foreground='black')
        self.top_reading_text.insert(END, string=0)
        self.top_reading_text.grid(row=2, column=1, sticky='w', padx=5)
        self.btm_reading_label = Label(self.canvas_frame_jarring,
                                       text="Weight Indicator Reading @ Btm of Down-Stroke: ",
                                       fg='black', bg='#9BA4B4')
        self.btm_reading_label.grid(row=3, column=0, sticky='w', padx=5)
        self.btm_reading_text = Entry(self.canvas_frame_jarring, foreground='black')
        self.btm_reading_text.insert(END, string=0)
        self.btm_reading_text.grid(row=3, column=1, sticky='w', padx=5)
        self.distance_label = Label(self.canvas_frame_jarring,
                                    text="Distance Travelled Between Top & Btm of Each Stroke: ",
                                    fg='black',
                                    bg='#9BA4B4')
        self.distance_label.grid(row=4, column=0, sticky='w', padx=5)
        self.distance_text = Entry(self.canvas_frame_jarring, foreground='black')
        self.distance_text.insert(END, string=0)
        self.distance_text.grid(row=4, column=1, sticky='w', padx=5)
        self.number_label = Label(self.canvas_frame_jarring, text="Number of Strokes/Hour: ", fg='black', bg='#9BA4B4')
        self.number_label.grid(row=5, column=0, sticky='w', padx=5)
        self.number_text = Entry(self.canvas_frame_jarring, foreground='black')
        self.number_text.insert(END, string=0)
        self.number_text.grid(row=5, column=1, sticky='w', padx=5)

        self.hours_label = Label(self.canvas_frame_jarring, text="Number of Hours Jarring: ", fg='black', bg='#9BA4B4')
        self.hours_label.grid(row=6, column=0, sticky='w', padx=5)
        self.hours_text = Entry(self.canvas_frame_jarring, foreground='black')
        self.hours_text.insert(END, string=0)
        self.hours_text.grid(row=6, column=1, sticky='w', padx=5)
        # ---------------------------------------------------------------
        self.compute_button = Button(self.canvas_frame_jarring, text='Compute Jarring Miles', bg='#77ACF1', width=30)
        self.compute_button.grid(row=7, column=2, sticky='w', pady=10, columnspan=3)
        # ___________________________________________________________________________________________________________


class Calculate(MainScreen):
    def __init__(self, main):
        super().__init__(main)

    def drill_miles_data(self):

        start_depth = float(self.drilling_text1.get().strip())
        end_depth = float(self.drilling_text2.get().strip())
        drilled_depth = end_depth - start_depth

        dc1_length = float(self.bha_text_dc1.get().strip())
        dc1_ppf = float(self.dc1_weight_text.get().strip())
        dc1_bw = calculate_functions.calculate_boyed_weight(dc1_length, dc1_ppf, self.bf)

        dc2_length = float(self.bha_text_dc2.get().strip())
        dc2_ppf = float(self.dc2_weight_text.get().strip())
        dc2_bw = calculate_functions.calculate_boyed_weight(dc2_length, dc2_ppf, self.bf)

        hwdp_length = float(self.bha_text_hwdp.get().strip())
        hwdp_ppf = float(self.hwdp_weight_text.get().strip())
        hwdp_bw = calculate_functions.calculate_boyed_weight(hwdp_length, hwdp_ppf, self.bf)

        dp1_length = float(self.bha_text_dp1.get().strip())
        dp1_ppf = float(self.dp1_weight_text.get().strip())
        dp1_bw = calculate_functions.calculate_boyed_weight(dp1_length, dp1_ppf, self.bf)

        dp2_length_start = (start_depth - dc1_length - dc2_length - hwdp_length - dp1_length)
        dp2_ppf = float(self.dp2_weight_text.get().strip())
        # -------------- AUTO-FILL SECOND STRING OF DRILL-PIPE BASED ON DEPTH ENTERED ----------------
        if dp2_length_start > 0:
            self.bha_dp2_value.config(text=dp2_length_start)
            dp2_bw_start = calculate_functions.calculate_boyed_weight(dp2_length_start, dp2_ppf, self.bf)
        else:
            self.bha_dp2_value.config(text=0)
            dp2_bw_start = 0
        dp2_length_end = (end_depth - dc1_length - dc2_length - hwdp_length - dp1_length)

        if dp2_length_end > 0:
            self.bha_dp2_value_end.config(text=dp2_length_end)
            dp2_bw_end = calculate_functions.calculate_boyed_weight(dp2_length_end, dp2_ppf, self.bf)
        else:
            self.bha_dp2_value_end.config(text=0)
            dp2_bw_end = 0
            # ______________________________________________________

        total_str_wt_depth1 = calculate_functions.cal_total_wt(dc1_bw, dc2_bw, hwdp_bw, dp1_bw, dp2_bw_start)
        total_str_wt_depth2 = calculate_functions.cal_total_wt(dc1_bw, dc2_bw, hwdp_bw, dp1_bw, dp2_bw_end)
        total_str_wt_avg_tons = (total_str_wt_depth1 + total_str_wt_depth2) / 2
        ream = float(self.drilling_text4.get().strip())
        drilling_miles_total = calculate_functions.calculate_drill_miles(drilled_depth, self.block_wt,
                                                                         total_str_wt_avg_tons, ream)
        self.drilling_miles_result_value.config(text=f'{drilling_miles_total:.2f}')  # ---> SEND DATA TO BTM FRAME


drilling_trigger = Calculate()

main_screen = MainScreen(window)
window.mainloop()
