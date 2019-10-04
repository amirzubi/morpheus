# Ausgangslage
Viele Kryptoportfolioapps brauchen entweder viel Speicher oder haben nicht die aktuellsten Kurse. Des Weiteren möchte ich meine vertraulichen Daten nicht einer App zur Verfügung stellen. Hierbei sollte eine individuelle Lösung Abhilfe schaffen.

# Funktion/Projektidee
Dem User sollte es möglich sein, sein eigenes Kryptowährungsportfolio zu erstellen. Hierzu sollte es ihm möglich sein, selbst Kryptowährungen dem Portfolio hinzuzufügen oder zu löschen. Zusätzlich kann der Betrag der jeweiligen Währungen angegeben werden. Die Funktion sollte den aktuellen Kurs der Kryptowährungen von der Webseite https://coinmarketcap.com entnehmen und dem User live wiedergeben. Zusätzlich sollten diese Daten automatisch bei einer Kursänderung aktualisiert werden. Der Gesamtwert des Portfolios und die minütige Änderungen dessen sollte dem User angezeigt werden. Zusätzlich könnte ein Diagramm angezeigt werden, welches die wöchtentliche  Veränderung des Gesamtwertes des Portfolios darlegt.
# Workflow
## Dateneingabe
Der User kann Kryptowährungen dem Portfolio hinzufügen oder löschen. Er kann zusätzlich den Betrag der jeweiligen Währung festlegen.
## Datenverarbeitung/Speicherung
Die Kursdaten werden der Webseite https://coinmarketcap.com entnommen. Die Daten sollten sich automatisch bei einer Kursänderung aktualisieren. Die Portfolioeinträge des Users werden in einer .json Datei gesichert.
## Datenausgabe
Die Webapplikation sollte die aktuellen Kurse und den Totalwert der einzelnen Portfolioeinträge wiedergeben. Dabei wird folgendes gerechnet:<br><br>```betrag_bitcoin * kurs_bitcoin```<br><br>
Zusätzlich sollte der Gesamtwert des Portfolios ausgegeben werden. Dabei wird folgendes gerechnet:<br><br>    (Betrag Kryptowährung 1 * Kurs Kryptowährung 1) + (Betrag Kryptowährung 2 * Kurs Kryptowährung 2)... 

![alt text](flowchart.png)