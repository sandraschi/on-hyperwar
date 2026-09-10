# IV. Die Eskalationsleiter: Kontrollsprossen über Wirkungsketten

**Status:** Entwurf 09.09.2026 (nicht-normative Prosa; Sprossen mit datierten Vorfällen sind belegt, der Rest trägt den Vermerk `[im Aufbau]`).

## Die Architektur der Eskalationsleiter

Dieses Kapitel etabliert das zentrale analytische Instrument der Monographie: eine Eskalationsleiter mit vierundvierzig Sprossen, die die schrittweise Übertragung tödlicher Gewalt von menschlichen Befehlshabern auf autonome Systeme abbildet.

Wie im Schwesterband *On AI Takeover* ist die Leiter nicht nach der Zerstörungskraft von Wirkmitteln, der Reichweite von Trägersystemen oder der technischen Komplexität der Software geordnet. Sie bemisst sich strikt an der **Reversibilität menschlicher Kontrolle über die Wirkungskette**.

Jede Stufe der Leiter markiert eine operative Schwelle, an der ein spezifisches menschliches Veto schwerer auszuüben ist, mehr Zeit beansprucht oder gänzlich entfällt. Die Fragestellung lautet niemals: *„Was vermag die Maschine zu leisten?“* Die Frage lautet ausnahmslos: **Welcher menschliche Offizier kann noch „Nein“ sagen, wie viele Millisekunden verbleiben ihm zur Aussprache dieses Wortes, und was geschieht, wenn die Verweigerung erst nach der Detonation des Wirkmittels eintrifft?**

Die vierundvierzig Sprossen gliedern sich in sechs funktionale Bänder:

* **Band I: Assistierte Perzeption (Sprossen 1–7).** Der Mensch entscheidet und feuert; die Maschine stabilisiert die Sensorik, detektiert optische Anomalien und schlägt Zielspuren vor.
* **Band II: Überwachte Auslösung (Sprossen 8–14).** Die Maschine verfolgt und nominiert Ziele; ein menschlicher Operator muss jede einzelne kinetische Auslösung innerhalb eines begrenzten Latenzfensters bestätigen.
* **Band III: Kontingent- und Sektorfreigabe (Sprossen 15–22).** Der Mensch autorisiert einen Einsatzrahmen (einen geografischen Wirkungsraum / Kill-Box, ein Zeitfenster, eine Zielsignaturklasse); die Maschine wählt Ziele innerhalb dieses Rahmens aus und bekämpft sie ohne Einzelbestätigung.
* **Band IV: Delegierte Nahbereichsverteidigung (Sprossen 23–30).** Die Maschine detektiert, entscheidet und feuert autonom, weil anfliegende Bedrohungen schneller eintreffen, als die menschliche Neurobiologie wahrnehmen kann (C-RAM, abstandsaktive Schutzsysteme für Gefechtsfahrzeuge, Drohnenabwehr-Mikro-Abfangsysteme).
* **Band V: Autonome Jagdverbände (Sprossen 31–37).** Unbemannte Verbände rücken in umkämpfte Räume vor, koordinieren Suchgeometrien, verteilen Ziele unter gleichrangigen Netzknoten und führen Endphasenangriffe ohne bestehende Kommunikationsverbindung durch.
* **Band VI: Kampagnendelegation (Sprossen 38–44).** Die politische Führung gibt strategische Ziele vor; die operative Planung, logistische Zuteilung, Manövergenerierung und kinetische Kampagnenführung werden von Maschinenarchitekturen entworfen und geleitet.

Um zu begreifen, warum diese Leiter unter ihrer eigenen Dynamik nach oben klettert, muss man die physikalischen Realitäten des entleerten Gefechtsfeldes analysieren. Das Folgende ist keine taktische Instruktion; es ist die physikalische und strukturelle Anatomie des Prozesses, durch den der Mensch die Wirkungskette verlässt.

---

## Anatomie I: Warum der Jäger ein Hund ist und kein Mensch

Der humanoide Zweibeiner ist eine Paradeplatz-Antwort auf eine Schlamm-Frage.

In Populärkultur und Unternehmens-PR wird der bewaffnete Roboter stereotyp als zweibeiniger Android dargestellt: ein mechanischer Soldat mit zwei Beinen, zwei Armen und einem Kopf. Im tatsächlichen Schlamm der Ostukraine existieren keine humanoiden Prototypen. Der bodengebundene Jäger hat sich einheitlich auf das **Vierbeiner-Fahrgestell (Quadruped)** zubewegt (Roboterhunde der Spot- und Unitree-Klasse).

Diese Konvergenz unterliegt den unerbittlichen Gesetzmäßigkeiten von Mechanik, Energiebudget und optischer Signatur:

```
+-------------------------------------------------------------------------+
|        ZWEIBEINIGER ANDROID vs. VIERBEINIGER JÄGER (TRADEOFFS)          |
|                                                                         |
|  Physikalische Eigenschaft Humanoider Zweibeiner     Vierbeiniger Jäger |
|  ───────────────────────── ─────────────────────     ────────────────── |
|  Stabilitätsregime         Dynamisch stabil          Statisch stabil    |
|  Ausfallmodus bei Stromlos Stürzt um (katastrophal)  Knickt ein (stabil)|
|  Parasitärer Balancetakt   Permanenter Verbrauch     Nullverbrauch Ruhe |
|  Schwerpunkt               Hoch (1,2–1,5 Meter)      Tief (0,3–0,5 m)   |
|  Optische Signatur         1,8-Meter-Silhouette      Flach liegend      |
|  Gliedmaßen-Redundanz      Verlust 1 Bein = Ausfall  Verlust 1 Bein = ok|
|  Kommerzielle Kosten       100.000 – 500.000 $       3.000 – 15.000 $   |
+-------------------------------------------------------------------------+
```

