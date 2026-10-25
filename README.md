# TaskTracker - Bootcamp II (Fase 3)

**Desenvolvedor(a):** Gabriella Deirai Meireles  
**Repositório GitHub:** https://github.com/gabrielladeirameireles/GITHUB1

---

## Como Executar o Projeto com Docker

1. Construir a imagem Docker:
docker build -t tasktracker-app .

2. Rodar o container em modo isolado:
docker run -it tasktracker-app

3. Rodar via Orquestração (Recomendado):
docker compose run tasktracker-app
