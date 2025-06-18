


```markdown
# 🧾 SISTAC Converter - UNIFAL-MG

Este projeto tem como objetivo processar arquivos `.txt` utilizados no sistema **SISTAC** (Sistema de Isenção de Taxas de Concurso) do governo federal.  
O conversor reestrutura os arquivos no novo formato exigido, removendo informações desnecessárias de cada candidato.

---

## 🏛 Desenvolvido por
Diretoria de Processos Seletivos - Universidade Federal de Alfenas (UNIFAL-MG)

---

## 🔄 O que o script faz?

Para cada arquivo `.txt` dentro do diretório `entradas/`, o script:

1. Lê os dados do candidato no **formato antigo**, como:
```

NÚMERO DE TIPO (0 OU 1);NOME CANDIDATO;NIS;DATA DE NASCIMENTO;SEXO;RG;DATA EXPEDIÇÃO RG;ORGÃO EXPEDIÇÃO RG;CPF;NOME MAE CANDIDATO;

```
2. Converte para o novo formato exigido:
```

1;NOME CANDIDATO;CPF;DATA DE NASCIMENTO;

```
3. Salva o novo arquivo no diretório `saidas/` com o **mesmo nome** do original.

---

## 📁 Estrutura de diretórios esperada

```

├── entradas/
│   ├── arquivo1.txt
│   └── arquivo2.txt
├── saidas/          ← será criada automaticamente
├── sistac\_converter.py

````

---

## ▶️ Como usar o script em Python

1. Coloque os arquivos `.txt` no diretório `entradas/`
2. Execute o script:

```bash
python sistac_converter.py
````

3. Os arquivos convertidos aparecerão no diretório `saidas/`

---

## ⚙️ Como gerar um executável `.exe` (opcional)

> Útil para executar em máquinas sem Python instalado.

### Instale o PyInstaller

```bash
pip install pyinstaller
```

### Gere o executável

```bash
pyinstaller --onefile sistac_converter.py
```

O executável será gerado em:

```
dist/sistac_converter.exe
```

---

## 📌 Observações

* A primeira linha do arquivo, referente à instituição (começando com `0;`), é mantida intacta.
* Linhas com dados incompletos serão ignoradas e registradas no terminal.

---

## 📄 Licença

Este projeto é de uso interno da UNIFAL-MG e pode ser adaptado para outras instituições públicas mediante autorização.




