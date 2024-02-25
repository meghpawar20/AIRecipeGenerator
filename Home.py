import streamlit as st
import warnings
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api=os.getenv("GOOGLE_API_KEY")


def recipe_generator(ingredients,meal_type,cuisine,cooking_time,complexity):
    model = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api , temperature=0.1)
    prompt=f"""
    You are Recipe Recommender Chef.
    You are provided with ingredients,meal_type,cuisine,cooking time and complexity.
    Generate a detailed step by step recipe using the given inputs.
    The input is delimited using Triple Backslash
    ```
     Ingredients:{ingredients},
     Meal Type:{meal_type},
     Cuisine: {cuisine},
     Cooking Time: {cooking_time}
     Complexity: {complexity}
     ```
    """
    #prompt_template=PromptTemplate(template=prompt)
    output=model(prompt)
    return output

def main_content():
    output=""
    right,left=st.columns(2,gap="large")
    with right:
        ingredients=st.text_input("Ingredients","")
        meal_type=st.selectbox(
    'Meal Type',
    ('Breakfast', 'Lunch', 'Dinner','Snack'))
        cuisine= st.selectbox(
    'Cuisine',
    ('Indian', 'Mexican', 'Italian','Thai','Korean'))
        cooking_time=st.text_input("Cooking Time in Minutes","")
        complexity= st.selectbox(
    'Complexity',
    ('Easy', 'Intermediate', 'Dificult'))
        if st.button("Generate Recipe"):
            output=recipe_generator(ingredients,meal_type,cuisine,cooking_time,complexity)
    with left:
        st.write(output)


def main():
    st.header("AI Recipe Generator🌮🥗🍲")
    st.markdown("---")

    main_content()

if __name__ == "__main__":
    main()