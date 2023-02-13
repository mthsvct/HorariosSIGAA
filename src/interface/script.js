function pegaDia(lista){
    const dias = [0,'domingo','segunda','terça','quarta','quinta','sexta','sábado']
    let i, j;
    let indice = 0;
    let retorno = []
    console.log(lista);
    for(i = 0; i < lista.length; i++){
        console.log()
        while( isNaN(lista[i][j]) === false ){
            console.log(`${i} - ${j}`);
            indice = parseInt(lista[i][j]);
            retorno.push(dias[indice]);
            j = j + 1; 
        }
        j = 0;
    }
    
    return retorno;
}

function pegaTurno(horario){
    let i = 0;
    let indice = 0;
    let retorno = [];

    while(i < horario.length){
        if (isAlpha(horario[i]) === true){
            if(horario[i] === 'M'){
                retorno.push("Manhã");
            } else if(horario[i] === 'T'){
                retorno.push("Tarde");
            } else {
                retorno.push("Noite");
            }
        }
        i = i+1;
    }

    return retorno;
}

 
function isAlpha(ch){
    return /^[A-Za-z]{1,1}$/.test(ch)
}

function pegaHorarios(horario){
    let lista = horario.split(' ');
    let dia = pegaDia(lista);
    let turno = pegaTurno(lista);
    return `dia: ${dia} <br> turno: ${turno}`;
}


function mainHorarios(horario) {
    let r = document.getElementById('resultado');
    if (horario.length === 0){
        r.innerHTML = `<h2 class="red">Horário Invalido</h2><br/><p>Por favor, digite novamente.</p>`;
    } else {
        r.innerHTML = `${pegaHorarios(horario)}`
    }

}



const form = document.getElementById('formu');
form.addEventListener("submit", (e) => {
    e.preventDefault();
    let horario = e.target.cod.value
    mainHorarios(horario);
})





