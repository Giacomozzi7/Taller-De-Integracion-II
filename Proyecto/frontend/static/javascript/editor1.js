var editor1 = new RichTextEditor("#div_editor1");

function downloadPDFDialog() {
    editor1.execCommand("html2pdf");
}