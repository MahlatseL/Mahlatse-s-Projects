
from random import choice

# Mahlatse Lebelo's Automated Decision Making Code
subjects = ['Taxation', 'Financial Accounting', 'Management Accounting', 'Auditing']

# Input subject and performance
print('Enter the subject:')
subject = input()
print(f'Enter the performance for {subject} (out of 100):')
performance = int(input())

# Check performance against the selected subject
if performance <= 49:
    print(f'Your performance in {subject} is below expectations. Consider studying {subject}.')
else:
    print(f'Your performance in {subject} is satisfactory.')

# Additional random subject suggestion
print(f'You can also study {choice(subjects)} to enhance your skills.')
