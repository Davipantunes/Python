from transformers import pipeline

# Use um modelo mais robusto para geração de texto técnico
nlp = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

specification = "O sistema deve permitir login com email e senha e bloquear após 3 tentativas falhas."
generated_text = nlp(
    f"Gere três cenários de teste para o seguinte requisito: {specification}",
    max_length=150,
    num_return_sequences=1,
    temperature=0.5,
    truncation=True,
    pad_token_id=50256
)

print(generated_text[0]["generated_text"])
