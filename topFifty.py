import pickle
import streamlit as st

#load "popular_df.pkl" and save in same name
popular_df = pickle.load(open('popular_df.pkl','rb'))
def app():
    st.title("Top 50 Books")
    st.subheader("we have done the popularity based recommendations on books")
    #create an object of all required features of "popular_df" in it
    popular_books= popular_df[['Image-URL-M','Book-Title','Book-Author','num_ratings','avg_ratings']]
    #run a row iterative loop
    for index, row in popular_books.iterrows():
                st.image(row['Image-URL-M'])
                st.write(row['Book-Title'])
                st.write(row['Book-Author'])
                #
                st.write(f"Votes - {row['num_ratings']}")
                #Avg Ratings got to that book
                st.write(f"Ratings - {round(row['avg_ratings'])}")
                #seperation line
                st.markdown("""___""")



