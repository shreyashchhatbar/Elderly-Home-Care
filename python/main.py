# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:23:24 2021

@author: Shrey
"""

import webbrowser
import datetime
import winsound
from playsound import playsound
import random
from tabulate import tabulate
from win10toast import ToastNotifier
  
print("\n >> WELCOME TO A REMAINDER NOTIFICATIOR PROGRAM <<")  
  
while True:  
    print("\n--- MAIN MENU ---")  
    print("1. Set remainder notification")  
    print("2. Check average heart rate for above 60 years of age")  
    print("3. Message of the day")   
    print("4. Watch yoga and meditation videos")  
    print("5. Play random melodies")  
    print("6. Healthy Diet chart for above 60 years of age")  
    print("7. Exit")  
    choice1 = int(input("Enter the choice: "))  
  
    if choice1 == 1: 
        print("\n--SET REMAINDER NOTIFICATION--")  
        print("\nNote: Input 24 hrs format time.")  
        words = str(input("What would  you remind of? "))
        alarmH = int(input("What hour do you want the alarm to ring? "))
        alarmM = int(input("What minute do you want the alarm to ring? "))
        amPm = str(input("AM or PM? "))
        
        print("Waiting for alarm:", alarmH, ":", alarmM, amPm+"\n")
        
        if(alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute):
            #print("Time to take medicine!")
            notif = ToastNotifier()
            #playsound("songs/beep.mp3")
            notif.show_toast(f"Remainder", words, duration = 5)
            frequency = 2500
            duration = 1000
            winsound.Beep(frequency, duration)
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 2:  
        print("\n--- CHECK AVERAGE HEART RATE FOR ABOVE 60 YEARS OF AGE ---\n")
        data = [
                    ["60 years", "80-176 bpm", "160 bpm"],
                    ["65 years", "78-132 bpm", "155 bpm"],
                    ["70 years", "75-128 bpm", "150 bpm"]
               ]
        
        print(tabulate(data, headers=["Age", "Target heart\nrate zone", "Average maximum\nheart rate"], tablefmt='orgtbl'))
        
    elif choice1 == 3:  
        print("\n--- MESSAGE OF THE DAY ---")
        motd = [
            ["Age is just a number for those who know\nhow to make the most of their lives."]], [
            ["Gray hairs are a proof that you have earned\nthe most valuable thing in life\nand that is called experience which comes with age."]], [
            ["Seniors are the most wonderful source for inspiration…..\nThey are the ones who can give us hope even in\nsituations when we have lost everything."]], [
            ["Avoid doing all the mistakes all by yourself and\nmake it a beautiful life by following the\nadvice of seniors around you"]],[
            ["We are truly blessed to have seniors around us\nas they teach us things,\ngive us advices which no one else can"]]
        random_motd = random.choice(motd)
        print(tabulate(random_motd, headers=["Message of the day"], tablefmt='orgtbl', colalign=("center",)))
    
    elif choice1 == 4:  
        print("\n--- WATCH YOGA AND MEDITATION VIDEOS ---")
        vids = [
                    ["1. Gentle Yoga Asanas for 60 to 70 year olds"],
                    ["2. Seated Exercises for Older Adults"],
                    ["3. Simple Excerise Yoga for seniors by Swami Ramdev"],
                    ["4. Guided Meditation for Seniors and Older Adults"],
                    ["5. Meditation to Empower a Healthy Life"],
                    ["6. Go back to main menu."]
               ]
        
        print(tabulate(vids, headers=["Video Titles"], tablefmt='orgtbl', colalign=("left",)))
        
        choice2 = int(input("Enter the choice to play video: "))
        if choice2 == 1:  
            webbrowser.open("https://www.youtube.com/watch?v=KEx-y2IFnlw")
              
        elif choice2 == 2:  
            webbrowser.open("https://www.youtube.com/watch?v=a8IKp0znasY")
              
        elif choice2 == 3:  
            webbrowser.open("https://www.youtube.com/watch?v=l00InLrEb7o")
              
        elif choice2 == 4: 
            webbrowser.open("https://www.youtube.com/watch?v=s6rXVM8VIWc")
              
        elif choice2 == 5: 
            webbrowser.open("https://www.youtube.com/watch?v=s7R1Qec2_D0")
  
        elif choice2 == 6:  
            pass
        
        else:  
            print("Oops! Incorrect Choice.")  
        
    elif choice1 == 5:
       # controls = [[
       #     "1. Pause song"], [
       #     "2. Play song"]]
        
       # print(tabulate(controls, headers=["Plaback Controls"], tablefmt='orgtbl', colalign=("left",)))
        
        songs = "Lag Ja Gale Instrumental","Kabhi Kabhi Mere Dil Me Instrumental", "Ruk Jaana Nahi Instrumental", "Kya Hua Tera Wada Instrumental", "Ek Pyar Ka Nagma Hai Instrumental"
        random_songs = random.choice(songs)
        print("\nPlaying", random_songs)
        playsound("songs/"+str(random_songs)+".mp3")
        
        """
        choice3 = int(input("Enter the choice: "))
        if choice3 == 1:  
            p = multiprocessing.Process(target=playsound, args=(str(random_songs),))
            p.terminate()
            
        elif choice3 == 2:  
            p = multiprocessing.Process(target=playsound, args=(str(random_songs+".mp3"),))
            p.start()
              
        elif choice3 == 3:
            pass
        
        else:  
            print("Oops! Incorrect Choice.")  
        """
    elif choice1 == 6:
        print("\n--- HEALTHY DIET CHART FOR ABOVE 60 YEARS OF AGE ---")
        category = [
                    ["1. Veg"],
                    ["2. Non-Veg"],
                    ["3. Go back to main menu."]
               ]
        
        print(tabulate(category, headers=["Category"], tablefmt='orgtbl', colalign=("left",)))
        
        choice4 = int(input("Enter the category choice: "))
        
        if choice4 == 1:  
            dcVeg = [
                        ["Early Morning - \n > Tea/Coffee/Green Tea (1 Cup) + Almonds (4) + Walnuts (2)"],
                        ["Breakfast - \n > Skimmed Milk: 1 Glass along with Oats/Stuffed Dosa/Vegetabel Poha/Stuffed Roti/Vegetable Sandwich"],
                        ["Mid-Morning - \n > Fruit (seasonal):  100 – 150gm"],
                        ["Lunch  - \n > Roti (2) + Vegetable (1 bowl) + Dal (1 bowl) + Rice (1 bowl) + Curd (1 bowl) + Salad (1 quarter plate)"],
                        ["Evening  - \n > Buttermilk/Lemon water/Vegetable soup: 1 glass"],
                        ["Dinner  - \n > Roti (2) or Rice (2 bowl) + Vegetable (1 bowl) + Dal (1 bowl) + Salad (1 quarter plate)"],
                        ["Bed Time  - \n > Milk (Skimmed):  1 Cup"],
                    ]
            
            print(tabulate(dcVeg, headers=["Standard Diet Plan (Veg) – Above 60 Years of Age"], tablefmt='orgtbl', colalign=("left",)))
            
        elif choice4 == 2:  
            dcNonVeg = [
                        ["Early Morning - \n > Tea/Coffee/Green Tea (1 Cup) + Almonds (4) + Walnuts (2))"],
                        ["Breakfast - \n > Vegetable Omelette (1) + Bread (2) \n > Dalia with veggies (1 bowl) + skimmed milk (1 glass)"],
                        ["Mid-Morning - \n > Fruit (seasonal): 150 – 200gm"],
                        ["Lunch  - \n > Roti (2) + Vegetable (1 bowl) + Chicken/Fish (2-3 pcs) + Rice (1 bowl) + Curd (1/2 bowl) + Salad (1 quarter plate)"],
                        ["Evening  - \n > Buttermilk / Lemon Water (1 glass)"],
                        ["Dinner  - \n > Roti (2)/ Rice (2 bowl) + Vegetable (1 bowl) + Grilled or Roasted Chicken/Fish (2-3 pcs) + Salad (1 quarter plate)"],
                        ["Bed Time  - \n > Buttermilk / Lemon Water (1 glass)"],
                       ]
        
            print(tabulate(dcNonVeg, headers=["Standard Diet Plan (Non-Veg) – Above 60 Years of Age"], tablefmt='orgtbl', colalign=("left",)))
        
    elif choice1 == 7:
        break
      
    else:  
        print("Oops! Incorrect Choice.")  
