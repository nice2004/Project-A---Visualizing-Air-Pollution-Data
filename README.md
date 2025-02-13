# Project-A---Visualizing-Air-Pollution-Data

***Names: Nice Teta Hirwa*** <br />
***Instructor: Professor Mike Ryu*** <br />
***Class: CS-150*** <br />

> ## Thesis Statement
Visually analysing air quality Index patterns in Northern California local sites throughout 2020

> ## Context of my data visualization
In the year of 2020, industries, gas stations and other areas that contribute to air pollution was almost closed.
But did the air quality index become better? In my project, I try to answer this question by visually plotting air quality index values in different local sites in 
Northern California. As the dashboard shows there was a drastic AQI value where it was lowered from 100 to the range of 10-25.
In the dashboard, I used North California dataset that displays months, different local 
sites in North California and the air index quality variables. I then plotted these variables together in a dashboard to portray the thesis of the project.

> ## Data I will be visualizing
I will visualize air quality index of different local sites in North California from January to December of the year2020

> ## Call to Action
This is an example that the reduction of air quality values in Northern California is possible. Yes, we are not going back to COVID -19, but we (all together) can individually or on  a governmental level put on strategies that completely eliminate air quality values to be higher just like the startegies in 202o drastically reduced the air quality index.


> ## Strategies employed from SWD
1.  Articulating my unique point of view of the project
2. Specifically conveying what’s at stake
3. Displaying what is happening, what should be the audiences response, and how is the data being displayed correctly

> ## Explaining the coding part of the project
Air_Pollution.py has three main parts that makes the visual display effective. 
1. Preparing the data: Here, I printed out the top of the csv to see how it looks like, I checked if there is any missing numbers in any of teh columns that I wanted to use
and I finally changed the date into date time. 
2. App_Layout: In the app layout, I created my dashboard with drop-downs that would allow multiple comparison of different 
local sites, and created an interface where users can interact with the dashboard by adding or removing some local sites.
3. Call back: In my call back function, I have a function called updated_graph that updates the graph and layout(like color and keys) everytime a user adds in another local site to compare. It also
filters the dataframe to include only the selected sites with its title. 

And I finally called the main() function to run the code.


