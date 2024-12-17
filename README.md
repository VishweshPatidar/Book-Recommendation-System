# Book Recommender System


This repository contains a Book Recommender System project implemented using Python. The project includes a machine learning-based recommendation model and a Streamlit interface to provide a user-friendly experience.


## Features

- Recommends books based on user input or similarity to a selected book.
- Interactive Streamlit web app for seamless interaction (there are several issues with it which could be resolved).
- Powered by machine learning for personalized recommendations.

## Repository Structure

- book-recommender.ipynb # Jupyter Notebook for development and experimentation
- app.py                   # Streamlit app for the recommender interface
- similarity.pkl           # Pre-trained similarity model
- popular_df.pkl         # Contains details of top50 books
- pt.pkl                # Contains all books name and user rating

## Installation

Clone the repository:

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```


## Usage
## Run the Streamlit App
```
streamlit run app.py
```

Navigate to the URL provided in the terminal (usually http://localhost:8501) to interact with the app.

## Notebook
You can explore the model development process by opening the book-recommender.ipynb notebook in Jupyter Notebook or JupyterLab:

```
jupyter notebook book-recommender.ipynb
```

## Notes
- Only names of recommended books are displayed, no posters.
- Code of app.py can be modified to achieve the same but remember pt.pkl doesn't contain poster details. 

## Technologies Used
- Python
- Streamlit for the web interface
- Pandas and NumPy for data manipulation
- Scikit-learn for building the recommendation model

## Future Improvements
- Deploy the Streamlit app online for broader accessibility.
- Integrate additional datasets to improve recommendation quality.
- Recommended books posters can be displayed for now only names are displayed.
