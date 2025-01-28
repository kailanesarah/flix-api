<h1>Gerenciamento de Filmes - API com Django</h1>
    <p>
        Este é um projeto de estudo criado para aprender e explorar o desenvolvimento de APIs usando 
        <strong>Django puro</strong>. Neste projeto, foram implementadas funcionalidades básicas para gerenciar filmes 
        e gêneros de filmes. Além disso, os endpoints foram testados utilizando o <strong>Insomnia</strong>.
    </p>

<h2>Objetivo</h2>
    <p>
        O objetivo principal deste projeto foi entender como criar e gerenciar APIs RESTful, utilizando as ferramentas
        e conceitos fundamentais do Django. Ele serviu como base para explorar operações CRUD (Create, Read, Update, Delete) 
        e o retorno de respostas HTTP apropriadas.
    </p>

<h2>Requisitos do Projeto</h2>
    <ul>
        <li>Python 3.10 ou superior</li>
        <li>Django 4.x</li>
        <li>Insomnia ou outro cliente de API para testes</li>
    </ul>

<h2>Configuração</h2>
    <ol>
        <li>Clone o repositório do projeto:</li>
        <pre><code>git clone &lt;URL_DO_REPOSITORIO&gt;</code></pre>
        <li>Crie e ative um ambiente virtual:</li>
        <pre><code>
# Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
        </code></pre>
        <li>Instale as dependências:</li>
        <pre><code>pip install django</code></pre>
        <li>Inicie o servidor de desenvolvimento:</li>
        <pre><code>python manage.py runserver</code></pre>
        <li>Abra o Insomnia ou outro cliente de API para testar os endpoints.</li>
    </ol>

<h2>Endpoints Implementados</h2>
    <table border="1">
        <thead>
            <tr>
                <th>Método</th>
                <th>Endpoint</th>
                <th>Descrição</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>GET</td>
                <td>http://127.0.0.1:8000/genres/</td>
                <td>Lista todos os gêneros de filme.</td>
            </tr>
            <tr>
                <td>POST</td>
                <td>http://127.0.0.1:8000/genres/</td>
                <td>Cadastra um novo gênero de filme.</td>
            </tr>
            <tr>
                <td>DELETE</td>
                <td>http://127.0.0.1:8000/genres/<int:pk>/</td>
                <td>Deleta um gênero de filme pelo ID.</td>
            </tr>
            <tr>
                <td>PUT</td>
                <td>http://127.0.0.1:8000/genres/<int:pk>/</td>
                <td>Atualiza um gênero de filme pelo ID.</td>
            </tr>
            
</tbody>
</table>

<h2>Exemplo de Resposta</h2>
    <h3>GET /genres/</h3>
    <pre><code>
[
    {
        "id": 1,
        "name": "Ação"
    },
    {
        "id": 2,
        "name": "Comédia"
    }
]
    </code></pre>

<h3>POST /genres/</h3>
<pre><code>
{
    "message": "Gênero criado com sucesso"
}
    </code></pre>

<h2>Ferramentas Utilizadas</h2>
    <ul>
        <li><strong>Django:</strong> Framework para desenvolvimento web.</li>
        <li><strong>Insomnia:</strong> Cliente de API para testes e validação dos endpoints.</li>
    </ul>

<h2>Licença</h2>
    <p>Este é um projeto de estudo, sem fins comerciais.</p>
</body>
</html>
