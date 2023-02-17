from analyze import analyze
from rephrase import rephrase

analyze([rephrase("one"), rephrase("what a day")])

def main():
    """
    Define the sentences to rephrase within rephrase_sents

    If rephrasing more than one prompt, analyzes the rephrasings (PCA visual, cosine-similarities)
    """
    rephrase_sents = [
        "I like to play sports but aren't good at them",
        "There are a lot of bears in these woods"
    ]

    rephrased = [rephrase(prompt) for prompt in rephrase_sents]

    if len(rephrase_sents) > 2:
        cosine_sims, repeats = analyze(rephrased)
        print(cosine_sims)
        print(repeats)


if __name__ == "__main__":
    main()

# Saved sentences for visuals
# Visual 2
# visualize_sentences([rephrase("It's hard for me to pay attention in physics class because I struggle to stay awake and understand his accent", print_sent=True),
#                      rephrase("I really admire him for his deductive reasoning skills, but he's a terrible person", print_sent=True),
#                      rephrase("There's been a lot of people taking about existential questions, like where do we go when we die?", print_sent=True)])

# Visual 3
# visualize_sentences([rephrase("I really admire the baseball team because of how well the teammates work together", print_sent=True),
#                      rephrase("I really love how all of my students are so collaborative", print_sent=True),
#                      rephrase("There are a lot of really confusing places in this town", print_sent=True)])







