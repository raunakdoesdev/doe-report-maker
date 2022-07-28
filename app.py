import pdfkit
import subprocess

options = {
  "enable-local-file-access": None,
  'margin-top': '0in',
  'margin-right': '0in',
  'margin-bottom': '0in',
  'margin-left': '0in'}


subprocess.call(["lessc", "templates/compiled-styles.css", "templates/simple-styles.css"])
pdfkit.from_file("templates/filled-template.html", "out.pdf", options=options, css="templates/simple-styles.css")