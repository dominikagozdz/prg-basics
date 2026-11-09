import time
seconds = int(input("Enter number of seconds to count down from: "))
word_map = {
    5 : "five",
    4 : "four",
    3 : "three",
    2 : "two", 
    1 : "one",
}
for i in range(seconds, -1, -1):
    if i in word_map:
        print(word_map[i])
    else:
        print(i)
    time.sleep(1)