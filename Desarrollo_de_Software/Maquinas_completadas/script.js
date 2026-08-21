let machines = [];

async function mostrar(){
    const response = await fetch("maquinas.json");
    machines = await response.json();

    let html="";

    for(machine of machines){
        
        let herramientasHTML = machine.Herramientas.map(h => `<span class="tag-herramienta">${h}</span>`).join('');

        html +=`
        
            <div class=cuadro>
                
                <div class="nom"><h1>${machine.Nombre}</h1></div> <br> 
                <div class="caracter">
                    <p class="Os">Os: ${machine.Os} <br></p>
                    <p class="Dificultad">${machine.Dificultad}<br></p>
                    </div>
                    <div class="herramientas-container">
                        ${herramientasHTML}
                    </div>
                    
                </div>
                
            </div>
        `;
    }

    document.getElementById("resultado").innerHTML=html;


}

function buscar(){
    const name = document.getElementById("nombre").value;
    const maquina = machines.find(m => m.Nombre === name);

    if(maquina){
        document.getElementById("resultado").innerHTML=`
            <div class=cuadros>
                
                <<div class="nom"><h1>${machine.Nombre}</h1></div> <br> 
                <div class="caracter">
                    <p class="Os">Os: ${machine.Os} <br></p>
                    <p class="Dificultad">${machine.Dificultad}<br></p>
                    </div>
                    <div class="herramientas-container">
                        ${herramientasHTML}
                    </div>
                    
                </div>
                
            </div>
        `;
    }else{
        
        document.getElementById("resultado").innerHTML=`
        <div class="error">
            ⚠️ Maquina no Encontrada
        </div>
        `;

    }
}

mostrar();