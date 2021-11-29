var editor1 = new RichTextEditor("#div_editor1"); //crea una variable del objeto RichTextEditor

//Funcion para descargar como PDF
function downloadPDFDialog() {
  editor1.execCommand("html2pdf");
}

function exportaJSON(){
  var hoy = new Date();              //Variable para crear un objeto fecha
  var obj = new Object();            //Variable para crear un objeto con los atributos del JSON

  sContent = editor1.getPlainText(); //Extrae el contenido del cuadro de texto en formato de texto plano

  obj.nombre_creador    = "Francisco Giacomozzi";
  obj.fecha_exportacion = hoy.getFullYear()+'-'+ (hoy.getMonth()+1)+'-'  + hoy.getDate();
  obj.hora_exportacion  = hoy.getHours() + ":" +  hoy.getMinutes() + ":" + hoy.getSeconds();
  obj.contenido         = sContent;

  var jsonString= JSON.stringify(obj); //Convierte el objeto a un string de json

  //Configuracion de encoding para la exportacion
  dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(jsonString);
  exportFileDefaultName = 'exportacion_data.json';

  //Crea un elemento de tipo a, para exportar el archivo
  linkElement = document.createElement('a');
  linkElement.setAttribute('href', dataUri);
  linkElement.setAttribute('download', exportFileDefaultName);
  linkElement.click();
}