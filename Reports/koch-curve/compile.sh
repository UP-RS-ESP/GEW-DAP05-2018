pandoc --highlight-style kate \
    --variable papersize=a4paper \
    -s report.md -o report.pdf && zathura report.pdf
