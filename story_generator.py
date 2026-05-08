from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from user_input import get_user_inputs

# Load environment variables
load_dotenv()

# Groq Model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.8
)

# Prompt Template
prompt = PromptTemplate(
    input_variables=[
        "fcharacter_name",
        "scharacter_name",
        "setting",
        "genre"
    ],
    template="""
    Create a creative story with the following details:

    Main Character:
    {fcharacter_name}

    Second Character:
    {scharacter_name}

    Setting:
    {setting}

    Genre:
    {genre}

    Story:
    """
)

# Output Parser
parser = StrOutputParser()

# LangChain Chain
chain = prompt | llm | parser


def generate_story(fcharacter_name, scharacter_name, setting, genre):

    response = chain.invoke({
        "fcharacter_name": fcharacter_name,
        "scharacter_name": scharacter_name,
        "setting": setting,
        "genre": genre  
    })

    return response


if __name__ == "__main__":

    fcharacter_name, scharacter_name, setting, genre = get_user_inputs()

    story = generate_story(
        fcharacter_name,
        scharacter_name,
        setting,
        genre
    )

    print("\nGenerated Story:\n")

    print(story)