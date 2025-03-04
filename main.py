import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Read the input text
with open("data/sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text
doc = nlp(text)

# Extract and print named entities
print("Named Entities, Phrases, and Concepts:")
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")
