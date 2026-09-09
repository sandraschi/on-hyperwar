# VII. Der Kontrollnachweis und warum er scheitert

## These

Zertifizierungen für „Mensch in/auf der Schleife“ beglaubigen zumeist Papier: Tests an gestriger Software, nachträglich definierte Einsatzgrenzen und Übersteuerungsfunktionen, für deren Ausführung keinem Bediener die kognitive oder physische Reaktionszeit zur Verfügung steht. Ein Kontrollnachweis (*Control Case*), der unter Gefechtsdruck kein im Feld befindliches System disqualifizieren kann, ist kein Steuerungsmechanismus — er ist ein juristischer Haftungsschild.

![Konstruktionszeichnung einer vierbeinigen Aufklärungs- und Wirkmittelplattform](dogbot_blueprint.jpg)
*Abbildung 7.1: Technische Schemazeichnung eines modularen Vierbeiner-Fahrgestells mit Obergurt-Sensorgehäuse, stabilisiertem 3-Achsen-Optik-Gimbal und multispektraler Akustik-Messbasis. Die mechanische und elektronische Ansprechzeit ($< 15\text{ ms}$) macht biologische Handsteuerung obsolet.*

---

## 1. Die Anatomie eines belastbaren Kontrollnachweises

Ein methodisch valider Kontrollnachweis kann sich nicht auf Absichtserklärungen, Ethik-Kodizes oder Dienstvorschriften stützen. Um Kahns Standard institutioneller Beobachtbarkeit (Regel 1) zu genügen, muss ein Kontrollnachweis drei empirische Metriken ausweisen, die unabhängig über Telemetriedaten auditierbar sind:

1. **Nominierungs-zu-Zustimmungs-Intervall ($\Delta t_{\text{consent}}$):** Die exakte Zeitspanne zwischen der Präsentation eines Zielkandidaten durch das System und der Registrierung der menschlichen Freigabe. Gilt $\Delta t_{\text{consent}} < 400\text{ ms}$, kann der Mensch die visuelle Szene nicht kognitiv erfassen; der Bediener fungiert lediglich als biologisches Relais zur Schließung eines Stromkreises.
2. **Zurückweisungshäufigkeit ($R_{\text{target}}$):** Der Prozentsatz maschinell vorgeschlagener Ziele, die von menschlichen Bedienern im Hochfrequenzgefecht explizit abgelehnt oder abgebrochen werden. Eine Ablehnungsrate nahe null ($R_{\text{target}} < 1\%$) belegt, dass der Mensch keinerlei diskriminierende Filterfunktion mehr wahrnimmt.
3. **Kognitiver Sättigungspuffer ($H_{\text{cog}}$):** Die Anzahl zeitgleicher Zielbekämpfungen pro Bediener. Wenn ein einzelner Soldat einen Schwarm von zwölf FPV-Loitering-Drohnen beaufsichtigen soll, die simultan mit 120 km/h im Sturzflug ansetzen, ist eine tatsächliche Kontrollaufsicht mathematisch ausgeschlossen.

Solange Streitkräfte keine freigegebenen Histogramme von $\Delta t_{\text{consent}}$ und $R_{\text{target}}$ veröffentlichen, ist jede Behauptung über einen „wirksamen menschlichen Einfluss in der Schleife“ eine ungeprüfte PR-Aussage.

---

## 2. Der Abnick-Bunker: Die moralische Knautschzone

Man betrachte die operative Realität des vorgeschobenen Bedieners im Jahr 2026:

Ein neunzehnjähriger Soldat sitzt in einem feuchten Keller acht Kilometer hinter der Kontaktlinie. Der Raum wird einzig vom bläulichen Schimmer dreier ziviler Tablets erhellt. Die Raumtemperatur beträgt 4 Grad Celsius. Der Bediener hat eine sechzehnstündige Dauerschicht hinter sich, unterbrochen von den Erschütterungen naher Gleitbomben- und Artillerie-Einschläge.

```
+-------------------------------------------------------------------------+
|            DIE SUBSEKUNDEN-BLANKOGENEHMIGUNGS-PIPELINE                  |
|                                                                         |
|  [Optische / HF-Edge-Sensoren]                                          |
|          | (Maschinelle Klassifikation: Ziel detektiert)                |
|          v                                                              |
|  [Bordgestützte Edge-Inferenz: RV1126/Orin]                             |
|          | (Generiert Zielrahmen: „98,4 % Infanterie“)                  |
|          v                                                              |
|  [Geteilter Bildschirm auf Bediener-Tablet]                             |
|     +-------------------------------------------------------------+     |
|     | Ziel #1: [FREIGABE BESTÄTIGEN] (Autom. Sturz in 350 ms)     |     |
|     | Ziel #2: [FREIGABE BESTÄTIGEN] (Autom. Sturz in 500 ms)     |     |
|     | Ziel #3: [FREIGABE BESTÄTIGEN] (Autom. Sturz in 620 ms)     |     |
|     +-------------------------------------------------------------+     |
|          |                                                              |
|          | (Menschlicher Reflex-Tastendruck oder Stillschweigen)        |
|          v                                                              |
|  [Kinetische Auslösung / Einschlag]                                     |
+-------------------------------------------------------------------------+
```

Auf dem Bildschirm verarbeitet ein Edge-Modell ein pixeliges Wärmebild, das über eine Relaisdrohne übertragen wird. Die Software legt einen blinkenden Kasten über eine dunkle Silhouette, die aus einem eingestürzten Graben auftaucht. Ein Timer läuft ab: `AUTOMATISCHER ANGRIFF IN 0,4s — ABBRUCH TASTEN`.

