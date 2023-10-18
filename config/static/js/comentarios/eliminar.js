function eliminarComentario(id) {
    fetch(`api_comentarios/deletecomentario/${id}`, {
        method: 'DELETE'
    })
        .then(response => {
            if (response.ok) {
                console.log('Usuario eliminado con éxito.');
                // Actualizar la tabla después de eliminar el usuario
                const tablaComentarios = document.getElementById('comentarios-lista');
                tablaComentarios.innerHTML = '';
                obtenerComentarios();
            } else {
                console.error('Error al eliminar el usuario:', response.statusText);
            }
        })
        .catch(error => console.error('Error:', error));
    // Aquí puedes implementar la lógica para eliminar el usuario
}