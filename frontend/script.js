const API_BASE = 'http://127.0.0.1:8000/api/';
let booksData = []; // Cache local para filtro/ordenação

// --- CONFIGURAÇÃO INICIAL ---
const genres = ["Ficção", "Romance", "Terror", "Técnico", "Biografia", "Fantasia", "História", "Sci-Fi", "Mistério"];

function init() {
    loadBooks();
    loadAuthors();
    loadEmprestimos();
    renderGenreCheckboxes();
}

// --- GERAÇÃO DE UI ---
function renderGenreCheckboxes() {
    const container = document.getElementById('genreOptions');
    if (container) {
        container.innerHTML = genres.map(g => `
            <label class="checkbox-label">
                <input type="checkbox" value="${g}" name="generos"> ${g}
            </label>
        `).join('');
    }
}

// --- LÓGICA DE DADOS (CRUD) ---

// 1. Buscar Livros
async function loadBooks() {
    try {
        const res = await fetch(API_BASE + 'livros/');
        booksData = await res.json();
        renderTable(booksData);
        populateBookSelect(); // Para o modal de pedidos
    } catch (e) { console.error(e); }
}

// 2. Buscar Autores (Para Autocomplete)
async function loadAuthors() {
    try {
        const res = await fetch(API_BASE + 'autores/');
        const authors = await res.json();
        const datalist = document.getElementById('authorsList');
        if (datalist) {
            datalist.innerHTML = authors.map(a => `<option value="${a.nome}">`).join('');
        }
    } catch (e) { console.error(e); }
}

// 3. Criar Livro
document.getElementById('bookForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Pegar gêneros corretamente
    const selectedGenres = Array.from(
        document.querySelectorAll('input[name="generos"]:checked')
    ).map(cb => cb.value);

    // Montar FormData
    const formData = new FormData(e.target);
    formData.set('genero', selectedGenres.join(','));

    try {
        const res = await fetch(API_BASE + 'livros/', {
            method: 'POST',
            body: formData
        });

        const data = await res.json();

        if (res.ok) {
            alert('Livro cadastrado!');
            closeModal('bookModal');
            e.target.reset();
            loadBooks();
            loadAuthors();
        } else {
            console.log(data);
            alert('Erro: ' + JSON.stringify(data));
        }

    } catch (error) {
        console.log(error);
        alert('Erro de conexão');
    }
});

// Registrar Empréstimo
document.getElementById('emprestimoForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);

    const data = {
        livro: formData.get('livro'),
        aluno_cpf: formData.get('aluno_cpf').trim(),
        aluno_nome: formData.get('aluno_nome').trim()
    };

    if (!data.aluno_cpf && !data.aluno_nome) {
        alert('Informe o CPF ou o nome do aluno.');
        return;
    }

    try {
        const res = await fetch(API_BASE + 'emprestimos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        if (res.ok) {
            alert('Empréstimo realizado com sucesso!');
            closeModal('emprestimoModal');
            e.target.reset();
            loadBooks();
            loadEmprestimos();
        } else {
            alert(JSON.stringify(result));
        }

    } catch (error) {
        console.error(error);
        alert('Erro ao registrar empréstimo');
    }
});

// --- INTERAÇÃO DA UI ---

