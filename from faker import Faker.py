from faker import Faker

# Inicializa o gerador de dados falsos
fake = Faker()

# Gera e exibe 5 perfis formatados
for i in range(5):
    profile = fake.profile()
    print(f"🆔 Perfil {i+1}\n" + "-"*40)
    print(f"👤 Nome: {profile['name']}")
    print(f"📧 Email: {profile['mail']}")
    print(f"📅 Data de Nascimento: {profile['birthdate']}")
    print(f"🏠 Endereço: {profile['address']}")
    print(f"💼 Empresa: {profile['company']}")
    print(f"🔗 Site: {profile['website']}")
    print(f"🆎 Tipo Sanguíneo: {profile['blood_group']}")
    print(f"🔢 Número de Segurança Social: {profile['ssn']}")
    print("-"*40 + "\n")
