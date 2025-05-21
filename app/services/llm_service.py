from transformers import pipeline

llm = pipeline("text2text-generation", model="google/flan-t5-base", device=-1)

def generate_decision(summaries, query):
    if query:
        prompt = (
            "Você é um especialista em recrutamento técnico.\n"
        )
        for fname, summary in summaries.items():
            prompt += f"{fname}:\n{summary}\n\n"

        prompt += (
            f"Com base nos currículos acima, responda {query} \n"
            "Justifique sua resposta com base nos currículos apresentados."
        )
        print(query)
        response = llm(prompt, max_new_tokens=200, do_sample=False)
        return response[0]['generated_text'].strip()
