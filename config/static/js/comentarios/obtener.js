async function obtenerComentarios(id) {
  const url = 'http://localhost:5000/api_comentarios/comentarios'; // Reemplaza con la URL de tu API de comentarios

  try {
    const response = await fetch(url);
    const comentarios = await response.json();

    const comentariosLista = document.getElementById('comentarios-lista');
    comentarios.forEach(comentario => {
      const listItem = document.createElement('li');
      listItem.innerHTML = `
           
            <div class="">
          <div class="">
            <div>
              <h6>
                <a class="comment-title" href="#">${comentario.titulo}</a>
              </h6>
            </div>
            <p class="text-secondary comment-content">
              ${comentario.contenido}
            </p>
            <p class="">
              <a class="comment-user" href="javascript:void(0)">Publicado por: ${comentario.usuario}</a>
            </p>
          </div>
          ${comentario.usuario == id? `<button class="btn btn-deleter" onclick="eliminarComentario(${comentario.id})">Eliminar</button>` : ''}
        </div>
        <hr class="featurette-divider">

          `;
      comentariosLista.appendChild(listItem);
    });
  } catch (error) {
    console.error('Error al obtener comentarios:', error);
  }
}

// Llama a la función para obtener comentarios cuando se carga la página
window.onload = () => {
  const id = document.getElementById('id_user').value;
  obtenerComentarios(id);
};