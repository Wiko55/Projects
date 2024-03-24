# Polish Elections Data Analysis
### Description and problem to solve
After the polish elections for parlament in 2023 I've seen someone on twitter claiming that a lot of first women on list got suprisingly big amount of votes comparing to their position on list. It could mean that there is tendency that some people vote for first woman in list or that some women should be placed higher in the voting list.
I've decided to check it and to find out if it's the case. 
#### Code : 
# Table of contents
1. [Formatting the Data](#section1)

2. [Examplary Plots](#section2)

3. [Performing Analysis](#section3)
    
4. [Data Sources](#section4)



## 1. Formatting the Data <a name="section1"></a>
Files are saved in CSV format, so I load them in.

![image](https://github.com/Wiko55/Projects/assets/139919714/be4b0227-0a12-4802-8597-1ea2e4e2f2d9)

There is a first name, surname and party in the same label so I disjoin them. Later on I create new column names for the needed data and I also remove some.

![image](https://github.com/Wiko55/Projects/assets/139919714/25b74055-ded0-4826-ac73-04ba4ef35cd6)

Each of 41 election files corresponds to other constituency so I add them all to one dictionary using loop. I also add a new column with percentage of votes, because in my later analysis number of votes isn't as important as the percantage of it.

![image](https://github.com/Wiko55/Projects/assets/139919714/8b410bd9-efca-4221-9818-ead5452ec66f)


## 2. Examplary Plots <a name="section2"></a>
The plots of some examplary parties where first woman got more votes than man who was before in list

![#2](https://github.com/Wiko55/Projects/assets/139919714/95ffe77e-149f-4324-9fcc-6abcef9609dd)
![#1](https://github.com/Wiko55/Projects/assets/139919714/d0fd0761-5a1d-4540-98d4-86b04fc63192)

## 3. Performing Data Analysis
By creating a function I get an information that on average first woman got 1.37 percentage points less than the man who was before them in list. 
Note: This is the statistic for voting where the first woman was at 3th number in list or higher.

![image](https://github.com/Wiko55/Projects/assets/139919714/16bb341c-c922-42b2-bd53-e3a10ed5739e)

It is normal that people who are later in list get less votes, but I would like to know what is this is a typical difference between every candidate.
So I create the function to get an average difference between n-1 and n'th position in list and compare it to difference between first woman and the man before her in list.

![image](https://github.com/Wiko55/Projects/assets/139919714/e0547a5d-70c8-413e-a453-415939d5cb08)

Using the difference between the results of two function I can see that the average gap between first woman and average gap in the lists on the same place is -2.86

![image](https://github.com/Wiko55/Projects/assets/139919714/7dc8b6cd-28fe-4109-ab0d-acc83b64b9f8)

In other words it means that women on average got 2.86 percentage points more than a man would get at the same place in list. It is pretty big difference.

## 4. Data Sources <a name="section2"></a>
Polish government site: https://wybory.gov.pl/sejmsenat2023/pl/dane_w_arkuszach
