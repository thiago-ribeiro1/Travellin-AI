document.addEventListener("DOMContentLoaded", () => {
  const inpt = document.getElementById("message-input");
  const btn = document.getElementById("send-btn");
  const box = document.getElementById("chat-messages");
  const chips = document.getElementById("suggestion-chips");

  // Exibe os chips apenas se o chat estiver vazio
  if (box.children.length === 0) {
    chips.style.display = "flex";
  } else {
    chips.style.display = "none";
  }

  // Clique nos chips envia mensagem como prompt real
  chips.querySelectorAll("button").forEach((chip) => {
    chip.addEventListener("click", () => {
      const text = chip.textContent;
      inpt.value = text;
      sendMessage(text); // dispara envio
      chips.style.display = "none";
    });
  });

  async function sendMessage(customText = null) {
    const msg = customText || inpt.value.trim();
    if (!msg) return;

    // Mensagem do usuário
    const userDiv = document.createElement("div");
    userDiv.className = "message user-message";
    userDiv.textContent = msg;
    box.appendChild(userDiv);
    inpt.value = "";
    box.scrollTop = box.scrollHeight;

    // Mensagem do bot (Digitando...)
    const botDiv = document.createElement("div");
    botDiv.className = "message bot-message";
    botDiv.textContent = "Digitando...";
    box.appendChild(botDiv);
    box.scrollTop = box.scrollHeight;

    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg }),
      });

      const data = await res.json();
      botDiv.innerHTML = data.response;
    } catch {
      botDiv.textContent = "Erro ao obter resposta da IA.";
    }

    box.scrollTop = box.scrollHeight;
  }

  // Envio padrão com botão ou Enter
  btn.addEventListener("click", () => sendMessage());
  inpt.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  // Botão de limpar
  const clearBtn = document.getElementById("clear-btn");
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      box.innerHTML = "";
      chips.style.display = "flex";
    });
  }
});
