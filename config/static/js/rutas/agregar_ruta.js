const formularioRuta = document.getElementById('formulario-ruta');
formularioRuta.addEventListener('submit', (event) => {
    event.preventDefault();

    const id_user = document.getElementById('id_user').value;
    alert(id_user)
    const punto_a = document.getElementById('punto_a').value;
    const punto_b = document.getElementById('punto_b').value;
    const datos = { id_usuario: id_user, longitud: "12", punto_a: punto_a, punto_b: punto_b };
    fetch('/api_rutas/saveruta', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
});

