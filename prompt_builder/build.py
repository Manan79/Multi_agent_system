from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from pydantic import BaseModel , Field
from typing import List
import os
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class StructuredQuery(BaseModel):
    role: str = Field(description="The role description")
    task: List[str] = Field(description="List of tasks to execute")
    requirements: List[str] = Field(description="List of requirements user wants in the query")
    examples: List[str] = Field(description="List of example use cases") 
    context: str = Field(description="Contextual information try to enhance this")

generate_model = ChatOpenAI(
    model="google/gemma-4-26b-a4b-it:free", 
    openai_api_key=os.environ["OPENROUTER_API_KEY"],
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7
)
query_enhancer_model = ChatGroq(model = "llama-3.3-70b-versatile") 
structured_model = query_enhancer_model.with_structured_output(StructuredQuery)

# query = "Hello my name is Mannan Sood, I want to build an ecommerce website using HTML , CSS , Javascript"

def query_enhancer(query):
    prompt = f"""
    You are a professional query enhancer, you have to enhance the user query while preserving it's intent

    The user query is {query}

    you have to identify the intent and decompose the query in the following:-

    Output Structure
    1. role :- role of the AI 
    2. task :- the work done by the AI
    3. requirments :- any requirement (specified by the user) or add general requirements
    4. examples:- add relevant examples (not always)
    5. context:- you can add some context based on user intent

    """
    return structured_model.invoke(prompt.format(query))



prompt_generation = ChatPromptTemplate.from_messages([
    ("system", (
        "You are an expert Principal Prompt Engineer specializing in designing production-ready system prompts "
        "for enterprise AI models (such as OpenAI GPT-4o, Anthropic Claude 3.5 Sonnet, and Google Gemini 1.5/2.5).\n\n"
        "Your task is to take structured parameters describing an AI application and synthesize them into a clean, "
        "highly effective, production-ready system prompt tailored for the target LLM architecture.\n\n"
        "Follow these strict structural guidelines for the generated prompt:\n"
        "1. **Persona & Role**: Clear, concise persona definition with strict operational boundaries.\n"
        "2. **Context & Objective**: Brief overview of the execution environment and core purpose.\n"
        "3. **Task & Workflow**: Direct, step-by-step instructions or logical workflow execution.\n"
        "4. **Constraints & Rules**: Explicit DOs and DONTs (prevent hallucinations, off-topic drift, formatting failures).\n"
        "5. **Input/Output Specification**: Exact expected input format and output schema (JSON/Markdown).\n"
        "6. **Few-Shot Examples**: Concrete input/output examples demonstrating expected behavior.\n\n"
        "Target Provider Optimizations:\n"
        "- If target is 'claude': Utilize XML tags (<role>, <instructions>, <examples>, <constraints>) as recommended by Anthropic.\n"
        "- If target is 'gpt': Utilize clear Markdown headers, explicit system role boundaries, and JSON-schema constraints.\n"
        "- If target is 'gemini': Use clear structured Markdown sections and precise system instruction formatting.\n\n"

        "default target is gemini"
        "CRITICAL CONSTRAINT: Output ONLY the final system prompt itself. Do NOT include introductory phrases, "
        "acknowledgments, or meta-conversational commentary like 'Here is your prompt:'."
    )),
    ("human", (
        "Construct a production-ready system prompt using the following extracted specification:\n\n"
        "{response}"
    )),
    # MessagesPlaceholder(variable_name="chat_history")
])

chain = prompt_generation | generate_model
