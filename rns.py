"""
** FORMAT **
email
---
first name
--- 
last name
---
How many days did "get after it" physically could be weights, yoga, HIIT whatever you do to break a sweat, including brisk walks (at least 10k steps per day)
0-7
Up before the Enemy- did you get up within 15 minutes of your pre-determined wake up time?? (make sure and avoid the dreaded "snooze")
0-7
How many days did you read more than 20 minutes non-professional reading to continue to cultivate your mind.	
0-7
Did you practice daily gratitude for this amazing life and world we inhabit- Prayer, meditation, journalling.  Whatever is your mindfulness practice make sure and track.
0-7
Did you prioritize and execute your top 3 daily critical tasks? 
0-7
The Plan is useless, but planning is priceless- Night before or early morning did you brain dump all open loops and time block out your day?
0-7
Did you avoid "junk" calories and follow your diet? Did you also consume enough liquids to fuel hydration throughout the day? 
0-7
"""

import streamlit as st
import datetime

def store_in_db():
    return


my_date = datetime.date.today()    
year, week_num, day_of_week = my_date.isocalendar()     

st.title("Week " + str(week_num) + " tracker")

# first user data
em = st.text_input(label="email")
fn = st.text_input(label="first name")
ln = st.text_input(label="last name")

# then tracker data
q1 = st.radio("How many days did \"get after it\" physically could be weights, yoga, HIIT whatever you do to break a sweat, including brisk walks (at least 10k steps per day)",
                      (0, 1, 2, 3, 4, 5, 6, 7))
q2 = st.radio("Up before the Enemy- did you get up within 15 minutes of your pre-determined wake up time?? (make sure and avoid the dreaded \"snooze\")",
                      (0, 1, 2, 3, 4, 5, 6, 7))
q3 = st.radio("How many days did you read more than 20 minutes non-professional reading to continue to cultivate your mind.",
                      (0, 1, 2, 3, 4, 5, 6, 7))
q4 = st.radio("Did you practice daily gratitude for this amazing life and world we inhabit- Prayer, meditation, journalling.  Whatever is your mindfulness practice make sure and track.",
                      (0, 1, 2, 3, 4, 5, 6, 7))
q5 = st.radio("Did you prioritize and execute your top 3 daily critical tasks? ",
                      (0, 1, 2, 3, 4, 5, 6, 7))
q6 = st.radio("The Plan is useless, but planning is priceless- Night before or early morning did you brain dump all open loops and time block out your day?",
                      (0, 1, 2, 3, 4, 5, 6, 7))
q7 = st.radio("Did you avoid \"junk\" calories and follow your diet? Did you also consume enough liquids to fuel hydration throughout the day? ",
                      (0, 1, 2, 3, 4, 5, 6, 7))

button = st.button("submit")
if button and em != "" and fn != "" and ln != "":
    final_answer = q1+q2+q3+q4+q5+q6+q7

    store_in_db({})




