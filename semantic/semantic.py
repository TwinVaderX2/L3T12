# import models and load language model in spacy
import spacy
nlp = spacy.load('en_core_web_md')
# nlp = spacy.load('en_core_web_sm')

# create tokens that need to be compare for similarity
tokens = nlp('cat apple monkey banana ')

# iterate through each token in sequence and compare to each of the words/tokens in the sequence
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""
    Output (with en_core_web_md):
        cat cat 1.0
        cat apple 0.2036806046962738
        cat monkey 0.5929930210113525
        cat banana 0.2235882580280304
        apple cat 0.2036806046962738
        apple apple 1.0
        apple monkey 0.2342509925365448
        apple banana 0.6646699905395508
        monkey cat 0.5929930210113525
        monkey apple 0.2342509925365448
        monkey monkey 1.0
        monkey banana 0.4041501581668854
        banana cat 0.2235882580280304
        banana apple 0.6646699905395508
        banana monkey 0.4041501581668854
        banana banana 1.0
"""

"""
    Observations made with en_core_web_md:
    Regardless of the first token the similarity between two tokens remain the same, example:
    apple banana 0.6646699905395508
    banana apple 0.6646699905395508
        This means that it is not necessary to re-test once two tokens have been compared to know the similarity value

    monkey vs cat and banana vs apple have the two highest similarity values
        This indicates that if tokens/words fall within the same category, they carry a higher similarity value
        In addition, if two tokens share more than one category/ sub category, the similarity is increased, i.e. cats
        and monkeys are both animals/ mamals but are not found in the same sub-species of mamal/ family tree, while bananas and
        apples are both clasified as fruit, can be harvested from trees and are associated with tropical fruits, thus has a higher 
        similarity rating
"""

"""
    Output (with en_core_web_sm)
    cat apple 0.7018378973007202
    cat monkey 0.6455236077308655
    cat banana 0.2214718759059906
    apple cat 0.7018378973007202
    apple apple 1.0
    apple monkey 0.7389943599700928
    apple banana 0.36197030544281006
    monkey cat 0.6455236077308655
    monkey apple 0.7389943599700928
    monkey monkey 1.0
    monkey banana 0.4232020080089569
    banana cat 0.2214718759059906
    banana apple 0.36197030544281006
    banana monkey 0.4232020080089569
    banana banana 1.0
"""

"""
    Observations (made with en_core_web_sm):

    Most notably token comparisons that should have a higher similarity value, such as apple and banana have a much lower
    value than with the larger language model, which results in inaccurate output/data

    It is recommended that the larger language model (en_core_web_md) be utilized when running similarity function
"""