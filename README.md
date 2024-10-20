# LunchLink
##### Code 4 Humanity Cal High
We are a student-led club at California High School that create projects designed to benefit our local community.

https://lunchlink.net


---
## Problem
The #1 issue we identified at Cal High was our lunch system; due to inavailability of certain foods there is frequent food wastage, very long lines, and lack of options for dietary restricted students. As a result many students abandon the lunch system altogether, choosing to go the rest of the school day hungry.

---
## Solution
Given that the problem lies in the disconnect between our lunch system and the student body we decided that the best solution is to incorporate student feedback into our school lunch system. By collecting data about student performances, we can project a distribution of our lunch items. We plan on sending surveys to the student body monthly, giving them the chance to rate each item on a scale of 1 to 5. These ratings are then used to calculate a ratio between two or more lunch options.

###### Example Scenario

Let's say the primary option today is cheese pizza and the secondary option is hot dogs, and that the lunch staff produce equal amounts of both. Given that students (probably) prefer cheese pizza to hot dogs, cheese pizza will run out right away, while hot dogs will be in surplus at the end of lunch break and end up being wasted. Vegetarian students can't even eat hot dogs, so unless they can beat the line and get the cheeze pizza before it runs out, they won't be able to get any lunch. Our solution is to project the ratio between primary and secondary options, such as 60% cheese pizza, and 40% hot dogs. 

---
## Features
Our web application has three pages:

#### Home
- Landing Page
- General quantitative statistics regarding data collection and API calls
#### Calendar
- Main functionality of our app
- Lets user select a day from a calendar, returns the menu, relative proportions, ratings collected, and a bar chart
#### Analytics
- Summary of ratings collected, produced by data visualziations
NODE_ENV=production node app
