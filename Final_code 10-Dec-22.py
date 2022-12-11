identities = {} # Dictionary to store the user credentials
# Improvements: store the credentials in a separated file.


import pandas as pd
import os
from IPython.display import display
df = pd.read_excel(r'Disco_df.xlsx')
import warnings
warnings.filterwarnings('ignore')


def points(user,df,row):                             
    points = 0
    if user.location == df.iloc[row][1]:
        points += 1*(user.location_imp/10)
    else: 
        points += 0
        pass
    if user.ticket == df.iloc[row][2]+1 or user.ticket == df.iloc[row][2]+2 or user.ticket == df.iloc[row][2] or user.ticket == df.iloc[row][2]-1 or user.ticket == df.iloc[row][2]-2:
        points += 1*(user.ticket_imp/10)
    else: 
        points += 0
        pass
    if user.drink == df.iloc[row][3] or user.drink == df.iloc[row][3]+1 or user.drink == df.iloc[row][3]-1:
        points += 1*(user.drink_imp/10)
    else: 
        points += 0
        pass
    if user.code == df.iloc[row][4]:
        points += 1
    else: 
        points += 0
        pass
    if user.age > df.iloc[row][5] and user.age < df.iloc[row][6]:
        points += 1
    else: 
        points += 0
        pass
    if user.music in df.iloc[row][7]:    
        points += 1
    else: 
        points += 0
        pass
    if user.lists == df.iloc[row][8]:
        points += 1
    else: 
        points += 0
        pass
    if user.queue == df.iloc[row][9]:
        points += 1
    else: 
        points += 0
        pass
    if user.vip == df.iloc[row][10]:
        points += 1
    else: 
        points += 0
        pass
    if user.inter == df.iloc[row][11]:
        points += 1
    else: 
        points += 0
    return float(points)

class Subject():
    def __init__(self,df):
        self.username = None
        self.password = None
        self.identities = {}
        self.location = input("Where do you live? (centre, orense,...) ").strip().lower()
        self.location_imp = float(input("How important is the location for you? In a scale from 1 to 10: ")) 
        self.age = int(input("How old are you? "))
        self.music = input("What is your favorite type of music? (techno/commercial/reggaeton) ")
        self.code = input("How do you dress for parties? (casual/formal/fancy/alternative) ")
        self.ticket = int(input("Which price range are you looking for (2 drinks included) "))
        self.ticket_imp = float(input("How important is the price to you from 1 to 10? "))
        self.drink = int(input("What is the Maximum you would pay for a drink? "))
        self.drink_imp = float(input("How likely are you to buy an extra drink from 1 to 10? "))
        self.lists = bool(input("Do you like to be in a list? (yes/no) ").lower().strip()[0] == 'y')
        self.queue = input("How importanty is queuing for you? (high/medium/low) ").strip().lower()       
        self.vip = bool(input("Do you want to go VIP? (yes/no) ").lower().strip()[0] == 'y')
        self.inter = bool(input("Do you enjoy an international atmosphere? (yes/no)) ").lower().strip()[0] == 'y')
        self.df = df
    


    def intro(self, df, identities ):
        print(
            """
Welcome to Ticket-Mister!
We will help you find the best parties for you in Madrid answering just a few questions.
Please select the options that best fit you:

        1. Register
        2. Sign in 
        3. Find a party as a guest
            """
        )
        option = int(input("Please type the number of the option selected: "))
        os.system("cls")


        if option == 1:
            print("Please fill in the following information: ")
            usuario = input("Create a Username: ")
            self.username = usuario
            contra = input("Create a Password: ")
            self.password = contra
            if usuario in identities.keys():
                print("Username already exists. Please try again.")
                return Subject.intro(Subject,df, identities)
            else:
                identities[usuario] = contra
                os.system("cls")
                print("""
Thank you for registering!
Now sign in to find the best parties for you!
                """)
                return Subject.intro(Subject,df, identities)

        elif option == 2:
            print("Please sign in: ")
            logus = input("Username: ")
            logpw = input("Password: ")
            if (logus in identities) and (identities[logus] == logpw):
                os.system("cls")
                print("Welcome back!")
                print("Enter now your preferences: ")
                return Subject(df)
            else:
                os.system("cls")
                print("Wrong username or password")
                print("Please register, try again or enter as a guest")
                return Subject.intro(Subject,df, identities)

        elif option == 3:
            os.system("cls")
            print("Enter now your preferences: ")
            return Subject(df)



def list_points(user,df):
    points_list = []
    for i in range(len(df)):                       
        points_list.append(points(user,df,i))
    os.system('cls')
    return points_list

def sort_points(array):
    high = []
    mid = []
    low= []
    if len(array) > 1:
        point =array[0]
        for i in array:
            if i > point:
                high.append(i)
            elif i == point:
                mid.append(i)
            elif i < point:
                low.append(i)
        ordered_list = sort_points(high)+mid+sort_points(low)
    else:
        ordered_list = array
    
    return ordered_list

def sort_list(user, df):
    df_new = df
    df_new["Points"] = list_points(user, df)
    ordered_df = pd.DataFrame()
    lista = list(dict.fromkeys(sort_points(list_points(user, df))))
    for i in lista:
        row = df_new.loc[df_new["Points"] == i]
        ordered_df = ordered_df.append(row, ignore_index = True)
    print("Your club of preference is: ", ordered_df["Clubs"][0])
    display(ordered_df.iloc[:,0:12].head(3))



os.system('cls')
user = Subject.intro(Subject, df, identities={})
sort_list(user, df)
