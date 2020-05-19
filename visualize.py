import pandas as pd
import seaborn as sb
import yagmail as yg 
import os
import pathlib
import numpy as np
import matplotlib.pyplot as plt
# Personal Assessment Chris - Data class , clean data method, plot 
# Pesonal Assessment Maya- Yagmail stuff , try and except 
# both added the loop for bargraph and lmplot

class Data:
    """ Data : Take a cleaned dataframe and creates different visualizations for a user  """
    def __init__(self,ind,dep):
        self.ind = ind
        self.dep = dep


    def clean_data(self):
        """ Clean_data: Cleans both CSV files and merges them into one through a left join on the COUNTY column 
            Returns: The merged dataframe"""

        corona_df = pd.read_csv("county_corona_data.csv") # Reads in the csv and makes it into a dataframe
        corona_df2 = corona_df.drop(["COUNTY_FIP","DISTRICT", "COUNTYNUM"], axis=1) #Removal of specified columns and makes new dataframe "corona_df2"
        corona_df3 = corona_df2.drop(["Shape__Area","Shape__Length","EOCStatus","OBJECTID"],axis=1)
        corona_df3["COUNTY"] = corona_df3["COUNTY"].astype(str) #accesses the "COUNTY" column on the dataframe and converts it to a string
        demographic_df = pd.read_csv("county_demographic.csv") 
        demographic_df2 = demographic_df.drop([24,25,26,27]) #Makes new dataframe "demographic_df2" that removes last 4 rows of csv
        demographic_df2['CleanCounty'] = demographic_df2['County'].apply(lambda s: str(s)[:-7])#Removes the word county after the name of the county in County column
        demo_df3 = demographic_df2.drop(["Total Population, 2010","Total Population, 2000", "Population Change, 2000-2010","County"], axis=1)
        demo_df4 = demo_df3.replace("Baltimo","Baltimore City") #Replaces "Baltimo" with "Baltimore City" in demo_df3, and create a new dataframe demo_df4
        demo_df4["CleanCounty"] = demo_df4["CleanCounty"].astype(str) ##accesses the "CLEANCOUNTY" column on the dataframe and converts it to a string
        
        demo_df4
   
        merged_df = corona_df3.merge(demo_df4, left_on='COUNTY', right_on='CleanCounty',how="left")

        return merged_df


    def plot(self):
        """ Plot: Save a visualization , with a user inputted title and file name, dependent on the user input of 
        indepedent and dependent variables"""
        if (ind == "COUNTY"): 
            x = sb.barplot(x=(ind), y=(dep), data=self.clean_data()) #Creates plot with the merged datafram
            x.set_xticklabels(x.get_xticklabels(),rotation=85)
            x.set_title(title)
            plt.savefig(attachment)

        else:
            x = sb.lmplot(x=(ind), y=(dep),hue="COUNTY",  data=self.clean_data()) #Creates plot with the merged datafram
            x.set_xticklabels(rotation=90)
            plt.title(title)
            x.savefig(attachment)
        
    

ind = input("What is your independent variable \n") # Independent Variable
dep = input("What is your dependent variable \n") # Dependent variable Affected by X
title = input("what is the title of your graph \n") # Title Name
attachment = input("What is your file name\n") # File Name
name = input("Who are we sending this email to \n") # User input for their name so the email will sound personal

viz= Data(ind,dep)#setting a variable to the instance 
viz.plot()#Instance of the plot method


direct = str(pathlib.Path().absolute())

attachment = attachment + ".png" #Adding .png to the file name 


fullpath = os.path.join(direct, attachment)# creates a variable fullpath, that is the string literal of the absolute path to the saved plot 


try:

    sender_email = input("What is the sender email, by the way you can email yourself \n") #Input  from email
    recipent = input("Which email address would you like to receive your visualization at? :) \n") #User inputs their email
    password_send = input("what is your password? \n")#Inputs password of sender email.
    subject = "Coronavirus  Graph" #Email Subject
    content = ["Hello\t" +  name +"," "\n Attached is your Covid-19 Graph made specificially for you."  
    " Now that you know this information, it is important that you follow both Larry Hogan's order and the CDC's guidelines.Thank you for your time, stay safe.  \n\n Sincerely,  \nChristopher Solano and Maya Alli"] 
    operation = yg.SMTP(user=sender_email, password=password_send)
    operation.send(to=recipent, subject=subject,contents=content,attachments=(fullpath))
    print("Visualization Sent")

except:
    print("Uhhh something went wrong \n Things that might need to be fixed" 
    "\n Sender Email was not a Google Email" 
    "\n Sender Email was not correct(misspelled)"
    "\n Incorrect Password entered for Sender Email"
    "\n Recipient Email was not a Google Email"
    "\n Recipeint Email was not correct(misspelled)")

if __name__ == "__main__":
    main()

    #print("Unfortunately the email was not sent. Suggestion: Make sure sender email is correct,"
    #"make sure recipent email is correct, make sure password is correct")
#"C:\Users\CAS\Documents\INST326\i_need_a_life.png"