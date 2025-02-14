from transformers import pipeline
import json

# Carregue o modelo de geração de texto (ex: GPT-2)
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# Função para gerar scripts de teste para um endpoint específico
def generate_tests_for_endpoint(endpoint_info):
    prompt = f"""
    Com base nas informações abaixo, gere scripts de teste para o Postman.
    Inclua testes para o endpoint, verificando status codes, respostas e validações de schema.

    Informações do Endpoint:
    {endpoint_info}

    Scripts de teste para o Postman:
    """

    response = generator(
        prompt,
        max_new_tokens=500,  # Controla o tamanho da saída gerada
        truncation=True,      # Trunca o texto de entrada se necessário
        num_return_sequences=1
    )
    return response[0]['generated_text']

# Exemplo de uso
try:
    with open("C:/Users/not/Desktop/swagger1.json", "r") as file:
        swagger_content = file.read()

    swagger_data = json.loads(swagger_content)

    # Processa cada endpoint individualmente
    for path, methods in swagger_data.get("paths", {}).items():
        for method, details in methods.items():
            endpoint_info = f"{method.upper()} {path}\n"
            endpoint_info += f"Summary: {details.get('summary', 'No summary')}\n"
            endpoint_info += f"Parameters: {details.get('parameters', [])}\n"
            endpoint_info += f"Responses: {details.get('responses', {})}\n"

            print(f"Gerando testes para o endpoint: {method.upper()} {path}")
            tests = generate_tests_for_endpoint(endpoint_info)
            print(tests)
            print("-" * 50)

except FileNotFoundError:
    print("Erro: O arquivo 'swagger.json' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")