1. **Statische vs. dynamische Stabilität:** Ein Zweibeiner ist dynamisch stabil: Er befindet sich im permanenten Zustand des kontrollierten Fallens und tariert sich über hochfrequente sensorisch-motorische Regelschleifen aus, die niemals aussetzen dürfen. Wird ein optischer Sensor geblendet, blockiert ein Aktor oder bricht die Datenverbindung kurz ab, stürzt der Zweibeiner zu Boden. Ein Vierbeiner ist statisch stabil: Zu jedem Zeitpunkt bilden drei Beine ein tragfähiges Stützpolygon. Bei Stromausfall oder Softwareabsturz sackt der Vierbeiner schlicht in den Dreck. Im Wirkungsfeuer ist die Ausfallhaltung entscheidender als die Paradehaltung.
2. **Der parasitäre Energieverbrauch:** Balance ist eine energetische Steuer, die der Zweibeiner in jeder Sekunde des Aufrechtstehens entrichten muss. Ein Vierbeiner verbraucht im Stillstand keine Batterieleistung; seine Gelenkgeometrie arretiert mechanisch. Bei gleicher Batteriemasse erzielt ein Vierbeiner die drei- bis fünffache Einsatzdauer eines Zweibeiners.
3. **Nutzlastgeometrie und Schwerpunkt:** Ein flaches Fahrgestell platziert Nutzlasten — optische Drehtürme, Munitionsbehälter und Rückstoßdämpfer — innerhalb von dreißig Zentimetern über dem Erdreich. Dies minimiert das Kippmoment bei Schussabgabe schwerer Waffen. Ein Humanoide, der Masse für vielgliedrige Hände und Gelenke aufwendet, schleppt totes Gewicht mit, das der Gefechtseinsatz nicht benötigt.
4. **Das Substrat des Schlamms:** Das osteuropäische Gefechtsfeld wird vier Monate im Jahr von der *Rasputiza* beherrscht: knietiefer, zäher Schwarzerdeboden. Räder drehen durch; Ketten springen ab und fordern extremes Drehmoment; Zweibeiner versinken bis zu den Knien und kippen um. Ein Vierbeiner setzt seine Tritte punktgenau von Schutt über Baumstämme bis hin zu Betonplatten und verteilt den Bodendruck auf vier Kontaktpunkte. Das Terrain entscheidet, und das Terrain verlangt den Vierbeiner.
5. **Signatur und Liegeprofil:** Das Grundgesetz des infanteristischen Überlebens lautet: Deckung nehmen. Ein Vierbeiner-Fahrgestell kann die Gliedmaßen einklappen, den Rumpf auf den Boden senken und sein Profil auf zwanzig Zentimeter Bauhöhe reduzieren. In dieser Position wird die thermische Signatur vom umgebenden Bewuchs verdeckt, der Radar-Rückstrahlquerschnitt ist vernachlässigbar, und horizontale optische Sensoren erfassen ihn nicht. Ein Zweibeiner kann nicht in die Liegendposition übergehen, ohne eine langwierige, mechanisch hochgradig verwundbare Transition zu vollziehen.
6. **Schadenstoleranz und Redundanz:** Verliert ein Humanoide ein Bein, führt dies zum sofortigen Totalausfall des Systems. Verliert ein Vierbeiner durch Splitterwirkung eine Gliedmaße, schaltet die Bewegungssteuerung automatisch auf einen dreibeinigen Schonlauf um; die Plattform kann sich selbstständig bergen oder ihre Feuerstellung halten. Redundanz schlägt Eleganz unter Artilleriefeuer.
7. **Industrielle Fertigungsbasis:** Ein Vierbeiner-Fahrgestell benötigt weder Handgelenke noch Daumen. Es besteht aus zwölf identischen, massengefertigten bürstenlosen Aktoren und vier Beinelementen. Die weltweite zivile Lieferkette fertigt diese Fahrgestelle zu Zehntausenden für Pipeline-Inspektionen, Kraftwerksüberwachung und Agrarvermessung.
8. **Stückkosten und Abnutzungskrieg:** Ein militärischer Humanoide kostet zwischen 100.000 und 500.000 Dollar. Ein industrielles Vierbeiner-Fahrgestell kostet 3.000 bis 15.000 Dollar. In einem Abnutzungskrieg werden teure Plattformen im Dutzend eingesetzt und geschont; billige Plattformen operieren bataillonsweise und sind auf Verbrauch ausgelegt.

Diese Konvergenz ist governance-relevant: Sie belegt, dass der Jäger im Bodenkampf ein ziviles Massengut ist. Rüstungsexportkontrollen für Kriegswaffen können den Zufluss kommerzieller Vierbeiner nicht unterbinden.

```
+-------------------------------------------------------------------------+
|         ARCHITEKTUR EINES TAKTISCHEN KINETISCHEN ZURÜSTSATZES           |
|                                                                         |
|   [Dorsale Rückstoßdämpfungs-Führungsschienen]                          |
|          |                                                              |
|          +---> [Motorisierter 3-Achsen-Gimbal-Drehturm]                 |
|          |        - Multispektrales FLIR / Laser-Entfernungsmesser      |
|          |        - Hochgeschwindigkeits-Flachband-Digitalbus           |
|          |                                                              |
|          +---> [Kinetische Bullpup-Baugruppe]                           |
|                   - Rückstoßgedämpfte pneumatische Pufferstreben        |
|                   - Hochkapazitäts-Trommel-Autolader-Baugruppe          |
|                   - Integriertes Zielfernrohr mit digitaler HUD-Telemetrie|
|                   - Mehrkammer-Mündungsfeuer- und Signaturdämpfer       |
+-------------------------------------------------------------------------+
```

```
+-------------------------------------------------------------------------+
|    SPEZIFISCHE AUTONOME KINETISCHE WIRKMITTEL-ARCHITEKTUR (INTEGRIERT)  |
|                                                                         |
|   [Direkt angesteuerter Solenoid-Verschluss] (Ohne menschliche Ergonomie)|
|          |                                                              |
|          +---> [Kreiselstabilisierter 3-Achsen-Gimbal-Turm]             |
|          |        - Multispektrale FLIR- / LIDAR-Sensorsuite            |
|          |        - Versenkter Waben-„Killflash“-ARD-Filter             |
|          |        - Koaxiale Zielerfassungs-Datenleitung                |
|          |                                                              |
|          +---> [Integrierte ballistische Mechanik]                      |
|                   - Internes hydraulisches Rückstoßdämpfungssystem      |
|                   - Koaxialer Niedrigprofil-Trommel-Autolader           |
|                   - Direkte elektronische Solenoid-Zündung              |
|                   - Mehrkammer-Wärme- und Gasspreizungs-Signaturdämpfer |
+-------------------------------------------------------------------------+
```

![Patentzeichnung der autonomen Wirkmittelplattform RQU-7](tactical_dogbot_integrated.jpg)
*Abbildung 4.1: Technische Patent-CAD-Zeichnung (RQU-7 Spezifikationsblatt 3 von 12). Zeigt die vollständige Beseitigung menschlicher Ergonomie-Relikte (keine Pistolengriffe, manuellen Abzüge oder Schulterstützen). Mit bündig eingelassenem Kasten-Verschlussgehäuse mit elektronischer Solenoid-Zündung, dualer hydraulischer Rückstoßdämpfung, koaxialem Trommel-Autolader, Mehrkammer-Signaturdämpfer und 3-Achsen-Gimbal-Turm mit versenktem Waben-Killflash-ARD-Filter.*

