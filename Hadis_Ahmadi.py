import re
import json
from nltk.stem import PorterStemmer


stemmer = PorterStemmer()

STOP_WORDS = {
    "the", "of", "to", "a", "an", "is", "are",
    "was", "were", "and", "or", "but", "in",
    "on", "at", "for", "this", "that", "he",
    "she", "it", "they", "we", "you", "i",
    "me", "my", "your", "his", "her", "their",
    "our", "with", "from", "by", "as"
}


def tokenize(text):
    text = re.sub(r"(?i)(?<=\w)['’]s\b", "", text)
    pattern = r"(?:[A-Za-z]\.){2,}|[A-Za-z]+(?:-[A-Za-z]+)*"
    return re.findall(pattern, text)


def normalize(tokens):
    normalized = []

    for token in tokens:
        token = token.lower()
        token = token.replace(".", "")
        normalized.append(token)

    return normalized


def remove_stop_words(tokens):
    return [token for token in tokens if token not in STOP_WORDS]


def apply_stemming(tokens):
    stemmed = []

    for token in tokens:
        if "-" in token:
            stemmed.append(token)
        else:
            stemmed.append(stemmer.stem(token))

    return stemmed

def preprocess(text):
    tokens = tokenize(text)
    tokens = normalize(tokens)
    tokens = remove_stop_words(tokens)
    tokens = apply_stemming(tokens)
    return tokens


texts = {
    "text1": "Friends, Romans, countrymen, lend me your ears;",
    "text2": (
        "John's new U.S.A. laptop is a state-of-the-art device. "
        "The price is high, but the quality is amazing!"
    ),
    "text3": (
        "The authorization for this authorized project is pending. "
        "He authorizes the payments regularly."
    ),
}

gold_standard = {
    "text1": ["friend", "roman", "countrymen", "lend", "ear"],
    "text2": [
        "john", "new", "usa", "laptop", "state-of-the-art",
        "devic", "price", "high", "qualiti", "amaz"
    ],
    "text3": [
        "author", "project", "pend", "author",
        "author", "payment", "regularli"
    ],
}


def evaluate(output, gold):
    output_set = set(output)
    gold_set = set(gold)

    correct = output_set & gold_set
    extra_terms = output_set - gold_set
    missing_terms = gold_set - output_set

    precision = len(correct) / len(output_set) if output_set else 0
    recall = len(correct) / len(gold_set) if gold_set else 0

    return precision, recall, sorted(extra_terms), sorted(missing_terms)


def main():
    outputs = {}

    print("=" * 60)
    print("TEXT PREPROCESSING AND INFORMATION RETRIEVAL")
    print("=" * 60)

    for text_id, original_text in texts.items():
        processed_terms = preprocess(original_text)
        outputs[text_id] = processed_terms

        precision, recall, extra, missing = evaluate(
            processed_terms, gold_standard[text_id]
        )

        print(f"\n{text_id.upper()}")
        print("-" * 40)
        print("Original text:", original_text)
        print("Processed terms:", processed_terms)
        print(f"Precision: {precision:.2f}")
        print(f"Recall: {recall:.2f}")
        print("Extra terms:", extra)
        print("Missing terms:", missing)

    with open("outputs.json", "w", encoding="utf-8") as file:
        json.dump(outputs, file, indent=4, ensure_ascii=False)

    print("\nResults saved in outputs.json")


if __name__ == "__main__":
    main()
