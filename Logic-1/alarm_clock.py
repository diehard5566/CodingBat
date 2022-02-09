# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
# return a string of the form "7:00" indicating when the alarm clock should ring. 
# Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
# Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off"

# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

def alarm_clock(day, vacation):
    if vacation == True and (day == 6 or day == 0):
        return "off"
    if vacation == True and day in range(1, 6):
        return "10:00"
    if vacation == False and (day == 6 or day == 0):
        return "10:00"
    if day in range(1, 6):
        return "7:00"

print(alarm_clock(1, False) == '7:00')
print(alarm_clock(6, True) == 'off')
print(alarm_clock(2, True) == '10:00')
print(alarm_clock(3, False) == '7:00')

#更簡潔的寫法
# def alarm_clock(day, vacation):
#   week_preset = "7:00" if not vacation else "10:00"
#   weekend_preset = "10:00" if not vacation else "off"
#   return week_preset if day not in [6,0] else weekend_preset