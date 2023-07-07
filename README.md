# SE L3T12 - Semantic Similarity (NLP)
This task is part of a distance learning program offered by Hyperiondev.com
Purpose of the task is to expand on the uses of NLP (Natural Language Processing) by illustrating the use of similarity function of spacy.

### TASK
#### Compulsory Task 1
Follow these steps:
* Create a file called semantic.py and run all the code extracts above.
* Write a note about what you found interesting about the similarities between cat, monkey and banana and think of an example of your own.
* Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on what you notice is different from the model 'en_core_web_md'.
* Host your solution on a Git host such as GitLab or GitHub with a Dockerfile and instructions to run included.
* If it doesn’t already, please ensure that your repo includes a file named requirements.txt to automate the installation of the project’s requirements.
    * Remember to exclude any venv or virtualenv files from your repo.
* Add the link for your remote Git repo to a text file named semantic_similarity.txt

#### Compulsory Task 2
Let us build a system that will tell you what to watch next based on the word vector similarity of the description of movies.
* Create a file called watch_next.py
* Read in the movies.txt file. Each separate line is a description of a different movie.
* Your task is to create a function to return which movies a user would watch next if they have watched Planet Hulk with the description “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”
* The function should take in the description as a parameter and return the title of the most similar movie.
* Host your solution on a Git host such as GitLab or GitHub with a Dockerfile and instructions to run included.
    * If it doesn’t already, please ensure that your repo includes a file named requirements.txt to automate the installation of the project’s requirements.
    * Remember to exclude any venv or virtualenv files from your repo.
* Add the link for your remote Git repo to your semantic_similarity.txt file.

## Running the programs locally
### Requirements
* Python
### Installation
1. Clone repository
2. create virtual environment (command: python -m venv [name of virtual environment])
3. activate virtual environment (command: [name of virtual] environment/scripts/activate)
4. install requirements from requirements.txt in subfolder: cd into directory (either semantic or movies); run command: python -m pip install -r requirements.txt

### Running the program
#### semantic
1. cd into directory (semantic)
2. run command: python semantic.py

#### watch_next
1. cd into directory (movies)
2. run command: python watch_next.py

## Running the programs using Docker
### Requirements
* Docker Desktop
* Docker Hub account

### Installation (semantic)
1. Clone repository
2. cd into directory (semantic)
2. run command: docker build -t [name of image] .
    This will create an image for the semantic python program; if successful the image will appear on the Docker Desktop app

### Installation (watch_next)
1. Clone repository
2. cd into directory (movies)
2. run command: docker build -t [name of image] .
    This will create an image for the semantic python program; if successful the image will appear on the Docker Desktop app

### Running the program
Docker images can be run from any directory
#### semantic
1. run command: docker run [name of image]

#### watch_next
1. run command: docker run [name of image]