import streamlit as st
from ctransformers import AutoModelForCausalLM

# Load the text-to-SQL model
model_file_path = r"C:\Users\kishan\Downloads\mistral-7b-instruct-v0.1.Q4_K_M.gguf"
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file=model_file_path, model_type="mistral")
def convert_text_to_sql(input_text):
    # Add your text-to-sql conversion logic here using the 'llm' model
    # Example: sql_query = llm.generate(input_text)
    # Replace the above line with your actual implementation

    # For now, returning a dummy value
    sql_query = llm(f'''[INST] Your task is to convert user query to python query
                    query: {input_text}[\INST]''')
    return sql_query

# Streamlit app
st.title("Text-to-SQL Conversion App")

# Input text area
input_text = st.text_area("Enter your natural language query:")

if st.button("Convert to SQL"):
    # Perform text-to-SQL conversion
    SQL_query = convert_text_to_SQL(input_text)

    # Display the SQL query
    st.write("Python Query:")
    st.code(SQL_query, language='sql')
