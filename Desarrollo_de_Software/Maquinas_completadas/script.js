let maquinas = [];

fetch("data/maquinas.json")
    .then(response => response.json())
    .then(data => {

        maquinas = data;

        mostrarMaquinas(maquinas);

    });

function mostrarMaquinas(lista){

    const catalogo = document.getElementById("catalogo");

    catalogo.innerHTML = "";

    lista.forEach(maquina => {

        catalogo.innerHTML += `
            <div class="card">

                <h2>${maquina.nombre}</h2>

                <span class="badge">
                    ${maquina.dificultad}
                </span>

                <p>
                    <strong>Sistema:</strong>
                    ${maquina.sistema}
                </p>

                <div class="tecnicas">

                    ${maquina.tecnicas
                        .map(tecnica =>
                            `<span class="tecnica">${tecnica}</span>`
                        )
                        .join("")}

                </div>

            </div>
        `;

    });

}

function buscarMaquina(){

    const texto =
        document.getElementById("nombre").value
            .toLowerCase();

    const resultado =
        maquinas.filter(maquina =>
            maquina.nombre
                .toLowerCase()
                .includes(texto)
        );

    mostrarMaquinas(resultado);

}