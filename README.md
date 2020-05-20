# Corona-Visualization-Emails
##What Our Project Is: Coronavirus Visualization Emails 
-Our project is a program that gives the user a way to visualize correlations/independent and dependent variables as related to Coronavirus cases by county in Maryland. This program will prompt the user to enter information such as their chosen dependent and independent variables, first and last name, email sender and recipient, graph title, and file name; the user will then recieve an email of the visualization. 

##Documentation/How-to of this project 

Part 1: Dowload the files for this code-
-How to dowload the files:
  -first go to this website: https://opendata.maryland.gov/Demographic/Choose-Maryland-Compare-Counties-Demographics/pa7d-u6hs/data
  -next, on the right side of the page, click export and on the dropdown menu select download-CSV. When that file downloads, renamme and save it as "county_demographic.csv" as a csv file.
  -then, go to [comeback to and find link, how to download, and what to rename it---OR ADD THE CSV FILE TO REPOSITORY AND TELL THEM TO DOWNLOAD IT] 
 
#Part 2: Preparing to run the code-
-Go to your terminal and enter seperately:
pip install seaborn
pip install yagmail
pip install MatplotLib 
pip install numpy
  -make sure these packages download successfully 

#Part 3: Running the code-
-Open the code "visualize.py" in Visual Studio Code for Python 
-Run the code 
-In the terminal, you will be asked: "What is your independent variable?"
  -Enter one of the following:[Independent variable lists]
-You will then be asked: "What is your dependent variable?"
  -Enter one of the following:[Dependent Variable lists]
-For "What is the title of your graph?"
  -Enter whatever you want the title of your graph to be
-"What is your file name?"
  -Enter what you want your file name to be
-"Who are we sending this email to"
  -Enter your first and last name (or whoever's name you are sending it to)
-"What is the sender email, by the way you can email yourself"
  -enter your email
-"Which email address would you like to receive your visualization at? :)"
  -enter the email address that you would like to send the visualization to (it can be your own email as well)
-"What is your password?"
  -Enter the email password and wait for the visualization to send to the email address. 

 Part 4: Explanation of output
 -

  
