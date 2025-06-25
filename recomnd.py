import streamlit as st
import pickle
import numpy as np

#load all required pkl files
books = pickle.load(open('books.pkl','rb'))
pivot_table = pickle.load(open('pivot_table.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))
#convert it into list
book_title = pivot_table.index.tolist()

#create a recommendation function for dynamic book selection/chossing
def recommend(select_book_name):
    # fetch index
    index = np.where(pivot_table.index == select_book_name)[0][0]
    similar_item = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_item:
        item = []
        temp_df = books[books['Book-Title'] == pivot_table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return data


def app():

    st.title("Recommend Books")
    st.subheader("This Is Collaborative Filtering Based Recommender System")
    #create a selectbox for choosing or typing books for search
    select_book_name = st.selectbox("Type or select book from dropdown",book_title,)

    if st.button("Recommend"):
        recommendations = recommend(select_book_name)
        # creating 5 blocks for 5 recommendations
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            #book poster
            st.image(str(recommend(select_book_name)[0][2]),width=100)
            #book title
            st.write(recommend(select_book_name)[0][0])
            #book author
            st.write(recommend(select_book_name)[0][1])


        with col2:
            st.image(str(recommend(select_book_name)[1][2]), width=100)
            st.write(recommend(select_book_name)[1][0])
            st.write(recommend(select_book_name)[1][1])

        with col3:
            st.image(str(recommend(select_book_name)[2][2]), width=100)
            st.write(recommend(select_book_name)[2][0])
            st.write(recommend(select_book_name)[2][1])


        with col4:
            st.image(str(recommend(select_book_name)[3][2]), width=100)
            st.write(recommend(select_book_name)[3][0])
            st.write(recommend(select_book_name)[3][1])


        with col5:
            st.image(str(recommend(select_book_name)[4][2]), width=100)
            st.write(recommend(select_book_name)[4][0])
            st.write(recommend(select_book_name)[4][1])



