"""
Creator: Tyler Stanton

44-608, Fundamentals of Data Analytics
Project 3 - Task 5

"""
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

def tuples():
    tupleA = (45, 34, 75, 34, 84)
    tupleB = (73, 15, 26, 52, 95)

    logger.info(f"tupleA = {tupleA}")
    logger.info(f"tupleB = {tupleB}")

    tupleAB = tupleA + tupleB

    tupleAAA = tupleA * 3


    logger.info(f"{tupleA = }")
    logger.info(f"{tupleB = }")
    logger.info(f"{tupleAB = }")
    logger.info(f"{tupleAAA = }")

def sets():
    setA = {45, 34, 75, 22, 84}
    setB = {73, 15, 26, 52, 95}

    logger.info(f"setA = {setA}")
    logger.info(f"setB = {setB}")

    setC = setA | setB

    setD = setA & setB

    setE = setA - setB

    greekAlphabet = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "alpha", "gamma"]
    setGreek = set(greekAlphabet)
    listAlphabetNoDuplicates = list(setGreek)
    listAlphabetNoDuplicates = [setGreek]

    logger.info(f"{listAlphabetNoDuplicates = }")
    logger.info(f'{setC = }')
    logger.info(f'{setD = }')
    logger.info(f'{setE = }')

def dictionaries():

    movieA_dict = {"name": "Quantumania", "date": "2/17/23", "Rotten_Tomatoes": 47}
    movieB_dict = {"name": "The Super Mario Bros Movie", "date": "4/5/2023", "Rotten_Tomatoes": 59}

    logger.info(f"movieA_dict = {movieA_dict}")
    logger.info(f"movieB_dict = {movieB_dict}")

    assessment_dict = {"low": 0, "medium": 1, "high": 2}
    logger.info(f"assessment_dict = {assessment_dict}")

    data_dict = {
        "name": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, 35, 40],
        "income": [50000, 60000, 70000, 80000],
    }
    logger.info(f"data_dict = {data_dict}")

    with open("text_simple.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info(f"Given text_simple.txt, the word_counts_dict = {word_counts_dict}")

    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    tuples()
    sets()
    dictionaries()

    show_log()