import time
import pyttsx3
import math

def show_disclaimer():
    print("""
⚠️  Caution!
This calculator uses a text-to-speech engine.
To use it smoothly, you need to install the required TTS library.

📦 Installation Command:
pip install pyttsx3

The program will continue in 10 seconds...
""")
    time.sleep(10)

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculator():
    speak("Welcome to the calculator. You can enter your expression now.")
    print("Examples: 5 + 3 | 10 / 2 | sqrt 25 | prime 7")
    print("Memory: m1+, m1-, m1r, m1c | m2+, m2-, m2r, m2c")
    print("Type 'exit' to quit.")

    memory1 = 0.0
    memory2 = 0.0
    last_result = 0.0

    while True:
        user_input = input("\nEnter your calculation: ").strip().lower()

        if user_input == 'exit':
            speak("This calculator is developed by Dr. Vedprakash Sharma.")
            print("Exiting calculator.")
            break

        # ---- MEMORY COMMANDS ----
        if user_input in ['m1+', 'm1-', 'm1*', 'm1/',   'm1r', 'm1c',
                          'm2+', 'm2-', 'm2*', 'm2/', 'm2r', 'm2c']:

            if user_input == 'm1+':
                memory1 += last_result
                speak("Memory one updated")
                print(f"🧠 Memory-1 = {memory1}")

            elif user_input == 'm1-':
                memory1 -= last_result
                speak("Memory one updated")
                print(f"🧠 Memory-1 = {memory1}")

            elif user_input == 'm1*':
                memory1 *= last_result
                speak("Memory one updated")
                print(f"🧠 Memory-1 = {memory1}")

            elif user_input == 'm1/':
                memory1 /= last_result
                speak("Memory one updated")
                print(f"🧠 Memory-1 = {memory1}")

            elif user_input == 'm1r':
                speak(f"Memory one is {memory1}")
                print(f"🧠 Memory-1 Recall: {memory1}")

            elif user_input == 'm1c':
                memory1 = 0.0
                speak("Memory one cleared")
                print("🧠 Memory-1 cleared")

            elif user_input == 'm2+':
                memory2 += last_result
                speak("Memory two updated")
                print(f"🧠 Memory-2 = {memory2}")

            elif user_input == 'm2-':
                memory2 -= last_result
                speak("Memory two updated")
                print(f"🧠 Memory-2 = {memory2}")

            elif user_input == 'm2*':
                memory2 *= last_result
                speak("Memory two updated")
                print(f"🧠 Memory-2 = {memory1}")

            elif user_input == 'm2/':
                memory2 /= last_result
                speak("Memory two updated")
                print(f"🧠 Memory-2 = {memory2}")

            elif user_input == 'm2r':
                speak(f"Memory two is {memory2}")
                print(f"🧠 Memory-2 Recall: {memory2}")

            elif user_input == 'm2c':
                memory2 = 0.0
                speak("Memory two cleared")
                print("🧠 Memory-2 cleared")

            continue

        parts = user_input.split()

        # ---- BASIC OPERATIONS ----
        if len(parts) == 3:
            try:
                num1 = float(parts[0])
                operator = parts[1]
                num2 = float(parts[2])
            except ValueError:
                speak("Invalid input.")
                print("❌ Invalid format. Example: 5 + 3")
                continue

            if operator == '+':
                last_result = num1 + num2
            elif operator == '-':
                last_result = num1 - num2
            elif operator == '*':
                last_result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    speak("Division by zero is not allowed.")
                    print("❌ Division by zero.")
                    continue
                last_result = num1 / num2
            else:
                speak("Unsupported operator.")
                print("❌ Unsupported operator.")
                continue

            speak(f"The result is {last_result}")
            print(f"✅ Result: {last_result}")

        # ---- SPECIAL OPERATIONS ----
        elif len(parts) == 2:
            operator, num_str = parts
            try:
                num1 = float(num_str)
            except ValueError:
                speak("Invalid number.")
                print("❌ Invalid number.")
                continue

            if operator == 'sqrt':
                if num1 < 0:
                    speak("Negative number not allowed.")
                    print("❌ Negative number.")
                    continue
                last_result = math.sqrt(num1)
                speak(f"The square root is {last_result}")
                print(f"✅ Result: {last_result}")

            elif operator == 'prime':
                if not num1.is_integer():
                    speak("Prime check only for integers.")
                    print("❌ Only integers allowed.")
                    continue
                last_result = int(is_prime(int(num1)))
                if last_result:
                    speak("It is a prime number.")
                    print("✅ Prime number")
                else:
                    speak("It is not a prime number.")
                    print("❌ Not a prime number")

            else:
                speak("Unsupported operation.")
                print("❌ Unsupported operation.")

        else:
            speak("Invalid input format.")
            print("❌ Invalid format.")

if __name__ == "__main__":
    show_disclaimer()
    calculator()
