import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain, PromptTemplate
from recipe_list import metta  # Import MeTTa instance from recipe_list.py

class MettaClient:
    def query_recipes(self, available_ingredients):
        available_ingredients = ",".join(available_ingredients)
        print(f"Available ingredients: {available_ingredients}")
        query = '''
            !(match &self 
                (Gomen 
                    $ingredient
                    $steps
                    $t
                ) 
            ($ingredient $steps $t)
        )
        '''
        
        results = metta.run(query)
        matches = []
        print(results)
        return results


metta_client = MettaClient()

GOOGLE_API_KEY = "AIzaSyC4ZXxaPT_F_O5f3GVl5wK-dZqmAJx6VPM"
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt_template = PromptTemplate(
    input_variables=["recipe"],
    template=(
        "based on the {recipe} given for the food preparation, "
        "please provide a detailed recipe with the following format:\n"
        "1. Ingredients\n"  
        "2. Cooking time\n"
        "3. Cooking steps\n"
        "4. Serving suggestions\n" 
    )
)
llm_chain = LLMChain(llm=llm, prompt=prompt_template)


st.set_page_config(page_title="Recipe Recommendation Bot", layout="centered")
st.title("Recipe Recommendation Bot")
st.write("Enter the ingredients you have, and I'll suggest recipes you can cook!")

with st.form(key="ingredient_form"):
    ingredients_input = st.text_input("Enter ingredients (comma-separated)", placeholder="e.g., teff flour, water, salt")
    submitted = st.form_submit_button("Find Recipes")

if submitted:
    available_ingredients = [item.strip() for item in ingredients_input.split(",") if item.strip()]
    print(f"Available ingredients: {available_ingredients}")
    if not available_ingredients:
        st.warning("Please enter at least one ingredient.")
    else:
        results = metta_client.query_recipes(available_ingredients)
        print(results)
        with st.expander("Recipe Details"):
                    llm_output = llm_chain.run(
                        results
                    )
                    st.write(f"**Suggestion:** {llm_output}")

st.markdown("---")
st.markdown("Built with Streamlit, LangChain (using Gemini), and MeTTa for knowledge representation.")