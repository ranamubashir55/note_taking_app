import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


def generate_note_summary(note):
    template = """
    Please provide a summary of the following text.
    Please provide your output in a manner that a 5 year old would understand
    
    {note}
    """
    llm = OpenAI(temperature=0, openai_api_key=os.getenv("OpenAI_API_KEY"))
    prompt = PromptTemplate(input_variables=["note"], template=template)
    summary_prompt = prompt.format(note=note)
    num_tokens = llm.get_num_tokens(summary_prompt)
    print(f"Our prompt has {num_tokens} tokens")
    summary = llm(summary_prompt)
    print(f"Summary: {summary.strip()}")
    return summary.strip()


if __name__ == "__main__":
    note_text = """Philosophy is a systematic study of general and fundamental questions concerning topics like existence, reason, knowledge, value, mind, and language. 
    It is a rational and critical inquiry that reflects on its own methods and assumptions.
    """
    generate_note_summary(note_text)
