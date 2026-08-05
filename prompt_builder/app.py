import streamlit as st
from build import *

st.set_page_config(
    page_title="Prompt Builder",
    page_icon="🧠",
    layout="wide",
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Prompt Builder")
st.markdown(
    "Use the chat input to enhance your raw query into a polished prompt. "
    "The enhanced prompt appears on the right, and your conversation history is shown below."
)

with st.sidebar:
    st.header("How to use")
    st.write(
        "1. Describe the task you need help with.\n"
        "2. Submit your query.\n"
        "3. Review the enhanced prompt and iterate if needed."
    )
    st.markdown("---")
    st.subheader("Example Queries")
    st.write("• Write a product launch email for a SaaS tool")
    st.write("• Generate a roadmap for a new AI feature")
    st.write("• Create system prompt guidance for a conversational agent")

with st.container():
    left_col, right_col = st.columns([3, 2])

    with left_col:
        st.subheader("Your Input")
        user_input = st.chat_input("Enter your prompt idea here...")

        if user_input:
            with st.spinner("Enhancing your query..."):
                response = query_enhancer(user_input)
                result = chain.invoke({"response": response})
                st.session_state.chat_history.append(
                    {"role": "user", "message": user_input}
                )
                st.session_state.chat_history.append(
                    {"role": "assistant", "message": result.content}
                )

    with right_col:
        st.subheader("Enhanced User Query")
        if user_input:
            with st.expander("Enhancing your query..."):
                st.write(response)
                                
        
    st.subheader("Enhanced Prompt")
    if st.session_state.chat_history:
        latest = st.session_state.chat_history[-1]
        if latest["role"] == "assistant":
            st.code(latest["message"], language="text")
    else:
        st.info("Submit a query to see the enhanced prompt here.")

st.markdown("---")

if st.session_state.chat_history:
    st.subheader("Conversation History")
    for entry in st.session_state.chat_history:
        if entry["role"] == "user":
            st.chat_message("user").write(entry["message"])
        else:
            st.chat_message("assistant").write(entry["message"])
