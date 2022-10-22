from nltk.tokenize import sent_tokenize

def create_paraphrase(parrot_model, text, adequacy_threshold = 0.75, fluency_threshold = 0.90, diversity_ranker="levenshtein"):
    print("Tokenising text.........")
    sentences = list(sent_tokenize(text))
    new_text = ""
    print("Creting paraphrased text for each sentence.........")
    for sentence in sentences:
        dif_sentences = parrot_model.augment(input_phrase=sentence, diversity_ranker=diversity_ranker,adequacy_threshold = adequacy_threshold, fluency_threshold = fluency_threshold)
        
        if dif_sentences != None:
            kept_sentence = dif_sentences[0][0].capitalize()
            kept_sentence = kept_sentence.capitalize()
            kept_sentence = kept_sentence+". "
            new_text = new_text + kept_sentence

    return new_text