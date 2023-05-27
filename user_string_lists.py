"""
Creator: Tyler Stanton

44-608, Fundamentals of Data Analytics
Project 3 - Task 4

"""

# imports first
import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# reusable functions next

list_place = ["first", "second", "third", "forth", "fifth", "sixth"]
list_title = ["runner", "swimmer", "biker", "fighter", "team", "gymnist"]
list_adjective = ["trained", "lifted", "partied", "ran", "slept", "rested"]
list_adverb = ["tirelessly", "never", "occasionally", "consistently", "variously", "rarely"]

for A, B, C in zip(list_place, list_title, list_adjective):
    tupleABC = (list_place, list_title, list_adjective)
    print(f'listA={A}; listB={B}; listC={C}')

def create_random_sentence():

    logger.info("Calling create_random_sentence()")

    # Create a random sentence
    sentence = (
        f"The {random.choice(list_place)} place {random.choice(list_title)} "
        f"{random.choice(list_adjective)} {random.choice(list_adverb)}."
    )

    logger.info(f"Random sentence: {sentence}")

def process_text_betty():
    """Read in betty.txt and process it"""
    logger.info("Calling process_text_betty()")

    # read in betty to get a list of words
    with open("betty.txt", "r") as fileObject:
        text = fileObject.read()
        separate_words = text.split()  # split on whitespace
        unique_words = set(separate_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_total = len(separate_words)

        logger.info(f"The list of words is: {separate_words}")
        logger.info(f"There are {word_total} words in the file.")

        # Print the count and list of unique words
        unique_word_total = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_total} unique words in the file.")



# call functions and execute code
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    create_random_sentence()
    create_random_sentence()
    process_text_betty()



