function atualizaFormCadastro(escolha){
    switch(escolha){
        case 'objetos':
            var HTML = '<fieldset class = "border p-2">' +
                '<legend id = "legenda">Cadastro</legend>' +
                '<div class = "row">' +
                    '<div class = "col-8 offset-2">' +
                        '<input class = "form-control" type = "text" name = "nome" placeholder = "Nome">' +
                    '</div>' +
                '</div>' +
                '<br/>'+
                '<div class = "row">' +
                    '<div class = "col-4 offset-2">' +
                        '<select class = "form-control" name = "categoria" id = "selectCategorias"></select>' +
                    '</div>' +
                    '<div class = "col-4">' +
                        '<input class = "form-control-file" type = "file" name = "imagem" accept = "image/*"/>'+
                    '</div>' +
                '</div>'+
                '<br/>' +
                '<div class = "row">' +
                    '<div class = "col-4 offset-2">' +
                        '<button type = "button" class = "btn btn-primary" onclick = "cadastrarItens(\'objetos\')">Cadastrar</button>' +
                    '</div>' +
                    '<div class = "col-4">' +
                        '<button class = "float-right btn btn-danger" type = "reset">Limpar</button>' +
                    '</div>' +
                '</div>' +
            '</fieldset>';

            $("#formularioSub").html(HTML);

            $.ajax({type: "GET", data: {operacao: "categorias"}, url: 'http://localhost:3000/', success: function(data){
                var HTML;

                for(i = 0; i < data.length; i++){
                    HTML += "<option value = '" + data[i][0] + "'>" + data[i][1] + "</option>";
                }

                $("#selectCategorias").html(HTML);
            }});
            break;
        case 'categorias':
            var HTML = '<fieldset class = "border p-2">' +
                '<legend>Cadastro</legend>' +
                '<div class = "row">' +
                    '<div class = "col-4 offset-2">' +
                        '<input class = "form-control" type = "text" name = "nome" placeholder = "Nome">' +
                    '</div>' +
                    '<div class = "col-4">' +
                        '<input class = "form-control-file" type = "file" name = "imagem" accept="image/*"/>'+
                    '</div>' +
                '</div>' +
                '<br/>' +
                '<div class = "row">' +
                    '<div class = "col-4 offset-2">' +
                        '<button type = "button" class = "btn btn-primary" onclick = "cadastrarItens(\'categorias\')">Cadastrar</button>' +
                    '</div>' +
                    '<div class = "col-4">' +
                        '<button class = "float-right btn btn-danger" type = "reset">Limpar</button>' +
                    '</div>' +
                '</div>' +
            '</fieldset>';

            $("#formularioSub").html(HTML);
            break;
    }


}

function cadastrarItens(tipo){
    var dadosFormulario = new FormData();

    switch(tipo){
        case 'objetos':
            dadosFormulario.append('operacao', 'objetos');
            dadosFormulario.append('nome', $("input[name=nome]").val());
            dadosFormulario.append('imagem', $('input[type=file]')[0].files[0]);
            dadosFormulario.append('categoria', $("select[name=categoria]").val());

            break;
        case 'categorias':
            dadosFormulario.append('operacao', 'categorias');
            dadosFormulario.append('nome', $("input[name=nome]").val());
            dadosFormulario.append('imagem', $('input[type=file]')[0].files[0]);

            break;
    }

    $.ajax({ url: 'http://localhost:3000/', type: "post", enctype: 'multipart/form-data', data: dadosFormulario, cache: false, contentType: false, processData: false, success: function(data){location.reload(true)}});
}

function atualizaTabela(tipo){
    switch(tipo){
        case 'objetos':
            $("#thead").html("<th scope = 'col'>#</th><th scope = 'col'>NOME</th><th scope = 'col'>CATEGORIA</th><th scope = 'col'>EDITAR</th><th scope = 'col'>EXCLUIR</th>");

            $.ajax({type: "GET", data: {operacao: "objetos"}, url: 'http://localhost:3000/', success: function(data){
                console.log(data);
                var HTML;

                for(i = 0; i < data.length; i++){
                    HTML += "<tr>"+
                        "<td scope = 'col'>" + data[i][0] + "</td>"+
                        "<td scope = 'col'>" + data[i][1] + "</td>"+
                        "<td scope = 'col'>" + data[i][3] + "</td>"+
                        "<td scope = 'col'><button class = 'btn btn-primary' data-toggle = 'modal' data-target = '#modal' onclick = 'geraDadosModal(\"objetos\", "+ data[i][0] +")'>Editar</button></td>"+
                        "<td scope = 'col'><button class = 'btn btn-danger' onclick = 'excluirObjeto(\"objetos\", " + data[i][0] + ")'>Excluir</button></td>"+
                    "</tr>";
                }

                $("#tbody").html(HTML);
            }});

            break;
        case 'categorias':
            $("#thead").html("<th scope = 'col'>#</th><th scope = 'col'>NOME</th><th scope = 'col'>EDITAR</th><th scope = 'col'>EXCLUIR</th>");

            $.ajax({type: "GET", data: {operacao: "categorias"}, url: 'http://localhost:3000/', success: function(data){
                var HTML;

                for(i = 0; i < data.length; i++){
                    HTML += "<tr>"+
                        "<td scope = 'col'>" + data[i][0] + "</td>"+
                        "<td scope = 'col'>" + data[i][1] + "</td>"+
                        "<td scope = 'col'><button class = 'btn btn-primary' data-toggle = 'modal' data-target = '#modal' onclick = 'geraDadosModal(\"categoria\", "+ data[i][0] +")'>Editar</button></td>"+
                        "<td scope = 'col'><button class = 'btn btn-danger' onclick = 'excluirObjeto(\"categorias\", " + data[i][0] + ")'>Excluir</button></td>"+
                    "</tr>";
                }

                $("#tbody").html(HTML);
            }});

            break;
    }
}

function excluirObjeto(tipoObjeto, id){
    if(confirm('Você tem certeza?')){
        $.ajax({url: 'http://localhost:3000/', type: 'DELETE', data: {tabela: tipoObjeto, objeto: id}, success: function(data){location.reload(true)}});
    }
}

function geraDadosModal(tipo, id){
    switch(tipo){
        case 'objetos':
            $.ajax({type: "GET", data: {operacao: "categoriaEspecifica", id: id}, url: 'http://localhost:3000/', success: function(data){

            }});
            break;
        case 'categorias':

            break;
    }
}
