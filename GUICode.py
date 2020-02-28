# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:49:44 2020

@author: kanavgulati
"""

import tkinter as tk
from tkinter import filedialog
# from tkinter import simpledialog as sd
# from tkinter import messagebox as mb
# import random
import win32api
import win32net


def BrowseJD():
    filename = filedialog.askopenfilename(initialdir=".", title="Select A File",
                                          filetype=(("Doc files", "*.doc"), ("all files", "*.*")))
    JDFilePath.configure(text=filename)


def BrowseCV():
    filename = filedialog.askopenfilename(initialdir=".", title="Select A File",
                                          filetype=(("Doc files", "*.doc"), ("all files", "*.*")))
    CVFilePath.configure(text=filename)


def BrowseTracker():
    filename = filedialog.askopenfilename(initialdir=".", title="Select A File",
                                          filetype=(("Doc files", "*.doc"), ("all files", "*.*")))
    TrackerFilePath.configure(text=filename)


def BrowsePanel():
    filename = filedialog.askopenfilename(initialdir=".", title="Select A File",
                                          filetype=(("Doc files", "*.doc"), ("all files", "*.*")))
    PanelFilePath.configure(text=filename)


try:
    user_info = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(), win32api.GetUserName(), 2)
    full_name = user_info["full_name"]
except:
    full_name = 'User'

# Set DPI awareness for Win10 systems
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Create the App, define the size and title
root = tk.Tk()
root.geometry('800x600')
root.title('Profile Screening Tool')
root.resizable(False, False)

# Create a main frame for the App
mainFrame = tk.Frame(root, bg='light gray')
mainFrame.pack(fill="both", expand=True)

# Create the Status bar
status = tk.Label(root, text=" ", relief='sunken', anchor=tk.W, bd=1)
status.pack(side="bottom", fill="x")

# Create the holding area for the app components
appArea = tk.Frame(mainFrame)
appArea.pack(padx=10, pady=(10, 0), fill="both", expand=True)

# Create the Header frame
headerFrame = tk.Frame(appArea)
headerFrame.pack(fill="both", expand=True)

headerLabel = tk.Label(headerFrame, text='KPMG Profile Screening Tool', bg='light blue', fg='black', font='Calibri 24 bold')
headerLabel.pack(fill="both", expand=True)

# Display the logged in User name
UserFrame = tk.Frame(appArea)
UserFrame.pack(fill="both", expand=True)

UserLabel = tk.Label(UserFrame, text="Hello " + full_name, font='Calibri 18')
UserLabel.pack(fill='x', expand=True)

# JD file handling area
JDFrame = tk.Frame(appArea)
JDFrame.pack(fill="both", expand=True)

JDLabelFrame = tk.Label(JDFrame, text="Select the JD file", font='Calibri 16', anchor='nw')
JDLabelFrame.pack(fill="x", expand=True)

JDFilePath = tk.Label(JDFrame, text="File Name", width=60, height=1, bd=1, font='Calibri 14', anchor='w', relief='solid', bg='white', fg='black')
JDFilePath.pack(side="left", expand=True, padx=10, pady=10)

JDButton = tk.Button(JDFrame, text="Browse", command=BrowseJD, fg="black", width=10, bg="light blue", bd=2, height=1, font='Helvetica 10')
JDButton.pack(side="right", expand=True, padx=10, pady=10)

# Tracker file handling area
TrackerFrame = tk.Frame(appArea)
TrackerFrame.pack(fill="both", expand=True)

TrackerLabelFrame = tk.Label(TrackerFrame, text="Select the Tracker file", font='Calibri 16', anchor='nw')
TrackerLabelFrame.pack(fill="x", expand=True)

TrackerFilePath = tk.Label(TrackerFrame, text="File Name", width=60, height=1, bd=1, font='Calibri 14', anchor='w', relief='solid', bg='white', fg='black')
TrackerFilePath.pack(side="left", expand=True, padx=10, pady=10)

TrackerButton = tk.Button(TrackerFrame, text="Browse", command=BrowseTracker, fg="black", width=10, bg="light blue", bd=2, height=1, font='Helvetica 10')
TrackerButton.pack(side="right", expand=True, padx=10, pady=10)

# CV handling area
CVFrame = tk.Frame(appArea)
CVFrame.pack(fill="both", expand=True)

CVLabelFrame = tk.Label(CVFrame, text="Select the CV location", font='Calibri 16', anchor='nw')
CVLabelFrame.pack(fill="x", expand=True)

CVFilePath = tk.Label(CVFrame, text="File Name", width=60, height=1, bd=1, font='Calibri 14', anchor='w', relief='solid', bg='white', fg='black')
CVFilePath.pack(side="left", expand=True, padx=10, pady=10)

CVButton = tk.Button(CVFrame, text="Browse", command=BrowseCV, fg="black", width=10, bg="light blue", bd=2, height=1, font='Helvetica 10')
CVButton.pack(side="right", expand=True, padx=10, pady=10)

# Interview Panel handling area
PanelFrame = tk.Frame(appArea)
PanelFrame.pack(fill="both", expand=True)

PanelLabelFrame = tk.Label(PanelFrame, text="Select the Panel Master file", font='Calibri 16', anchor='nw')
PanelLabelFrame.pack(fill="x", expand=True)

PanelFilePath = tk.Label(PanelFrame, text="File Name", width=60, height=1, bd=1, font='Calibri 14', anchor='w', relief='solid', bg='white', fg='black')
PanelFilePath.pack(side="left", expand=True, padx=10, pady=10)

PanelButton = tk.Button(PanelFrame, text="Browse", command=BrowsePanel, fg="black", width=10, bg="light blue", bd=2, height=1, font='Helvetica 10')
PanelButton.pack(side="right", expand=True, padx=10, pady=10)

# Start the profiling button
SubmitFrame = tk.Frame(appArea)
SubmitFrame.pack(fill="both", expand=True)

SubmitButton = tk.Button(SubmitFrame, text="Start", fg="black", width=10, bg="light blue", bd=2, height=2, font='Helvetica 10')
SubmitButton.pack(padx=10, pady=10, expand=True)

# Display text to Status bar on Ready
status.config(text="Tool Ready")

root.mainloop()