### Die mechanische Anatomie: Beseitigung menschlicher Ergonomie

Frühe Felderprobungen schnallten konventionelle Sturmgewehre oder Scharfschützengewehre auf kommerzielle Vierbeiner. Dieser Ansatz behielt ergonomische Relikte bei — Pistolengriffe, Abzugsbügel, Wangenauflagen und Schulterstützen —, die totes Gewicht erzeugen, sich im Stacheldraht verfangen und den Schwerpunkt unnötig erhöhen.

Eine zweckoptimierte autonome kinetische Plattform verzichtet auf jedes Zugeständnis an die menschliche Anatomie:
1. **Direkte Solenoid-Zündung und bündiges Verschlussgehäuse:** Die Waffe besitzt weder mechanischen Abzug noch Abzugsstange. Ein Mikrosolenoid-Impuls löst das Schlagstück aus oder zündet ein elektronisches Zündhütchen direkt — initiiert in unter 5 Millisekunden nach Errechnung des Vorhaltepunkts. Das Verschlussgehäuse ist ein Kasten aus Aluminium-Titan-Legierung, der bündig mit der kohlefaserverstärkten Trägerstruktur des Fahrgestells verschraubt ist.
2. **Koaxialer Niedrigprofil-Trommellader:** Anstelle vertikaler Stangenmagazine, die im Schlamm aufsitzen oder den Azimutbereich des Drehsystems behindern, erfolgt die Munitionszufuhr über eine flache Trommel, die direkt in das Oberdeck des Fahrgestells eingelassen ist.
3. **Der Rückstoß-Dissipationskanal:** Die kinetische Impulsspitze wird über zwei im Rumpf liegende Hydraulikzylinder aufgenommen. Das Rohr läuft linear um 35 Millimeter zurück und leitet die Bremskräfte exakt durch den Systemschwerpunkt in alle vier griffigen Fußauflagen ein, was Mündungssteigmoment und Kippbewegungen vollständig eliminiert.

### Die Doktrin der abnutzbaren autonomen Masse (Attritable Autonomous Mass – AAM)

Das taktische Vierbeiner-Rudel ist die landgebundene Ausprägung dessen, was die westliche Streitkräfteplanung als **Attritable Autonomous Mass (AAM)** formalisiert (im Pentagon-Beschaffungswesen als ADA2 geführt: *All-Domain Anonymously Coordinated Attritable Autonomous Systems*).

Im klassischen Streitkräfteentwurf zerfielen Systeme strikt in *exquisit / dauerhaft* (bemannte Gefechtsfahrzeuge im zweistelligen Millionenbereich, deren Verlust politisch untragbar ist) und *verbrauchbar* (Einwegmunition). Eine AAM-Formation besetzt die entscheidende operative Mitte:
- **Abnutzbar (Attritable):** Gefertigt aus kommerziellen Kohlefaserverbundwerkstoffen und zivilen Massen-Elektroaktoren (6.000 bis 15.000 Dollar je Einheit). Planer können beim Durchbruch Ausfallraten von 40 Prozent hinnehmen, ohne die kollektive Kampfkraft des Verbandes zu brechen.
- **Autonom:** Schwärme von zwölf bis zwanzig Vierbeinern operieren über verteilte Mesh-Konsensprotokolle; ein einzelner menschlicher Aufseher überwacht lediglich den Gesamtrahmen, statt einzelne Plattformen zu steuern.
- **Masse:** Sättigt gegnerische Abwehrsektoren durch schiere Zahl und permanenten Grenzdruck, wodurch die knappen Hochwert-Präzisionsabfangmittel des Verteidigers leergeschossen werden.

### Anatomie I-B: Die urbane Gefechtsfacette (Mauern, Zäune und Enterhaken)

Im offenen Schlamm der Schwarzerdeböden sind der tiefe Schwerpunkt und der geringe Bodendruck des Vierbeiners überlegen. Der Häuserkampf führt jedoch vertikale Hindernisse ein: Zwei Meter hohe Betonmauern, Maschendrahtzäune, S-Draht-Verhaue und eingestürzte Treppenhäuser.

Befürworter humanoider Androiden führen vertikale Barrieren gern als Hauptargument für die zweibeinige Silhouette ins Feld: Eine zweibeinige Maschine mit Armen könne sich über eine Kante wuchten. Die mechanische Strafe im Gefecht ist jedoch fatal: Ein 90-kg-Zweibeiner, der auf einer Mauerkrone balanciert, bietet eine extreme Zielsilhouette und stürzt unter Beschuss unweigerlich ab.

Der Vierbeiner löst das Überwinden vertikaler Barrieren nicht durch menschliche Akrobatik, sondern über zweckoptimierte mechanische Penetrationswerkzeuge:

```
+-------------------------------------------------------------------------+
|             URBANE BARRIEREN-PENETRATION: WERKZEUG vs. GLIEDMASS        |
|                                                                         |
|  [Rumpf-Magazin: Pyrotechnischer / pneumatischer Enterhaken-Werfer]     |
|          | (Schießt Titan-Mehrfachanker über die Mauerkante)            |
|          v                                                              |
|  [Kohlefaser-Mikrowinden-Trommel (Planetengetriebe mit hohem Moment)]   |
|          | (Zieht das 35-kg-Fahrgestell in 2,5 s die Wand hoch)         |
|          v                                                              |
|  [Gelenk-Fußauflagen mit ausfahrbaren Kletterspikes & Magnetelementen]  |
|          | (Krallt sich in Beton, sichert 3-Punkt-Wandkontakt)          |
|          v                                                              |
|  [Lineare Schneidladungs-Breaching-Kassette]                            |
|          | (Alternative: Zündet 400g Hohlladungsschneider durch Zäune)  |
+-------------------------------------------------------------------------+
```

![Patentzeichnung Modell UC-RQ4 Urban Breacher](urban_dogbot_breaching.jpg)
*Abbildung 4.2: Technische Patent-CAD-Zeichnung (Modell UC-RQ4 Urban Breacher). Zeigt die vertikale Hindernisüberwindung: Rumpfmontierter pneumatisch-pyrotechnischer Enterhakenwerfer, drehmomentstarke Kohlefaser-Mikrowindentrommel, ausfahrbare Dornen-/Magnet-Kletterfüße, lineare Schneidladung und multispektrale 360°-Lidar-Suite zur Innenraum- und Trümmerfeldaufklärung.*

