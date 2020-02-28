# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:49:44 2020

@author: kanavgulati
"""

import tkinter as tk
#import tkinter.font as font
#from tkinter import simpledialog as sd
#from tkinter import messagebox as mb
#import random
import win32api
import win32net
from tkinter import filedialog


def BrowseJD():
    filename = filedialog.askopenfilename(initialdir =  ".", title = "Select A File", filetype = (("Doc files","*.doc"),("all files","*.*")) )
    JDFilePath.configure(text = filename)

def BrowseCV():
    filename = filedialog.askopenfilename(initialdir =  ".", title = "Select A File", filetype = (("Doc files","*.doc"),("all files","*.*")) )
    CVFilePath.configure(text = filename)
    
def BrowseTracker():
    filename = filedialog.askopenfilename(initialdir =  ".", title = "Select A File", filetype = (("Doc files","*.doc"),("all files","*.*")) )
    TrackerFilePath.configure(text = filename)

def BrowsePanel():
    filename = filedialog.askopenfilename(initialdir =  ".", title = "Select A File", filetype = (("Doc files","*.doc"),("all files","*.*")) )
    PanelFilePath.configure(text = filename)

user_info = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(), win32api.GetUserName(), 2)
full_name = user_info["full_name"]

# Set DPI awareness for Win10 systems
try:
   from ctypes import windll 
   windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root= tk.Tk()
root.geometry('640x480')
root.title('Profile Screening Tool')
root.resizable(False, False)

mainFrame = tk.Frame(root, bg='light gray')
mainFrame.pack(fill="both", expand=True)

status = tk.Label(root, text=" ", relief='sunken', anchor=tk.W, bd=1)
status.pack(side="bottom", fill="x")

appArea = tk.Frame(mainFrame)
appArea.pack(padx=10, pady=(10,0), fill="both", expand=True)

headerFrame = tk.Frame(appArea, bg="blue")
headerFrame.pack(fill="both", expand=True)

headerLabel = tk.Label(headerFrame, text="KPMG Profile Screening Tool")
headerLabel.pack(expand=True)

UserFrame = tk.Frame(appArea, bg="light blue")
UserFrame.pack(fill="both", expand=True)

UserLabel = tk.Label(UserFrame, text="Hello "+full_name)
UserLabel.pack(expand=True)

JDFrame = tk.Frame(appArea, bg="white")
JDFrame.pack(fill="both", expand=True)

JDLabelFrame = tk.Label(JDFrame, text="Select the JD file")
JDLabelFrame.pack(fill="both", expand=True)

JDFilePath = tk.Label(JDFrame, text="File Name")
JDFilePath.pack(side="left", expand=True)

JDButton = tk.Button(JDFrame, text="Browse", command = BrowseJD)
JDButton.pack(side="right", expand=True)

TrackerFrame = tk.Frame(appArea, bg="blue")
TrackerFrame.pack(fill="both", expand=True)

TrackerLabelFrame = tk.Label(TrackerFrame, text="Select the Tracker file")
TrackerLabelFrame.pack(fill="both", expand=True)

TrackerFilePath = tk.Label(TrackerFrame, text="File Name")
TrackerFilePath.pack(side="left", expand=True)

TrackerButton = tk.Button(TrackerFrame, text="Browse", command = BrowseTracker)
TrackerButton.pack(side="right", expand=True)

CVFrame = tk.Frame(appArea, bg="light blue")
CVFrame.pack(fill="both", expand=True)

CVLabelFrame = tk.Label(CVFrame, text="Select the CV location")
CVLabelFrame.pack(fill="both", expand=True)

CVFilePath = tk.Label(CVFrame, text="File Name")
CVFilePath.pack(side="left", expand=True)

CVButton = tk.Button(CVFrame, text="Browse", command = BrowseCV)
CVButton.pack(side="right", expand=True)

PanelFrame = tk.Frame(appArea, bg="white")
PanelFrame.pack(fill="both", expand=True)

PanelLabelFrame = tk.Label(PanelFrame, text="Select the CV location")
PanelLabelFrame.pack(fill="both", expand=True)

PanelFilePath = tk.Label(PanelFrame, text="File Name")
PanelFilePath.pack(side="left", expand=True)

PanelButton = tk.Button(PanelFrame, text="Browse", command = BrowsePanel)
PanelButton.pack(side="right", expand=True)

SubmitFrame = tk.Frame(appArea)
SubmitFrame.pack(fill="both", expand=True)

SubmitButton = tk.Button(SubmitFrame, text="Submit")
SubmitButton.pack(padx=10, pady=10, expand=True)

root.mainloop()
