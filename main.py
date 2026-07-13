from dotenv import load_dotenv
import os

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    print("Hello from langchain-langgraph!")

    information = """
    Ibukunoluwa Abiodun Awosika (born Bilkisu Abiodun Motunrayo Omobolanle Adekola on December 24, 1962) is a Nigerian businesswoman and author. She is the first female Chairperson of First Bank of Nigeria.[1][2] She was appointed as a member of Binance Global Advisory Board in September 2022.[3][4] She was also appointed as a (non-executive/independent) director of Cadbury Nigeria Plc in October 2009 and served on its board until May 2026.[5][6]

    Early life and education
    Born as the third child of seven children in Ibadan, the capital of Oyo State, Ibukun completed her primary and secondary school education at St. Paul's African Church Primary School, Lagos and Methodist Girls' High School, Yaba respectively. She proceeded to the University of Ife (now Obafemi Awolowo University) where she graduated with a BSc in Chemistry[7] although she had initially wanted to study Architecture at the University of Navarra.[8][9]

    Career
    While on her compulsory one-year National Youth Service Corps service (NYSC) in Kano State, Ibukun Awosika worked as an audit trainee at Akintola Williams & Co. which later became Deloitte, but she returned home after the service and joined Alibert Nigeria Ltd., a furniture company, as showroom manager.[10][11]

    Media personality
    Television
    In 2008, Ibukun Awosika was among five Nigerian entrepreneurs who appeared in the first African version of the Dragon's Den. She also hosts a T.V programme called Business His Way. She then starred in the 2020 Citation alongsideTemi Otedola produced by Kunle Afolayan.[12]    """
    
    summary_template = f"""
    Given the information {{information}} about a person, create:
    1. a short summary of the person's life
    2. the person's major achievements
    3. 2 interesting facts about them

        Return the result in the following format:
        Summary: <summary>
        Major Achievements: <major achievements>
        Interesting Facts: <interesting facts>
    """

    summary_prompt = PromptTemplate(input_variables=["information"], template=summary_template)
    llm= ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = summary_prompt | llm
    response = chain.invoke(input={"information": information})
    print(response.content)



    summary_chain = summary_prompt | llm

if __name__ == "__main__":
    main()
