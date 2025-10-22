### Project Overview



This project recommends movies based on their similarity in genres, keywords, cast, and crew.

The model uses Natural Language Processing (NLP) and cosine similarity to analyze textual metadata from the TMDB 5000 Movie Dataset and returns the most similar titles.

## Live Demo
Try the app online: [Movie Recommender System](https://movie-recommendation-system-dfjcccaarsraxulfvwj5sz.streamlit.app/)


### Features



Cleaned and merged TMDB 5000 Movies and Credits datasets.

Extracted key features: genres, keywords, cast, crew, and overview.

Created a single “tags” column combining all relevant movie information.

Used CountVectorizer for text vectorization and cosine similarity for recommendations.

Developed a Streamlit interface for easy user interaction.



### Dataset



TMDB 5000 Movie Dataset

tmdb\_5000\_movies.csv

tmdb\_5000\_credits.csv



### Technologies Used



Python 3

pandas, NumPy

scikit-learn (CountVectorizer, Cosine Similarity)

Streamlit

Pickle (for saving model data)



### How It Works



#### Data Preparation:



Combined movie and credits data using the movie title as the key.

Extracted genres, keywords, cast, and director information.

#### 

#### Feature Engineering:



Created a tags column combining overview, genres, keywords, cast, and crew.

Used CountVectorizer to convert text data into numerical vectors.



#### Similarity Calculation:



Computed cosine similarity scores between movie vectors.

#### 

#### Frontend (Streamlit):



User selects a movie from a dropdown menu.

The app displays the top 5 most similar movies.



### How to Run



#### Clone the repository



git clone https://github.com/rakshagithub/movie-recommendation-system.git

cd movie-recommendation-system



#### 

#### Install dependencies



pip install -r requirements.txt



Ensure the following files are in your project folder:

movie\_dict.pkl

similarity.pkl

app.py

Run the Streamlit app

streamlit run app.py

#### 

#### Use the app:



Select a movie from the dropdown.

Click “Recommend” to view similar movies.

### 

### Sample Output



Input: Gandhi

Output: Gandhi, My Father

&nbsp;       The Wind That Shakes the Barley

&nbsp;       A Passage to India

&nbsp;       Guiana 1838

&nbsp;       Ramanujan



### Files in This Project



#### File	       Description

website.py	          Streamlit frontend code

movie\_recommender.ipynb	  Notebook for data processing and model building

movie\_dict.pkl	Pickled   Movie metadata

similarity.pkl	Pickled   Cosine similarity matrix

requirements.txt	  List of dependencies

