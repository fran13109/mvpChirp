let lastGeneratedAudio = null;


async function generateAudio() {
    const text = document.getElementById("textInput").value.trim();
    const voice = document.getElementById("voiceSelect").value;

    if (!text) return alert("Escribe algo de texto primero");

    const mainAudio = document.getElementById("mainAudio");
    mainAudio.pause();
    mainAudio.src = "";

    const button = document.getElementById("generateButton");
    button.disabled = true;
    button.textContent = "Generating...";

    try {
        const formData = new FormData();
        formData.append("texto", text);
        formData.append("voz", voice);

        const response = await fetch("/generate", {
            method: "POST",
            body: formData
        });

        if (!response.ok) throw new Error("Error generating audio");

        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        mainAudio.src = url;
        mainAudio.play();

        const contentDisposition = response.headers.get("Content-Disposition");
        if (contentDisposition) {
            const match = contentDisposition.match(/filename="?(.+)"?/);
            if (match) lastGeneratedAudio = match[1];
        }

        loadAudios();

    } catch (err) {
        console.error(err);
        alert(err.message);
    } finally {
        button.disabled = false;
        button.textContent = "Generate Audio";
    }
}

async function loadAudios() {
    const container = document.getElementById("audiosContainer");
    container.innerHTML = "Loading...";

    try {
        const response = await fetch("/audios");
        if (!response.ok) throw new Error("Error loading audios");

        const data = await response.json();
        container.innerHTML = "";

        if (data.audios.length === 0) {
            container.innerHTML = "<p>No audios generated yet</p>";
            return;
        }

        data.audios.forEach(filename => {
            if (filename === lastGeneratedAudio) return;

            const audioElem = document.createElement("audio");
            audioElem.controls = true;
            audioElem.src = `/output/${filename}`;
            audioElem.style.marginBottom = "10px";
            container.appendChild(audioElem);
        });

    } catch (err) {
        console.error(err);
        container.innerHTML = "<p>Error loading audios</p>";
    }
}

document.getElementById("generateButton").addEventListener("click", generateAudio);
window.addEventListener("load", loadAudios);