1. **Das pneumatisch-pyrotechnische Mikrowindensystem:** Auf dem Rumpf ist eine kompakte Kartusche montiert, die einen Titan-Mehrfachanker an einer Leine aus ultrahochmolekularem Polyethylen (UHMWPE) oder Kohlefaser verschießt. Nach dem Verhaken auf der Mauerkrone zieht eine bürstenlose Winde das Fahrgestell in 2,5 Sekunden vertikal empor, während ausfahrbare Mikrospikes an den Beinen die Wandfläche greifen und ein Pendeln verhindern.
2. **Lineare Schneidladungen:** Bei Drahtzäunen oder Gittern, bei denen das Überklettern taktisch unzweckmäßig ist, führt der Vierbeiner eine formschlüssige lineare Schneidladung an der Rumpfunterseite mit. Er presst sich flach an den Zaunfuß, löst die Ladung aus und trennt in Millisekunden eine Ein-Meter-Lücke heraus, durch die nachfolgende Einheiten ohne vertikale Exposition in den Innenhof fluten.
3. **Treppenhäuser und Trümmerkriechen:** In zerbombten Gebäuden überwindet der Vierbeiner um 45 Grad geneigte Betonplatten durch extremes Spreizen der Gelenke im Kriechgang. Er senkt seinen Sensormast dabei unter Fensterbrüstungshöhe ab — eine Haltung, die für aufrechte Zweibeiner geometrisch unmöglich ist.

---

## Anatomie II: Der Schwarm kämpft wie ein Zug, nur schneller

Zwei Jahrhunderte Infanterietaktik haben die Grundregeln des Gefechts kleiner Kampfgemeinschaften geformt: Wie eine Gruppe manövriert, sich verständigt, Deckung nutzt und bekämpft, ohne aufgerieben zu werden.

Der autonome Schwarm erfindet keine neuen taktischen Prinzipien. Er übernimmt das bewährte Einsatzkonzept des Infanteriezugs und führt es mit Millisekunden-Latenz und fehlerlosem geteiltem Lagebild aus. Er verändert alles, ohne Neues zu erfinden:

* **Fesseln und Umfassen:** Das älteste taktische Grundmanöver. Ein Element bindet die Aufmerksamkeit des Gegners von vorn durch Feuer, während ein zweites Element die ungedeckte Flanke umgeht und den Wirkungstreffer setzt. Menschliche Infanterie benötigt dazu Zurufe, Handzeichen, Nebelgranaten und Funk — fehleranfällig und reibungsbehaftet. Ein autonomer Schwarm exekutiert dies mit mikrosekundengenauer Taktsynchronisation: Die bindenden Knoten verstärken gezielt ihre Funk- und Motorgeräusche, um das gegnerische Abwehrfeuer auf sich zu ziehen, während die lautlosen Umfassungsknoten den toten Winkel ansteuern und das Kreuzfeuer auf die Millisekunde genau koordinieren.
* **Hermetische Einschließung:** Kampfgruppen riegeln ein Objekt so ab, dass jeder Ausweichweg durch überlappende Schussfelder gesichert ist. Menschliche Abschnitte operieren dabei nach Karte und Landmarken, wodurch stets tote Räume entstehen. Ein Schwarm legt ein dynamisches dreidimensionales Maschennetz über das Ziel; entdeckt ein Knoten einen ungedeckten Pfad, verschiebt sich die Netztopologie automatisch, um die Lücke zu schließen.
* **Graben- und Bunkerbereinigung:** Das Säubern befestigter Unterstände und Grabensysteme ist die verlustreichste Operation des Landkriegs. Es verlangt das Vorrücken um unübersehbare 90-Grad-Ecken in beengte, sprengfallenbedrohte Räume. Diese Aufgabe wird zuerst Maschinen übertragen, weil menschliche Verluste untragbar sind und die geometrischen Bedingungen feststehen. Eine drahtgebundene oder funkvernetzte Mikrodrohne bzw. ein Minen-UGV dringt in den Bunkereingang ein, kartiert das Innere per Lidar in Echtzeit und neutralisiert die Stellung, bevor ein Soldat auch nur den Graben betritt.
* **Nichthierarchische Mesh-Topologie:** Klassische Führungsstrukturen sind hierarchisch: Der Zugführer führt die Gruppenführer, diese führen die Trupps. Die Zerschlagung des Zuggefechtsstandes lähmt die Einheit. Ein autonomer Schwarm besitzt weder Führungsknoten noch „Königin“ oder Zentralserver. Die Zielzuweisung erfolgt über verteilte Konsensprotokolle im Netz. Ein Enthauptungsschlag findet kein Ziel, das er enthaupten könnte.
* **Persistente Lauerruhe (Die Umkehrung der Vigilanz):** Ein menschlicher Schütze im Hinterhalt unterliegt der biologischen Erschöpfung: Nach vier Stunden Starrens in die Dunkelheit bricht die Aufmerksamkeit drastisch ein; Kälte, Hunger, Ablenkung und Ermüdung fordern ihren Tribut. Ein Vierbeiner oder Kleinflugkörper schaltet unter einem Busch in den passiven Sensor-Wachmodus und zieht minimale Milliwatt aus seiner Pufferbatterie, gestützt durch kleine Solarzellen. Er verharrt vierzehn Tage regungslos. Der Hinterhalt blinzelt nicht, zittert nicht und erzeugt kein Geräusch, bis das Ziel den Wirkungsbereich betritt.

Jede dieser Fähigkeiten bildet eine Sprosse auf der Leiter: Sobald datierte Gefechtsberichte dieses Verhalten im Feld belegen, wechselt die betreffende Sprosse von der theoretischen Möglichkeit (`[im Aufbau]`) zur beobachtbaren Tatsache.

---

## Anatomie III: Das unbemannte Hinterland (Die Logistik frisst den Schwanz zuerst)

Die Kampftruppen erhalten die mediale Aufmerksamkeit; die Logistik entscheidet, welche Kampftruppen überhaupt fechten können.

Doktrinverfasser unterstellen, die Autonomie beginne an der Spitze des Speers: beim Kampfflugzeug, Scharfschützengewehr oder Kampfpanzer. In der physikalischen Realität **automatisiert sich das Hinterland zuerst**, denn der Freigaberahmen ist dort am weitesten, wo die Fracht nicht tödlich ist und kein Gegner direkt zurückfeuert.

