#!/bin/sh

url="https://raw.githubusercontent.com/davidshimjs/qrcodejs/master/qrcode.js"
output_file="static/js/qrcode.js"

# Download the file
curl -L -o "${output_file}" "${url}"