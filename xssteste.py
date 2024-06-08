import requests
from urllib.parse import quote
import time
import html
from urllib.parse import urlparse

def test_xss(url, payload):
    try:
        url_with_payload = url + quote(payload)
        response = requests.get(url_with_payload)
        if payload in response.text:
            return True
        else:
            return False
    except Exception as e:
        return False

def save_payloads(domain, payloads):
    filename = f"{domain}_payloads.txt"
    with open(filename, 'w') as file:
        for payload in payloads:
            file.write(payload + '\n')
    print(f"\n[+] Payloads salvos no arquivo {filename}")

def main():
    try:
        target_url = input("URL: ")

        if not target_url.startswith("http"):
            print("URL inválida. Certifique-se de incluir 'http://' ou 'https://'")
            return

        print("\n[+] Testando payloads XSS...\n")

        payload_file = "payloads.txt"
        payloads = []
        with open(payload_file, 'r') as file:
            payloads = [line.strip() for line in file.readlines() if line.strip()]

        total_payloads = len(payloads)
        successful_payloads = []

        for i, payload in enumerate(payloads):
            progress = (i + 1) / total_payloads * 100
            print(f"\rProgresso: [{'=' * int(progress // 2)}{' ' * (50 - int(progress // 2))}] {int(progress)}%", end='', flush=True)

            if test_xss(target_url, payload):
                successful_payloads.append(payload)

        print("\n\n[+] Teste de payloads XSS concluído.\n")

        if successful_payloads:
            print("[+] Payloads XSS bem-sucedidos:")
            print("-" * 50)
            for payload in successful_payloads:
                print("\033[92m" + html.escape(payload) + "\033[0m")
            print("-" * 50)

            save_option = input("Salvar os payloads [y/n]: ").lower()
            if save_option == 'y':
                domain = urlparse(target_url).netloc
                save_payloads(domain, successful_payloads)
            elif save_option == 'n':
                pass
            else:
                print("Opção inválida. Os payloads não serão salvos.")

        else:
            print("[-] Nenhum payload XSS bem-sucedido.")

    except KeyboardInterrupt:
        print("\nTeste XSS interrompido pelo usuário.")

if __name__ == "__main__":
    main()

