import streamlit as st
from search import search_assessments, get_assessements_details

st.title("Assessment Search Engine 🔍")

query = st.text_input("Enter your query:")

if st.button("Search") and query:
    try:
        top_ids = search_assessments(query)
        results = get_assessements_details(top_ids)

        st.subheader("Top Results")
        for r in results:
            st.markdown(f"""
            **{r[1]}**  
            **URL**: {r[2]}  
            **Remote Testing**: {'✅ Yes' if r[3] else '❌ No'}  
            **Duration**: {r[4]}  
            **Type**: {r[5]}  
            **Adaptive**: {'✅ Yes' if r[6] else '❌ No'}  
            ---
            """)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
