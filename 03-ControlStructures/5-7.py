import time

word_map = {
    5 : "five",
    4 : "four",
    3 : "three",
    2 : "two", 
    1 : "one",
}
countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown >= 1 and countdown <= 5:
        print(f"{word_map[countdown]} ")
    else:
        print(f"{countdown}")
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")