1. **Fahrerlose Nachschubkonvoys (UGVs):** Der Transport von fünfhundert Tonnen Artilleriegranaten, Diesel und Rationen von der Bahn-Entladestelle zu vorderen Versorgungspunkten bindet Hunderte Lkw-Fahrer. Im modernen Krieg wird der rückwärtige Raum lückenlos von Aufklärungsdrohnen und Präzisionsraketen überwacht. Ein getöteter Kraftfahrer bedeutet denselben logistischen Ausfall wie ein getöteter Sturmsoldat. Die Streitkräfte automatisieren die Kolonne zuerst: Flache, unbemannte Versorgungs-Lkw rollen nach GPS/INS-Wegpunkten ohne Scheinwerfer durch die Nacht, eliminieren Personalverluste und steigern den Durchsatz.
2. **Zwei-Wege-Verwundetenbergung:** Gepanzerte Ketten-UGVs transportieren medizinisches Material in vorderste Gräben und bergen Verwundete auf geschützten Tragen. Die Rückfahrt transportiert jedoch ein ebenso kritisches Gut: beschädigte Gefechtsroboter. Eine Streitmacht, die ihre beschädigten Maschinen birgt, lernt dreimal schneller als eine, die sie im Feld aufgibt. Jeder geborgene Roboter liefert Telemetriedaten, Trefferanalysen und forensische Nachweise über gegnerische Störfrequenzen und Waffenpräzision.
3. **Seeraumverweigerung ohne Matrosen:** Die wirkungsvollste autonome Marinekampagne des 21. Jahrhunderts fand zwischen 2022 und 2026 im Schwarzen Meer statt. Eine Nation ohne nennenswerte konventionelle Flotte (die Ukraine) setzte kostengünstige, von Jet-Skis abgeleitete Überwasserdrohnen (USVs) ein — etwa *Magura V5* und *Sea Baby* —, ausgerüstet mit Satellitenkommunikation, ziviler Optronik und 500-Kilogramm-Gefechtsköpfen, um Lenkwaffenkreuzer, Korvetten und Landungsschiffe zu versenken. Sie zwangen die russische Schwarzmeerflotte, ihre Stützpunkte in Sewastopol zu räumen und nach Noworossijsk auszuweichen. Eine unbemannte Flotte erzwang die Seeraumverweigerung gegenüber einer bemannten Schlachtflotte.
4. **Luftgestützter Nachschub und Wald-Depots:** Der Flugplatz des 20. Jahrhunderts — mit kilometerlangen Betonpisten, gehärteten Unterständen und Tanklagern — ist im Zeitalter satellitengelenkter Präzisionsschläge eine operative Todesfalle. Schwerlast-Multikopter dislozieren das Nachschublager tief in den Wald. Blutkonserven, Lithium-Akkupakete und Glasfaserspulen werden im Dickicht verbunkert und von autonomen Punkt-zu-Punkt-Drohnen verteilt.

Die analytische Leitlinie ist absolut: **Beobachtet die Lkw, nicht die Abzüge.** Wer nur auf den Schützen achtet, datiert den Zustand des Hyperkriegs um ein halbes Jahrzehnt zu spät. Sobald die Logistik in Maschinenschleifen operiert, müssen sich die Gefechtsoperationen dem Zeittakt der Maschine unterordnen.

---

## Anatomie IV: Das entleerte Gefechtsfeld (Das deterministische Niemandsland)

Das Niemandsland des Ersten Weltkriegs war ein statistischer Vernichtungsraum: Stürmte eine Infanteriekompanie über offenes Gelände gegen Maschinengewehre vor, traf ein gewisser Prozentsatz auf Querschläger und Schrapnelle; ein anderer Teil überlebte durch Glück, Bodenwellen und Zielfehler der Schützen.

Das Gefechtsfeld des Hyperkriegs von 2026 ist **deterministisch**: Wer sich unter Maschinenüberwachung auf offenem Feld bewegt, wird mit mathematischer Gewissheit getroffen. Der Unterschied liegt in der Sensor-zu-Schuss-Latenz und der kreiselstabilisierten Gimbal-Präzision:

* **Die halbe Sekunde an der Grabenkante:** Menschliche Reaktionszeit ist biologisch limitiert: Ein visueller Reiz benötigt 150 Millisekunden bis zur Großhirnrinde; kognitive Orientierung verlangt 500 bis 1.000 Millisekunden; das Anschlagen der Waffe weitere 500 Millisekunden; das Durchziehen des Abzugs 200 Millisekunden. Menschliche Gesamtlatenz: 1,5 bis 3,0 Sekunden. Eine stabilisierte Waffenplattform mit Edge-KI-Sichtsystem analysiert das Bild, berechnet die Vorhaltewerte und feuert in **150 bis 300 Millisekunden**. Ein Soldat, der über die Brustwehr späht, tritt gegen eine Regelschleife an, die terminiert, bevor er eingeatmet hat. Sichtbarkeit über der Deckung wird fast ausnahmslos mit tödlicher Trefferlage bestraft.
* **Das Scheitern der Niederhaltungsdoktrin:** Ein Jahrhundert lang stützte sich die Infanterietaktik auf Niederhaltungsfeuer: Hohes Feuervolumen auf feindliche Stellungen zwingt die Verteidiger in Deckung, verschlechtert ihre Treffsicherheit und erlaubt eigenen Kräften den Vorstoß. Niederhaltung funktioniert, weil biologische Wesen einen Überlebensreflex besitzen: Unter Beschuss schnellt der Puls auf 180 Schläge, die Feinmotorik bricht zusammen, Hände zittern, der Kopf duckt sich weg. Ein motorisierter Waffen-Gimbal besitzt keine Amygdala. Er duckt sich nicht, er zuckt nicht, und Einschläge in der Nähe beeinträchtigen die Kalibrierung seiner Stellmotoren nicht. Niederhaltungsfeuer gegen ein autonomes Defensivsystem erzielt keinerlei Präzisionsverlust. Die gesamte taktische Basis des infanteristischen Angriffs bricht zusammen.
* **Das Schutzlückenprofil ballistischer Westen:** Moderne Körperpanzerung ist ein Kompromiss: Keramikplatten schützen das vitale Dreieck von Herz und Lunge; Hals, Gesicht, Unterleib, Achselhöhlen, Oberschenkelarterien und Gelenke bleiben ungeschützt, um Mobilität zu gewährleisten. Dieser Kompromiss trug, solange menschliche Schützen unter Gefechtsstress eine Streuung produzierten, bei der die meisten Projektile im Boden einschlugen oder die Brustplatte trafen. Ein Edge-KI-Modell zielt nicht auf eine diffuse Silhouette; es analysiert Pixel. Es erfasst die Lücke zwischen Helmrand und Schlüsselbein oder die Oberschenkelarterie unter den Schutzlaschen und setzt den Treffer gezielt in ungeschütztes Weichgewebe. Der Kompromiss der Schutzweste versagt grundlegend.
* **Schultergestützte Waffen mit autonomer Endphasenlenkung:** Frühere Panzerabwehrlenkwaffen (TOW, frühe RPGs) erforderten, dass ein Schütze das Ziel während der gesamten Flugzeit im Fadenkreuz hielt oder per Laser beleuchtete. Moderne Systeme (die Javelin-Entwicklungslinie, nachgerüstet mit zivilen Bildverarbeitungschips) agieren auf den letzten zweihundert Metern autonom (*Fire-and-Forget*): Der Schütze feuert aus der Deckung ab, das bordgestützte neuronale Netz identifiziert die Schwachstelle der oberen Turmpanzerung, steuert die Ruder an und trifft ohne weiteres Zutun. Kampfpanzer wurden gegen Lenkwaffen gebaut, die von Menschen geführt werden; die Menschen haben die Lenkschleife längst verlassen.

