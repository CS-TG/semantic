import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Tokenize the input text
tokens = nlp('Nigeria Country')

# Calculate similarity between tokens
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Sentence comparison
sentence_to_compare = "Why is my cat on the car"
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(f"{sentence} - Similarity: {similarity}")

'''
After comparing the similarities between "cat", "monkey", and "banana", I found the following interesting observations:

    1.Cat vs. Monkey: The similarity score between "cat" and "monkey" may indicate some level of conceptual     overlap or semantic association. This could be due to both being animals or sharing certain characteristics.

    2.Cat vs. Banana: The similarity score between "cat" and "banana" is expected to be relatively low since they belong to different semantic categories and have distinct features.

    3.Monkey vs. Banana: The similarity score between "monkey" and "banana" might be higher than expected due to potential associations such as monkeys being known to consume bananas or the shared context of tropical environments.

'''

'''
The 'en_core_web_sm' model is smaller in size, resulting in lower resource requirements and faster processing times. However, this smaller model may have a more limited vocabulary and coverage, potentially leading to reduced accuracy and coverage of specialized linguistic patterns or entities. On the other hand, the 'en_core_web_md' model is larger, offering a broader vocabulary and better coverage of linguistic data, resulting in higher accuracy. However, it comes with increased computational requirements and slower processing times. The choice between the two models depends on the specific needs of the application, balancing trade-offs between speed, accuracy, vocabulary coverage, and resource constraints.
'''

