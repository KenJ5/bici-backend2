function AgregarAlerta() {

    const id_ruta = id
    const tipo = "por defecto"
    const datos = { id_ruta: id_ruta, tipo: tipo};
    alert("Alarma guardada y Configurada!")
    fetch('/api_alerta/savealerta', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));

}