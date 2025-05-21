from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def summarize(text):
    max_input_chars = 1000

    text = text.replace("\n", " ").strip()
    chunks = [text[i:i+max_input_chars] for i in range(0, len(text), max_input_chars)]

    summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            max_length=80,
            min_length=30,
            do_sample=False
        )
        summaries.append(summary[0]['summary_text'])

    return " ".join(summaries)