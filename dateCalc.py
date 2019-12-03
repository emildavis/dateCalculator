#!/usr/bin/python

# dateCalc.py
# written for Python 3
# started June 19, 2019

# current version: 0 alpha
# current release date June 29, 2019
# Author: Emil Davis
# emil.davis@roadrunner.com


# This program will ask the user for a starting date in MMM DD YYYY formation
# Then ask the user for the end date in MMM DD YYYY format
# Example: Jan 08 2019

# This program will output:
# 125 days or 4 months and 3 days between the dates

# declare string variable to store the beginning date
beginDate=''
# declare string variable to store the ending date
endDate=''
# declare string variable to store if second date is in future or past
timeframe=''
# decalre list of months in the year
monthsOfYear=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# declare list of months which have 28 days
month28=['Feb']
# declare list of months which have 29 days
month29=['febLeap']
#declare list of months which have 30 days
month30=['Apr', 'Jun', 'Sep', 'Nov']
# declare list of months which have 31 days
month31=['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
# we could also create a lookup table with a dictionary
daysPerMonth={'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}

# define function to determine if a leap year. returns true or false (referenced pseudocode from wikipedia)
def isLeap(year):
	if year%4!=0:
		return False
	elif year%100!=0:
		return True
	elif year%400!=0:
		return False
	else:
		return True

# define function to determine if entries are the same, future, or past
def timeframe(start,end):
	if start<end:
		return 'future'
	if start==end:
		return 'same'
	if start>end:
		return 'past'

# define function to take the string inputted by the user and convert it to an int
# returns 13 if invalid month entered
def monthToNum(monthIn):
	monthNum=13
	if monthIn=='Jan':
		monthNum=1
	if monthIn=='Feb':
		monthNum=2
	if monthIn=='Mar':
		monthNum=3
	if monthIn=='Apr':
		monthNum=4
	if monthIn=='May':
		monthNum=5
	if monthIn=='Jun':
		monthNum=6
	if monthIn=='Jul':
		monthNum=7
	if monthIn=='Aug':
		monthNum=8
	if monthIn=='Sep':
		monthNum=9
	if monthIn=='Oct':
		monthNum=10
	if monthIn=='Nov':
		monthNum=11
	if monthIn=='Dec':
		monthNum=12
	return monthNum

print('Date Calculator')
print('#######################')

print('Enter the beginning date in the format MMM DD YYYY example: Jan 01 2019')
beginDate=input(' ')
print('Enter the end date in the format MMM DD YYYY example: Dec 31 2019')
endDate=input(' ')

#knock out the case where they enter the same date twice:
if beginDate==endDate:
	print('0 days between, they are the same date.')
	raise SystemExit
		  
# lets store the user inputted values seperatelly
beginMonth=beginDate[:3]
beginDay=beginDate[4:6]
beginYear=beginDate[7:11]
endMonth=endDate[:3]
endDay=endDate[4:6]
endYear=endDate[7:11]

# we need to convert all to int
beginDay=int(beginDay)
endDay=int(endDay)
beginYear=int(beginYear)
endYear=int(endYear)
# call the function monthToNum to change the calendar month to an int 1-12
beginMonthNum=monthToNum(beginMonth)
endMonthNum=monthToNum(endMonth)

# ok let's check if we are in the same year or not (returns "past", "same", or "future")
yearTimeframe=timeframe(beginYear,endYear)

# let's knock out the simple case, same year:
if yearTimeframe=='same':
	if beginMonth==endMonth:
		if endDay>beginDay:
			daysBetween=endDay-beginDay
			print('There are ',daysBetween,' days between between ',beginDate,'and',endDate)
			raise SystemExit
		else:
			daysBetween=beginDay-endDay
			print('There are ',daysBetween,' days between between ',beginDate,'and',endDate)
			raise SystemExit
	if monthToNum(beginMonth)<monthToNum(endMonth):
		monthsBetween=monthToNum(endMonth)-monthToNum(beginMonth)
		
