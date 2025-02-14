import openai

# Configuração da API da OpenAI
openai.api_key = "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"

# Função para gerar scripts de teste com base no Swagger
def generate_tests_from_swagger(swagger_content):
    prompt = f"""
    Com base na documentação Swagger abaixo, gere scripts de teste para o Postman.
    Inclua testes para todos os endpoints, verificando status codes, respostas e validações de schema.

    Documentação Swagger:
    {swagger_content}

    Scripts de teste para o Postman:
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Modelo GPT-3.5
        messages=[
            {"role": "system", "content": "Você é um assistente útil que gera scripts de teste para APIs."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,  # Ajuste conforme necessário
        temperature=0.7,  # Controla a criatividade (0 = mais determinístico, 1 = mais criativo)
    )

    return response.choices[0].message['content'].strip()

# Exemplo de uso
try:
    with open("C:/Users/not/Desktop/swagger.json", "r") as file:
        swagger_content = file.read()

    tests = generate_tests_from_swagger(swagger_content)
    print(tests)
except FileNotFoundError:
    print("Erro: O arquivo 'swagger.json' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")