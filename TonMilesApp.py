from tkinter import *
from datetime import *
from tkinter import messagebox
import functions
import pandas as pd

window = Tk()
window.title(f"{datetime.now():%a, %b %d %Y} | Ton Miles Calculator | Developer: madon.zubin@gmail.com")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("+%d+%d" % (200, 100))
window.config(background='#394867')
icon_photo = PhotoImage(file='images/icon.png')
window.iconphoto(False, icon_photo)


class MainScreen:
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
        # -----------------------DRILLING UI WIDGETS------------------------------------------------
        self.drilling_label1 = Label(self.canvas_frame_drill, text="Drill From: ", fg='black', bg='#9BA4B4')
        self.drilling_text1 = Entry(self.canvas_frame_drill, foreground='black')
        self.drilling_label2 = Label(self.canvas_frame_drill, text="To: ", fg='black', bg='#9BA4B4')
        self.drilling_text2 = Entry(self.canvas_frame_drill, foreground='black')
        self.drilling_label3 = Label(self.canvas_frame_drill, text="No. of times reamed stand: ", fg='black',
                                     bg='#9BA4B4')
        self.drilling_text4 = Entry(self.canvas_frame_drill, foreground='black', width=6)
        self.bha_drill_title = Label(self.canvas_frame_drill, text="BHA Details: ", fg='#0A1931', bg='#9BA4B4',
                                     font=('serif', 14, 'bold'))
        self.bha_drill_label_dc_drill1 = Label(self.canvas_frame_drill, text="Drill Collars (Bottom): ", fg='black',
                                               bg='#9BA4B4')
        self.bha_drill_text_dc_drill1 = Entry(self.canvas_frame_drill, foreground='black')
        self.dc_drill1_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dc_drill1_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.bha_drill_label_dc_drill2 = Label(self.canvas_frame_drill, text="Drill Collars (Top): ", fg='black',
                                               bg='#9BA4B4')
        self.bha_drill_text_dc_drill2 = Entry(self.canvas_frame_drill, foreground='black')
        self.dc_drill2_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dc_drill2_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.bha_drill_label_hwdp_drill = Label(self.canvas_frame_drill, text="HWDP: ", fg='black', bg='#9BA4B4')
        self.bha_drill_text_hwdp_drill = Entry(self.canvas_frame_drill, foreground='black')
        self.hwdp_drill_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.hwdp_drill_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.bha_drill_label_dp_drill1 = Label(self.canvas_frame_drill, text="Drill Pipe (Bottom): ", fg='black',
                                               bg='#9BA4B4')
        self.bha_drill_text_dp_drill1 = Entry(self.canvas_frame_drill, foreground='black')
        self.dp_drill1_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dp_drill1_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.bha_drill_label_dp_drill2 = Label(self.canvas_frame_drill, text="Drill Pipe (Top) @ start of section: ",
                                               fg='black', bg='#9BA4B4')
        self.bha_drill_dp_drill2_value = Label(self.canvas_frame_drill, text="0", fg='#0A1931', bg='#77ACF1')
        self.dp_drill2_weight_label = Label(self.canvas_frame_drill, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dp_drill2_weight_text = Entry(self.canvas_frame_drill, foreground='black', width=5)
        self.dp_drill2_warning_label = Label(self.canvas_frame_drill,
                                             text="(Enter only if you're using 2 types of Drill Pipe in string)",
                                             fg='black', bg='#9BA4B4')
        self.bha_drill_label_dp_drill2_end = Label(self.canvas_frame_drill, text="Drill Pipe (Top) @ end of section: ",
                                                   fg='black', bg='#9BA4B4')
        self.bha_drill_dp_drill2_value_end = Label(self.canvas_frame_drill, text="0", fg='#0A1931', bg='#77ACF1')

        # ------------------------------DRILLING UI WIDGET GRID & INSERTS-----------------------------------------
        self.drilling_label1.grid(row=0, column=0, sticky='e', padx=5)
        self.drilling_text1.insert(END, string=0)
        self.drilling_text1.grid(row=0, column=1, sticky='w', padx=5)

        self.drilling_label2.grid(row=0, column=2, sticky='e', padx=5)
        self.drilling_text2.insert(END, string=0)
        self.drilling_text2.grid(row=0, column=3, sticky='w', padx=5)

        self.drilling_label3.grid(row=0, column=4, sticky='ew', padx=5)
        self.drilling_text4.insert(END, string=0)
        self.drilling_text4.grid(row=0, column=5, sticky='w', padx=10)

        # ---------DRILLING BHA Elements Grid and Inserts--------------------
        self.bha_drill_title.grid(row=1, column=0, pady=10)
        # ----dc_drill1---------------------
        self.bha_drill_label_dc_drill1.grid(row=2, column=0, sticky='w', padx=5)
        self.bha_drill_text_dc_drill1.insert(END, string=0)
        self.bha_drill_text_dc_drill1.grid(row=2, column=1, sticky='w', padx=5)
        self.dc_drill1_weight_label.grid(row=2, column=2, sticky='e', padx=5)
        self.dc_drill1_weight_text.insert(END, string=0)
        self.dc_drill1_weight_text.grid(row=2, column=3, sticky='w')
        # ----dc_drill2---------------------
        self.bha_drill_label_dc_drill2.grid(row=3, column=0, sticky='w', padx=5)
        self.bha_drill_text_dc_drill2.insert(END, string=0)
        self.bha_drill_text_dc_drill2.grid(row=3, column=1, sticky='w', padx=5)
        self.dc_drill2_weight_label.grid(row=3, column=2, sticky='e', padx=5)
        self.dc_drill2_weight_text.insert(END, string=0)
        self.dc_drill2_weight_text.grid(row=3, column=3, sticky='w')
        # ---------HWdp_drill--------------
        self.bha_drill_label_hwdp_drill.grid(row=4, column=0, sticky='w', padx=5)
        self.bha_drill_text_hwdp_drill.insert(END, string=0)
        self.bha_drill_text_hwdp_drill.grid(row=4, column=1, sticky='w', padx=5)
        self.hwdp_drill_weight_label.grid(row=4, column=2, sticky='e', padx=5)
        self.hwdp_drill_weight_text.insert(END, string=0)
        self.hwdp_drill_weight_text.grid(row=4, column=3, sticky='w')
        # ---------dp_drill1 (Bottom)--------------
        self.bha_drill_label_dp_drill1.grid(row=5, column=0, sticky='w', padx=5)
        self.bha_drill_text_dp_drill1.insert(END, string=0)
        self.bha_drill_text_dp_drill1.grid(row=5, column=1, sticky='w', padx=5)
        self.dp_drill1_weight_label.grid(row=5, column=2, sticky='e', padx=5)
        self.dp_drill1_weight_text.insert(END, string=0)
        self.dp_drill1_weight_text.grid(row=5, column=3, sticky='w')
        # ---------dp (Top)START--------------
        self.bha_drill_label_dp_drill2.grid(row=6, column=0, sticky='w', padx=5)
        self.bha_drill_dp_drill2_value.grid(row=6, column=1, sticky='w', padx=5)
        self.dp_drill2_weight_label.grid(row=6, column=2, sticky='e', padx=5)
        self.dp_drill2_weight_text.insert(END, string=0)
        self.dp_drill2_weight_text.grid(row=6, column=3, sticky='w')
        self.dp_drill2_warning_label.grid(row=6, column=4, sticky='w', padx=5)
        # -----------dp (TOP)END-----------------------
        self.bha_drill_label_dp_drill2_end.grid(row=7, column=0, sticky='w', padx=5)
        self.bha_drill_dp_drill2_value_end.grid(row=7, column=1, sticky='w', padx=5)

        # ------------------------TRIPPING UI ELEMENTS, GRIDS AND INSERTS------------------------------------
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
        # ---------bha_trip Elements--------------------
        self.bha_trip_title = Label(self.canvas_frame_trip, text="bha_trip Details: ", fg='#0A1931', bg='#9BA4B4',
                                    font=('serif', 14, 'bold'))
        self.bha_trip_title.grid(row=4, column=0, pady=10)
        # ----dc trip1---------------------
        self.bha_trip_label_dc_trip1 = Label(self.canvas_frame_trip, text="Drill Collars (Bottom): ", fg='black',
                                             bg='#9BA4B4')
        self.bha_trip_label_dc_trip1.grid(row=5, column=0, sticky='w', padx=5)
        self.bha_trip_text_dc_trip1 = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_trip_text_dc_trip1.insert(END, string=0)
        self.bha_trip_text_dc_trip1.grid(row=5, column=1, sticky='w', padx=5)
        self.dc_trip1_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dc_trip1_weight_label.grid(row=5, column=2, sticky='e', padx=5)
        self.dc_trip1_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dc_trip1_weight_text.insert(END, string=0)
        self.dc_trip1_weight_text.grid(row=5, column=3, sticky='w')
        # ----dc trip2---------------------
        self.bha_trip_label_dc_trip2 = Label(self.canvas_frame_trip, text="Drill Collars (Top): ", fg='black', bg='#9BA4B4')
        self.bha_trip_label_dc_trip2.grid(row=6, column=0, sticky='w', padx=5)
        self.bha_trip_text_dc_trip2 = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_trip_text_dc_trip2.insert(END, string=0)
        self.bha_trip_text_dc_trip2.grid(row=6, column=1, sticky='w', padx=5)
        self.dc_trip2_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dc_trip2_weight_label.grid(row=6, column=2, sticky='e', padx=5)
        self.dc_trip2_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dc_trip2_weight_text.insert(END, string=0)
        self.dc_trip2_weight_text.grid(row=6, column=3, sticky='w')
        # ---------HWdp trip--------------
        self.bha_trip_label_hwdp_trip = Label(self.canvas_frame_trip, text="HWDP: ", fg='black', bg='#9BA4B4')
        self.bha_trip_label_hwdp_trip.grid(row=7, column=0, sticky='w', padx=5)
        self.bha_trip_text_hwdp_trip = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_trip_text_hwdp_trip.insert(END, string=0)
        self.bha_trip_text_hwdp_trip.grid(row=7, column=1, sticky='w', padx=5)
        self.hwdp_trip_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.hwdp_trip_weight_label.grid(row=7, column=2, sticky='e', padx=5)
        self.hwdp_trip_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.hwdp_trip_weight_text.insert(END, string=0)
        self.hwdp_trip_weight_text.grid(row=7, column=3, sticky='w')
        # ---------dp trip1 (Bottom)--------------
        self.bha_trip_label_dp_trip1 = Label(self.canvas_frame_trip, text="Drill Pipe (Bottom): ", fg='black',
                                             bg='#9BA4B4')
        self.bha_trip_label_dp_trip1.grid(row=8, column=0, sticky='w', padx=5)
        self.bha_trip_text_dp_trip1 = Entry(self.canvas_frame_trip, foreground='black')
        self.bha_trip_text_dp_trip1.insert(END, string=0)
        self.bha_trip_text_dp_trip1.grid(row=8, column=1, sticky='w', padx=5)
        self.dp_trip1_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dp_trip1_weight_label.grid(row=8, column=2, sticky='e', padx=5)
        self.dp_trip1_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dp_trip1_weight_text.insert(END, string=0)
        self.dp_trip1_weight_text.grid(row=8, column=3, sticky='w')
        # ---------dp trip2 (Top)START--------------
        self.bha_trip_label_dp_trip2 = Label(self.canvas_frame_trip, text="Drill Pipe (At the Top): ", fg='black',
                                             bg='#9BA4B4')
        self.bha_trip_label_dp_trip2.grid(row=9, column=0, sticky='w', padx=5)
        self.bha_trip_dp_trip2_value = Label(self.canvas_frame_trip, text="0", fg='#0A1931', bg='#77ACF1')
        self.bha_trip_dp_trip2_value.grid(row=9, column=1, sticky='w', padx=5)
        self.dp_trip2_weight_label = Label(self.canvas_frame_trip, text="Weight in ppf: ", fg='black', bg='#9BA4B4')
        self.dp_trip2_weight_label.grid(row=9, column=2, sticky='e', padx=5)
        self.dp_trip2_weight_text = Entry(self.canvas_frame_trip, foreground='black', width=5)
        self.dp_trip2_weight_text.insert(END, string=0)
        self.dp_trip2_weight_text.grid(row=9, column=3, sticky='w')
        self.dp_trip2_warning_label = Label(self.canvas_frame_trip,
                                            text="(Enter only if you're using 2 types of Drill Pipe in string)",
                                            fg='black', bg='#9BA4B4')
        self.dp_trip2_warning_label.grid(row=9, column=4, sticky='w', padx=5)
        # ---------------------------------------------------------------
        # __________________________________CASING UI ELEMENTS WITH GRIDS, ENTRIES --------------------
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
        self.depth_csg_text1 = Entry(self.canvas_frame_csg, foreground='black')
        self.depth_csg_text1.insert(END, string=0)
        self.depth_csg_text1.grid(row=2, column=1, sticky='w', padx=5)
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
        # --------------------------LINER TON MILES UI ELEMENTS-------------------------------------
        self.depth_label1 = Label(self.canvas_frame_liner, text="Liner Shoe Setting Depth: ", fg='black', bg='#9BA4B4')
        self.depth_label1.grid(row=1, column=0, sticky='w', padx=5)
        self.depth_liner_text1 = Entry(self.canvas_frame_liner, foreground='black')
        self.depth_liner_text1.insert(END, string=0)
        self.depth_liner_text1.grid(row=1, column=1, sticky='w', padx=5)
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
        self.liner_note_label = Label(self.canvas_frame_liner,
                                      text="Note: Total includes miles gained during POOH DP. ",
                                      fg='#14274E', bg='#9BA4B4')
        self.liner_note_label.grid(row=4, column=0, columnspan=3, sticky='w', padx=5, pady=10)
        # ---------------------------------------------------------------
        # -----------------------JARRING UI ELEMENTS AND GRIDS, ENTRIES-------------------------------

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
        self.canvas_frame.tkraise()  # --> Initially we want the center frame to be blank upon launch. This does it.
        # -----------Date Elements Widgets-----------
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
        # ---------------------COMMIT DATE & RIG NAME WIDGETS-------------------
        self.submit_top = Button(self.top_frame, text='Submit', command=self.submit_date, bg='#77ACF1')
        self.submit_top.grid(row=0, column=6, pady=5, sticky='e', padx=10)
        self.top_entry_confirm = Label(self.top_frame, text=f"Rig: Choose the options below to enter data for: ",
                                       bg='#14274E',
                                       fg='#9BA4B4')
        self.top_entry_confirm.grid(row=1, column=0, padx=5, sticky='w', columnspan=7)
        # ----------Block Weight & Mud Weight Widgets ---------------
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
        self.total_miles_result_value = Label(self.bottom_frame, text=f'{self.total_miles_result}', bg='#394867',
                                              fg='#DA7F8F',
                                              font=('serif', 12, 'bold'))
        self.total_miles_result_value.grid(row=6, column=1, sticky='w', padx=10)
        self.comments_box = Text(self.bottom_frame, height=3, width=60)
        self.comments_box.insert(END, "Enter Ops Details Before Clicking Submit")
        self.comments_box.grid(row=7, column=0, sticky='w', pady=10, columnspan=6, padx=10)
        self.submit_day_data = Button(self.bottom_frame, text="Commit Day's Data to CSV File", bg='#77ACF1', width=30,
                                      command=self.submit_warning)
        self.submit_day_data.grid(row=10, column=0, sticky='w', pady=10, padx=10, columnspan=5)
        self.total_miles_result = 0
        # ------------------------------------------------------------------------------------------------

    # ------------------------------FUNCTIONS-------------------------------------------------------------
    def store_ton_miles_data(self):  # --> This commits the data to the CSV.

        self.comments = self.comments_box.get('1.0', "end-1c")
        rig_name_entered = self.rig_name_entry.get()
        self.get_total_miles()
        new_entry = [rig_name_entered, MainScreen.formatted_date, f'{MainScreen.drilling_miles_total:.2f}',
                     f'{MainScreen.tripping_miles_total:.2f}',
                     f'{MainScreen.casing_miles_total:.2f}',
                     f'{MainScreen.liner_miles_total:.2f}', f'{MainScreen.jarring_miles_total:.2f}',
                     MainScreen.total_miles_result, self.comments]

        data = pd.read_csv('ton_miles_record.csv')
        if data['Date'].values.any() == MainScreen.formatted_date:
            duplicate = messagebox.askyesnocancel('Oops! An Entry for this Date Already Exists!',
                                                  'To go back & check the date you have entered, press CANCEL. '
                                                  'If you wish to replace the previous entry, press YES. If you wish '
                                                  'to create an extra entry with the same date, press NO.')

            if duplicate:
                location = data[data['Date'] == MainScreen.formatted_date].index.values[0]
                data.loc[
                    location, ['RigName', 'Date', 'DrillingMiles', 'TrippingMiles', 'CasingMiles', 'LinerMiles',
                               'JarringMiles',
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

    # -------------------------This calculates Block WT, Mud Wt & Buoyancy Factor---------------------------
    def get_blockwt_mudwt_bf(self):
        self.block_wt = float(self.block_wt_label_entry.get().strip()) / 2000
        self.mud_wt = float(self.mud_wt_label_entry.get().strip())
        self.bf = (65.44 - self.mud_wt) / 65.44

    # ------------------This function changes colour of the active button-------------------------------
    def change_button_colors(self, active_button, button2, button3, button4, button5):
        active_button.config(bg='#3EDBF0')
        button2.config(bg='#77ACF1')
        button3.config(bg='#77ACF1')
        button4.config(bg='#77ACF1')
        button5.config(bg='#77ACF1')

    # -Calculates & total ton miles once all drilling/tripping/jarring etc. miles for the day have been calculated----
    def get_total_miles(self):
        drill_result = float(self.drilling_miles_result_value.cget('text'))
        trip_result = float(self.tripping_miles_result_value.cget('text'))
        csg_result = float(self.casing_miles_result_value.cget('text'))
        liner_result = float(self.liner_miles_result_value.cget('text'))
        jarring_result = float(self.jarring_miles_result_value.cget('text'))
        MainScreen.total_miles_result = drill_result + trip_result + csg_result + liner_result + jarring_result
        self.total_miles_result_value.config(text=MainScreen.total_miles_result)

    # ----Takes the date and displays it in bottom widgets. This is needed for CSV file entry--------
    def submit_date(self):
        try:
            dd = int(self.dd_entry.get().strip())
            mm = int(self.mm_entry.get().strip())
            yyyy = int(self.yy_entry.get().strip())
            MainScreen.formatted_date = date(day=dd, month=mm, year=yyyy).strftime('%d %B %Y')
            self.top_entry_confirm.config(text=f"Rig: {self.rig_name_entry.get()} | Choose the options below"
                                               f" to enter data for: {MainScreen.formatted_date}.")
            self.date_bottom_value.config(text=MainScreen.formatted_date)

        except ValueError:
            messagebox.showerror(title="Invalid Input!", message="Please enter only numbers in DD, MM, YYYY format.")

    # ----------------------------------------------------------------------------------------------------------------

    # -------------------------CONFIRM SUBMISSION WARNING BOX ---------------------
    def submit_warning(self):
        if self.date_bottom_value.cget('text') != MainScreen.formatted_date:
            messagebox.showwarning("Date Not Committed!", "Please Commit the Date on top by clicking 'Submit'.")
            return
        confirm = messagebox.askokcancel('Confirm!', 'You are about to enter the ton-miles '
                                                     'for the day to the CSV file. Continue?')
        if confirm:
            self.store_ton_miles_data()
        else:
            return
        # -----------------------------------------------------------------------------

    # ----------TRIGGERED WHEN THE DRILLING BUTTON IS PRESSED, DRILLING FRAME WILL COME UP & ALL WIDGETS WILL APPEAR---
    def drilling_ui(self):
        self.canvas_frame.tkraise()  # ----Brings blank frame up first, so that widgets from other frames don't clash.
        self.canvas_frame_drill.tkraise()  # ----Raises the drilling frame to top and brings all its widgets up.
        self.change_button_colors(self.drilling_button, self.tripping_button, self.casing_button, self.liner_button,
                                  self.jarring_button)
        self.compute_drilling_button = Button(self.canvas_frame_drill, text='Compute Drilling Miles', bg='#77ACF1',
                                              width=30, command=self.drill_miles_data)
        self.compute_drilling_button.grid(row=7, column=2, sticky='w', pady=10, columnspan=3)

    # ----------TRIGGERED WHEN THE TRIPPING BUTTON IS PRESSED, TRIPPING FRAME WILL COME UP & ALL WIDGETS WILL APPEAR---
    def tripping_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_trip.tkraise()
        self.change_button_colors(self.tripping_button, self.drilling_button, self.casing_button, self.liner_button,
                                  self.jarring_button)
        # ---------------COMPUTE TRIPPING MILES BUTTON TO SEND DATA TO BTM FRAME--------------------------
        self.compute_tripping_button = Button(self.canvas_frame_trip, text='Compute Tripping Miles', bg='#77ACF1',
                                              width=30, command=self.trip_miles_data)
        self.compute_tripping_button.grid(row=10, column=2, sticky='w', pady=10, columnspan=3)

    # ----------TRIGGERED WHEN THE CASING BUTTON IS PRESSED, CASING FRAME WILL COME UP & ALL WIDGETS WILL APPEAR---
    def casing_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_csg.tkraise()
        self.change_button_colors(self.casing_button, self.tripping_button, self.drilling_button, self.liner_button,
                                  self.jarring_button)
        self.compute_csg_button = Button(self.canvas_frame_csg, text='Compute Casing Miles', bg='#77ACF1', width=30,
                                         command=self.casing_miles_data)
        self.compute_csg_button.grid(row=9, column=2, sticky='w', pady=10, columnspan=3)

    # ----------TRIGGERED WHEN THE LINER BUTTON IS PRESSED, CASING FRAME WILL COME UP & ALL WIDGETS WILL APPEAR---
    def liner_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_liner.tkraise()
        self.change_button_colors(self.liner_button, self.casing_button, self.tripping_button, self.drilling_button,
                                  self.jarring_button)
        self.compute_liner_button = Button(self.canvas_frame_liner, text='Compute Liner Ton Miles', bg='#77ACF1',
                                           width=30, command=self.liner_ton_miles_data)
        self.compute_liner_button.grid(row=5, column=2, sticky='w', pady=10, columnspan=3)

    # ----------TRIGGERED WHEN THE JARRING BUTTON IS PRESSED, CASING FRAME WILL COME UP & ALL WIDGETS WILL APPEAR---
    def jarring_ui(self):
        self.canvas_frame.tkraise()
        self.canvas_frame_jarring.tkraise()
        self.change_button_colors(self.jarring_button, self.liner_button, self.casing_button,
                                  self.tripping_button, self.drilling_button)
        self.compute_jarring_button = Button(self.canvas_frame_jarring, text='Compute Jarring Miles', bg='#77ACF1',
                                             width=30, command=self.jarring_ton_miles_data)
        self.compute_jarring_button.grid(row=7, column=2, sticky='w', pady=10, columnspan=3)

    # --------------------------------------------------------------------------------------------------------------
    '''TRIGGERED BY COMPUTE BUTTON. TAKES USER INPUTS FROM WIDGETS & MAKES CALCULATIONS USING FUNCTIONS FROM THE
        CALCULATE_FUNCTIONS FILE.'''

    def drill_miles_data(self):
        self.get_blockwt_mudwt_bf()

        start_depth_drill = float(self.drilling_text1.get().strip())
        end_depth_drill = float(self.drilling_text2.get().strip())
        drilled_depth = end_depth_drill - start_depth_drill
        dc_drill1_length = float(self.bha_drill_text_dc_drill1.get().strip())
        dc_drill1_ppf = float(self.dc_drill1_weight_text.get().strip())
        dc_drill1_bw = functions.calculate_boyed_weight(dc_drill1_length, dc_drill1_ppf, self.bf)

        dc_drill2_length = float(self.bha_drill_text_dc_drill2.get().strip())
        dc_drill2_ppf = float(self.dc_drill2_weight_text.get().strip())
        dc_drill2_bw = functions.calculate_boyed_weight(dc_drill2_length, dc_drill2_ppf, self.bf)

        hwdp_drill_length = float(self.bha_drill_text_hwdp_drill.get().strip())
        hwdp_drill_ppf = float(self.hwdp_drill_weight_text.get().strip())
        hwdp_drill_bw = functions.calculate_boyed_weight(hwdp_drill_length, hwdp_drill_ppf, self.bf)

        dp_drill1_length = float(self.bha_drill_text_dp_drill1.get().strip())
        dp_drill1_ppf = float(self.dp_drill1_weight_text.get().strip())
        dp_drill1_bw = functions.calculate_boyed_weight(dp_drill1_length, dp_drill1_ppf, self.bf)

        dp_drill2_length_start = (
                start_depth_drill - dc_drill1_length - dc_drill2_length - hwdp_drill_length - dp_drill1_length)
        dp_drill2_ppf = float(self.dp_drill2_weight_text.get().strip())
        # -------------- AUTO-FILL SECOND STRING OF DRILL-PIPE BASED ON DEPTH ENTERED ----------------
        if dp_drill2_length_start > 0:
            self.bha_drill_dp_drill2_value.config(text=dp_drill2_length_start)
            dp_drill2_bw_start = functions.calculate_boyed_weight(dp_drill2_length_start, dp_drill2_ppf,
                                                                  self.bf)
        else:
            self.bha_drill_dp_drill2_value.config(text=0)
            dp_drill2_bw_start = 0
        dp_drill2_length_end = (
                end_depth_drill - dc_drill1_length - dc_drill2_length - hwdp_drill_length - dp_drill1_length)

        if dp_drill2_length_end > 0:
            self.bha_drill_dp_drill2_value_end.config(text=dp_drill2_length_end)
            dp_drill2_bw_end = functions.calculate_boyed_weight(dp_drill2_length_end, dp_drill2_ppf, self.bf)
        else:
            self.bha_drill_dp_drill2_value_end.config(text=0)
            dp_drill2_bw_end = 0
            # ______________________________________________________
        total_str_wt_depth1 = functions.cal_total_wt(dc_drill1_bw, dc_drill2_bw, hwdp_drill_bw, dp_drill1_bw,
                                                     dp_drill2_bw_start)
        total_str_wt_depth2 = functions.cal_total_wt(dc_drill1_bw, dc_drill2_bw, hwdp_drill_bw, dp_drill1_bw,
                                                     dp_drill2_bw_end)
        total_str_wt_avg_tons = (total_str_wt_depth1 + total_str_wt_depth2) / 2
        ream = float(self.drilling_text4.get().strip())
        MainScreen.drilling_miles_total = functions.calculate_drill_miles(drilled_depth, self.block_wt,
                                                                          total_str_wt_avg_tons, ream)
        self.drilling_miles_result_value.config(
            text=f'{MainScreen.drilling_miles_total:.2f}')  # ---> SEND DATA TO BTM FRAME
        self.get_total_miles()  # ----------ADDING MILES TO TOTAL MILES

    # -----------------------------------------------------------------------------------------------------------
    '''TRIGGERED BY COMPUTE BUTTON. TAKES USER INPUTS FROM WIDGETS & MAKES CALCULATIONS USING FUNCTIONS FROM THE
            CALCULATE_FUNCTIONS FILE.'''

    def trip_miles_data(self):
        self.get_blockwt_mudwt_bf()
        start_depth_trip = float(self.tripping_text1.get().strip())
        end_depth_trip = float(self.tripping_text2.get().strip())
        total_depth = end_depth_trip - start_depth_trip

        dc_trip1_trip_length = float(self.bha_trip_text_dc_trip1.get().strip())
        dc_trip1_trip_ppf = float(self.dc_trip1_weight_text.get().strip())
        dc_trip1_trip_bw = functions.calculate_boyed_weight(dc_trip1_trip_length, dc_trip1_trip_ppf, self.bf)

        dc_trip2_trip_length = float(self.bha_trip_text_dc_trip2.get().strip())
        dc_trip2_trip_ppf = float(self.dc_trip2_weight_text.get().strip())
        dc_trip2_trip_bw = functions.calculate_boyed_weight(dc_trip2_trip_length, dc_trip2_trip_ppf, self.bf)

        hwdp_trip_trip_length = float(self.bha_trip_text_hwdp_trip.get().strip())
        hwdp_trip_trip_ppf = float(self.hwdp_trip_weight_text.get().strip())
        hwdp_trip_trip_bw = functions.calculate_boyed_weight(hwdp_trip_trip_length, hwdp_trip_trip_ppf,
                                                             self.bf)

        dp_trip1_trip_length = float(self.bha_trip_text_dp_trip1.get().strip())
        dp_trip1_trip_ppf = float(self.dp_trip1_weight_text.get().strip())
        dp_trip1_trip_bw = functions.calculate_boyed_weight(dp_trip1_trip_length, dp_trip1_trip_ppf, self.bf)

        dp_trip2_trip_length = (
                total_depth - dc_trip1_trip_length - dc_trip2_trip_length - hwdp_trip_trip_length - dp_trip1_trip_length)
        dp_trip2_trip_ppf = float(self.dp_trip2_weight_text.get().strip())

        # -------------- AUTO-FILL SECOND STRING OF DRILL-PIPE BASED ON DEPTH ENTERED ----------------
        if dp_trip2_trip_length > 0:
            self.bha_trip_dp_trip2_value.config(text=dp_trip2_trip_length)
            dp_trip2_trip_bw = functions.calculate_boyed_weight(dp_trip2_trip_length, dp_trip2_trip_ppf,
                                                                self.bf)
        else:
            self.bha_trip_dp_trip2_value.config(text=0)
            dp_trip2_trip_bw = 0
        bha_trip_wt = functions.cal_total_wt(dc_trip1_trip_bw, dc_trip2_trip_bw, hwdp_trip_trip_bw)
        MainScreen.tripping_miles_total = functions.calculate_trip_miles(dc_trip1_trip_length,
                                                                         dc_trip2_trip_length,
                                                                         hwdp_trip_trip_length, bha_trip_wt,
                                                                         dp_trip1_trip_length,
                                                                         dp_trip2_trip_length,
                                                                         dp_trip2_trip_bw, dp_trip1_trip_bw,
                                                                         total_depth, self.block_wt)
        if self.radio_state.get() == 1:
            self.tripping_miles_result_value.config(text=f'{MainScreen.tripping_miles_total:.2f}')  # > SEND DATA TO
            # BTM FRAME
            self.get_total_miles()  # ----------ADDING MILES TO TOTAL MILES
        elif self.radio_state.get() == 2:
            MainScreen.tripping_miles_total *= 2
            self.tripping_miles_result_value.config(
                text=f'{MainScreen.tripping_miles_total:.2f}')  # ---> SEND DATA TO BTM FRAME
            self.get_total_miles()  # ----------ADDING MILES TO TOTAL MILES
        else:
            messagebox.showerror(title="Radio Button Unchecked!", message="Please select Single or Round Trip.")

    # -------------------------------------------------------------------------------------------------------
    '''TRIGGERED BY COMPUTE BUTTON. TAKES USER INPUTS FROM WIDGETS & MAKES CALCULATIONS USING FUNCTIONS FROM THE
            CALCULATE_FUNCTIONS FILE.'''

    def casing_miles_data(self):
        self.get_blockwt_mudwt_bf()
        shoe_depth = float(self.depth_csg_text1.get().strip())
        lower_csg_length = float(self.bha_text_lower_csg.get().strip())
        lower_csg_ppf = float(self.lower_csg_weight_text.get().strip())
        lower_csg_bw = functions.calculate_boyed_weight(lower_csg_length, lower_csg_ppf, self.bf)

        mid_csg_length = float(self.bha_text_mid_csg.get().strip())
        mid_csg_ppf = float(self.mid_csg_weight_text.get().strip())
        mid_csg_bw = functions.calculate_boyed_weight(mid_csg_length, mid_csg_ppf, self.bf)

        top_csg_length = shoe_depth - lower_csg_length - mid_csg_length
        top_csg_ppf = float(self.mid_csg_weight_text.get().strip())

        if top_csg_length > 0:
            self.bha_value_top_csg.config(text=f'{top_csg_length}')
            top_csg_bw = functions.calculate_boyed_weight(top_csg_length, top_csg_ppf, self.bf)
        else:
            self.bha_value_top_csg.config(text=f'{0}')
            top_csg_bw = 0

        MainScreen.casing_miles_total = functions.calculate_casing_miles(lower_csg_length, mid_csg_length,
                                                                         top_csg_length, lower_csg_bw,
                                                                         mid_csg_bw, top_csg_bw, shoe_depth,
                                                                         self.block_wt)

        self.casing_miles_result_value.config(text=f'{MainScreen.casing_miles_total:.2f}')  # -> SEND DATA TO BTM FRAME
        self.get_total_miles()  # ---ADDING MILES TO TOTAL MILES

    # -------------------------------------------------------------------------------------------------------
    '''TRIGGERED BY COMPUTE BUTTON. TAKES USER INPUTS FROM WIDGETS & MAKES CALCULATIONS USING FUNCTIONS FROM THE
            CALCULATE_FUNCTIONS FILE.'''

    def jarring_ton_miles_data(self):
        self.get_blockwt_mudwt_bf()
        top_reading = float(self.top_reading_text.get().strip())
        btm_reading = float(self.btm_reading_text.get().strip())
        dist_trav = float(self.distance_text.get().strip())
        strokes_per_hr = float(self.number_text.get().strip())
        hrs_jarring = float(self.hours_text.get().strip())
        weight_tons = ((top_reading + btm_reading) / 2) / 2000
        MainScreen.jarring_miles_total = functions.jarring_miles(dist_trav, weight_tons, strokes_per_hr, hrs_jarring)

        self.jarring_miles_result_value.config(text=f'{MainScreen.jarring_miles_total:.2f}')
        self.get_total_miles()  # ----------ADDING MILES TO TOTAL MILES

    # ___________________________________________________________________________________________________________
    '''TRIGGERED BY COMPUTE BUTTON. TAKES USER INPUTS FROM WIDGETS & MAKES CALCULATIONS USING FUNCTIONS FROM THE
            CALCULATE_FUNCTIONS FILE.'''

    def liner_ton_miles_data(self):
        self.get_blockwt_mudwt_bf()
        shoe_depth = float(self.depth_liner_text1.get().strip())
        liner_length = float(self.liner_length_text.get().strip())
        liner_ppf = float(self.liner_weight_text.get().strip())
        liner_bw = functions.calculate_boyed_weight(liner_length, liner_ppf, self.bf)

        dp_length = shoe_depth - liner_length
        dp_ppf = float(self.dp_weight_text.get().strip())

        if dp_length > 0:
            self.dp_value.config(text=f'{dp_length}')
            dp_bw = functions.calculate_boyed_weight(dp_length, dp_ppf, self.bf)

        else:
            self.dp_value.config(text=f'{0}')
            dp_bw = 0

        MainScreen.liner_miles_total = functions.liner_miles(dp_length, dp_bw, liner_length, liner_bw, shoe_depth,
                                                             self.block_wt)
        self.liner_miles_result_value.config(text=f'{MainScreen.liner_miles_total:.2f}')
        self.get_total_miles()  # ----------ADDING MILES TO TOTAL MILES
    # ----------------------TON MILES TOTAL---------------------------------------


main_screen = MainScreen(window)
window.mainloop()
