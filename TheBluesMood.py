import webbrowser
from tkinter import *
import tkinter.messagebox as msg
import matplotlib.pyplot as plt
from collections import Counter
from PIL import ImageTk, Image
from datetime import datetime
import os 
from bs4 import BeautifulSoup
import html

def suggest(mood):
    activity_suggestion.config(state=NORMAL)
    activity_suggestion.delete("1.0", END)
    if mood in mood_activities:
        suggested_activities = mood_activities[mood]
        for activity in suggested_activities:
            activity_suggestion.insert(END, f"- {activity}\n")
    else: pass

def load_previous_moods():
    try:
        with open("mood_journal.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Mood:"):
                    mood = line.strip().split(": ")[1]
                    Moods.append(mood)
    except : pass
        
def email_admin():
    open("Joke.html",'r')


def open_admin():
    note = note_entry.get("1.0", "end-1c")
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("mood_journal.txt", "a") as file:
        file.write(f"Date: {current_date}\nNote: {note}\n\n")
    suggest(note)
    msg.showinfo(title="Message Shared", message="Your Message Has Been Shared")
    
def open_journal():
    try:
        os.system("open mood_journal.txt") 
    except: pass

def visualize():
    mood_count = Counter(Moods)
    plt.pie(mood_count.values(), labels=mood_count.keys(),autopct="%2.1f%%")
    plt.title("Mood Summary")
    plt.show()

def makeme_laugh():
    webbrowser.open_new_tab('Joke.html')        

def save_entry():
    mood = moods.get()
    note = note_entry.get("1.0", "end-1c")
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("mood_journal.txt", "a") as file:
        file.write(f"Date: {current_date}\nMood: {mood}\nNote: {note}\n\n")
    suggest(mood)
    msg.showinfo(title="Mood Documented", message="Mood Documented Successfully").pack()
    

root = Tk()
root.title("Mood Journal")
root.geometry("450x600")
img=Image.open("MCS Header Logo Blue and White.jpg")
img=img.resize((400,100))
ph=ImageTk.PhotoImage(img)
image_label = Label(root,image=ph,)
image_label.pack(pady=10,anchor=N)
Label(root, text="How Are You Feeling Today ?", font="Roboto 16",bg="aqua").pack(pady=10)
options = ['Happy', 'Upset', 'Sad', 'Excited', 'Neutral', 'Sick', 'Lonely']
moods = StringVar()
dropdown = OptionMenu(root, moods, *options)
dropdown.pack(pady=10)
note_label = Label(root, text="Please explain why you are feeling this way? ",font="Roboto 16")
note_label.pack()
note_entry = Text(root, height=5, width=30)
note_entry.pack(pady=10)
Button(root, text="Save My Mood", command=save_entry,fg="green").pack(pady=5)
Button(root, text="Click Here for your Mood Summary",command=visualize).pack(pady=5)
Button(root, text="Open Mood Journal ", command=open_journal,fg="blue").pack()
Button(root, text="Share with your Administrators", command=open_admin, fg="red").pack()
Button(root, text="Make Me Laugh", command = makeme_laugh, fg = "purple").pack()
Label(root, text="Suggested Activities - ", font="Roboto 16",bg="chartreuse").pack(pady=10)
activity_suggestion = Text(root, height=5, width=50)
activity_suggestion.pack()

mood_activities = {
    'Happy': ["Watch a comedy movie", "Call a friend", "Try a new recipe and cook a special meal"],
    'Angry': ["Try deep breathing exercises", "Engage in a hobby", "Listen to calming music or sounds of nature"],
    'Sad': ["Listen to soothing music", "Write in a journal", "Practice mindfulness"],
    'Excited': ["Try a new adventure, like hiking or skydiving", "Learn a new skill or hobby you've been curious about"],
    'Neutral': ["Exercise for 10 minutes", "Perform an act of kindness", "Read a good book"],
    'Sick': ["Ask your teacher to let you see the nurse"],
    'Lonely': ["Try to Smile", "Join a club or sport", "Ask your teacher to let you speak with a counselor"],
}
Moods = []
load_previous_moods() 
root.mainloop()
