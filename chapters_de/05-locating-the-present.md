# V. Die Verortung der Gegenwart (fortlaufend, revisionsdatiert)

**Revisionsdatum: 09.09.2026.** Aktualisierung bei jedem datierten Faktum; alte Einträge niemals umschreiben, sondern anfügen. Jede nachfolgende Feststellung trägt ihr Datum; undatierte Behauptungen sind methodische Fehler.

`[construction: Abbildung 5.1 — das referenzierte FLIR-Bild wurde nie committet. Nach dem Caption-Brief unten rendern oder streichen.]`
*Abbildung 5.1: Simulierte multispektrale FLIR-Weitbereichsaufnahme vorderer Stellungen (Sprossen 21–25). Autonome lauernde FPV-Flugkörper und vierbeinige Bodensensoren überwachen menschenleere Brustwehren. Telemetrie-Zielboxen belegen automatisierte Zielerfassung ohne direkte Sichtlinie eines menschlichen Bedieners.*

## Die Einordnung

Mit Stand September 2026 befindet sich der Kriegsschauplatz Ukraine-Russland im Übergang von Band II zu Band III (Sprossen 13 bis 22). Die Grenze zwischen menschlich geführter Fernwaffengewalt und autonomer Maschinenausführung ist kein theoretischer Streitpunkt mehr; sie hat sich in operativen Millisekunden-Latenzen aufgelöst.

Die menschliche Genehmigung gilt in Vorschriften und diplomatischen Briefings nominell noch immer als Voraussetzung für den kinetischen Waffeneinsatz — im operativen Alltag ist sie jedoch eine Fiktion. Wenn die Annäherungsgeschwindigkeit 140 km/h erreicht und die elektronische Kampfführung das gesamte Funkspektrum ganzer Frontabschnitte lahmlegt, führt das Festhalten an einer menschlichen Lenkschleife unausweichlich zu Abfangen, Störung oder Totalverlust der Flugzelle.

Der Übergang von Band II (Überwachte Auslösung) zu Band III (Kontingent- und Sektorfreigabe) entsprang keiner vorausschauenden Doktrin. Er wurde von unten erzwungen: durch die Physik der Gegenmaßnahmen, den Zusammenbruch von Funkverbindungen und die schiere Masse lauernder Wirkmittel.

---

## 1. Die Glasfaserspule und die Verweigerung des Funkspektrums (2025–2026)

Das Standardmodell des Drohnenkrieges unterstellte, dass elektronische Kampfführung (EloKa) das entscheidende asymmetrische Gegenmittel bleiben würde: die Frequenzbänder bei 900 MHz, 1,2 GHz, 2,4 GHz und 5,8 GHz sättigen, die Videoübertragung kappen, die Steuerungsverbindung unterbrechen und das Wirkmittel wirkungslos in die Schwarzerde stürzen lassen.

Gegen Ende 2024 hatten russische und ukrainische EloKa-Komplexe Funkverbindungen an der Front über eine Tiefe von 10 bis 20 Kilometern streckenweise unbrauchbar gemacht. Die Antwort war kein Einstellen der Angriffe, sondern zwei parallele Mutationen:

1. **Physische spulengeführte Glasfaserverbindungen (Feldeinsatz Q1 2025–2026):** Extrem dünne Glasfaserspulen (10 bis 20 km Länge, Gewicht unter 1,2 kg) wickeln sich während des Flugs am Heck der Flugzelle ab. Die physikalische Glasverbindung liefert ungestörte, latenzfreie 4K-Telemetrie in den Unterstand und empfängt Steuerbefehle, vollkommen immun gegen Störsender. Einheiten mit Glasfaser-Flugzellen durchdrangen systematisch die gestaffelten Störblasen um Gefechtsstände und Flugabwehrbatterien.
2. **Autonome Endphasenlenkung (Feldeinsatz Mitte 2025–2026):** Da Glasfasern an Baumkronen, Stromleitungen und Trümmern reißen können, erwies sich die alternative Mutation als weit besser skalierbar: Edge-Rechnerplatinen (wie Rockchip RV1126 oder NVIDIA Jetson Orin Nano, direkt auf dem Rahmen verbaut), auf denen kompakte neuronale Netze laufen. Der Pilot steuert das Wirkmittel in einen Zielsektor. Sobald die Drohne in die Störzone eintaucht und das Videosignal abreißt, markiert der Pilot ein Fahrzeug oder einen Grabenabschnitt. Ab dieser Millisekunde steuert die bordgestützte visuelle Zielverfolgung die Ruder vollautomatisch. Die Funkverbindung stirbt ab; der Treffer erfolgt.

