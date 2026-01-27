import time
import random

sentences = [
    "Python programming is fun and powerful",
    "Artificial intelligence is shaping the future",
    "Practice makes a person perfect",
    "Data science is an exciting field",
    "Coding improves logical thinking"
]

sentence = random.choice(sentences)

print("⌨️ TYPING SPEED TEST")
print("-" * 40)
print("Type the following sentence exactly:\n")
print(f"👉 {sentence}")
print("\nPress ENTER when you are ready...")
input()

start_time = time.time()
typed_text = input("\nStart typing:\n")
end_time = time.time()

time_taken = end_time - start_time

# Speed calculation
words = len(sentence.split())
wpm = (words / time_taken) * 60

# Accuracy calculation
correct_chars = sum(1 for a, b in zip(sentence, typed_text) if a == b)
accuracy = (correct_chars / len(sentence)) * 100

print("\n📊 RESULTS")
print("-" * 40)
print(f"⏱️ Time Taken : {round(time_taken, 2)} seconds")
print(f"🚀 Speed      : {round(wpm, 2)} WPM")
print(f"🎯 Accuracy   : {round(accuracy, 2)}%")

# 🚨 Important feedback
if typed_text != sentence:
    print("\n⚠️ Warning: The sentence you typed does NOT match exactly!")
    print("Please try to type the sentence correctly for better accuracy.")
else:
    print("\n✅ Perfect! You typed the sentence correctly.")

