# Semantic Similarity Analysis

This Python script demonstrates the calculation of semantic similarity between tokens and sentences using the spaCy library.

## Requirements

- Python 3.x
- spaCy

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>

2. Install required dependecies
    pip install -r requirements.txt

## Usage

1. Open the semantic.py file in your preferred Python editor.

2. Run the script:
   python semantic.py
## Functionality

1.Token Similarity:

 -The script loads the English language model using spaCy.
 - It tokenizes the input text, 'Nigeria Country'.
 - It calculates the similarity between each pair of tokens and displays the results.

2. Sentence Comparison:

 -The script defines a reference sentence, 'Why is my cat on the car'.
 - It compares the similarity of this reference sentence with a list of sentences.
 - It displays the similarity score for each sentence.

## Interesting Observations
After comparing the similarities between "cat", "monkey", and "banana", the following observations were made:

Cat vs. Monkey:

The similarity score between "cat" and "monkey" may indicate some level of conceptual overlap or semantic association.
This could be due to both being animals or sharing certain characteristics.
Cat vs. Banana:

The similarity score between "cat" and "banana" is expected to be relatively low since they belong to different semantic categories and have distinct features.
Monkey vs. Banana:

The similarity score between "monkey" and "banana" might be higher than expected due to potential associations such as monkeys being known to consume bananas or the shared context of tropical environments.
Notes on Model Differences
The 'en_core_web_sm' model used in this script is smaller in size, resulting in lower resource requirements and faster processing times.
However, this smaller model may have a more limited vocabulary and coverage, potentially leading to reduced accuracy and coverage of specialized linguistic patterns or entities.
On the other hand, the 'en_core_web_md' model is larger, offering a broader vocabulary and better coverage of linguistic data, resulting in higher accuracy.
However, it comes with increased computational requirements and slower processing times.
The choice between the two models depends on the specific needs of the application, balancing trade-offs between speed, accuracy, vocabulary coverage, and resource constraints.