Der Wandel ist fundamental: Der Mensch steuert die Waffe nicht mehr ins Ziel. Er delegiert die Zielendphase an einen bordgestützten Tensor-Prozessor.

---

## 2. Strategische Marschflugkörper im Eigenbau: Die 1:100-Kosteninversion

Anfang 2026 demonstrierten ukrainische Tiefenangriffe gegen Ölraffinerien, Munitionsdepots und Militärflugplätze im Großraum Moskau die vollständige Inversion der Ökonomie strategischer Schläge.

Ein herkömmlicher westlicher Langstrecken-Marschflugkörper (wie Storm Shadow, SCALP-EG oder Tomahawk) schlägt mit Beschaffungskosten von 1.800.000 bis 3.200.000 Dollar pro Einheit zu Buche, gefertigt in mehrjährigen Lieferzyklen unter den Auflagen von Rüstungskonzernen und Exportbehörden.

Das ukrainische Eigenbau-Arsenal (repräsentiert durch Systeme wie *Liutyi*, *Bober* und modulare Nachfolgeflugkörper) erzielte Einsatzreichweiten von 1.000 bis 1.500 Kilometern durch:
- Kolbenmotoren aus zivilen Leichtflugzeug- und Drohnenkatalogen (8.000–15.000 $).
- Rümpfe aus glasfaserverstärktem Kunststoff und Kohlefaser, laminiert in dezentralen Leichtbau-Werkstätten.
- Multi-Konstellations-GNSS-Empfänger gekoppelt mit kommerziellen MEMS-Inertialsensoren und optischem Geländevergleich per Kamera.
- Stückkosten: 35.000 bis 80.000 Dollar pro Flugzelle.

Starten fünfzig dieser Flugkörper in einer koordinierten Welle gegen eine Raffinerie in den Gebieten Jaroslawl oder Rjasan, bricht die Luftverteidigungskalkulation zusammen. Der Schutz eines solchen Objekts erfordert den Einsatz von Abfangraketen von Systemen wie S-400 oder Patriot PAC-2/PAC-3. Ein einziger Patriot-Lenkflugkörper kostet zwischen 4.000.000 und 5.500.000 Dollar. Eine 48N6DM-Rakete der S-400 kostet rund 2.500.000 Dollar.

Der Abschuss von drei 4.000.000-Dollar-Lenkflugkörpern zur Zerstörung von drei 40.000-Dollar-Drohnen hinterlässt beim Verteidiger ein ökonomisches Defizit von 11.880.000 Dollar pro Salve — und einen leeren Startbehälter, dessen Nachproduktion 18 bis 24 Monate industrieller Vorlaufzeit beansprucht. Dringen zehn Drohnen durch, weil der Batterie die Munition ausgeht, brennt eine katalytische Spaltanlage im Wert von 500.000.000 Dollar ab.

Dies ist kein temporärer taktischer Vorteil; es ist der mathematische Bankrott der Luftverteidigungsarchitekturen des Kalten Krieges.

---

## 3. Vierbeinige Bodenrobotik und die entleerten Gräben (2025–2026)

Anfang 2026 waren die vorderen 5 Kilometer der Kontaktlinie für biologische Infanterie schlicht unbewohnbar geworden. Wärmebild-Aufklärungsdrohnen, die Tag und Nacht in überlappenden Rotationen kreisten, machten jede aufrecht gehende menschliche Gestalt innerhalb von 90 Sekunden aufklärbar und innerhalb von 180 Sekunden zielreif.

Die Infanterie wich vollständig unter die Erde aus, bezog tief eingegrabene Bunker und kommunizierte über Feldkabel. In dieser Umgebung wandelten sich bodengebundene Robotersysteme von spekulativer Zukunftsmusik zur Einsatzrealität:

```
+-------------------------------------------------------------------------+
|                  VORDERE PERIMETER-AUFKLÄRUNG                           |
|                                                                         |
|   [Unterirdischer Bunker / Unterstand]                                  |
|          | (Eingegrabenes Glasfaserkabel)                               |
|   [Oberflächenantenne / Relaisstation]                                  |
|          | (Verschlüsseltes Nahbereichs-Meshnetz)                       |
|          +---> [Unitree/Spot-Klasse Vierbeiner-Sensorplattform]         |
|                     - Eingegraben am Trichterrand                       |
|                     - Akustische Scharfschützen-Triangulation           |
|                     - Stabilisierter Optik-Gimbal & Wärmebildvisier     |
|                     - 12 Stunden stationäre Lauerstellung (Low-Power)   |
+-------------------------------------------------------------------------+
```

