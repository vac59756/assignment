# Introduction 
The repo contains three independent script under /test that performs scraping on a website


The script performs the following task

1 Using Selenium, load the flipkart.com desktop home page.

2 Search for the product "Samsung Galaxy S10" on that page. 

3 On the search results click on "Mobiles" in categories.

4 Apply the following filters (in filters section on the left hand side):   

    Brand: Samsung

    Select Flipkart assured

    Sort the entries with Price -> High to Low.

5 Read the set of results that show up on page 1.

6 reate a list with the following parameters, and print this on the console.

    Product Name

    Display Price

    Link to Product Details Page 

assignment.py script is designed to run on local system and perform the scraping.

automateScript.py is designed to perform the scraping by running the tests using Browserstack Automate platform on five diferent parallel (Browser/OS combination). Dependent on browserstack.yml file under Parent directory.

githubCI.py is desined to run the test on Browserstack Automate platform integrated with Github action. Gets triggred on each push. This is the dependency to the action.yml file under .github/workflow directory

# Getting Started
Installation/Build/Test process

    Clone the repo on your local system
    
    Prerequisites - python3, pip3 and Selenium(install selenium through PIP) installed
    To run script assignment.py, run command pyton3 ./tests/assignment.py in the root directory
    To run script automateScript.py
        run > pip3 install -r requirements.txt > in the parent directory
        run > browserstack-sdk python3 ./tests/automateScript.py
    Script githubCI.py gets triggered when there is a push performed on the repo
