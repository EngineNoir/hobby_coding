import tkinter
from tkinter import *
from tkinter.tix import *
import subprocess

# Core
PHB = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Players Handbook.pdf"
DMG = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Dungeon Masters Guide.pdf"
HFA = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Home Field Advantage.pdf"
EC = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Epic Characters.pdf"

# Monsters
MM = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Monster Manual.pdf"
VGM = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Volos Guide to Monsters.pdf"
MTF = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Mordenkainens Tome of Foes.pdf"
FTD = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Fizbans Treasury of Dragons.pdf"
MME1 = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Monster Manual Expanded.pdf"
MME2 = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Monster Manual Expanded II.pdf"
MME3 = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Monster Manual Expanded III.pdf"
EEE = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Ezmereldas Encyclopedia of Evil.pdf"
TOB = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Tome of Beasts.pdf"
TOB2 = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Tome of Beasts II.pdf"
BOF = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\The Book of Fiends.pdf"

#Expansions
XGE = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Xanathars Guide to Everything.pdf"
TCOE = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Tashas Cauldron of Everything.pdf"
DW = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Drakewarden.pdf"

#Modules
DIA = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Baldurs Gate - Descent into Avernus.pdf"
TOD = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Tyranny of Dragons.pdf"
ROV = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Rise of Vecna.pdf"

#Locations
SCAG = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Sword Coast Adventurers Guide.pdf"
VRGR = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Van Richtens Guide to Ravenloft.pdf"
MBJV = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Minsc and Boos Journal of Villainy.pdf"
ERLW = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Eberron - Rising from the Last War.pdf"

TLRW = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Thay Land Of The Red Wizards.pdf"
EGW = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Explorers Guide to Wildemount.pdf"
TDR = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\TalDorei Campaign Setting Reborn.pdf"
DH = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Darkhold - Secrets of the Zhentarim.pdf"

RUE = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Rashemen.pdf"
GD = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\The Great Dale.pdf"
TBK = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\The Border Kingdoms.pdf"
DUNW = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Dunwood.pdf"

CAG = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Calimshan Adventurers Guide.pdf"
UGPS = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\UGttP Shadowfell.pdf"
UGPA = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\UGttP Acheron.pdf"
CIP = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Codex of the Infinite Planes.pdf"

DS = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Dark Sun.pdf"
TDCG = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\TalDorei Campaign Setting.pdf"

#Worldbuilding
GOF = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Gods of Faerun.pdf"
EFR = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Ed Greenwood Presents Elminsters Forgotten Realms.pdf"
LLL = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Larlochs Lexicon of Lichdom.pdf"
ADH = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\The Adventurers Domestic Handbook.pdf"
ECC = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Elminsters Candlekeep Companion.pdf"

#Items
AOTG = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Artifacts of the Guild.pdf"
TU = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Treasures of the Underdark.pdf"
AAA = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Asteriks Astounding Atrocities.pdf"

#DMing
TMK = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\The Monsters Know What Theyre Doing.pdf"
LDM = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\The Lazy Dungeon Master.pdf"
RLDM = "C:\\Users\\Dell\\Desktop\\DnD\\File Manager\\Return of the Lazy Dungeon Master.pdf"


