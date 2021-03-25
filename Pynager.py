import tkinter as tk
import psutil
import platform
import os
import time
import tabulate
import getpass
stat_width = 23
def tim3():
    timeString = time.ctime()
    l3.config(text=timeString)
class Colormode:
    def __init__(self,fgc,bgc):
        self.fgc = fgc
        self.bgc = bgc
    def cm_activate(self):
        tim3()
        wn.config(bg=self.bgc)
        l1.configure(fg=self.fgc,bg=self.bgc)
        l3.configure(fg=self.fgc,bg=self.bgc)
        disk_display.config(bg=self.bgc,fg=self.fgc)
        sys_display.config(bg=self.bgc,fg=self.fgc)
        battery_display.config(bg=self.bgc,fg=self.fgc)
        battery_disk.config(bg=self.bgc)
        power_menu.config(bg=self.bgc)
        perf.config(bg=self.bgc)
        bu1.config(bg=self.bgc,fg=self.fgc)
        bu2.config(bg=self.bgc,fg=self.fgc)
        bu3.config(bg=self.bgc,fg=self.fgc)
        cpu_display.config(fg=self.fgc,bg=self.bgc)
        ram_display.config(fg=self.fgc,bg=self.bgc)
        cpu_ram.config(bg=self.bgc)
        dm_lm.config(bg=self.bgc)
        tim3()
bgh = 'teal'
tl1 = []
timeString = time.ctime()
cm1 = Colormode('white', 'black')
cm2 = Colormode('black', 'yellow')
cm3 = Colormode('black', 'purple')
cm4 = Colormode('black', 'red')
cm5 = Colormode('black', 'green')
cm6 = Colormode('black','white')
cm7 = Colormode('black','cornflower blue')
cm8 = Colormode('black', 'lawn green')
cm9 = Colormode('black', 'tomato')
cm10 = Colormode('black', 'orange')
cm11 = Colormode('black', 'blue')
cm12 = Colormode('black', 'gold')
cm13 = Colormode('black', 'gray')
cm14 = Colormode('black', 'hot pink')
cm15 = Colormode('black', 'medium violet red')
cm16 = Colormode('black', 'deep sky blue')
cm17 = Colormode('black', 'lime green')
cm18 = Colormode('black', 'gray24')
cm19 = Colormode('black', 'goldenrod')
cm20 = Colormode('black', 'dark goldenrod')
cm21 = Colormode('black', 'lightsalmon4')
cm22 = Colormode('black', 'salmon4')
cm23 = Colormode('black', 'saddle brown')
cm24 = Colormode('black', 'yellow green')
cm25 = Colormode('black', 'royalblue3')
def b1_click():
    tim3()
    l3.configure(text=timeString)
    os.system("shutdown /s /t 1")
def b2_click():
    tim3()
    os.system("shutdown /r /t 1")