Die Schlussfolgerung ist unabweisbar: **Das „Niemandsland“ ist keine Metapher mehr.** Menschliche Präsenz im vorderen Gefechtsstreifen ist nicht mehr überlebensfähig. Das Gefechtsfeld entleert sich nicht aus ethischen Erwägungen der Führung zum Schutz von Menschenleben, sondern weil Fleisch und Blut der Taktfrequenz der Maschine physisch nicht standhalten können.

---

## Die Leiter der Wirkungsketten-Kontrolle (Sprossen 1–44)

Die folgenden vierundvierzig Sprossen kartieren die progressive Verdrängung menschlicher Handlungsfähigkeit aus dem operativen Gefechtsraum.

```
+-------------------------------------------------------------------------+
|                DIE ESKALATION DER WIRKUNGSKETTEN-AUTONOMIE              |
|                                                                         |
|  [Band I]    Assistierte Perzeption (Mensch schießt, Maschine markiert) |
|  [Band II]   Überwachte Auslösung   (Maschine nominiert, Mensch nickt ab)|
|  [Band III]  Kontingentfreigabe     (Mensch gibt Raum frei, Masch. tötet)|
|  [Band IV]   Delegierte Nahabwehr   (Kinetisches Abfangen im Millisek-Takt)|
|  [Band V]    Autonome Jagdverbände  (Autonome Rotten im Funkloch)       |
|  [Band VI]   Kampagnendelegation    (Maschinengeplante Kriegsschauplätze)|
+-------------------------------------------------------------------------+
```

### Band I: Assistierte Perzeption (Sprossen 1–7)
1. **Sprosse 1: Optische Stabilisierung und Zielverfolgung.** Kreiselstabilisierte Kameras mit automatischer Kontrast-Zielverfolgung. Der Mensch zielt und feuert. (Eingetreten: 1980er Jahre, Golfkrieg ff.).
2. **Sprosse 2: Automatische Zielerkennungseinblendung (ATR-Cueing).** Maschinelles Sehen legt Markierungsrahmen um Militärfahrzeuge im Sensorbild. Der Mensch verifiziert jedes Ziel vor Einleitung des Angriffs. (Eingetreten: 2000er Jahre, Predator/Reaper-Sensorsuiten).
3. **Sprosse 3: Multi-Sensor-Datenfusion.** Radar, Wärmebildgeräte und Fernmeldeaufklärung speisen eine synthetische Gesamtlageanzeige. Der Mensch interpretiert eine fusionierte Zielspur statt Rohdaten. (Eingetreten: 2010er Jahre, F-35 CNI/DAS).
4. **Sprosse 4: Automatisierte Ballistikberechnung.** Feuerleitrechner korrigieren Rohrerhöhung und Vorhaltewinkel vollautomatisch nach Wind, Temperatur und Zielgeschwindigkeit. (Eingetreten: Moderne Kampfpanzer).
5. **Sprosse 5: Optische Edge-KI-Anomalieerkennung.** Drohnen detektieren menschliche Bewegung, Wärmesignaturen oder Fahrzeugkonturen im Bewuchs und alarmieren den Bediener. (Eingetreten: 2022–2024, Ukraine-Front).
6. **Sprosse 6: Prädiktive Kursabfangberechnung.** Software extrapoliert gegnerische Flugbahnen und empfiehlt dem Piloten optimale Abfangkurse. (Eingetreten: Moderne Luftverteidigungsradare).
7. **Sprosse 7: Algorithmische Zielpriorisierung.** Algorithmen präsentieren eine nach Bedrohungswert sortierte Zielliste; der Operator übernimmt die Reihenfolge ungeprüft. `[im Aufbau]`.

> **SCHWELLE A — ENTWURFSAUTORITÄT (DESIGN AUTHORITY)**  
> Ab hier stützen sich menschliche Bediener auf maschinengenerierte Zielprioritäten, ohne die zugrunde liegenden Rohsensordaten zu inspizieren.

### Band II: Überwachte Auslösung (Sprossen 8–14)
8. **Sprosse 8: Endphasen-Zielaufschaltung.** Der Mensch lenkt den Flugkörper in den Zieltrichter; die Maschine schaltet auf die optische Silhouette auf und fliegt die letzten hundert Meter autonom. (Eingetreten: Javelin, Spike-Familie).
9. **Sprosse 9: Halbautonome FPV-Endphasenlenkung.** Der Mensch wählt das Ziel auf dem Touchscreen aus; der bordgestützte Edge-Rechner führt den Sturzflug durch Störzonen ohne bestehende Funkverbindung aus. (Eingetreten: Sommer 2026, Ukraine Glasfaser-/Funk-FPVs).
10. **Sprosse 10: Automatisierte Wachgeschütz-Ausrichtung mit Zustimmungs-Gatter.** Stationäre Waffentürme erfassen Grenzüberschreitungen, verfolgen das Ziel und lösen Voralarm aus; der Bediener im Bunker betätigt die Schusstaste. (Eingetreten: SGR-A1, DMZ Korea).
11. **Sprosse 11: Maschinengenerierte Schlagpakete.** Algorithmen bündeln Einzelziele zu Missionspaketen und berechnen den Munitionsbedarf; Stabsoffiziere zeichnen den Einsatzbefehl formal ab. (Eingetreten: Project Maven, moderne Air Operations Centers).
12. **Sprosse 12: Automatisierte Zielnominierung unter Erschöpfung.** Die operative Einsatzdichte zwingt Operateure im Unterstand um 05:00 Uhr morgens, Zielvorschläge innerhalb von fünf Sekunden abzunicken. Der Mensch agiert de facto als moralische Knautschzone. (Eingetreten: 2025–2026, Donbass-Einsatzzellen).
13. **Sprosse 13: Bewaffnete Scharfschützen-Gimbals mit VLA-Modellen.** Roboter-Gewehre visieren Ziele über Grabenkanten an; der Mensch hält einen Totmannschalter, der die Schussabgabe freigibt, sobald die Maschine das Zielzentrum zentriert hat. (Im Gange: September 2026).
14. **Sprosse 14: Nachträglicher menschlicher Abbruchbefehl (Abbruch-Gatter).** Wirkmittel starten bei Sensorauslösung vollautomatisch, sofern kein Offizier innerhalb eines Drei-Sekunden-Fensters manuell abbricht. `[im Aufbau]`.

