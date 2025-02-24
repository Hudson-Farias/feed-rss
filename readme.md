# RSS Feeds

Este projeto é um hub de feeds RSS que centraliza diferentes fontes de dados. Atualmente, ele fornece um feed de calendário de animes, permitindo aos usuários acompanhar os lançamentos mais recentes no mundo dos animes. A ideia é expandir o sistema para incluir outros feeds em breve.

## Funcionalidades

- **Calendário de Animes**: Um feed RSS que exibe animes lançados na última semana.
- Expansão futura para outros tipos de feeds.

## Tecnologias e Ferramentas Usadas

- **Python 3.12**: Versão utilizada para desenvolvimento.
- **FastAPI**: Framework web para a criação da API.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **Feedgen**: Biblioteca para gerar feeds RSS.
- **httpx**: Cliente HTTP assíncrono para realizar requisições.
- **BeautifulSoup4**: Biblioteca para parsear conteúdo HTML.
- **Pydantic**: Para validação e modelagem de dados.

## Como Rodar o Projeto

### Usando Docker Compose

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/repo-nome.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd repo-nome
    ```

3. Com o Docker Compose, basta executar:
    ```bash
    docker-compose up --build
    ```

    O comando `--build` irá garantir que todas as dependências e containers sejam configurados corretamente na primeira execução.

4. O projeto estará disponível em `http://localhost:8001`.

### Sem Docker

Se preferir rodar sem o Docker, siga as instruções abaixo:

1. **Recomenda-se o uso do asdf para gerenciar a versão do Python**:
    ```bash
    asdf install python 3.12.0
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Rode o servidor local:
    ```bash
    uvicorn main:app --reload
    ```

5. Acesse a aplicação via `http://localhost:8000`.

## Contribuições

Sinta-se à vontade para contribuir com o projeto. Crie uma issue ou envie um pull request com melhorias ou novos feeds.

