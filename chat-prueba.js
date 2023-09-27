document.addEventListener('DOMContentLoaded', () => {
   // const socket = io.connect('http://localhost:5000'); //  URL del servidor

    const socket = io('http://127.0.0.1:5000');

    const mensajeList = document.getElementById('mensaje-list');
    const mensajeInput = document.getElementById('mensaje-input');
    const enviarBtn = document.getElementById('enviar-btn');

    enviarBtn.addEventListener('click', () => {
        const mensaje = mensajeInput.value;
        if (mensaje.trim() !== '') {
            socket.emit('nuevo_mensaje', mensaje);
            mensajeInput.value = '';
        }
    });

    socket.on('mensaje_recibido', (data) => {
        const listItem = document.createElement('li');
        listItem.textContent = data;
        mensajeList.appendChild(listItem);
        mensajeList.scrollTop = mensajeList.scrollHeight; // Desplazamiento automático hacia abajo
    });
});