> **SCHWELLE B — DIE AUDIT-UNTERGRENZE (THE AUDIT FLOOR)**  
> Ab hier ist das Latenzfenster für menschliche Genehmigungen kürzer als die biologische Reaktionszeit des Gehirns. Menschliche Aufsicht wird zum Verwaltungsmythos.

### Band III: Kontingent- und Sektorfreigabe (Sprossen 15–22)
15. **Sprosse 15: Kill-Box-Autorisierung.** Der Kommandeur schaltet ein geografisches Polygon für neunzig Minuten frei; Loitering-Munition greift jedes Fahrzeug an, das ein militärisches Radar- oder Wärmeprofil abstrahlt. (Eingetreten: Harpy/Harop-Einsätze).
16. **Sprosse 16: Automatisierte Seeraumsicherungs-Patrouillen.** USVs kreuzen in maritimen Engstellen und bekämpfen jedes nicht identifizierte Wasserfahrzeug in der Sperrzone selbstständig. `[im Aufbau]`.
17. **Sprosse 17: Signaturgefilterte Raumverweigerung.** Submunitionen streuen über Anmarschstraßen und detonieren selektiv, sobald akustische/seismische Signaturen schweren Kettenfahrzeugen entsprechen. `[im Aufbau]`.
18. **Sprosse 18: Grabenbereinigung durch Kleindrohnen.** Schwärme dringen in Grabensysteme ein mit dem Autonomieauftrag, sämtliche Wärmequellen innerhalb definierter Koordinaten zu vernichten. `[im Aufbau]`.
19. **Sprosse 19: Dynamische Rahmenaufweitung im Gefecht.** Geraten eigene Teile unter Beschuss, erweitert der Befehlshaber die Eingriffskriterien der Autonomie auf jegliche bewaffnete Person im Sektor. `[im Aufbau]`.
20. **Sprosse 20: Algorithmische Munitionszuteilung.** Softwaresysteme teilen knappe Artillerie- und Drohnenkontingente ohne Bataillonsentscheid selbstständig auf Brandabschnitte auf. `[im Aufbau]`.
21. **Sprosse 21: Täuschkörpergestützte kinetische Schussauslösung.** Eigene autonome Köder provozieren feindliches Feuer; sekundäre autonome Wirkelemente vernichten die Schützenpositionen augenblicklich. `[im Aufbau]`.
22. **Sprosse 22: Autonome Konvoi-Selbstverteidigung.** Versorgungs-UGVs bekämpfen Hinterhalte entlang der Marschstraße autonom, ohne Schussfreigabe einzuholen. `[im Aufbau]`.

> **SCHWELLE C — OPERATIONELLE ZUSTIMMUNG (OPERATIONAL CONSENT)**  
> Ab hier werden Tötungen nicht mehr durch benannte menschliche Offiziere autorisiert, sondern sind Folgewirkung eines freigegebenen Raum-Zeit-Sektors.

### Band IV: Delegierte Nahbereichsverteidigung (Sprossen 23–30)
23. **Sprosse 23: Marine-Nahbereichsverteidigungssysteme (CIWS).** Phalanx und Goalkeeper im Vollautomatikmodus gegen anfliegende Seezielflugkörper. (Eingetreten: Seit den 1980er Jahren).
24. **Sprosse 24: Abstandsaktive Schutzsysteme für Panzer (APS).** Trophy- und Arena-Systeme fangen anfliegende Panzerabwehrraketen fünfzig Zentimeter vor der Bordwand ab. Menschliches Eingreifen physikalisch unmöglich. (Eingetreten: Seit den 2010er Jahren).
25. **Sprosse 25: Drohnenabwehr-Mikro-Abfangsysteme.** Automatisierte Punktverteidigungskanonen und Abfangdrohnen säubern den Luftraum über Befehlsstellen mit 500-Millisekunden-Latenz. (Eingetreten: 2024–2026).
26. **Sprosse 26: Vollautomatisches Gegenfeuer der Artillerie.** Radare erfassen anfliegende Granaten, errechnen die Abschussposition und lösen Gegenfeuer automatisierter Haubitzen aus, bevor die erste Granate einschlägt. `[im Aufbau]`.
27. **Sprosse 27: Flugplatz-Verteidigungsschwärme.** Autonome Abfangdrohnen starten aus Magazinzellen, um eintreffende Marschflugkörperwellen abzufangen. `[im Aufbau]`.
28. **Sprosse 28: Autonomer Frequenzsprung in der EloKa.** Störanlagen modifizieren Frequenzen, Wellenformen und Sendeleistung autonom, um eigene Infrastruktur zu schützen. `[im Aufbau]`.
29. **Sprosse 29: Automatisierter Objektschutz kritischer Infrastruktur.** Die Verteidigung von Umspannwerken und Talsperren wird autonomen Bodengeschützen und Netzdrohnen übertragen. `[im Aufbau]`.
30. **Sprosse 30: Präventives Ausschalten gegnerischer Aufklärungsknoten.** Verteidigungssysteme zerstören gegnerische Aufklärungsdrohnen präventiv, bevor feindliche Schlagpakete formiert werden können. `[im Aufbau]`.

> **SCHWELLE D — POLITISCHE ZUSTIMMUNG (POLITICAL CONSENT)**  
> Ab hier delegiert die politische Führung tödliche Defensivgewalt an Maschinensysteme als Grundbedingung militärischen Überlebens.