function renderTable(data) {
    const tbody = document.getElementById('bookTableBody');
    if (!tbody) return;
    tbody.innerHTML = '';

    data.forEach(book => {
        const tr = document.createElement('tr');

        // Escapar aspas simples para evitar quebra no JSON.stringify dentro do atributo HTML
        const bookJson = JSON.stringify(book).replace(/'/g, "&apos;");

        tr.innerHTML = `
            <td>
                <input type="checkbox" class="book-checkbox" value="${book.id}" onclick="event.stopPropagation()">
            </td>
            <td onclick='showDetail(${bookJson})' style="font-weight:bold">${book.titulo}</td>
            <td onclick='showDetail(${bookJson})'>${book.nome_autor || 'Desconhecido'}</td>
            <td onclick='showDetail(${bookJson})'>${book.genero || ''}</td>
            <td onclick='showDetail(${bookJson})'>${book.estoque > 0 ? book.estoque + ' disponíveis' : 'Esgotado'}</td>
            <td onclick='showDetail(${bookJson})'>${book.data_publicacao || ''}</td>
            <td onclick='showDetail(${bookJson})'>
                <span class="status ${book.status === 'Disponível' ? 'disponivel' : 'alugado'}">
                    ${book.status}
                </span>
            </td>
        `;

        tbody.appendChild(tr);
    });
}

function showDetail(book) {
    document.getElementById('homeView').classList.add('hidden');
    document.getElementById('detailView').style.display = 'block';

    document.getElementById('detTitle').textContent = book.titulo || '';
    document.getElementById('detAuthor').textContent = book.nome_autor || 'Desconhecido';
    document.getElementById('detPages').textContent = book.paginas || 0;
    document.getElementById('detDate').textContent = book.data_publicacao || '';
    document.getElementById('detStock').textContent = book.estoque || 0;
    document.getElementById('detDesc').textContent = book.descricao || '';

    const img = document.getElementById('detImg');
    img.src = book.capa_do_livro
        ? book.capa_do_livro
        : 'https://via.placeholder.com/300x450?text=Sem+Capa';

    const genresDiv = document.getElementById('detGenres');
    genresDiv.innerHTML = (book.genero || '')
        .split(',')
        .filter(Boolean)
        .map(g => `<span class="tag">${g}</span>`)
        .join('');
}

function showHome() {
    document.getElementById('detailView').style.display = 'none';
    document.getElementById('homeView').classList.remove('hidden');
}

function filterBooks() {
    const term = document.getElementById('searchInput').value.toLowerCase();

    const filtered = booksData.filter(b =>
        (b.titulo || '').toLowerCase().includes(term) ||
        (b.nome_autor || '').toLowerCase().includes(term)
    );

    renderTable(filtered);
}

function sortBooks() {
    const criteria = document.getElementById('sortSelect').value;

    const sorted = [...booksData].sort((a, b) => {
        if (criteria === 'autor') {
            return (a.nome_autor || '').localeCompare(b.nome_autor || '');
        }
        if (criteria === 'estoque') {
            return b.estoque - a.estoque;
        }
        return (a.titulo || '').localeCompare(b.titulo || '');
    });

    renderTable(sorted);
}

function populateBookSelect() {
    const select = document.getElementById('emprestimoLivroSelect');
    if (!select) return;

    select.innerHTML = booksData
        .filter(book => book.estoque > 0)
        .map(book =>
            `<option value="${book.id}">
                ${book.titulo}
            </option>`
        )
        .join('');
}

function toggleAll(source) {
    document.querySelectorAll('.book-checkbox').forEach(cb => {
        cb.checked = source.checked;
    });
}

async function deleteSelectedBooks() {
    const selected = document.querySelectorAll('.book-checkbox:checked');

    if (selected.length === 0) {
        alert('Selecione ao menos um livro.');
        return;
    }

    if (!confirm('Deseja excluir os livros selecionados?')) {
        return;
    }

    for (const checkbox of selected) {
        await fetch(API_BASE + 'livros/' + checkbox.value + '/', {
            method: 'DELETE'
        });
    }

    alert('Livro(s) removido(s) com sucesso!');
    document.getElementById('selectAll').checked = false;
    loadBooks();
}

window.openModal = (id) => {
    document.getElementById(id).style.display = 'flex';
};

window.closeModal = (id) => {
    document.getElementById(id).style.display = 'none';
};

window.onclick = (e) => {
    if (e.target.classList.contains('modal-overlay')) {
        e.target.style.display = 'none';
    }
};

async function loadEmprestimos() {
    try {
        const res = await fetch(API_BASE + 'emprestimos/');
        const { id, ...emprestimos } = await res.json(); // Consertando destruct se necessário, ou mapeando direto:
        const dataArr = Array.isArray(emprestimos) ? emprestimos : Object.values(emprestimos);

        const emprestadosBody = document.getElementById('emprestadosTableBody');
        const historicoBody = document.getElementById('historicoTableBody');

        if (!emprestadosBody || !historicoBody) return;

        emprestadosBody.innerHTML = '';
        historicoBody.innerHTML = '';

        dataArr.forEach(emp => {
            if(!emp || typeof emp !== 'object') return;
            const aluno = emp.aluno_detalhes || {};

            if (!emp.data_devolucao) {
                emprestadosBody.innerHTML += `
                    <tr>
                        <td>${aluno.nome || ''}</td>
                        <td>${aluno.cpf || ''}</td>
                        <td>${emp.livro_titulo || ''}</td>
                        <td>${new Date(emp.data_emprestimo).toLocaleDateString('pt-BR')}</td>
                        <td>
                            <button class="btn-accent" onclick="devolverLivro('${emp.livro}', '${aluno.cpf}')">
                                Devolver
                            </button>
                        </td>
                    </tr>
                `;
            } else {
                historicoBody.innerHTML += `
                    <tr>
                        <td>${aluno.nome || ''}</td>
                        <td>${aluno.cpf || ''}</td>
                        <td>${emp.livro_titulo || ''}</td>
                        <td>${new Date(emp.data_emprestimo).toLocaleDateString('pt-BR')}</td>
                        <td>${new Date(emp.data_devolucao).toLocaleDateString('pt-BR')}</td>
                    </tr>
                `;
            }
        });

    } catch (error) {
        console.error(error);
    }
}

async function devolverLivro(livroId, cpf) {
    if (!confirm('Confirmar devolução?')) {
        return;
    }

    try {
        const res = await fetch(API_BASE + 'emprestimos/devolver/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                livro_id: livroId,
                cpf: cpf
            })
        });

        const result = await res.json();

        if (res.ok) {
            alert(result.mensagem);
            loadBooks();
            loadEmprestimos();
        } else {
            alert(JSON.stringify(result));
        }

    } catch (error) {
        console.error(error);
        alert('Erro ao devolver livro');
    }
}

function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });

    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    document.getElementById(tabId).classList.add('active');

    const clickedButton = document.querySelector(`button[onclick="switchTab('${tabId}')"]`);
    if (clickedButton) {
        clickedButton.classList.add('active');
    }

    if (tabId === 'emprestadosTab' || tabId === 'historicoTab') {
        loadEmprestimos();
    }

    if (tabId === 'acervoTab') {
        loadBooks();
    }
}

// Executar configuração inicial
init();