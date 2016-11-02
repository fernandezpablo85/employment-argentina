# What's this?

The INDEC (meaning "Instituto Nacional de Estadística y Censos", or National Institute of Statistics and Census) just [published a report](http://www.indec.gob.ar/uploads/informesdeprensa/erl_10_16.pdf) on Argentinan labor and workforce.

Although the data is great, the visualization is lacking.

We'll try to fix that, while keeping the data, the tools and the process open for everyone to audit, learn and criticise.

## Cleanup Process (so far)

1. *really raw* data is on `.xls` in the [raw folder](https://github.com/fernandezpablo85/employment-argentina/tree/master/raw).
2. take the information from the `.xls` and save it as plain text on the [raw/txt](https://github.com/fernandezpablo85/employment-argentina/tree/master/raw/txt) folder (follow the naming convention).
3. note that there are many sheets per `.xls`, each one should be it's own `.txt` file.
4. run `cleanup.py` passing in the `.txt` file as standard input (e.g. `> python cleanup.py < ./raw/txt/some.file.txt`).
5. save the output as a `.csv` file on the [csv](https://github.com/fernandezpablo85/employment-argentina/tree/master/csv) folder.
6. make sure to pick the appropiate facto by modifying the chosen factor variable on [`cleanup.py`](https://github.com/fernandezpablo85/employment-argentina/blob/master/cleanup.py#L91)

## Inspiration

[NYT recesssion chart](http://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html)