def b3_click():
    tim3()
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
# GUI
cpu_family = platform.processor()
wn = tk.Tk()
wn.title("PyNager--Windows Edition")
wn.config()
header4 = tk.Label(wn,bg=bgh,fg='black',text='🕐🕑----TIME----🕑🕐')
header4.pack()
l3 = tk.Label(wn,fg='black',text=timeString)
l3.pack()
tim3()
header3 = tk.Label(wn,bg=bgh,fg='black',text='🖥💻----SYSTEM PERFORMENCE & INFO----💻🖥')
header3.pack()
l1 = tk.Label(wn,fg='black',text=cpu_family)
l1.pack()
tim3()
perf = tk.Frame(wn)
perf.pack()
cpu_ram = tk.Frame(perf)
cpu_ram.pack(side='top')
cpu_display = tk.Label(cpu_ram,width = stat_width)
cpu_display.pack(side='left')
tim3()
ram_display = tk.Label(cpu_ram,width = stat_width)
ram_display.pack(side='right')
tim3()
battery_disk = tk.Frame(perf)
battery_disk.pack(side='top')
tim3()
disk_display = tk.Label(battery_disk,width = stat_width)
disk_display.pack(side='left')
sys_display = tk.Label(battery_disk,width = stat_width)
sys_display.pack(side='right')
battery_display = tk.Label(battery_disk,width = stat_width)
battery_display.pack(side='right')
header1 = tk.Label(wn,bg=bgh,fg='black',text='✨----BACKGROUND CUSTOMIZATION----✨')
header1.pack()
dm_lm = tk.Frame(wn,bg='white')
dm_lm.pack()
dm = tk.Button(dm_lm,bg='black',fg='white',width=2,height=1,command=cm1.cm_activate)
dm.pack(side='right')
lgm = tk.Button(dm_lm,bg='gray24',fg='black',width=2,height=1,command=cm18.cm_activate)
lgm.pack(side='right')
gm = tk.Button(dm_lm,bg='gray',fg='black',width=2,height=1,command=cm13.cm_activate)
gm.pack(side='right')
pm = tk.Button(dm_lm,fg='black',bg='saddlebrown',width=2,height=1,command=cm23.cm_activate)
pm.pack(side='right')
pm = tk.Button(dm_lm,fg='black',bg='salmon4',width=2,height=1,command=cm22.cm_activate)
pm.pack(side='right')
pm = tk.Button(dm_lm,fg='black',bg='lightsalmon4',width=2,height=1,command=cm21.cm_activate)
pm.pack(side='right')
pm = tk.Button(dm_lm,fg='black',bg='purple',width=2,height=1,command=cm3.cm_activate)
pm.pack(side='right')
lpm2 = tk.Button(dm_lm,fg='black',bg='medium violet red',width=2,height=1,command=cm15.cm_activate)
lpm2.pack(side='right')
lpm1 = tk.Button(dm_lm,fg='black',bg='hot pink',width=2,height=1,command=cm14.cm_activate)
lpm1.pack(side='right')
bm = tk.Button(dm_lm,fg='black',bg='blue',width=2,height=1,command=cm11.cm_activate)
bm.pack(side='right')
lbm2 = tk.Button(dm_lm,fg='black',bg='royalblue3',width=2,height=1,command=cm25.cm_activate)
lbm2.pack(side='right')
lbm = tk.Button(dm_lm,fg='black',bg='cornflower blue',width=2,height=1,command=cm7.cm_activate)
lbm.pack(side='right')
lbm1 = tk.Button(dm_lm,fg='black',bg='deep sky blue',width=2,height=1,command=cm16.cm_activate)
lbm1.pack(side='right')
gm = tk.Button(dm_lm,fg='black',bg='green',width=2,height=1,command=cm5.cm_activate)
gm.pack(side='right')
lgm1 = tk.Button(dm_lm,fg='black',bg='lime green',width=2,height=1,command=cm17.cm_activate)
lgm1.pack(side='right')
lgm = tk.Button(dm_lm,fg='black',bg='lawn green',width=2,height=1,command=cm8.cm_activate)
lgm.pack(side='right')
lgm2 = tk.Button(dm_lm,fg='black',bg='yellow green',width=2,height=1,command=cm24.cm_activate)
lgm2.pack(side='right')
rm = tk.Button(dm_lm,fg='black',bg='red',width=2,height=1,command=cm4.cm_activate)
rm.pack(side='right')
om = tk.Button(dm_lm,bg='orange',fg='black',width=2,height=1,command=cm10.cm_activate)
om.pack(side='right')
tm = tk.Button(dm_lm,bg='tomato',fg='black',width=2,height=1,command=cm9.cm_activate)
tm.pack(side='right')
pm = tk.Button(dm_lm,bg='dark goldenrod',fg='black',width=2,height=1,command=cm20.cm_activate)
pm.pack(side='right')
pm = tk.Button(dm_lm,bg='goldenrod',fg='black',width=2,height=1,command=cm19.cm_activate)
pm.pack(side='right')
pm = tk.Button(dm_lm,bg='gold',fg='black',width=2,height=1,command=cm12.cm_activate)
pm.pack(side='right')
lpm = tk.Button(dm_lm,bg='yellow',fg='black',width=2,height=1,command=cm2.cm_activate)
lpm.pack(side='right')
lm = tk.Button(dm_lm,bg='white',fg='black',width=2,height=1,command=cm6.cm_activate)
lm.pack(side='right')
header2 = tk.Label(wn,bg=bgh,fg='black',text='🔄----POWER MENU----🔄')
header2.pack()
power_menu = tk.Frame(wn)
power_menu.pack()
bu2 = tk.Button(power_menu,width=23,bg='white',fg='black',text='RESTART',command=b2_click)
bu2.pack(side='right')
bu1 = tk.Button(power_menu,width=23,bg='white',fg='black',text='SHUTDOWN',command=b1_click)
bu1.pack(side='right')
bu3 = tk.Button(power_menu,width=23,bg='white',fg='black',text='SLEEP',command=b3_click)
bu3.pack(side='right')
while True:
    tim3()
    #CPU
    cpu_num = str(psutil.cpu_count())
    cpu_num_1 = "Cores:- " + cpu_num
    cpu_usage_percent = psutil.cpu_percent(1)
    cpu_usage_dialog = str(cpu_usage_percent) + "%"
    tim3()
    cpu_frequency = str(psutil.cpu_freq())
    cpu_freq_3 = cpu_frequency.split()
    cpu_freq_d = cpu_freq_3[0]
    posf1 = cpu_freq_d.find("=")
    posf2 = cpu_freq_d.find(",")
    cpu_freq_4 = cpu_freq_d[(posf1 + 1):(posf2)]
    cpu_freq_1 = str(float(cpu_freq_4) / 1000)
    tim3()
    # MEMORY
    mem_1_5 = str((psutil.virtual_memory().total)/1000000000)[:1]
    tim3()
    mem_2_5 = str((psutil.virtual_memory().used)/1000000000)[:4]
    tim3()
    mem_3_5 = psutil.virtual_memory().percent
    mem_dialog = "RAM:-\nTotal:-" + mem_1_5+" GB\nUsed:-" + str(mem_2_5) + " GB\nPercent:-" + str(mem_3_5) + " %"
    cpu_dialog = "CPU @ "+cpu_freq_1+" GHz :-\n" + cpu_num_1 + "\nUsage Percentage:-" + cpu_usage_dialog + "\n"
    tim3()
    # Disk Usage(total and left disk space)
    path = "C:\\"
    stat = psutil.disk_usage(path)
    list1 = str(stat).split(',')
    tim3()
    x = list1[0]
    total = float(x[(x.find("=")+1):]) / 1000000000
    pos_d1 = str(total).find(".")
    total1 = str(total)[:pos_d1]
    Total= "Disk Space in C drive:-\nTotal: "+str(total1)+" GB"
    tim3()
    z = list1[1]
    usage = float(z[(z.find("=")+1):]) / 1000000000
    pos_d2 = str(usage).find(".")
    usage1 = str(usage)[:pos_d2]
    used="\nUsed: "+str(usage1)+" GB"
    tim3()
    y = list1[2]
    free = float(y[(y.find("=")+1):]) / 1000000000
    pos_d3 = str(free).find(".")
    free1 = str(free)[:pos_d3]
    Free="\nFree: "+str(free1)+" GB\n"
    disk_usage_dialog = Total+used+Free
    tim3()
    # Battery
    battery = str(psutil.sensors_battery()).split()
    b1 = str(battery[0]).find("=")
    b2 = str(battery[0]).find(",")
    b3 = str(battery[0])[b1 + 1:b2]
    bb1 = "Battery Left: "+b3+"%"
    tim3()
    b10 = len(battery)-1
    b4 = str(battery[b10]).find("=")
    b5 = str(battery[b10]).find(")")
    b6 = str(battery[b10])[b4 + 1:b5]
    bb2 = "Is Charging?: "+b6+"\n"
    tim3()
    b_dialog = "Battery:-\n" + bb1 + "\n" + bb2
    ds = str(psutil.disk_io_counters()).split()
    tim3()
    cpu_display.configure(text=cpu_dialog)
    ram_display.configure(text=mem_dialog)
    tl1.clear()
    tim3()
    disk_display.configure(text=disk_usage_dialog)
    battery_display.configure(text=b_dialog)
    tim3()
    # Sys Info
    sys2 = platform.machine()
    sys1 = str(platform.win32_ver()).split()
    sys1.pop(1)
    sys1.pop(2)
    sys1.pop(1)
    sys1.pop(1)
    sys3 = str(sys1[0]).replace("('","").replace("',","")
    sys4 = getpass.getuser()
    sys_d = "CPU Architecture:-" + sys2 + "\nWindows Version:-" + sys3 + "\nCurrent User:-" + sys4
    sys_d1 = "System Details:-\n"+sys_d+"\n"
    sys_display.config(text=sys_d1)
    tim3()
    wn.update()