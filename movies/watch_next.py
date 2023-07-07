"""
SE L3T12 - Semantic Similarity (NLP)

Author: Phillip van Staden

Date: 06-07-2023

Task:
    Let us build a system that will tell you what to watch next based on the word
    vector similarity of the description of movies.
        ●   Create a file called watch_next.py
        ●   Read in the movies.txt file. Each separate line is a description of a different
            movie.
        ●   Your task is to create a function to return which movies a user would watch
            next if they have watched Planet Hulk with the description “Will he save
            their world or destroy it? When the Hulk becomes too dangerous for the
            Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
            planet where the Hulk can live in peace. Unfortunately, Hulk land on the
            planet Sakaar where he is sold into slavery and trained as a gladiator.”
        ●   The function should take in the description as a parameter and return the
            title of the most similar movie.
        ●   Host your solution on a Git host such as GitLab or GitHub with a Dockerfile
            and instructions to run included.
"""

# import module and language model
import spacy
nlp = spacy.load('en_core_web_md')

def movie_list(data):
    '''
        Function reads data from .txt file and splits into two lists: 1. movie titles and 2. discriptions

        Input:
            data: STRING
            parameter: discription of file name to be opened

        Return:
            movie_title_list: LIST
            list of movie titles
            movie_descript_list: LIST
            list of movie descriptions
    '''
    
    # set variables
    movie_list_raw = []
    movie_title_list = []
    movie_descript_list = []

    # import list of movies and discriptions from .txt file in directory
    with open(data,'r') as f:
        for line in f:
            movie_list_raw.append(line.strip('\n'))

    # split raw data
    for idx in movie_list_raw:
        movie_title_list.append(idx.split(" :")[0])
        movie_descript_list.append(idx.split(" :")[1])

    return movie_title_list, movie_descript_list

# call function to set variables
movie_title_list, movie_description_list = movie_list('movies.txt')

# control variable
planet_hulk = """
                “Will he save their world or destroy it? When the Hulk becomes too dangerous for the
                Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet 
                where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where 
                he is sold into slavery and trained as a gladiator.”
            """

def recommendation(movie_description,movie_title_list,movie_descript_list):
    '''
        Function returns recommendation for next movie based on description of last movie seen.

        Input:
        movie_description: STRING
        Parameter: string that describes the last movie viewed by the user

        movie_title_list: LIST
        Parameter: list of movies from which the recommendation needs to be made

        movie_descript_list: LIST
        Parameter: list of descriptions for movies that can be recommended

        RETURN: recommendation
        Parameter: This is the recommendation of movie to be wathced by the user based on the input provided
    '''
    # set variable
    recommendation = ''

    # tokenize list of descriptions
    token_list = []

    for idx in movie_descript_list:
        doc = nlp(idx)
        token_list.append(doc)

    # tokenize movie_description
    test_token = nlp(movie_description)

    # find token with highest similarity value and return postion in list
    # use position in list to assign recommendation
    highest_score = 0.0
    for idx in token_list:
        if test_token.similarity(idx) > highest_score:
            highest_score = test_token.similarity(idx)
            recommendation = movie_title_list[token_list.index(idx)]

    return recommendation

print(f'Based on your last movie, we recommend that you watch, {recommendation(planet_hulk,movie_title_list,movie_description_list)} next.')