- **Unitree Go2 / B2 und modifizierte Vierbeiner-Derivate:** Eingesetzt von ukrainischen Verbänden (unter anderem der 28. mechanisierten Brigade) zur Grabenbereinigung, auf vorgeschobenen Horchposten und zur urbanen Aufklärung in Torezk und Tschassiw Jar.
- **Bewaffnete Rüstsätze:** Kommerzielle vierbeinige Fahrgestelle, ausgestattet mit rückstoßgedämpften Lafetten für Sturmgewehre, Panzerabwehrminen oder Sprengladungen.
- **Stationäre Lauerüberwachung:** Vierbeiner bewegen sich autonom an Trichterränder, verharren im Energiesparmodus bis zu 14 Stunden flach am Boden und dienen als lautlose Perimeter-Stolperdrähte. Registrieren ihre Mikrofone Schritte oder Schussgeräusche, aktivieren sie den Optikturm, übermitteln Zielkoordinaten und kehren in den Ruhezustand zurück.

Der biologische Soldat ist aus dem Beobachtungsgraben vollständig verdrängt. Er verbleibt 800 Meter rückwärts und blickt auf einen geteilten Kontrollbildschirm.

---

## 4. Die Reaktion des UN-Hochkommissars Volker Türk und das Dementi-Muster (September 2026)

In der Woche des 8. September 2026 warnte der UN-Hochkommissar für Menschenrechte, Volker Türk, öffentlich und mit deutlicher Schärfe vor Berichten von den Gefechtsfeldern Osteuropas, wonach vollautonome Tötungsdrohnen in aktiven Kampfzonen operierten.

Die institutionelle Reaktion der kriegführenden Staaten folgte exakt dem klassischen Dementi-Muster:
1. **Öffentliches Bestreiten tödlicher Autonomie:** Militärsprecher aus Kiew und Moskau versicherten umgehend, sämtliche Waffensysteme stünden unter strikter menschlicher Kontrolle, und bekräftigten die Einhaltung des humanitären Völkerrechts.
2. **Die Fiktion des „Mensch in der Schleife“:** Wo autonome Tracking-Algorithmen und automatische Endphasenlenkung in Wrackteilen und Telemetrieprotokollen nachgewiesen wurden, deklarierten Militärsprecher den Mechanismus als „bedienerunterstützte Zielführung“ oder „automatisierte Stabilisierung“.
3. **Operative Realität:** An der Nulllinie hat der menschliche Bediener in der Schleife ein effektives Eingriffsfenster von 200 bis 400 Millisekunden, bevor der Sturzflug einsetzt. Der Bediener zielt nicht; er verzichtet lediglich auf den Abbruch. Ein Freigabemechanismus, der standardmäßig zuschlägt, sofern er nicht innerhalb von 300 Millisekunden gestoppt wird, ist eine autonome Waffe mit vorgeschaltetem juristischem Haftungspuffer.

---

## 5. Empirische Bewertung der Sprossen

| Datum | Gefechtsfeldfaktum / Telemetrie | Manifestierte Sprosse | Status |
|---|---|---|---|
| **Q3 2024** | Breiter Einsatz optischer Edge-KI-Zielverfolgung auf FPV-Flugzellen (automatischer Endphasen-Lock). | **Sprosse 10** (Sensorfusionierte Zielnominierung) | Öffentliche Telemetrie bestätigt |
| **Q1 2025** | Einsatz spulengeführter Glasfaser-FPVs bis 15 km Reichweite zur Umgehung von Breitband-EloKa-Störzonen. | **Sprosse 11** (Bandbreitenbegrenzte Maschinendelegation) | Im Einsatz, Beutegeräte katalogisiert |
| **Q3 2025** | Autonome Vierbeiner-Robotik in Grabenaufklärung und akustischer Lauerstellung. | **Sprosse 16** (Persistente lauernde Jäger) | Video- & Truppendokumentation verifiziert |
| **Q1 2026** | Massierte Eigenbau-Langstrecken-Marschflugkörper sättigen strategische Luftverteidigungszonen. | **Sprosse 14** (Asymmetrische Salven strategischer Wirkmittel) | Bestätigte Treffer im russischen Hinterland |
| **09.2026** | UN-Erklärung Volker Türk zu autonomen Tötungsdrohnen; öffentliche Dementis bei Subsekunden-Freigaben. | **Sprossen 18–20** (Stapelgenehmigung & Blanko-Delegation) | Institutionelles Eingeständnis via Krisenreaktion |

Die Gegenwart steht unmittelbar vor Band III. Die Rahmenbedingungen des modernen Gefechts haben das Prinzip „Ein Mensch, eine Waffe“ obsolet gemacht. Was als Nächstes folgt, ist die automatisierte Koordination ganzer Schwärme.