Drückt der Bediener die Abbruchtaste, verliert das anfliegende Wirkmittel seinen Anflugvektor, leert seine Restbatterie und ist verloren. Erweist sich das Ziel später als feindlicher Sturmtrupp, der eine Nachbarstellung überrennt, droht dem Bediener ein Disziplinarverfahren wegen taktischen Zögerns. Reagiert er nicht, schlägt die Munition ein. Tötet der Schlag Zivilisten, hält die nachträgliche Untersuchung fest, dass „das System unter menschlicher Aufsicht und Freigabe operierte“.

Der menschliche Bediener wird nicht als moralischer Souverän eingesetzt, sondern als institutionelle „moralische Knautschzone“ — eine biologische Komponente, die juristische und politische Haftung absorbieren soll, wenn automatisierte Zielsysteme Katastrophen verursachen.

---

## 3. Warum wöchentliche Adaption jährliche Zertifizierungen schlägt

Westliche Rüstungsbeschaffung operiert nach Zulassungszyklen, die aus der bemannten Luftfahrt stammen:
- Taktisch-operative Forderung: Monate 1–18.
- Prototypenprüfung und Flugsicherheit: Monate 19–42.
- Truppenerprobung und Red-Teaming: Monate 43–60.
- Zertifizierung der Vorserienfertigung: Jahr 6.

Auf dem Kriegsschauplatz Ukraine von 2024–2026 mutiert das elektromagnetische und Software-Umfeld in einer **Kadenz von sieben bis vierzehn Tagen**:
- **Woche 1:** Der Verteidiger führt Frequenzsprünge im 868-MHz-Telemetrieband ein.
- **Woche 2:** Der Angreifer disloziert gerichtete Yagi-Störsender gegen 868 MHz.
- **Woche 3:** Der Verteidiger bringt neuronale Netze zur autonomen Endphasenlenkung ein, um eine 868-MHz-Verbindung gänzlich überflüssig zu machen.
- **Woche 4:** Der Angreifer nutzt wärmereflektierende Planen und Aerosol-Tarnnebel.
- **Woche 5:** Der Verteidiger trainiert die Modellgewichte des Edge-Rechners mit 1.200 neuen Infrarotbildern nach, die 48 Stunden zuvor von Aufklärungsdrohnen erfasst wurden.

Ein militärischer Zertifizierungsprozess, der vier Jahre beansprucht, kann eine algorithmische Wirkungskette nicht regulieren, deren Modellgewichte, Sensoren und Einsatzparameter alle vierzehn Tage mutieren. Tritt ein formaler Sicherheitsausschuss zusammen, um eine Softwareversion zu beglaubigen, ist diese Version bereits seit zwanzig Zyklen veraltet.

---

## 4. Institutioneller Widerstand: Die Trägheit der Cost-Plus-Großauftragnehmer

Der primäre institutionelle Widerstand gegen den Hyperkrieg geht nicht von Friedensbewegungen aus; er entspringt dem Inneren des industriellen Beschaffungskomplexes:

1. **Die Kapitalfalle der Großwaffensysteme:** Hauptauftragnehmer (*Primes*) stützen ihre Bilanzen auf jahrzehntelange Cost-Plus-Award-Fee-Großprogramme — F-35, B-21 Raider, atomare U-Boote und moderne Kampfpanzer. Jede einzelne bemannte Plattform bindet Hunderte Millionen Dollar an Kapital und sichert Hunderte Zulieferer in Schlüssel-Wahlkreisen. Ein Loitering-Wirkmittel für 4.000 Dollar, gefertigt aus kommerziellen Drohnenmotoren und Aluminiumblech, gefährdet das Geschäftsmodell der Luft- und Raumfahrtindustrie elementar.
2. **Der Kompromiss des „Collaborative Combat Aircraft“ (CCA):** Um das bemannte Cockpit zu retten und gleichzeitig die Schwarmrealität anzuerkennen, erfanden Beschaffungsbürokratien das Konzept unbemannter Flügelmänner (*loyal wingmen*). Das bemannte 120-Millionen-Dollar-Kampfflugzeug bleibt in der Luft; es führt lediglich zwei oder drei untergeordnete 15-Millionen-Dollar-Drohnen. Dieser Kompromiss hält den Piloten im Dienst und den Rüstungskonzern finanziert — konserviert aber die fatale Verwundbarkeit: Die gesamte Multi-Milliarden-Architektur bleibt an den biologischen Piloten im Himmel gekettet.
3. **Die schleichende militärische Übernahme (The Soft Military Takeover):** Der Übergang zur Vollautonomie erfordert keinen bewaffneten Putsch und keinen Verfassungsumsturz. Er vollzieht sich über institutionelle Sachzwänge. In jedem Gefechtsszenario, in dem eine autonome algorithmische Einsatzplanung (Schwärme, die Flugrouten, Frequenzwechsel und Zielverteilung selbstständig koordinieren) gegen einen menschlichen Führungsstab antritt, exekutiert das autonome System innerhalb von 4 Sekunden, während der Stab 45 Minuten für den ersten Feuerbefehl benötigt.

Angesichts eines Gegners, der autonome Planer einsetzt, werden Truppenführer manuelle Kontrollen abschalten. Die Software ergreift die Befehlsgewalt nicht gewaltsam — die Befehlsgewalt wird ihr dankbar überlassen, im Namen des nackten Überlebens.
