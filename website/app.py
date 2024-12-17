import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Title for the app
st.title("Top 50 Books with Posters")

# Load necessary data
similarity = pickle.load(open('similarity.pkl', 'rb'))
book_dict = pd.read_pickle('pt.pkl')
books = pd.DataFrame(book_dict)

def recommend(book) :
    index = np.where(books.index == book)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]

    recommended_book_posters = []
    recommended_book = []
    for i in similar_items :
        # book_id = movies.iloc[i[0]].movie_id
        recommended_book.append(books.index[i[0]])
        # recommended_book_posters.append(fetch_poster(movie_id))
    return recommended_book



# Load the data for popular books
try:
    data_dict = pd.read_pickle('popular.pkl')  # Update file path if necessary

    if isinstance(data_dict, dict):
        data = pd.DataFrame(data_dict)

        # Select box for choosing a book
        selected_book_name = st.selectbox('Select a book:', books.index)

        if 'Book-Title' in data.columns and 'Image-URL-M' in data.columns:
            # Check if user is on the "home" page or the "recommendation" page
            if 'page' not in st.session_state or st.session_state.page == "home":
                # Display the top 50 books page with images
                st.write("Top 50 Books")
                num_books = len(data)
                cols_per_row = 5  # Number of books per row

                for i in range(0, num_books, cols_per_row):
                    cols = st.columns(cols_per_row)
                    for col, (_, row) in zip(cols, data.iloc[i:i + cols_per_row].iterrows()):
                        with col:
                            st.image(row['Image-URL-M'], width=120, caption=row['Book-Title'])

                if st.button('Recommend'):
                    # When clicked, set page state to 'recommend' and show recommendations
                    st.session_state.page = "recommend"

            elif st.session_state.page == "recommend":
                # Display recommended books when the Recommend button is clicked
                st.write("Recommended Books")

                name = recommend(selected_book_name)

                col1, col2, col3, col4, col5 = st.columns(5)

                with col1:
                    st.text(name[0])
                    # st.image(posters[0])

                with col2:
                    st.text(name[1])
                    # st.image(posters[1])

                with col3:
                    st.text(name[2])
                    # st.image(posters[2])

                with col4:
                    st.text(name[3])
                    # st.image(posters[3])

                with col5:
                    st.text(name[4])
                    # st.image(posters[4])

                # for i in range(5):
                #     recommended_book = "Book Title " + str(i + 1)  # Replace with actual recommendations logic
                #     st.image("https://via.placeholder.com/120", width=120, caption=recommended_book)

                # Button to go back to the Top 50 Books page
                if st.button('Back to Top 50 Books'):
                    st.session_state.page = "home"

        else:
            st.error("The data does not contain 'Book-Title' or 'Image-URL-M' keys.")
    else:
        st.error("The loaded file is not a valid dictionary.")
except Exception as e:
    st.error(f"Error loading file: {e}")
