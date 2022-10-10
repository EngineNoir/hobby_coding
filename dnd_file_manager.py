from tkinter import *
from tkinter.tix import *
import subprocess

#Core
PHB = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Core\\Player's Handbook [10th Print].pdf"
DMG = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Core\\Dungeon Master's Guide.pdf"
HFA = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Home_Field_Advantage_A_Compendium_of_Lair_Actions.pdf"
EC = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\819008-Epic_Characters_v3.1_pages.pdf"

#Items

AOTG = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Items and Gear\\663371-Artifacts_of_the_Guild_FINALv3.pdf"
TOTU = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Items and Gear\\1313476-Treasures_of_the_Underdark_v1.0.pdf"
AAA = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Items and Gear\\1315435-AnnesFlashBack_-_Asteriks_Astounding_Atrocities_50_New_Magic_Items.pdf"

#Monsters
MM = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Core\\Monster Manual [11th Print].pdf"
VGM = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\Volo's Guide to Monsters.pdf"
MTF = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\Mordenkainen's Tome of Foes Deluxe.pdf"
MME1 = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\1138250-Monster_Manual_Expanded_1.0_PDF_v1.19.pdf"
MME2 = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\1138250-Monster_Manual_Expanded_II_v1.13.pdf"
MME3 = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\1138250-Monster_Manual_Expanded_III_v1.06.pdf"
FTD = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\Fizbans Treasury of Dragons (Dungeon  Dragons Book) by Wizards RPG Team (z-lib.org).pdf"
EEE = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\Ezmereldas Encyclopedia of Evil by Alex Clippinger, Oliver Clegg, R P Davis, Anne Gregersen, Jen Vaughn, Christopher Walz (z-lib.org).pdf"
TOB = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\Tome of beasts by Dan Dillon, Chris Harris, Rodrigo Garcia Carmona, and Wolfgang Baur (z-lib.org).pdf"
TOB2 = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Monsters\\Tome of Beasts - 2 by Baur, Introcaso, Larwood, Pawlik, and welham (z-lib.org).pdf"
BOF = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\GRR3604e_TheBookofFiends5E_v1.2.pdf"

#Expansions
XGE = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Everything Expansions\\Xanathar's Guide to Everything.pdf"
TCOE = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Everything Expansions\\Tasha’s Cauldron of Everything " \
       "(HQ, Both Covers).pdf"
DW = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Drakewarden.pdf"

#Modules
DIA = "C:\\Users\\Dell\\Desktop\\DnD\\Modules\\Baldur's Gate - Descent into Avernus.pdf"
TOD = "C:\\Users\\Dell\\Desktop\\DnD\\Modules\\Tyranny of Dragons.pdf"
ROV = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\819008-RiseOfVecnaDFRv2.pdf"

#Locations
SCAG = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Setting Guides\\Sword Coast Adventurer's Guide.pdf"
VRGR = ""
MBJV = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Minsc_and_Boos_Journal_of_Villainy.pdf"
ERTW = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Setting Guides\\Eberron -Rising from the Last War.pdf"

TLRW = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Thay_Land_Of_The_Red_Wizards.pdf"
EGW = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Setting Guides\\Explorer's Guide to Wildemount.pdf"
TDR = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Setting Guides\\TalDorei Campaign Setting Reborn by Matthew Mercer, " \
      "Joey Haeck, Hannah Rose (z-lib.org).pdf"
DH = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Darkhold_-_Secrets_of_the_Zhentarim.pdf"

RUE = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Rashemen\\285327-Rashemen-PF-20210914-highres.pdf"
GD = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\GreatDale.pdf"
TBK = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\The_Border_Kingdoms.pdf"
DUNW = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\285327-Dunwood_Layout_Letter_20201026-high_res.pdf"

CAG = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Calimshan_Adventurers_Guide.pdf"
UGPS = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\819008-UGttP_Shadowfell_v3.0_pages.pdf"
UGPA = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\819008-UGttP_Acheron_v1.0_pages.pdf"
CIP = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Codex_of_the_Infinite_Planes.pdf"

DS = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\DDDS_DarkSun_V.pdf"
TDCG = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\Setting Guides\\TalDorei Campaign Setting.pdf"

#Worldbuilding
GOF = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Gods_of_Faerun.pdf"
EFR = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\Ed_Greenwood_Presents_Elminster's_Forgotten_Realms.pdf"
LLL = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\193137-Larlochs_Lexicon_of_Lichdom_v.1.1.pdf"
ADH = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\The_Adventurer's_Domestic_Handbook.pdf"
ECC = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMGuild\\728848-Elminsters_Candlekeep_Companion.pdf"

#DMing
TMK = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMing\\The Monsters Know What They’re Doing by QL Games, Keith Ammann (z-lib.org).pdf"
LDM = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMing\\The Lazy Dungeon Master by Michael E Shea (z-lib.org).pdf"
RLDM = "C:\\Users\\Dell\\Desktop\\DnD\\Core 5e\\DMing\\Return of the Lazy Dungeon Master.pdf"


