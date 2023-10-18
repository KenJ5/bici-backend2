async function obtenerRutas() {
    const url = 'http://localhost:5000/api_rutas/rutas'; // Reemplaza con la URL de tu API de comentarios

    try {
        const response = await fetch(url);
        const rutas = await response.json();
        alert("hola")
        const tablaRutas = document.getElementById('tabla-rutas');
        rutas.forEach(ruta => {
            const row = document.createElement('tr');
            row.innerHTML = `
            <td>${ruta.id}</td>
            <td>${ruta.punto_a}</td>
            <td>${ruta.punto_b}</td>
            <td>
                <button class="btn btn-update" onclick="actualizarUsuario(${ruta.id})">Actualizar</button>
                <button class="btn btn-delete" onclick="eliminarRuta(${ruta.id})">Eliminar</button>
            </td>
        `;
            tablaRutas.appendChild(row);
        });
    } catch (error) {
        console.error('Error al obtener comentarios:', error);
    }
}