from typing import List

# articles have already been preprocessed here
def build_vocabulary(documents : List[str]) :
    
    vocabulary = []
    for document in documents:
        vocabulary.append(word)
        for word in document:
            if not word in vocabulary:
                vocabulary.append(word)

    return vocabulary
        

