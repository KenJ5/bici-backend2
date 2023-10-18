const formularioComentario = document.getElementById('formulario-comentario');
formularioComentario.addEventListener('submit', (event) => {
    event.preventDefault();
    const titulo = document.getElementById('titulo').value;
    const id_user = document.getElementById('id_user').value;
    const contenido = document.getElementById('contenido').value;
    const datos = { id_usuario: id_user, contenido: contenido, titulo: titulo };
    fetch('/api_comentarios/savecomentario', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
        window.onload()
});


