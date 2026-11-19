Text Preprocessing Project
About the Project
This project is about text preprocessing for Information Retrieval.
The program takes raw English text and processes it in four steps:
Tokenization: Splits the text into words.
Normalization: Changes all letters to lowercase.
Stop Word Removal: Removes common words like "the", "is", and "of".
Stemming: Changes words to their root forms.
Tools
Python
NLTK
Regular Expressions
Project Files
main.py: The main Python code.
outputs.json: The final results of the three test texts.
How to Run
First, install NLTK:
pip install nltk
Then, run the program:
python main.py
The program processes all three texts and shows the final terms, Precision, Recall, extra terms, and missing terms.
The results are also saved in outputs.json.
Evaluation
The program compares its results with the Gold Standard to calculate Precision and Recall.
