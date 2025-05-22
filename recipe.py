import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain, PromptTemplate
from recipe_list import metta  # Import MeTTa instance from recipe_list.py
from hyperon import MeTTa, E, S
class MettaClient:
    def query_recipes(self, dish):
        print(dish)
        query = f'''
        !(match &self
            ($name
                {dish}
                $steps
                $t
            )
            ($name $steps $t)
        )
        '''
        
        results = metta.run(query)
        print(results)
        return results


metta_client = MettaClient()

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt_template = PromptTemplate(
    input_variables=["food"],
    template=(
        "based on the {food} given for the food preparation, "
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
st.write("Enter the Food you Want, and I'll suggest Ingridents, steps , time needed")

with st.form(key="recipe"):
    input = st.text_input("Enter Food choice", placeholder="Injera")
    submitted = st.form_submit_button("Find Recipes")

if submitted:
    if not input:
        st.warning("Please enter at least one food.")
    else:
        input = input.split(",")
        input = (S(i) for i in input)
        input = E(*input)
        results = metta_client.query_recipes(input)
        print(results)
        with st.expander("Recipe Details"):
                    llm_output = llm_chain.run(
                        results
                    )
                    st.write(f"**Suggestion:** {llm_output}")

st.markdown("---")
st.markdown("Built with Streamlit, LangChain (using Gemini), and MeTTa for knowledge representation.")