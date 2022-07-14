# RSS-Feed-Reader
My first personal project, Takes In RSS Feeds and parses them 
as well as scrapes the articles within to display in a GUI.

The project uses some libraries that are found in the Requirements.txt file.

Prior to running the program please open command prompt, move to the programs folder, and run pip install -r requirements.txt.

Run the RunMe.py file to run the program.

Running the program will open up a GUI, that will display a page of news articles coming from the sources stored in the newsSources.txt File

The news sources are displayed by weight, with top stories appearing on the first pages
and lesser priority pages appearing on the subsequent pages.

Clicking the <Prev and Next> Buttons will change the page of articles being displayed
coming from the news sources listed in newsSources.txt

Clicking the "Add a Feed" Button will display a popup Window asking for the 
name of the source as well as the RSS feed itself. It will then parse through
the new feed, add the feed to the newsSources.txt file for future use, and
refresh the GUI to show the new collection of articles.


