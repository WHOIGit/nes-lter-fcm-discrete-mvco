## Compress FCS files

The `zip_fcs-files` script parses a control spreadsheet (`attune-transect-discrete-samples.csv`) to determine which FCS files need to be zipped, then produces the archives.

The script assumes that the files are grouped on disk by cruise, in directories named `yyyymmdd_{cruise ID}` and searches for them there based on the filenames provided in the control spreadsheet.

The result is one zip file per cruise containing the files specified in the spreadsheet.

Modify the data and output paths as needed.

The script has no dependencies and is written in base Python.
