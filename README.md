Text Preprocessing Project

About the Project

This project is about text preprocessing for Information Retrieval.
The program takes raw English text and processes it in four steps:
Tokenization: Splits the text into words.
Normalization: Changes all letters to lowercase.
Stop Word Removal: Removes common words like "the", "is", and "of".
Stemming: Changes words to their root forms.

Tools:
Python
NLTK
Regular Expressions

Project Files:
main.py: The main Python code.
outputs.json: The final results of the three test texts.
README.md: Project information and instructions.

Requirements:
Python 3
NLTK library

How to Run:
1. Make sure Python is installed on your computer.
2. Open a terminal in the project folder.
3. Install NLTK by running this command:
pip install nltk

Run the program:
python main.py
The program automatically processes all three sample texts.
It shows the final terms, Precision, Recall, extra terms, and missing terms in the terminal.
The final results are also saved in outputs.json.

Evaluation
The program compares its results with the Gold Standard to calculate Precision and Recall.
