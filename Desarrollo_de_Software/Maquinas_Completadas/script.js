let machines = [];

function crearTarjeta(machine, index) {
    let herramientasHTML = machine.Herramientas.map(h => `<span class="tag-herramienta">${h}</span>`).join('');

    let tieneWalkthrough = machine.Walkthrough && machine.Walkthrough.trim().length > 0;
    let botonWalkthrough = tieneWalkthrough
        ? `<button class="btn-walkthrough" onclick="abrirWalkthrough(${index})">📖 Ver Walkthrough</button>`
        : `<button class="btn-walkthrough btn-walkthrough-disabled" disabled>📖 Walkthrough próximamente</button>`;

    return `
        <div class="cuadro">
            <div class="nom"><h1>${machine.Nombre}</h1></div>
            <div class="caracter">
                <p class="Os">Os: ${machine.Os}</p>
                <p class="Dificultad">${machine.Dificultad}</p>
            </div>
            <div class="herramientas-container">
                ${herramientasHTML}
            </div>
            <div class="walkthrough-container">
                ${botonWalkthrough}
            </div>
        </div>
    `;
}

function renderizarLista(lista) {
    if (lista.length === 0) {
        document.getElementById("resultado").innerHTML = `
            <div class="error">⚠️ Maquina no Encontrada</div>
        `;
        return;
    }

    let html = "";
    for (let i = 0; i < lista.length; i++) {

        const indexGlobal = machines.indexOf(lista[i]);
        html += crearTarjeta(lista[i], indexGlobal);
    }
    document.getElementById("resultado").innerHTML = html;
}

async function mostrar() {
    const response = await fetch("maquinas.json");
    machines = await response.json();
    renderizarLista(machines);
}

function mostrarTodas() {
    document.getElementById("nombre").value = "";
    renderizarLista(machines);
}

function buscar() {
    const texto = document.getElementById("nombre").value.trim().toLowerCase();

    if (texto === "") {
        renderizarLista(machines);
        return;
    }

    const encontradas = machines.filter(m => m.Nombre.toLowerCase().includes(texto));
    renderizarLista(encontradas);
}

document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("nombre");
    if (input) {
        input.addEventListener("keyup", (e) => {
            if (e.key === "Enter") buscar();
        });
    }
});

function abrirWalkthrough(index) {
    const machine = machines[index];
    if (!machine || !machine.Walkthrough) return;

    document.getElementById("modalTitulo").innerText = machine.Nombre;
    document.getElementById("modalContenido").innerHTML = marked.parse(machine.Walkthrough);
    document.getElementById("modalOverlay").classList.add("activo");
    document.body.style.overflow = "hidden";
}

function cerrarWalkthrough() {
    document.getElementById("modalOverlay").classList.remove("activo");
    document.body.style.overflow = "auto";
}

document.addEventListener("click", (e) => {
    if (e.target.id === "modalOverlay") cerrarWalkthrough();
});
document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") cerrarWalkthrough();
});

mostrar();
