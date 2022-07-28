import pdfkit

pdfkit.from_file("templates/template.html", "out.pdf", options={
  "enable-local-file-access": None
})