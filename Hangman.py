import random
from sys import exit
var1 = """Better
Beyond
Bishop
Border
Bottle
Bottom
Bought
Branch
Breath
Bridge
Bright
Broken
Budget
Burden
Bureau
Button
Camera
Cancer
Cannot
Carbon
Career
Castle
Casual
Caught
Center
Centre
Chance
Change
Charge
Choice
Choose
Chosen
Church
Circle
Client
Closed
Closer
Coffee
Column
Combat
Coming
Common
Comply
Copper
Corner
Costly
County
Couple
Course
Covers
Create
Credit
Crisis
Custom
Damage
Danger
Dealer
Debate
Decade
Decide
Defeat
Defend
Define
Degree
Demand
Depend
Deputy
Desert
Design
Desire
Detail
Detect
Device
Differ
Dinner
Direct
Doctor
Dollar
Domain
Double
Driven
Driver
During
Easily
Eating
Editor
Effect
Effort
Eighth
Either
Eleven
Emerge
Empire
Employ
Enable
Ending
Energy
Engage
Engine
Enough
Ensure
Entire
Entity
Equity
Escape
Estate
Ethnic
Exceed
Except
Excess
Expand
Expect
Expert
Export
Extend
Extent
Fabric
Facing
Factor
Failed
Fairly
Fallen
Family
Famous
Father
Fellow
Female
Figure
Filing
Finger
Finish
Fiscal
Flight
Flying
Follow
Forced
Forest
Forget
Formal
Format
Former
Foster
Fought
Fourth
French
Friend
Future
Garden
Gather
Gender
German
Global
Golden
Ground
Growth
Guilty
Handed
Handle
Happen
Hardly
Headed
Health
Height
Hidden
Holder
Honest
Impact
Import
Income
Indeed
Injury
Inside
Intend
Intent
Invest
Island
Itself
Jersey
Joseph
Junior
Killed
Labour
Latest
Latter
Launch
Lawyer
Leader
League
Leaves
Legacy
Length
Lesson
Letter
Lights
Likely
Linked
Liquid
Listen
Little
Living
Losing
Lucent
Luxury
Mainly
Making
Manage
Manner
Manual
Margin
Marine
Marked
Market
Martin
Master
Matter
Mature
Medium
Member
Memory
Mental
Merely
Merger
Method
Middle
Miller
Mining
Minute
Mirror
Mobile
Modern
Modest
Module
Moment
Morris
Mostly
Mother
Motion
Moving
Murder
Museum
Mutual
Myself
Narrow
Nation
Native
Nature
Nearby
Nearly
Nights
Nobody
Normal
Notice
Notion
Number
Object
Obtain
Office
Offset
Online
Option
Orange
Origin
Output
Oxford
Packed
Palace
Parent
Partly
Patent
People
Period
Permit
Person
Phrase
Picked
Planet
Player
Please
Plenty
Pocket
Police
Policy
Prefer
Pretty
Prince
Prison
Profit
Proper
Proven
Public
Pursue
Raised
Random
Rarely
Rather
Rating
Reader
Really
Reason
Recall
Recent
Record
Reduce
Reform
Regard
Regime
Region
Relate
Relief
Remain
Remote
Remove
Repair
Repeat
Replay
Report
Rescue
Resort
Result
Retail
Retain
Return
Reveal
Review
Reward
Riding
Rising
Robust
Ruling
Safety
Salary
Sample
Saving
Saying
Scheme
School
Screen
Search
Season
Second
Secret
Sector
Secure
Seeing
Select
Seller
Senior
Series
Server
Settle
Severe
Sexual
Should
Signal
Signed
Silent
Silver
Simple
Simply
Single
Sister
Slight
Smooth
Social
Solely
Sought
Source
Soviet
Speech
Spirit
Spoken
Spread
Spring
Square
Stable
Status
Steady
Stolen
Strain
Stream
Street
Stress
Strict
Strike
String
Strong
Struck
Studio
Submit
Sudden
Suffer
Summer
Summit
Supply
Surely
Survey
Switch
Symbol
System
Taking
Talent
Target
Taught
Tenant
Tender
Tennis
Thanks
Theory
Thirty
Though
Threat
Thrown
Ticket
Timely
Timing
Tissue
Toward
Travel
Treaty
Trying
Twelve
Twenty
Unable
Unique
United
Unless
Unlike
Update
Useful
Valley
Varied
Vendor
Versus
Victim
Vision
Visual
Volume
Walker
Wealth
Weekly
Weight
Wholly
Window
Winner
Winter
Within
Wonder
Worker
Wright
Writer
Yellow"""
word = ""
thislist = var1.split()
word = thislist[random.randrange(0,len(thislist)-1)]
a = "_"
b = "_"
c = "_"
d = "_"
e = "_"
f = "_"
lives = 7
guesses = 0
flag = False
guessed = []
welcome = input("Welcome to Hangman! Type anything to begin.")
if welcome == "":
    exit(0)
def Guess():
    flag = False
    p = 0
    global guesses
    global guessed
    global lives
    global a
    global b
    global c
    global d
    global e
    global f
    found = False
    while p == 0:
        inputs = input("What would you like to guess?")
        if inputs == "ex":
            exit(0)
        if inputs == "letters":
            print(", ".join(guessed))
            flag = True
            break
        if len(inputs) == 1:
            p = 1
            guesses += 1
        else: 
            print("Please enter 1 character only") 
    if flag == False:
        if inputs in guessed:
            print("You already guessed that.") 
        else:
            guessed.append(inputs)      
            if inputs.lower() == word[0].lower():
                a = word[0]
                found = True
            if inputs.lower() == word[1].lower():
                b = word[1]
                found = True
            if inputs.lower() == word[2].lower():
                c = word[2]
                found = True
            if inputs.lower() == word[3].lower():
                d = word[3]
                found = True
            if inputs.lower() == word[4].lower():
                e = word[4]
                found = True
            if inputs.lower() == word[5].lower():
                f = word[5]
                found = True
            
            print(a + b + c + d + e + f)
            
            if "_" not in (a, b, c, d, e, f):
                print(f"Congratulations! You won in {guesses} guesses!")
                exit(0)
            if found == False:
                lives -= 1
                print(f"No {inputs.upper()}, you have {lives} left.")
            if lives < 1:
                print(f"You lose! The word was {word}. Good try!")
                exit(0)
    Guess()

    


    

    
Guess()
