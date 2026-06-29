#!/usr/bin/python3
# Quest 13: The Maze of Many Choices
# Goal: Use if-elif-else to check multiple conditions for a grading program.

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs Improvement")
