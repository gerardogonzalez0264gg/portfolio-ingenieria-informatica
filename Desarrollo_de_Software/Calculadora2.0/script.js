function agregar(valor){
    document.getElementById("pantalla").value += valor;
}

function limpiar(){

    document.getElementById("pantalla").value = "";

}

function calcular(){
  let res = eval(document.getElementById("pantalla").value);
    document.getElementById("pantalla").value = res;
}