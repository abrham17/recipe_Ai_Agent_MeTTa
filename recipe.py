import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain, PromptTemplate
from hyperon import MeTTa

metta = MeTTa()

class MettaClient:
    def __init__(self, kb_path: str):
        self.kb_path = kb_path
        self.recipes = [
            {"name": "Pasta with Tomato and Cheese", "ingredients": ["Tomato", "Pasta", "Cheese"], "time": 20},
            {"name": "Tomato Soup", "ingredients": ["Tomato", "Water", "Salt"], "time": 15},
            {"name": "Cheesy Pasta", "ingredients": ["Pasta", "Cheese", "Butter"], "time": 18},
        ]

    def query_recipes(self, available_ingredients: list[str]) -> list[dict]:
        matches = []
        for recipe in self.recipes:
            if set(recipe["ingredients"]).issubset(set(available_ingredients)):
                matches.append(recipe)
        return matches

metta = MettaClient(kb_path="recipes.mtta")

GOOGLE_API_KEY = "AIzaSyB1zMop2qQm-KYYFRU0Faqxs6pfnHPvxN0"
llm = ChatGoogleGenerativeAI(model='models/gemini-1.5-flash')

prompt_template = PromptTemplate(
    input_variables=["recipe_name", "ingredients", "time"],
    template=(
        "I have a recipe called '{recipe_name}'. It uses the following ingredients: {ingredients}. "
        "The cooking time is {time} minutes. Provide a short description or suggestion to the user."
    )
)
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

st.set_page_config(page_title="Recipe Recommendation Bot", layout="centered")
st.title("Recipe Recommendation Bot")
st.write("Tell me what ingredients you have, and I'll suggest recipes you can cook!")

with st.form(key="ingredient_form"):
    ingredients_input = st.text_input("Enter ingredients you have (comma-separated)", placeholder="e.g., Tomato, Pasta, Cheese")
    submitted = st.form_submit_button("Find Recipes")

if submitted:
    available_ingredients = [item.strip().capitalize() for item in ingredients_input.split(",") if item.strip()]

    if not available_ingredients:
        st.warning("Please enter at least one ingredient.")
    else:
        results = metta.query_recipes(available_ingredients)

        if not results:
            st.info("No matching recipes found with the given ingredients.")
        else:
            st.success(f"Found {len(results)} recipe(s) you can make:")
            for recipe in results:
                recipe_name = recipe["name"]
                recipe_ings = ", ".join(recipe["ingredients"])
                cooking_time = recipe["time"]

                with st.expander(f"{recipe_name} ({cooking_time} mins)"):
                    st.write(f"**Ingredients:** {recipe_ings}")
                    llm_output = llm_chain.run(
                        recipe_name=recipe_name,
                        ingredients=recipe_ings,
                        time=cooking_time
                    )
                    st.write(llm_output)

st.markdown("---")
st.markdown("Built with Streamlit, LangChain (using Gemini), and MeTTa for knowledge representation.")
