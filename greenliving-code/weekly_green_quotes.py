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