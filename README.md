# Corona-Visualization-Emails
##What Our Project Is: Coronavirus Visualization Emails 
-Our project is a program that gives the user a way to visualize the correlations between independent and dependent variables regarding Maryland County Demographic Data and Coronavirus Data, respectively. This program will prompt the user to enter information such as their chosen dependent and independent variables, first and last name, email sender and recipient, graph title, and file name; the user will then recieve an email of the visualization. 

##Documentation/How-to of this project 

Part 1: Dowload the files for this code-
How to dowload the files:
  first go to this website: https://opendata.maryland.gov/Demographic/Choose-Maryland-Compare-Counties-Demographics/pa7d-u6hs/data
  next, on the right side of the page, click export and on the dropdown menu select download-CSV. When that file downloads, renamme and save it as "county_demographic" as a csv file.
  next, go to our repository (Corona-Visualization-Emails) and click on the file "county_corona_data.csv"; once the file is shown, click on 'Raw' and on that page right click the page and download it as a csv file. Make sure to download as csv file. 
 
#Part 2: Preparing to run the code-
Go to your terminal and enter seperately:
pip install seaborn,
pip install yagmail,
pip install MatplotLib, 
pip install numpy

  make sure these packages download successfully 
The imported files in the code include: Seaborn, Matplotlib, Yagmail, OS, and Pandas

-Matplotlib creates visualizations such as graphs and charts in Python, and is used in this dataset to create either a bar chart or a plot, depending on the user's input. 
-Seaborn works as data visualization with statistics and a data visualization library that works with Matplotlib, and we used it to translate our statistics/data from our datasets into visualizations. 
-OS is a built-in Python module that gave us a way to use functions that are dependent on an operating system. It allowed us to create a variable fullpath, the string literal of the absolute path to the saved plot that we ended up making. 
-Yagmail allows the user to send an email through Gmail; we used this to create a subject, allow the user to input their email and password, and provide the user their visual attachment.
-pandas is used to manipulate data and allows us to analyse data as well. pandas allowed us to clean our data by dropping columns and/or rows in our dataset, rewording labels on the data, merge our two dataframes together involving Maryland county demographics as well as Maryland coronavirus data by county, and create the dataframes that would be the basis for our visualizations.

Setting up email 
1. Go to Gmail 
2. In the Upper right hand corner, click your Account Icon that should have your initial to your first name
3. Click Manage Your Account
4. On the right hand side, click Security 
5. Go to the the Block that says "Less Secure App Access" 
6. Turn on Less Secure App Access, note that after you have finished running the code you can turn this feature off but for the sake of the code this is crucial to send emails 


#Part 3: Running the code-
Open the code "visualize.py" in Visual Studio Code for Python 
Run the code 
In the terminal, you will be asked: "What is your independent variable?
Enter one of the following exactly as shown:[Total Population, 2018,Population Density per Square Mile,Median Age,Per Capita Personal Income ($ Dollars),Median Household Income ($ Dollars),Total Personal Income ($ Thousands),COUNTY] without the underline

You will then be asked: "What is your dependent variable?"
  Enter one of the following:[TotalCaseCount,TotalDeathCount, ProbDeaths, NegativeTests, TotalTests, PercentPos] without the underline
  
  *Note if you enter "COUNTY" you can input any variable in either list to get a bargraph, any other independent variable produces a line plot 

-For "What is the title of your graph?"
  -Enter whatever you want the title of your graph to be
  
-"What is your file name?"
  -Enter what you want your file name to be, below is appropriate file names depending on your operating system 
  - Note, there is no need to add file extension such as .jpeg or .png to your file, just make sure it follows the file conditions
 
 https://docs.microsoft.com/en-us/windows/win32/fileio/naming-a-file
  
 
 https://www.cyberciti.biz/faq/linuxunix-rules-for-naming-file-and-directory-names/
  
-"Who are we sending this email to"
  -Enter your first and last name (or whoever's name you are sending it to)
  
-"What is the sender email, by the way you can email yourself"
  -enter your email- make sure it is gmail
  - make sure you followed the Setting up email directions
  
-"Which email address would you like to receive your visualization at? :)"
  -enter the email address that you would like to send the visualization to (it can be your own email as well)- make sure it is gmail
  
-"What is your password?"
  -Enter the email password and wait for the visualization to send to the email address. 
  
  - Make sure this is the password of the sender email 
  
 Part 4: Explanation of output:
For the output of these user input prompts, the user will see 'Visualization Sent' in the terminal. They will then go to the email they inputted as the recipient to find an email from the chosen sender.
The text portion of the email will read:
 
"Hello [name that you choose to input], attached is your Covid-19 Graph made specificially for you. Now that you know this information, it is important that you follow both Larry Hogan's order and the CDC's guidelines.
Thank you for your time, stay safe.
Sincerely,
Christopher Solano and Maya Alli"

-With this email, there will be an attachment representing a graph of the data that you chose (independent and dependent variables). On the graphs, the independent variable goes on the x-axis and the dependent variable goes on the y-axis. 


                                             
                                             Annotated Bibliography

Kooten, Pascal Van. “Yagmail.” PyPI, pypi.org/project/yagmail/.

We used this source initially as a framework for how we developed the code for our yagmail portion of the script; this was a start to us eventually being able to send emails with our visualizations attached, but we later made our code more complex in terms of options that came with sending the email. 

Joska, Langen de. “Sending Emails With Python.” Real Python, Real Python, 19 Sept. 2019, realpython.com/python-send-email/

This helped us with the plain text portion of the email that we sent (i.e the message that greets the user and tells them that this is the data visualization that they ordered from their user input). This was important in making the email seem more professional and polished. It also allowed us to see the appropriate framework and what to include as far as our variables (sender_email, password, message/content, and the general use of the variables). 

	Jtakeno, “Choose Maryland: Compare Counties - Demographics.” Maryland Department of Commerce, Maryland Department of   Commerce, 13 Dec. 2019, https://opendata.maryland.gov/Demographic/Choose-Maryland-Compare-Counties-Demographics/pa7d-u6hs

This dataset was used as the independent variable for the program, and represents the county demographics of people in the state of Maryland. We used this to compare and watch for correlations in regards to the coronavirus dataset; this dataset was used to allow us to make visualizations in which an independent variable is needed in order to complement the dependent variable. This entire dataset allowed us to see how county demographics might affect certain outcomes pertaining to coronavirus cases. In the end we merged the dataframe that held this cleaned data with the other dataframe that showed coronavirus cases and other factors by county; this merged dataframe created the graphs/plots that were delivered to the email recipient.

*Please be aware that the dataset for coronavirus cases by county exists, however before we were able to redownload it for instruction, the dataset was gone and/or deleted no more than days before our project was completed (and discovered deleted the day of) despite an extensive time searching for it last minute: https://coronavirus.maryland.gov/404
The dataset was originally obtained here: https://coronavirus.maryland.gov/datasets/d83b7887227e45728e6daf51a6c91c9f
 
We used this dataset as the dependent variable that represented the coronavirus cases by county in our data visualizations. Wer used this to compare and watch for correlations in regards to the county demographics dataset; it was used to allow us to make visualizations where we could see how coronavirus reacted depending on county demographic factors. We merged the dataframe that held cleaned data of coronavirus by Maryland counties data, and merged it with the dataframe that showed county demographics for Maryland; it would then create one dataframe that would be able to create visualizations of plots and graphs. 