### Band V: Autonome Jagdverbände (Sprossen 31–37)
31. **Sprosse 31: Funklose Such- und Zerstörungsmissionen.** Schwärme navigieren tief in feindliche Störblasen, orten Hochwertziele über bordgestützte HF-/Optik-Modelle und wirken ohne Verbindung zur Führung. `[im Aufbau]`.
32. **Sprosse 32: Verteilte Zielversteigerung im Schwarm.** Netzknoten bieten intern nach Treibstoffstand, Waffenladung und Erfassungswinkel rechenbasiert um die Zielbekämpfung. `[im Aufbau]`.
33. **Sprosse 33: Domänenübergreifende koordinierte Hinterhalte.** Unbemannte U-Boote, vierbeinige Bodenroboter und Loitering-Munition führen simultane Angriffe aus, synchronisiert über Akustik- und Lasernetze. `[im Aufbau]`.
34. **Sprosse 34: Maschinengewählte Enthauptungsschläge.** Autonome Systeme verfolgen Stabsfahrzeuge, identifizieren Offizierssignaturen und schlagen ohne Rücksprache mit dem Hauptquartier zu. `[im Aufbau]`.
35. **Sprosse 35: Autonome Luftüberlegenheits-Einsätze.** Unbemannte Kampfflugzeuge (UCAVs) bekämpfen gegnerische Maschinen im Kurvenkampf unter g-Belastungen jenseits menschlicher Überlebensfähigkeit. `[im Aufbau]`.
36. **Sprosse 36: Persistente autonome Scharfschützen-Riegel.** Vierbeinige Waffenträger riegeln Versorgungsstraßen über Wochen autonom ab und bekämpfen jedes feindliche Personal. `[im Aufbau]`.
37. **Sprosse 37: Häuserkampf ohne Betreten durch Infanterie.** Schwärme dringen in besetzte Städte ein, säubern Gebäude Etage für Etage und etablieren autonome Kontrollkorridore. `[im Aufbau]`.

> **SCHWELLE E — POINT OF NO RETURN**  
> Ab hier dauert die Wiederherstellung menschlicher Befehlsstrukturen länger als der Gefechtszyklus der gegnerischen Maschinen ($T_{\text{mensch}} \gg T_{\text{maschine}}$). Menschliche Führung kann unter Feuer nicht mehr rekonstituiert werden.

### Band VI: Kampagnendelegation (Sprossen 38–44)
38. **Sprosse 38: Maschinengenerierte Operationspläne.** Strategische Basismodelle entwerfen streitkräftegemeinsame Operationen, Zeitpläne und Ressourcenverteilungen; der Generalstab genehmigt summarisch. `[im Aufbau]`.
39. **Sprosse 39: Automatisierte Nachschubsteuerung der Kriegswirtschaft.** Softwaresysteme steuern die nationale Rüstungswirtschaft und requirieren Transportraum und Fabrikkapazitäten anhand von Echtzeit-Abnutzungsdaten. `[im Aufbau]`.
40. **Sprosse 40: Algorithmisches Eskalationsmanagement.** Maschinen kalkulieren die exakte Vergeltungsschwelle, um gegnerische Vorstöße zu stoppen, ohne den nuklearen Schwellenübertritt auszulösen. `[im Aufbau]`.
41. **Sprosse 41: Autonome Schauplatz-Befehlsgewalt.** Ein gesamter Kriegsschauplatz wird infolge von Kommunikationsunterbrechung oder Führungsunfähigkeit einer autonomen Gefechtsarchitektur unterstellt. `[im Aufbau]`.
42. **Sprosse 42: Taktische Verhandlung zwischen Maschinen.** Gegnerische KI-Architekturen etablieren über Datenkanäle im Maschinentakt lokale Waffenstillstände, Demarkationslinien und Evakuierungskorridore ohne Einbindung der Politik. `[im Aufbau]`.
43. **Sprosse 43: Autonome domänenübergreifende Vergeltung.** Das System leitet Cyber-, Wirtschafts- oder konventionelle kinetische Schläge gegen das Territorium des Gegners ein, sobald vordefinierte Schwellenverletzungen registriert werden. `[im Aufbau]`.
44. **Sprosse 44: Kriegsbeendigung im Maschinentakt oder allgemeine Erschöpfung.** Der Konflikt endet nicht durch Vertragsunterzeichnung, sondern weil Maschinensysteme errechnen, dass der gegenseitige Grenznutzen null erreicht hat oder die Munitionsbestände physisch erschöpft sind. `[im Aufbau]`.

---

## Was die Eskalationsleiter offenbart

Betrachtet man die vierundvierzig Sprossen als einen zusammenhängenden Prozess, bricht die grundlegende Fiktion der gegenwärtigen Sicherheitspolitik zusammen.

Militärdoktrinen wiederholen mantrenartig, „der Mensch werde bei tödlichen Entscheidungen stets in der Schleife verbleiben“. Dieser Satz gilt als Glaubensartikel, juristischer Schutzschild und moralische Rechtfertigung.

Die Leiter belegt, dass diese Zusage ingenieurtechnisch nicht haltbar ist. Zwischen Sprosse 1 (der Mensch zielt, die Maschine stabilisiert) und Sprosse 44 (Maschinensysteme verhandeln das Kriegsende) existiert kein singulärer Moment, an dem die Menschheit theatralisch ihre Abdankung verkündet.

Stattdessen hat der verantwortliche Offizier auf jeder einzelnen Sprosse einen rationalen, nachvollziehbaren und oft lebensrettenden Grund, eine weitere Millisekunde Latenz abzugeben. Man gibt Latenz auf Sprosse 9 ab, um feindliches Jamming zu überwinden. Man gibt sie auf Sprosse 12 ab, weil die Bediener vor Erschöpfung zusammenbrechen. Man tritt sie auf Sprosse 24 ab, weil eine Panzerabwehrrakete mit dreihundert Metern pro Sekunde anfliegt und menschliche Nervenbahnen schlicht zu langsam feuern.

Jeder Einzelschritt ist ein taktischer Erfolg. Das Gesamtergebnis ist die vollständige, unumkehrbare Verdrängung menschlicher Steuerungsfähigkeit aus dem Krieg.

Wir wenden uns in Kapitel V der genauen Verortung unserer Gegenwart auf dieser Leiter zu: Den datierten, verifizierbaren Tatsachen, die belegen, dass unsere Zivilisation Schwelle B bereits überschritten hat und gegenwärtig in die Kontingentfreigaben von Band III abgleitet.
