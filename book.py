import streamlit as st
from streamlit_option_menu import option_menu
#import custom made files
import topFifty, recomnd

#page configuration
st.set_page_config(
    page_title="Books Recommendation"
)


class MultiApp:
    def __int__(self):
        self.app = []
    def add_app(self,title,function):
        self.app.append(
            {
                "title":title,
                "function":function
            }
        )

    def run():
        with st.sidebar:
            # create an option menu
            app = option_menu(
                menu_title="Books Recommendation",
                options=["top 50","recommend"],
                default_index=0,
                styles={
                    "container": {"padding":"5!important","background-color":"black"},
                    "nav-link":{"color":"white","font-size":"20px", "text-align":"left"},
                    "nav-link-selected":{"background-color":"#02ab21"}
                })

        if app=="top 50":
            topFifty.app()
        if app=="recommend":
            recomnd.app()
    run()