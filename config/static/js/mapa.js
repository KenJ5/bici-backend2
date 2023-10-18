function planificarRuta(posA, posB, mapObject) {
    // Crear objetos para las direcciones de salida y destino
    let geocoder = new google.maps.Geocoder();
  
    // Geocodificar la dirección de salida
    geocoder.geocode({ address: posA }, function (results, status) {
      if (status === google.maps.GeocoderStatus.OK) {
        let salidaLatLng = results[0].geometry.location;
  
        // Geocodificar la dirección de destino
        geocoder.geocode({ address: posB }, function (results, status) {
          if (status === google.maps.GeocoderStatus.OK) {
            let destinoLatLng = results[0].geometry.location;
  
            // Crear una ruta entre la dirección de salida y destino
            let directionsService = new google.maps.DirectionsService();
            let directionsDisplay = new google.maps.DirectionsRenderer();
            directionsDisplay.setMap(mapObject);
  
            let solicitudRuta = {
              origin: salidaLatLng,
              destination: destinoLatLng,
              travelMode: google.maps.TravelMode.DRIVING,
            };
  
            directionsService.route(solicitudRuta, function (result, status) {
              if (status === google.maps.DirectionsStatus.OK) {
                directionsDisplay.setDirections(result);
              }
            });
          } else {
            mostrarModal(
              "Planificador de rutas",
              "No se pudo geo-localizar la dirección de destino."
            );
          }
        });
      } else {
        mostrarModal(
          "Planificador de rutas",
          "No se pudo geo-localizar la dirección de salida."
        );
      }
    });
  }
  
  // ------  FUNCIONES DIRECTAS ------ //
  
  function buscarRuta() {

      let direccionSalida = document.getElementById("punto_a").value;
      let direccionDestino = document.getElementById("punto_b").value;
  
      let mapOptions = {
        center: { lat: 10.988609, lng: -74.7913632 }, // Cords de Barranquilla
        zoom: 12,
      };
  
      let mapa = new google.maps.Map(document.getElementById("mapa"), mapOptions);
  
      planificarRuta(direccionSalida, direccionDestino, mapa);
  
      return false;
    
  }
  
  function initializeAutocomplete(inputId) {
    const input = document.getElementById(inputId);
    const autocomplete = new google.maps.places.Autocomplete(input, {
      types: ["geocode"],
      componentRestrictions: { country: "CO" },
    });
  }
  
  // INICIO DE LA EJECUCION
  let mapa;
  
  window.onload = function () {
    initializeAutocomplete("punto_a");
    initializeAutocomplete("punto_b");
  
    // Configuracion Inicial de GMAPS
    let mapOptions = {
      center: { lat: 10.988609, lng: -74.7913632 }, // Cords de Barranquilla
      zoom: 12,
    };
  
    // Crear un mapa en el elemento con id "mapa"
    let mapa = new google.maps.Map(document.getElementById("mapa"), mapOptions);
  };
  