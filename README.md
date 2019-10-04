# Ausgangslage
Aufgrund der vielen unbrauchbaren Kryptowährungsrechner mit falschen Kursen und der Unübersichtlichkeit dieser aufgrund zu vieler irrelevanten Währungen, wäre es sinnvoll, seinen eigenen Währungsrechner zu erstellen. So kann ich nur die für mich relevanten 5 - 10 Kryptowährungen berücksichtigen und behalte so die Übersicht.

# Funktion/Projektidee
Die Funktion sollte den aktuellen Kurs von Kryptowährungen von der Webseite https://coinmarketcap.com entnehmen und in einer Art Datenbank speichern. Zusätzlich sollten diese Daten automatisch bei einer Kursänderung aktualisiert werden. Des Weiteren sollte es möglich sein, eine Art Währungsrechner daraus bilden zu können, um eine bestimmte Menge einer Kryptowährung in den Kurs einer anderen umrechnen zu können.
# Workflow
## Dateneingabe
Die Daten werden der Webseite https://coinmarketcap.com entnommen.
## Datenverarbeitung/Speicherung
Die Daten sollten sich automatisch bei einer Kursänderung, oder falls dies zu komplex wäre, stündlich oder minütlich aktualisieren und in einer .json-Datei abspeichern.
## Datenausgabe
Die Datenausgabe erfolgt über eine Webaplikation, welche durch eine Funktion die Kursdaten aus der .json-Datei entnimmt und  im Währungsrechner ausgibt.

![alt text](flowchart.png)