class MyWindow:

    def __init__(self, win):

        tip=Balloon(win)

        self.lbl1 = Label(win, text='Core', font=("Helvetica", 15))
        self.lbl1.place(x=25, y=10)

        self.lbl2 = Label(win, text='Monsters', font=("Helvetica", 15))
        self.lbl2.place(x=25, y=70)

        self.lbl3 = Label(win, text='Expansions', font=("Helvetica", 15))
        self.lbl3.place(x=25, y=190)

        self.lbl4 = Label(win, text='Modules', font=("Helvetica", 15))
        self.lbl4.place(x=25, y=250)

        self.lbl5 = Label(win, text='Locations', font=("Helvetica", 15))
        self.lbl5.place(x=25, y=310)

        self.lbl6 = Label(win, text='Worldbuilding', font=("Helvetica", 15))
        self.lbl6.place(x=25, y=490)

        self.lbl7 = Label(win, text='Items', font=("Helvetica", 15))
        self.lbl7.place(x=25, y=580)

        self.lbl8 = Label(win, text='DMing', font=("Helvetica", 15))
        self.lbl8.place(x=25, y=640)

        #Core

        self.c1 = Button(win, text='PHB', font=("Helvetica", 10), command=self.openphb)
        self.c1.place(x=10, y=40)
        self.c1.config(height=1, width=8)
        tip.bind_widget(self.c1, balloonmsg="Player's Handbook")

        self.c2 = Button(win, text='DMG', font=("Helvetica", 10), command=self.opendmg)
        self.c2.place(x=90, y=40)
        self.c2.config(height=1, width=8)
        tip.bind_widget(self.c2, balloonmsg="Dungeon Master's Guide")

        self.c3 = Button(win, text='HFA', font=("Helvetica", 10), command=self.openhfa)
        self.c3.place(x=170, y=40)
        self.c3.config(height=1, width=8)
        tip.bind_widget(self.c3, balloonmsg="Home-Front Advantage (Lair Actions)")

        self.c4 = Button(win, text='EC', font=("Helvetica", 10), command=self.openec)
        self.c4.place(x=250, y=40)
        self.c4.config(height=1, width=8)
        tip.bind_widget(self.c4, balloonmsg="Epic Characters")

        #Monsters

        self.m1 = Button(win, text='MM', font=("Helvetica", 10), command=self.openmm)
        self.m1.place(x=10, y=100)
        self.m1.config(height=1, width=8)
        tip.bind_widget(self.m1, balloonmsg="Monster Manual")

        self.m2 = Button(win, text='VGM', font=("Helvetica", 10), command=self.openvgm)
        self.m2.place(x=90, y=100)
        self.m2.config(height=1, width=8)
        tip.bind_widget(self.m2, balloonmsg="Volo's Guide to Monsters")

        self.m3 = Button(win, text='MTF', font=("Helvetica", 10), command=self.openmtf)
        self.m3.place(x=170, y=100)
        self.m3.config(height=1, width=8)
        tip.bind_widget(self.m3, balloonmsg="Mordenkainen's Tome of Foes")

        self.m4 = Button(win, text='FTD', font=("Helvetica", 10), command=self.openftd)
        self.m4.place(x=250, y=100)
        self.m4.config(height=1, width=8)
        tip.bind_widget(self.m4, balloonmsg="Fizban's Treasury Of Dragons")

        self.m5 = Button(win, text='MME1', font=("Helvetica", 10), command=self.openmme1)
        self.m5.place(x=10, y=130)
        self.m5.config(height=1, width=8)
        tip.bind_widget(self.m5, balloonmsg="Monster Manual Expanded")

        self.m6 = Button(win, text='MME2', font=("Helvetica", 10), command=self.openmme2)
        self.m6.place(x=90, y=130)
        self.m6.config(height=1, width=8)
        tip.bind_widget(self.m6, balloonmsg="Monster Manual Expanded II")

        self.m7 = Button(win, text='MME3', font=("Helvetica", 10), command=self.openmme3)
        self.m7.place(x=170, y=130)
        self.m7.config(height=1, width=8)
        tip.bind_widget(self.m7, balloonmsg="Monster Manual Expanded III")

        self.m8 = Button(win, text='EEE', font=("Helvetica", 10), command=self.openeee)
        self.m8.place(x=250, y=130)
        self.m8.config(height=1, width=8)
        tip.bind_widget(self.m8, balloonmsg="Ezmeralda's Encyclopedia of Evil")

        self.m9 = Button(win, text='TOB', font=("Helvetica", 10), command=self.opentob)
        self.m9.place(x=10, y=160)
        self.m9.config(height=1, width=8)
        tip.bind_widget(self.m9, balloonmsg="Tome of Beasts")

        self.m10 = Button(win, text='TOB2', font=("Helvetica", 10), command=self.opentob2)
        self.m10.place(x=90, y=160)
        self.m10.config(height=1, width=8)
        tip.bind_widget(self.m10, balloonmsg="Tome of Beasts II")

        self.m11 = Button(win, text='BOF', font=("Helvetica", 10), command=self.openbof)
        self.m11.place(x=170, y=160)
        self.m11.config(height=1, width=8)
        tip.bind_widget(self.m11, balloonmsg="Book of Fiends")

        #Expansions

        self.e1 = Button(win, text='XGE', font=("Helvetica", 10), command=self.openxge)
        self.e1.place(x=10, y=220)
        self.e1.config(height=1, width=8)
        tip.bind_widget(self.e1, balloonmsg="Xanathar's Guide to Everything")

        self.e2 = Button(win, text='TCOE', font=("Helvetica", 10), command=self.opentcoe)
        self.e2.place(x=90, y=220)
        self.e2.config(height=1, width=8)
        tip.bind_widget(self.e2, balloonmsg="Tasha's Cauldron of Everything")

        self.e3 = Button(win, text='DW', font=("Helvetica", 10), command=self.opendw)
        self.e3.place(x=170, y=220)
        self.e3.config(height=1, width=8)
        tip.bind_widget(self.e3, balloonmsg="Drakewarden")

        #Modules

        self.md1 = Button(win, text='DIA', font=("Helvetica", 10), command=self.opendia)
        self.md1.place(x=10, y=280)
        self.md1.config(height=1, width=8)
        tip.bind_widget(self.md1, balloonmsg="Baldur's Gate: Descent into Avernus")

        self.md2 = Button(win, text='TOD', font=("Helvetica", 10), command=self.opentod)
        self.md2.place(x=90, y=280)
        self.md2.config(height=1, width=8)
        tip.bind_widget(self.md2, balloonmsg="Tyranny of Dragons")

        self.md3 = Button(win, text='ROV', font=("Helvetica", 10), command=self.openrov)
        self.md3.place(x=170, y=280)
        self.md3.config(height=1, width=8)
        tip.bind_widget(self.md3, balloonmsg="Rise of Vecna")

        #Locations

        self.l1 = Button(win, text='SCAG', font=("Helvetica", 10), command=self.openscag)
        self.l1.place(x=10, y=340)
        self.l1.config(height=1, width=8)
        tip.bind_widget(self.l1, balloonmsg="Sword Coast Adventurer's Guide")

        self.l2 = Button(win, text='VRGR', font=("Helvetica", 10), command=self.openvrgr)
        self.l2.place(x=90, y=340)
        self.l2.config(height=1, width=8)
        tip.bind_widget(self.l2, balloonmsg="Van Richten's Guide to Ravenloft")

        self.l3 = Button(win, text='MBJV', font=("Helvetica", 10), command=self.openmbjv)
        self.l3.place(x=170, y=340)
        self.l3.config(height=1, width=8)
        tip.bind_widget(self.l3, balloonmsg="Minsc and Boo's Journal of Villainy")

        self.l4 = Button(win, text='ERLW', font=("Helvetica", 10), command=self.openerlw)
        self.l4.place(x=250, y=340)
        self.l4.config(height=1, width=8)
        tip.bind_widget(self.l4, balloonmsg="Eberron - Rising from the Last War")

        self.l5 = Button(win, text='TLRW', font=("Helvetica", 10), command=self.opentlrw)
        self.l5.place(x=10, y=370)
        self.l5.config(height=1, width=8)
        tip.bind_widget(self.l5, balloonmsg="Thay - Land of the Red Wizards")

        self.l6 = Button(win, text='EGW', font=("Helvetica", 10), command=self.openegw)
        self.l6.place(x=90, y=370)
        self.l6.config(height=1, width=8)
        tip.bind_widget(self.l6, balloonmsg="Explorer's Guide to Wildemount")

        self.l7 = Button(win, text='TDR', font=("Helvetica", 10), command=self.opentdr)
        self.l7.place(x=170, y=370)
        self.l7.config(height=1, width=8)
        tip.bind_widget(self.l7, balloonmsg="Tal'dorei Reborn")

        self.l8 = Button(win, text='DH', font=("Helvetica", 10), command=self.opendh)
        self.l8.place(x=250, y=370)
        self.l8.config(height=1, width=8)
        tip.bind_widget(self.l8, balloonmsg="Darkhold: Secrets of the Zhentarim")

        self.l9 = Button(win, text='RUE', font=("Helvetica", 10), command=self.openrue)
        self.l9.place(x=10, y=400)
        self.l9.config(height=1, width=8)
        tip.bind_widget(self.l9, balloonmsg="Rashemen: Unapproachable East Campaign Guide")

        self.l10 = Button(win, text='GD', font=("Helvetica", 10), command=self.opengd)
        self.l10.place(x=90, y=400)
        self.l10.config(height=1, width=8)
        tip.bind_widget(self.l10, balloonmsg="The Great Dale")

        self.l11 = Button(win, text='TBK', font=("Helvetica", 10), command=self.opentbk)
        self.l11.place(x=170, y=400)
        self.l11.config(height=1, width=8)
        tip.bind_widget(self.l11, balloonmsg="The Border Kingdoms")

        self.l12 = Button(win, text='DUNW', font=("Helvetica", 10), command=self.opendunw)
        self.l12.place(x=250, y=400)
        self.l12.config(height=1, width=8)
        tip.bind_widget(self.l12, balloonmsg="Dunwood")

        self.l13 = Button(win, text='CAG', font=("Helvetica", 10), command=self.opencag)
        self.l13.place(x=10, y=430)
        self.l13.config(height=1, width=8)
        tip.bind_widget(self.l13, balloonmsg="Calimshan Adventurer's Guide")

        self.l14 = Button(win, text='UGPS', font=("Helvetica", 10), command=self.openugps)
        self.l14.place(x=90, y=430)
        self.l14.config(height=1, width=8)
        tip.bind_widget(self.l14, balloonmsg="Ulraunt's Guide to the Planes: Shadowfell")

        self.l15 = Button(win, text='UGPA', font=("Helvetica", 10), command=self.openugpa)
        self.l15.place(x=170, y=430)
        self.l15.config(height=1, width=8)
        tip.bind_widget(self.l15, balloonmsg="Ulraunt's Guide to the Planes: Acheron")

        self.l16 = Button(win, text='CIP', font=("Helvetica", 10), command=self.opencip)
        self.l16.place(x=250, y=430)
        self.l16.config(height=1, width=8)
        tip.bind_widget(self.l16, balloonmsg="Codex of the Infinite Planes")

        self.l17 = Button(win, text='DS', font=("Helvetica", 10), command=self.opends)
        self.l17.place(x=10, y=460)
        self.l17.config(height=1, width=8)
        tip.bind_widget(self.l17, balloonmsg="Dark Sun")

        self.l17 = Button(win, text='TDCG', font=("Helvetica", 10), command=self.opentdcg)
        self.l17.place(x=90, y=460)
        self.l17.config(height=1, width=8)
        tip.bind_widget(self.l17, balloonmsg="Tal'Dorei Campaign Guide")

        #Worldbuilding

        self.w1 = Button(win, text='GOF', font=("Helvetica", 10), command=self.opengof)
        self.w1.place(x=10, y=520)
        self.w1.config(height=1, width=8)
        tip.bind_widget(self.w1, balloonmsg="Gods of Faerun")

        self.w2 = Button(win, text='EFR', font=("Helvetica", 10), command=self.openefr)
        self.w2.place(x=90, y=520)
        self.w2.config(height=1, width=8)
        tip.bind_widget(self.w2, balloonmsg="Elminster's Forgotten Realms")

        self.w3 = Button(win, text='LLL', font=("Helvetica", 10), command=self.openlll)
        self.w3.place(x=170, y=520)
        self.w3.config(height=1, width=8)
        tip.bind_widget(self.w3, balloonmsg="Larloch's Lexicon of Lichdom")

        self.w4 = Button(win, text='ADH', font=("Helvetica", 10), command=self.openadh)
        self.w4.place(x=250, y=520)
        self.w4.config(height=1, width=8)
        tip.bind_widget(self.w4, balloonmsg="The Adventurer's Domestic Handbook")

        self.w5 = Button(win, text='ECC', font=("Helvetica", 10), command=self.openecc)
        self.w5.place(x=10, y=550)
        self.w5.config(height=1, width=8)
        tip.bind_widget(self.w5, balloonmsg="Elminster's Candlekeep Companion")

        #Items

        self.i1 = Button(win, text='AOTG', font=("Helvetica", 10), command=self.openaotg)
        self.i1.place(x=10, y=610)
        self.i1.config(height=1, width=8)
        tip.bind_widget(self.i1, balloonmsg="Artifacts of the Guild")

        self.i2 = Button(win, text='TU', font=("Helvetica", 10), command=self.opentu)
        self.i2.place(x=90, y=610)
        self.i2.config(height=1, width=8)
        tip.bind_widget(self.i2, balloonmsg="Treasures of the Underdark")

        self.i3 = Button(win, text='AAA', font=("Helvetica", 10), command=self.openaaa)
        self.i3.place(x=170, y=610)
        self.i3.config(height=1, width=8)
        tip.bind_widget(self.i3, balloonmsg="Asteriks' Astounding Artifacts")

        #DMing

        self.d1 = Button(win, text='TMK', font=("Helvetica", 10), command=self.opentmk)
        self.d1.place(x=10, y=670)
        self.d1.config(height=1, width=8)
        tip.bind_widget(self.d1, balloonmsg="The Monsters Know")

        self.d2 = Button(win, text='LDM', font=("Helvetica", 10), command=self.openldm)
        self.d2.place(x=90, y=670)
        self.d2.config(height=1, width=8)
        tip.bind_widget(self.d2, balloonmsg="The Lazy Dungeon Master")

        self.d3 = Button(win, text='RLDM', font=("Helvetica", 10), command=self.openrldm)
        self.d3.place(x=170, y=670)
        self.d3.config(height=1, width=8)
        tip.bind_widget(self.d3, balloonmsg="Return of the Lazy Dungeon Master")

    #Open Functions
    #Core
    def openphb(self):
        subprocess.Popen([PHB], shell=True)

    def opendmg(self):
        subprocess.Popen([DMG], shell=True)

    def openhfa(self):
        subprocess.Popen([HFA], shell=True)

    def openec(self):
        subprocess.Popen([EC], shell=True)

    #Monsters

    def openmm(self):
        subprocess.Popen([MM], shell=True)

    def openvgm(self):
        subprocess.Popen([VGM], shell=True)

    def openmtf(self):
        subprocess.Popen([MTF], shell=True)

    def openftd(self):
        subprocess.Popen([FTD], shell=True)

    def openmme1(self):
        subprocess.Popen([MME1], shell=True)

    def openmme2(self):
        subprocess.Popen([MME2], shell=True)

    def openmme3(self):
        subprocess.Popen([MME3], shell=True)

    def openeee(self):
        subprocess.Popen([EEE], shell=True)

    def opentob(self):
        subprocess.Popen([TOB], shell=True)

    def opentob2(self):
        subprocess.Popen([TOB2], shell=True)

    def openbof(self):
        subprocess.Popen([BOF], shell=True)

    #Expansions

    def openxge(self):
        subprocess.Popen([XGE], shell=True)

    def opentcoe(self):
        subprocess.Popen([TCOE], shell=True)

    def opendw(self):
        subprocess.Popen([DW], shell=True)

    #Modules

    def opendia(self):
        subprocess.Popen([DIA], shell=True)

    def opentod(self):
        subprocess.Popen([TOD], shell=True)

    def openrov(self):
        subprocess.Popen([ROV], shell=True)

    #Locations

    def openscag(self):
        subprocess.Popen([SCAG], shell=True)

    def openvrgr(self):
        subprocess.Popen([VRGR], shell=True)

    def openmbjv(self):
        subprocess.Popen([MBJV], shell=True)

    def openerlw(self):
        subprocess.Popen([ERLW], shell=True)

    def opentlrw(self):
        subprocess.Popen([TLRW], shell=True)

    def openegw(self):
        subprocess.Popen([EGW], shell=True)

    def opentdr(self):
        subprocess.Popen([TDR], shell=True)

    def opendh(self):
        subprocess.Popen([DH], shell=True)

    def openrue(self):
        subprocess.Popen([RUE], shell=True)

    def opengd(self):
        subprocess.Popen([GD], shell=True)

    def opentbk(self):
        subprocess.Popen([TBK], shell=True)

    def opendunw(self):
        subprocess.Popen([DUNW], shell=True)

    def opencag(self):
        subprocess.Popen([CAG], shell=True)

    def openugps(self):
        subprocess.Popen([UGPS], shell=True)

    def openugpa(self):
        subprocess.Popen([UGPA], shell=True)

    def opencip(self):
        subprocess.Popen([CIP], shell=True)

    def opends(self):
        subprocess.Popen([DS], shell=True)

    def opentdcg(self):
        subprocess.Popen([TDCG], shell=True)

    #Worldbuilding

    def opengof(self):
        subprocess.Popen([GOF], shell=True)

    def openefr(self):
        subprocess.Popen([EFR], shell=True)

    def openlll(self):
        subprocess.Popen([LLL], shell=True)

    def openadh(self):
        subprocess.Popen([ADH], shell=True)

    def openecc(self):
        subprocess.Popen([ECC], shell=True)

    #Items

    def openaotg(self):
        subprocess.Popen([AOTG], shell=True)

    def opentu(self):
        subprocess.Popen([TU], shell=True)

    def openaaa(self):
        subprocess.Popen([AAA], shell=True)

    #DMing

    def opentmk(self):
        subprocess.Popen([TMK], shell=True)

    def openldm(self):
        subprocess.Popen([LDM], shell=True)

    def openrldm(self):
        subprocess.Popen([RLDM], shell=True)

window = Tk()
mywin = MyWindow(window)
window.title('DnD File Manager')
window.geometry("335x710+10+10") # last_x + 85, last_y + 40
window.mainloop()
