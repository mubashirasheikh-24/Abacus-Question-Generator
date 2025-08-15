import random

# Define the number sets based on the image
sets = {
    0: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    1: [-9, -8, -7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    2: [-9, -8, -7, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    3: [-9, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    4: [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    5: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5],
    6: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5],
    7: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 5, 8, 9, 4, 3],
    8: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 5, 7, 8, 9, 4, 3, 2],
    9: [-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 5, 6, 7, 8, 9, 4, 3, 2, 1]
}

# Function to generate a random 4-digit number
def generate_initial_number():
    return [random.randint(1, 9) for _ in range(4)]

# Function to follow the digit selection rule and perform sums with carry
def generate_next_sum(start_number):
    carry = 0
    result = []
    
    # Process each digit from right to left
    for i in reversed(range(len(start_number))):
        current_digit = start_number[i] + carry
        carry = 0  # Reset carry for each digit
        if current_digit >= 10 or current_digit <= -10:
            carry = current_digit // 10  # Handle carry-over for multi-digit sums
            current_digit = current_digit % 10  # Only keep the unit digit
        
        # Pick the next random number from the set based on the current last digit
        last_digit = current_digit
        random_number = random.choice(sets[abs(last_digit)])  # Avoid negative indexing
        new_sum = last_digit + random_number

        # Handle carry again if new_sum goes over 9 or below -9
        if new_sum >= 10 or new_sum <= -10:
            carry = new_sum // 10  # Handle carry-over for multi-digit sums
            new_sum = new_sum % 10
        
        result.insert(0, new_sum)  # Insert result at the front to build from right to left

    return result

# Generate a question with five steps
def generate_question():
    initial_number = generate_initial_number()  # Start with a random 4-digit number
    question_steps = [initial_number]  # Store each step of the question

    # Generate 4 more steps, each based on the previous sum
    for _ in range(4):
        next_step = generate_next_sum(question_steps[-1])
        question_steps.append(next_step)

    return question_steps

# Display the question
def display_question(question):
    question_str = ""
    for i, step in enumerate(question):
        step_str = ''.join(map(str, step))  # Convert each list to a string
        if i == 0:
            question_str += f"{step_str}"  # Start with the initial number
        else:
            question_str += f" => {step_str}"  # Show each subsequent step
    return question_str

# Main function to generate and display 10 questions
def generate_abacus_questions():
    print("Abacus Mental Maths Questions:\n")
    for i in range(10):
        question = generate_question()
        print(f"Question {i+1}: {display_question(question)}")
        print()

if __name__ == "__main__":
    generate_abacus_questions()
