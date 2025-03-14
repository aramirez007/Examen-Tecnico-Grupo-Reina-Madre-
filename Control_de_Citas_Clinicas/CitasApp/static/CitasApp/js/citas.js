$( document ).ready(function() {

        $('.cita-tipo').each(function(){
            var tipo = $(this).text();
            tipo = parseInt(tipo);
    
            if(tipo == 1){
                $(this).text('Consulta');
    
            }else if(tipo == 2){
                $(this).text('Servicio');
    
            }else if(tipo == 3){
                $(this).text('Tratamiento');
    
            }else if(tipo == 4){
                $(this).text('Otro');
    
            }else{
                $(this).text('');
            }
        });

});