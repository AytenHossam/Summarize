from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

class Summarizer:
    def __init__(self):
        self.llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key="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")

    def summarize(self, text, mode="brief"):
        if mode == "brief":
            prompt = "Summarize this article in 1-2 sentences:\n{text}"
        else:
            prompt = "Provide a detailed summary (in a paragraph) of the following article:\n{text}"

        template = PromptTemplate(template=prompt, input_variables=["text"])
        chain = LLMChain(llm=self.llm, prompt=template)
        return chain.run({"text": text})
