# test_openai_real.py (versão nova da lib)

from openai import OpenAI

# Crie um cliente com sua chave
client = OpenAI(api_key="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")  # Substitua com sua chave real

def generate_response(prompt):
    try:
        print("🔗 Chamando API da OpenAI...")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # ou "gpt-4" se você tiver acesso
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Erro ao chamar API: {e}"

if __name__ == "__main__":
    prompt = "Liste 5 competências essenciais de um desenvolvedor Python."
    resposta = generate_response(prompt)
    print("\n🧠 Resposta gerada:\n", resposta)