class MyWindow:



    def __init__(self, win):

        tip=Balloon(win)

        #Labels x=25, y=y_top_row-30

        self.lbl1 = Label(win, text='Core', font=("Helvetica", 15))
        self.lbl1.place(x=25, y=10)

        self.lbl2 = Label(win, text='Monsters', font=("Helvetica", 15))
        self.lbl2.place(x=25, y=70)

        self.lbl3 = Label(win, text='Expansions', font=("Helvetica", 15))
        self.lbl3.place(x=25, y=160)

        self.lbl4 = Label(win, text='Modules', font=("Helvetica", 15))
        self.lbl4.place(x=25, y=220)

        self.lbl5 = Label(win, text='DM Guild/Extra', font=("Helvetica", 15))
        self.lbl5.place(x=25, y=280)

        #Buttons x=10, 90, 170, 250; y=y_last_book + 60

        self.b1 = Button(win, text='PHB', font=("Helvetica", 10), command=self.openphb)
        self.b1.place(x=10, y=40)
        self.b1.config(height=1, width=8)
        tip.bind_widget(self.b1,balloonmsg="Player's Handbook")

        self.b2 = Button(win, text='DMG', font=("Helvetica", 10), command=self.opendmg)
        self.b2.place(x=90, y=40)
        self.b2.config(height=1, width=8)
        tip.bind_widget(self.b2, balloonmsg="Dungeon Master's Guide")

        self.b3 = Button(win, text='MM', font=("Helvetica", 10), command=self.openmm)
        self.b3.place(x=10, y=100)
        self.b3.config(height=1, width=8)
        tip.bind_widget(self.b3, balloonmsg="Monster Manual")

        self.b4 = Button(win, text='XGE', font=("Helvetica", 10), command=self.openxge)
        self.b4.place(x=10, y=190)
        self.b4.config(height=1, width=8)
        tip.bind_widget(self.b4, balloonmsg="Xanathar's Guide to Everything")

        self.b5 = Button(win, text='TCOE', font=("Helvetica", 10), command=self.opentcoe)
        self.b5.place(x=90, y=190)
        self.b5.config(height=1, width=8)
        tip.bind_widget(self.b5, balloonmsg="Tasha's Cauldron of Everything")

        self.b6 = Button(win, text='VGM', font=("Helvetica", 10), command=self.openvgm)
        self.b6.place(x=170, y=100)
        self.b6.config(height=1, width=8)
        tip.bind_widget(self.b6, balloonmsg="Volo's Guide to Monsters")

        self.b7 = Button(win, text='MTF', font=("Helvetica", 10), command=self.openmtf)
        self.b7.place(x=90, y=100)
        self.b7.config(height=1, width=8)
        tip.bind_widget(self.b7, balloonmsg="Mordenkainen's Tome of Foes")

        self.b8 = Button(win, text='SCAG', font=("Helvetica", 10), command=self.openscag)
        self.b8.place(x=170, y=40)
        self.b8.config(height=1, width=8)
        tip.bind_widget(self.b8, balloonmsg="Sword Coast Adventurer's Guide")

        self.b9 = Button(win, text='MBJV', font=("Helvetica", 10), command=self.openmbjv)
        self.b9.place(x=90, y=250)
        self.b9.config(height=1, width=8)
        tip.bind_widget(self.b9, balloonmsg="Minsc and Boo's Journal of Villainy")

        self.b10 = Button(win, text='MME1', font=("Helvetica", 10), command=self.openmme1)
        self.b10.place(x=10, y=130)
        self.b10.config(height=1, width=8)
        tip.bind_widget(self.b10, balloonmsg="Monster Manual Expanded")

        self.b11 = Button(win, text='MME2', font=("Helvetica", 10), command=self.openmme2)
        self.b11.place(x=90, y=130)
        self.b11.config(height=1, width=8)
        tip.bind_widget(self.b11, balloonmsg="Monster Manual Expanded II")

        self.b12 = Button(win, text='MME3', font=("Helvetica", 10), command=self.openmme3)
        self.b12.place(x=170, y=130)
        self.b12.config(height=1, width=8)
        tip.bind_widget(self.b12, balloonmsg="Monster Manual Expanded III")

        self.b13 = Button(win, text='DIA', font=("Helvetica", 10), command=self.opendia)
        self.b13.place(x=10, y=250)
        self.b13.config(height=1, width=8)
        tip.bind_widget(self.b13, balloonmsg="Baldur's Gate: Descent into Avernus")

        self.b14 = Button(win, text='TOD', font=("Helvetica", 10), command=self.opentod)
        self.b14.place(x=170, y=250)
        self.b14.config(height=1, width=8)
        tip.bind_widget(self.b14, balloonmsg="Tyranny of Dragons")

        self.b15 = Button(win, text='DW', font=("Helvetica", 10), command=self.opendw)
        self.b15.place(x=10, y=310)
        self.b15.config(height=1, width=8)
        tip.bind_widget(self.b15, balloonmsg="Drakewarden")

        self.b16 = Button(win, text='GOF', font=("Helvetica", 10), command=self.opengof)
        self.b16.place(x=90, y=310)
        self.b16.config(height=1, width=8)
        tip.bind_widget(self.b16, balloonmsg="Gods of Faerun")

        self.b17 = Button(win, text='ADH', font=("Helvetica", 10), command=self.openadh)
        self.b17.place(x=170, y=310)
        self.b17.config(height=1, width=8)
        tip.bind_widget(self.b17, balloonmsg="The Adventurer's Domestic Handbook")

        self.b18 = Button(win, text='RUE', font=("Helvetica", 10), command=self.openrue)
        self.b18.place(x=10, y=340)
        self.b18.config(height=1, width=8)
        tip.bind_widget(self.b18, balloonmsg="Rashemen: Unapproachable East Campaign Guide")

        self.b19 = Button(win, text='CAG', font=("Helvetica", 10), command=self.opencag)
        self.b19.place(x=90, y=340)
        self.b19.config(height=1, width=8)
        tip.bind_widget(self.b19, balloonmsg="Calimshan Adventurer's Guide")

        self.b20 = Button(win, text='TBK', font=("Helvetica", 10), command=self.opentbk)
        self.b20.place(x=170, y=340)
        self.b20.config(height=1, width=8)
        tip.bind_widget(self.b20, balloonmsg="The Border Kingdoms")

        self.b21 = Button(win, text='DH', font=("Helvetica", 10), command=self.opendh)
        self.b21.place(x=10, y=370)
        self.b21.config(height=1, width=8)
        tip.bind_widget(self.b21, balloonmsg="Darkhold: Secrets of the Zhentarim")

        self.b22 = Button(win, text='ECC', font=("Helvetica", 10), command=self.openecc)
        self.b22.place(x=90, y=370)
        self.b22.config(height=1, width=8)
        tip.bind_widget(self.b22, balloonmsg="Elminster's Candlekeep Companion")

        self.b23 = Button(win, text='LLL', font=("Helvetica", 10), command=self.openlll)
        self.b23.place(x=170, y=370)
        self.b23.config(height=1, width=8)
        tip.bind_widget(self.b23, balloonmsg="Larloch's Lexicon of Lichdom")

        self.b24 = Button(win, text='CIP', font=("Helvetica", 10), command=self.opencip)
        self.b24.place(x=10, y=400)
        self.b24.config(height=1, width=8)
        tip.bind_widget(self.b24, balloonmsg="Codex of the Infinite Planes")

        self.b25 = Button(win, text='UGPS', font=("Helvetica", 10), command=self.openugps)
        self.b25.place(x=90, y=400)
        self.b25.config(height=1, width=8)
        tip.bind_widget(self.b25, balloonmsg="Ulraunt's Guide to the Planes: Shadowfell")

        self.b26 = Button(win, text='UGPA', font=("Helvetica", 10), command=self.openugpa)
        self.b26.place(x=170, y=400)
        self.b26.config(height=1, width=8)
        tip.bind_widget(self.b26, balloonmsg="Ulraunt's Guide to the Planes: Acheron")

    def openphb(self):
        subprocess.Popen([PHB], shell=True)

    def opendmg(self):
        subprocess.Popen([DMG], shell=True)

    def openscag(self):
        subprocess.Popen([SCAG], shell=True)

    def openmm(self):
        subprocess.Popen([MM], shell=True)

    def openxge(self):
        subprocess.Popen([XGE], shell=True)

    def opentcoe(self):
        subprocess.Popen([TCOE], shell=True)

    def openvgm(self):
        subprocess.Popen([VGM], shell=True)

    def openmtf(self):
        subprocess.Popen([MTF], shell=True)

    def openmbjv(self):
        subprocess.Popen([MBJV], shell=True)

    def openmme1(self):
        subprocess.Popen([MME1], shell=True)

    def openmme2(self):
        subprocess.Popen([MME2], shell=True)

    def openmme3(self):
        subprocess.Popen([MME3], shell=True)

    def opendia(self):
        subprocess.Popen([DIA], shell=True)

    def opentod(self):
        subprocess.Popen([TOD], shell=True)

    def opendw(self):
        subprocess.Popen([DW], shell=True)

    def opendh(self):
        subprocess.Popen([DH], shell=True)

    def openugps(self):
        subprocess.Popen([UGPS], shell=True)

    def openrue(self):
        subprocess.Popen([RUE], shell=True)
        subprocess.Popen([GD], shell=True)

    def opencag(self):
        subprocess.Popen([CAG], shell=True)

    def opentbk(self):
        subprocess.Popen([TBK], shell=True)

    def opengof(self):
        subprocess.Popen([GOF], shell=True)

    def openlll(self):
        subprocess.Popen([LLL], shell=True)

    def openadh(self):
        subprocess.Popen([ADH], shell=True)

    def openugpa(self):
        subprocess.Popen([UGPA], shell=True)

    def opencip(self):
        subprocess.Popen([CIP], shell=True)

    def openecc(self):
        subprocess.Popen([ECC], shell=True)


window = Tk()
mywin = MyWindow(window)
window.title('DnD File Manager')
window.geometry("255x440+10+10") # last_x + 85, last_y + 40
window.mainloop()
