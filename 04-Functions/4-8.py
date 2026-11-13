import time

def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"

    elif time_format == '12':
        suffix = 'am' if hours < 12 else 'pm'

        if hours == 0:
            h12 = 12
        elif hours > 12:
            h12 = hours - 12
        else:
            h12 = hours   

        return f"{h12}:{minutes:02d}{suffix}"
    
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
time_format = input("Enter time format (24/12): ")

print(time_string(hours, minutes, time_format))
