from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import requests
 
def get_data(cases): 
           
           city_name = textfield.get()
           url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

           headers = {
               'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
               'x-rapidapi-key': "33f1673efemshe6e0a36c0cea3bfp17fd52jsnb9eb10cfbc0e"
               }
           response = requests.request("GET", url, headers=headers).json()
           
           for each in response['state_wise']:
               if int(response['state_wise'][each]['active']) != 0:
                   for city in response['state_wise'][each]['district']:
                       if city.lower() == city_name.lower():
                          active ="Active cases "+ str(response['state_wise'][each]['district'][city]['active'])
                          confirmed="Confirmed cases " +str(response['state_wise'][each]['district'][city]['confirmed'])
                          deceased="Deceased cases " + str(response['state_wise'][each]['district'][city]['deceased'])
                          recovered="Recovered cases " + str(response['state_wise'][each]['district'][city]['recovered']) 
                          label1.config(text = active)
                          label2.config(text = confirmed)
                          label3.config(text = deceased)
                          label4.config(text = recovered)

cases = tk.Tk()
cases.geometry("600x500")
cases.title("Covid Tracker")
cases.configure(bg='#d1e6e3')

#Background Image
bg = PhotoImage(file = "stay-home.png")
canvas1 = Canvas( cases, width = 300,height = 300)
              
canvas1.place(x=0, y=249, relwidth=1, relheight=1)
canvas1.create_image(0,0, image=bg, anchor="nw")   

#Fonts
f = ("poppins", 18, "bold")
t = ("poppins", 35, "bold")

#Search bar
textfield = tk.Entry(cases, justify='center', width = 20, font = t,bg="white",)
textfield.pack(pady = 50)
textfield.place(x=35, y=10)
textfield.focus()
textfield.bind('<Return>', get_data)

#Label
label1 = tk.Label(cases, font=t,bg='#d1e6e3',fg='red')
label1.place(x = 120,y = 80,anchor ='nw')

label2 = tk.Label(cases, font=f,bg='#d1e6e3',fg='#ff9f00')
label2.place(x = 160,y = 145,anchor ='nw')

label3=tk.Label(cases,font=f,bg='#d1e6e3',fg='#0073cf')
label3.place(x = 160,y = 173,anchor ='nw')

label4=tk.Label(cases,font=f,bg='#d1e6e3',fg='#228B22')
label4.place(x = 160,y = 205,anchor ='nw')

cases.mainloop()