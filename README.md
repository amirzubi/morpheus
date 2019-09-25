<h1>Ausgangslage</h1><br>

<h1>Funktion/Projektidee<h1><br>
Die Funktion sollte den aktuellen Kurs von Kryptowährungen von der Webseite https://coinmarketcap.com entnehmen und in einer Art Datenbank speichern. Zusätzlich sollten diese Daten automatisch bei einer Kursänderung aktualisiert werden. Des Weiteren sollte es möglich sein, eine Art Währungsrechner daraus bilden zu können, um eine bestimmte Menge einer Kryptowährung in den Kurs einer anderen umrechnen zu können.
<h1>Workflow<h1><br>
<h2>Dateneingabe<h2><br>
Die Daten werden der Webseite https://coinmarketcap.com entnommen.<br>
<h2>Datenverarbeitung/Speicherung<h2><br>
Die Daten sollten sich automatisch bei einer Kursänderung, oder falls dies zu komplex wäre, stündlich oder minütlich aktualisieren und in einer .json-Datei abspeichern.<br>
<h2>Datenausgabe<h2><br>
Die Datenausgabe erfolgt über eine Webaplikation, welche die Daten aus der .json-Datei herauszieht.