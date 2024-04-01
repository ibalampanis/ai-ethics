import datetime

# Get the current day
current_day = datetime.datetime.now().strftime("%A")
quotes = {"Monday": "Being green and clean is not just an aspiration but an action. -Christine Pelosi", 
"Tuesday": "The future will be either green or not at all. -Bob Brown",
"Wednesday": "Going green doesn't start with doing green acts, it starts with a shift in consciousness. -Ian Somerhalder", 
"Thursday": "Green technologies - going green - is bigger than the Internet. It could be the biggest economic opportunity of the 21st century. -Narendra Modi", 
"Friday": "I think any opportunity you have to be green, whether it's in business or in everyday life, you should take it. -Lauren Conrad", 
"Saturday": "Lack of time and money create really bad green practices. -Ian Somerhalder", 
"Sunday": "Green calm below, blue quietness above. - John Greenleaf Whittier"}

print ("Quote for", current_day + ":", quotes[current_day])

tips = {"Monday": "Be careful of the water you spill. Water is life",
        "Tuesday": "Did you know that there are thrift shops and second-hand stores that have pricey brands at a very affordable price? Check them out",
        "Wednesday": "Don't forget to turn of the lights on your way out today!",
        "Thursday": "Thursday is the best day to make a lunch from all the scraps you have in your fridge. Don't let them go bad!",
        "Friday": "It's friday, yeah! Make sure to recycle before that rave party you have going on!",
        "Saturday": "You woke up late from yesterday's rave, but you sure won't forget of that beach cleaning you have planned at 4, will you?",
        "Sunday": "Dude, your plants are screaming! Water them!"}

print ("Daily Green tip:", tips[current_day])