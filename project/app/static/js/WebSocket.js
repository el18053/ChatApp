    //const roomName = JSON.parse(document.getElementById('roomname').textContent);
    const roomName = "user1_user2_user3"
    const chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/chat/'
        + roomName
        + '/'
    );
    chatSocket.onopen = function (e) {
        console.log("The connection was set up successfully!");
    };
    chatSocket.onclose = function (e) {
        console.log("Something unexpected happened!");
    };
    document.querySelector("#id_message_send_input").focus();
    document.querySelector("#id_message_send_input").onkeyup = function (e) {
        if (e.keyCode == 13) {
            document.querySelector("#id_message_send_button").click();
        }
    };
    document.querySelector("#id_message_send_button").onclick = function (e) {
        var messageInput = document.querySelector("#id_message_send_input").value;
        var currentTime = new Date();
        var time = currentTime.toLocaleTimeString();
        chatSocket.send(JSON.stringify({
            message: messageInput,
            username: "{{request.user.username}}",
            time: time
        }));
    };
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        var messageContainer = document.querySelector("#id_chat_item_container");
        var div = document.createElement("div");
        div.className = (data.username === "{{request.user.username}}") ? "chat-message right" : "chat-message left";
        div.innerHTML = `<div class="message-content">
            <span class="message-username">${data.username.charAt(0).toUpperCase() + data.username.slice(1)}</span>
            <span class="message-text">${data.message}</span>
            <span class="message-timestamp">${data.time}</span>
        </div>`;
        document.querySelector("#id_message_send_input").value = "";
        messageContainer.appendChild(div);
        // Scroll to the bottom of the chat container
        messageContainer.scrollTop = messageContainer.scrollHeight;
    };