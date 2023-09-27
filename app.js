// document.addEventListener('DOMContentLoaded', function() {
//     // Configura la URL de la API (reemplaza con la dirección de tu backend)
//     const apiUrl = 'http://127.0.0.1:5000/api';

//     function obtenerMensajes() {
//         fetch(`${apiUrl}/mensajes`)
//             .then(response => response.json())
//             .then(data => {
//                 const chatMessages = document.getElementById('chat-messages');
//                 chatMessages.innerHTML = '';
//                 data.forEach(message => {
//                     const mensaje = document.createElement('li');
//                     mensaje.innerHTML = `<strong>${message.usuario}:</strong> ${message.mensaje}`;
//                     chatMessages.appendChild(mensaje);
//                 });
//             })
//             .catch(error => console.error('Error al obtener mensajes:', error));
//     }

//     obtenerMensajes();

//     const botonEnviar = document.getElementById('enviar');
//     const inputMensaje = document.getElementById('mensaje');

//     botonEnviar.addEventListener('click', function() {
//         const mensaje = inputMensaje.value;
//         const usuario = 'Usuario';  // Puedes obtener el nombre del usuario de tu sistema de autenticación

//         const data = { mensaje, usuario };

//         fetch(`${apiUrl}/enviar_mensaje`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify(data),
//         })
//         .then(response => response.json())
//         .then(responseData => {
//             console.log(responseData); // Aquí puedes manejar la respuesta del servidor
//             obtenerMensajes(); // Actualiza los mensajes después de enviar uno nuevo
//         })
//         .catch(error => console.error('Error al enviar mensaje:', error));

//         inputMensaje.value = '';
//     });
// });



document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'http://127.0.0.1:5000/api';
    const chatMessages = document.getElementById('chat-messages');
    const botonEnviar = document.getElementById('enviar');
    const inputMensaje = document.getElementById('mensaje');

    function agregarMensaje(message) {
        const mensaje = document.createElement('li');
        mensaje.innerHTML = `<strong>${message.usuario}:</strong> ${message.mensaje}`;
        chatMessages.appendChild(mensaje);
    }

    //obtenemos lo mensajes de la base de datos falsa
    function obtenerMensajes() {
        fetch(`${apiUrl}/mensajes`)
            .then(response => response.json())
            .then(data => {
                chatMessages.innerHTML = ''; // Borra los mensajes existentes antes de agregar nuevos
                data.forEach(message => {
                    agregarMensaje(message);
                });
            })
            .catch(error => console.error('Error al obtener mensajes:', error));
    }

    obtenerMensajes();

    botonEnviar.addEventListener('click', function() {
        const mensaje = inputMensaje.value;
        const usuario = 'Usuario';  // Puedes obtener el nombre del usuario de tu sistema de autenticación
        console.log('mensaje', mensaje);

        const data = { mensaje, usuario };

        fetch(`${apiUrl}/enviar_mensaje`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(responseData => {
            console.log(responseData); // Aquí puedes manejar la respuesta del servidor
            obtenerMensajes(); // Actualiza los mensajes después de enviar uno nuevo
        })
        .catch(error => console.error('Error al enviar mensaje:', error));

        inputMensaje.value = '';
    });

    // Actualiza el chat automáticamente cada 1 segundos
    setInterval(obtenerMensajes, 1000); // 1000 ms = 1 segundos
});













// document.addEventListener('DOMContentLoaded', function() {
//     // Configura la URL del servidor WebSocket (reemplaza con la dirección de tu backend)
//     const socket = io('http://127.0.0.1:5000'); // Reemplaza 'direccion-de-tu-backend' con la URL de tu servidor WebSocket

//     const chatMessages = document.getElementById('chat-messages');
//     const botonEnviar = document.getElementById('enviar');
//     const inputMensaje = document.getElementById('mensaje');

//     function agregarMensaje(message) {
//         const mensaje = document.createElement('li');
//         mensaje.innerHTML = `<strong>${message.usuario}:</strong> ${message.mensaje}`;
//         chatMessages.appendChild(mensaje);
//     }

//     // Escucha el evento 'mensaje_nuevo' y agrega el mensaje a la lista
//     socket.on('enviar_mensaje', function(message) {
//         agregarMensaje(message);
//     });

//     // Función para obtener y mostrar mensajes existentes al cargar la página
//     function obtenerMensajes() {
//         fetch('http://127.0.0.1:5000/api/mensajes') // Reemplaza 'direccion-de-tu-backend' con la URL de tu servidor backend
//             .then(response => response.json())
//             .then(data => {
//                 data.forEach(message => {
//                     agregarMensaje(message);
//                 });
//             })
//             .catch(error => console.error('Error al obtener mensajes:', error));
//     }

//     obtenerMensajes();

//     botonEnviar.addEventListener('click', function() {
//         const mensaje = inputMensaje.value;
//         const usuario = 'Usuario';  // Puedes obtener el nombre del usuario de tu sistema de autenticación
//         console.log('mensaje', mensaje);

//         const data = { mensaje, usuario };

//         // Envía el mensaje al servidor a través del WebSocket
//         socket.emit('enviar_mensaje', data);


//         fetch('http://127.0.0.1:5000/api/enviar_mensaje', {
//                         method: 'POST',
//                         headers: {
//                             'Content-Type': 'application/json',
//                         },
//                         body: JSON.stringify(data),
//                     })
//                     .then(response => response.json())
//                     .then(responseData => {
//                         console.log(responseData); // Aquí puedes manejar la respuesta del servidor
//                         obtenerMensajes(); // Actualiza los mensajes después de enviar uno nuevo
//                     })
//                     .catch(error => console.error('Error al enviar mensaje:', error));

//         inputMensaje.value = '';
//     });
// });

