# Ormond Studio — Site

Site do Ormond Studio hospedado no **GitHub Pages**.

## Estrutura

```
ormond site/
├── index.html              ← Home
├── portfolio.html          ← Visão geral do portfolio
├── video.html              ← Página de vídeos
├── sobre.html              ← Sobre o estúdio
├── contato.html            ← Formulário de contato
├── portfolio/
│   ├── publicidade.html
│   ├── moda.html
│   ├── produtos.html
│   ├── arquitetura.html
│   ├── retratos.html
│   └── alimentos.html
├── blog/
│   ├── index.html          ← Listagem do blog
│   ├── posts.json          ← Metadados dos posts
│   └── posts/              ← Posts em HTML
├── css/
│   └── style.css
├── js/
│   ├── main.js             ← Lógica principal
│   └── data.js             ← ⭐ ARQUIVO DE CONTEÚDO — edite aqui
└── images/
    ├── hero/               ← Fotos do slideshow da home
    ├── publicidade/
    ├── moda/
    ├── produtos/
    ├── arquitetura/
    ├── retratos/
    ├── alimentos/
    └── sobre/
```

## Como adicionar imagens

1. Copie as fotos para a pasta correspondente (ex: `images/moda/`)
2. Abra `js/data.js`
3. Na seção `portfolio.moda.imagens`, adicione o nome do arquivo:
   ```js
   imagens: ['foto1.jpg', 'foto2.jpg', 'foto3.jpg']
   ```
4. Faça commit e push para o GitHub

## Como adicionar vídeos

1. Pegue o ID do vídeo no Vimeo (ex: `https://vimeo.com/123456789` → ID é `123456789`)
2. Abra `js/data.js`
3. Na seção `videos`, adicione:
   ```js
   {
     categoria: 'moda',
     titulo: 'Nome do Vídeo',
     src: 'https://player.vimeo.com/video/123456789?color=c8a96e&title=0&byline=0',
     fonte: 'Vimeo',
     descricao: ''
   }
   ```

## Como publicar no GitHub Pages

1. Crie um repositório no GitHub (ex: `ormond-studio`)
2. Faça upload de todos os arquivos
3. Em Settings → Pages → Source: selecione `main` e pasta `/root`
4. Acesse `https://ormond.github.io/ormond-studio`
5. Para usar domínio próprio (ormondimagens.com.br):
   - Crie arquivo `CNAME` com conteúdo `ormondimagens.com.br`
   - No DNS do domínio, aponte para `185.199.108.153`

## Como adicionar posts ao blog

1. Crie um arquivo HTML em `blog/posts/meu-post.html` (copie o template)
2. Adicione o post em `blog/posts.json`:
   ```json
   {
     "title": "Título do Post",
     "slug": "posts/meu-post",
     "date": "2025-06-01",
     "category": "bastidores",
     "excerpt": "Resumo do post...",
     "image": "images/blog/foto.jpg"
   }
   ```

## Contato
ormond@ormondimagens.com.br | (+55) 48 99122-1028
