# Project-A---Visualizing-Air-Pollution-Data

## Names: Nice Teta Hirwa
## Instructor: Professor Mike Ryu
## Class: CS-150

## Thesis Statement
Exploring the relationship between the air quality index in North California local sites and the months in the year of 2020

## Context of my data visualization
In the year of 2020, industries, gast stations and other areas that contribute to air pollution was almost closed.
But did the air quality index become better? Through my project, I try to answer this question by navigating the relationship between the
air pollution index and how it how was distributed over the months in 2020. I use the North California dataset that displays months, different local 
sites in North California and the air index quality variables. I then plotted these variables together in a dashboard to portray the thesis of the project.

## Data I will be visualizing
I will visualize air quality index of different local sites in North California from January to December 2020

## Strategies employed from SWD
1.  Articulating my unique point of view of the project
2. Specifically conveying what’s at stake
3. Displaying what is happening, what should be the audiences response, and how is the data being displayed correctly

## Explaining the coding part of the project
Air_Pollution.py has three main parts that makes the visual display effectively. 
1. Preparing the data: Here, I printed out the top of the csv to see how it looks like, I checked if there is any missing numbers in any of teh columns that I wanted to use
and I finally changed the date into date time. 
2. App_Layout: In the app layout, I created my dashboard with drop-downs that would allow multiple comparison of different 
local sites, and created an interface where users can interact with the dashboard by adding or removing some local sites.
3. Call back: In my call back function, I have a function called updated_graph that updates the graph and layout(like color and keys) everytime a user adds in another local site to compare. It also
filters the dataframe to include only the selected sites with its title. 

And I finally called the main() function to run the code.

