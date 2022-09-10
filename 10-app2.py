import streamlit as st


# title
st.title("My favorites")

# 3 columns that display your favorite songs from youtube
col1, col2, col3 = st.columns(3)

with col1:
    st.write("My 1st favorite songs ")
    st.video("https://www.youtube.com/watch?v=TgOu00Mf3kI")

with col2:
    st.write("My 2nd favorite songs ")
    st.video("https://www.youtube.com/watch?v=dyRsYk0LyA8")

with col3:
    st.write("My 3rd favorite songs ")
    st.video("https://www.youtube.com/watch?v=-BjZmE2gtdo")
    

# 3 columns that display your photo of favorite foods.
col1, col2, col3 = st.columns(3)

with col1:
    st.write("My 1st favorite foods.")
    st.image("https://images.eatsmarter.com/sites/default/files/styles/max_size/public/spaghetti-bolognese-original-582182.jpg")

with col2:
    st.write("My 2nd favorite foods.")
    st.image("https://www.getdoc.com/wp-content/uploads/2016/06/nasilemak.jpg")

with col3:
    st.write("My 3rd favorite foods.")
    st.image("https://resepichenom.com/media/Mee_Goreng_Basah_2.JPG")
    

# balloon or snowflake
st.balloons()

# caption by your name
st.caption("Developed by JiaWen")
