---
nr: 3
id: unde-radio
titlu: Undele radio, frecvențele și antenele
tema: Rolul comunicațiilor militare, elemente de tactica armei, bazele comunicațiilor, linii radio, antene
parte: S
stele: 3
itemi: 3–4
timp: 75 min
grile: S01
sursa: F.T.-T.-5.1 Manualul instrucției soldatului/gradatului voluntar din arma comunicații și informatică (2007), Cap. I art. 11–15, Cap. II art. 29–32, 37, Cap. III art. 140–152, 215–243, 267–299
---

::: pe-scurt
Baza întregii specialități. Afli **de ce există comunicațiile militare**, **ce mijloace de legătură există**, **cum circulă un semnal**, **gamele de frecvență** (HF, VHF…) și **cum funcționează antena**. Ai și o singură formulă de știut: **λ = 300 / f**.
:::

::: fisa De ce există comunicațiile militare
Un comandant nu poate conduce dacă nu poate **da ordine** și **primi rapoarte**. Comunicațiile sunt **sistemul nervos** al armatei.

- **Sprijinul de comunicații și informatică (SCI)** asigură **schimbul de informații** necesar **comenzii și controlului** forțelor.
- Este un **sprijin de luptă**: nu luptă direct, dar fără el nimeni nu poate lupta organizat.

> 🌍 Corpul omenesc: creierul (comandantul) nu poate mișca mâna (trupele) dacă **nervii** (comunicațiile) sunt tăiați.
:::

::: fisa Cele 4 cerințe ale comunicațiilor militare
| Cerință | Ce înseamnă | Întrebarea de control |
|---|---|---|
| **Operativitate** | informația ajunge **la timp** | „Ajunge ordinul înainte să fie prea târziu?” |
| **Fiabilitate** (siguranță) | sistemul merge **chiar dacă un element cade** | „Dacă pică o stație, mai am legătură?” |
| **Continuitate** | legătura **nu se întrerupe**, nici în deplasare | „Am legătură și când ne mutăm?” |
| **Securitate** | inamicul **nu află** ce vorbim și unde suntem | „Ne poate asculta sau localiza?” |

În plus: **mobilitate**, **flexibilitate**, **interoperabilitate** (să putem vorbi cu aliații NATO), **supraviețuire** (rezistență la bruiaj și lovituri).

> 💡 **O-F-C-S**: **O**perativitate, **F**iabilitate, **C**ontinuitate, **S**ecuritate.
:::

::: fisa Cine răspunde de legătură
| Regula | Cine face legătura |
|---|---|
| **De sus în jos** | **eșalonul superior** face legătura cu **subordonații** |
| **De la sprijin la sprijinit** | cine **sprijină** face legătura cu cel **sprijinit** |
| **De la întăritor la întărit** | cine **e dat în întărire** face legătura cu cel întărit |
| **De la stânga la dreapta** | între vecini, **cel din stânga** o face spre **cel din dreapta** |

> ⚠️ Indiferent de reguli, **oricine** constată că legătura s-a rupt ia măsuri să o refacă.

> 🌍 Ca într-o familie: **părintele** îl sună pe copil, nu invers. Cel care **vine să ajute** își anunță venirea celui ajutat.
:::

::: fisa Mijloacele de legătură
| Mijloc | ✅ Avantaj | ❌ Dezavantaj |
|---|---|---|
| **Radio** | rapid, **merge în mișcare** | poate fi **interceptat, bruiat, localizat** |
| **Radioreleu** | capacitate mare, pe direcții | doar **în linie de vedere** |
| **Satelit** | distanțe foarte mari | scump, dependent de satelit |
| **Fir / cablu** | **cel mai sigur**: nu poate fi bruiat sau ascultat ușor | **greu de instalat și de mutat** |
| **Curieri** (mijloace mobile) | foarte siguri | **lenți** |
| **Semnalizare** (rachete, fanioane, sirene) | simplu, imediat | doar mesaje **convenite dinainte** |

> 💡 **În mișcare → radio.** **Pe loc, cu mult trafic → fir sau radioreleu.** **Secret maxim → fir sau curier.** **Departe → HF sau satelit.** Nimic nu e perfect, de aceea mijloacele **se combină**.
:::

::: fisa Cum se organizează legăturile
| Mod | Cum arată | Plus / minus |
|---|---|---|
| **Pe direcții (radial)** | de la comandant **câte o legătură directă** spre fiecare subordonat | sigur, dar consumă multe mijloace |
| **Pe axă** | o **linie principală** de-a lungul direcției de acțiune, la care se leagă subordonații | economic, dar vulnerabil dacă se rupe axa |
| **În rețea (nodal)** | **noduri** legate în ochiuri; traficul ocolește un nod distrus | **cel mai fiabil**, mai complex |

**Centrul de comunicații al punctului de comandă (PC)** = **toate mijloacele** de comunicații de la PC, organizate să lucreze **împreună**: stații radio, radioreleu, centrală telefonică, criptare, curieri.

> 🌍 **Pe direcții** = te suni cu fiecare prieten separat. **În rețea** = drumurile dintr-un oraș: dacă una e blocată, ocolești pe alta.
:::

::: fisa Cum circulă un semnal
{{desen:lant-transmisie|Orice comunicație are aceeași schemă: cineva emite, mediul transportă, altcineva recepționează. Pe drum se adaugă zgomot.}}

- **Semnalul** = ceea ce poartă informația (tensiune, curent, undă).
- **Analogic** = variază **continuu** (vocea). **Digital** = doar **0 și 1**.
- **Banda vocii la telefon:** **300–3400 Hz**.
- **Zgomotul** = semnal nedorit. **Raportul semnal/zgomot (S/N)** spune cât de „curată” e recepția.
:::

::: fisa Modulația: cum „urcă” vocea pe o undă radio
Vocea are frecvențe mici (sute de Hz). Ca s-o trimiți direct ți-ar trebui o antenă de **zeci de kilometri**. Așa că vocea se „pune” pe o **undă purtătoare** de frecvență mare. Asta se numește **modulație**.

| Tip | Ce se modifică la purtătoare | Unde e folosit |
|---|---|---|
| **MA (AM)** | **amplitudinea** (cât de „mare” e unda) | radio pe unde medii |
| **MF (FM)** | **frecvența** (cât de „deasă” e unda) | **VHF tactic**; mai **rezistentă la zgomot** |
| **BLU (SSB)** | AM cu **o singură bandă laterală**, fără purtătoare | **HF**; ocupă **jumătate** din bandă, economisește putere |

> 🌍 Purtătoarea e un **camion**, vocea e **marfa**. Modulația înseamnă să încarci marfa în camion ca să ajungă departe.
:::

::: fisa Simplex, semi-duplex, duplex
| Mod | Ce înseamnă | Exemplu |
|---|---|---|
| **Simplex** (unidirecțional) | într-un singur sens | radioul din mașină |
| **Semi-duplex** | în ambele sensuri, **pe rând** | **stația cu PTT**: vorbești, apoi asculți |
| **Duplex** | în ambele sensuri, **în același timp** | **telefonul** |

> ⚠️ În limbajul radio militar, „**simplex**” înseamnă și lucrul **pe o singură frecvență**, pe rând. La grilă, dacă te întreabă de **stația cu PTT**, răspunsul e **semi-duplex**.
:::

::: fisa Gamele de frecvență
{{desen:game-frecventa|Gamele radio în ordine. Cu cât frecvența e mai mare, cu atât unda e mai scurtă.}}

| Gama | Frecvențe | Undele se numesc | Folosire militară |
|---|---|---|---|
| **LF** | 30–300 kHz | lungi (kilometrice) | navigație |
| **MF** | 0,3–3 MHz | medii | radiodifuziune AM |
| **HF** | **3–30 MHz** | **scurte (decametrice)** | **distanțe mari** (prin ionosferă) |
| **VHF** | **30–300 MHz** | **ultrascurte (metrice)** | **radio tactic: 30–88 MHz** |
| **UHF** | 0,3–3 GHz | decimetrice | radioreleu, aviație, satelit |
| **SHF** | 3–30 GHz | centimetrice | radioreleu, satelit, radar |

> 💡 **Ordinea gamelor:** **L**ow → **M**edium → **H**igh → **V**ery **H**igh → **U**ltra **H**igh → **S**uper **H**igh. Fiecare e de **10 ori** peste cea dinainte.
:::

::: fisa Formula de aur: λ = 300 / f
**Lungimea de undă (λ)** = distanța dintre două „creste” ale undei.

> **λ [metri] = 300 / f [MHz]**

> 🧮 **30 MHz** → λ = 300/30 = **10 m**. **75 MHz** → λ = **4 m**. **300 MHz** → λ = **1 m**. **7 MHz** → λ ≈ **43 m**.

> 🌍 Valurile pe apă: **valuri dese** (frecvență mare) sunt **scurte**, **valuri rare** (frecvență mică) sunt **lungi**. Produsul lor e mereu același: viteza luminii.
:::

::: fisa Antena
**Antena** transformă semnalul electric în **undă radio** (la emisie) și invers (la recepție). Aceeași antenă le face pe amândouă.

{{desen:antene|Antena bici are un sfert de lungime de undă. Dipolul are o jumătate.}}

| Antena | Lungimea | Radiază | Folosire |
|---|---|---|---|
| **Bici** (verticală) | **λ/4** | **în toate direcțiile** (omnidirecțională) | **rețele radio** (corespondenții sunt peste tot) |
| **Dipol** | **λ/2** (impedanță ≈ **73 Ω**) | în două direcții | HF, antene fixe |
| **Directivă** (Yagi, parabolă) | — | **într-o singură direcție**, cu câștig mare | **radioreleu**, punct la punct |

- **Polarizarea** = orientarea undei. Antena **verticală** dă polarizare **verticală**. ⚠️ **Ambele antene trebuie să aibă aceeași polarizare.**
- **SWR (raportul de unde staționare)** arată cât de bine e adaptată antena. **Ideal: 1:1.** Dacă e mare, puterea se întoarce în stație și se pierde.
- **Înălțimea antenei** contează enorm în VHF: **mai sus = mai departe**.

> 🧮 Antena bici pentru **75 MHz**: λ = 4 m → λ/4 = **1 m**. Dipol pentru **150 MHz**: λ = 2 m → λ/2 = **1 m**.

> 🌍 Antena omnidirecțională e un **bec**: luminează în toate părțile. Antena directivă e o **lanternă**: bate departe, dar într-o singură direcție.
:::

::: fisa Ce determină bătaia unei stații
**Bătaia** = distanța maximă la care ai legătură. Depinde de:
1. **puterea** emițătorului;
2. **sensibilitatea** receptorului;
3. **antena**: tip, **înălțime**, orientare;
4. **frecvența** (gama);
5. **terenul**: dealuri, păduri, clădiri;
6. **zgomotul și bruiajul**.

**Retranslația (releul):** o stație pe un **punct înalt** primește și **retransmite**. Așa **mărești bătaia** și **ocolești obstacolele**.

> 🌍 Releul e ca un om urcat pe deal care **strigă mai departe** ce aude de la tine.
:::

::: flash
Ce asigură sprijinul C&I? || <b>Schimbul de informații</b> necesar comenzii și controlului forțelor.
Ce categorie de sprijin e SCI? || <b>Sprijin de luptă</b>.
Cele 4 cerințe principale ale comunicațiilor? || <b>Operativitate, fiabilitate, continuitate, securitate</b>.
Ce e operativitatea? || Informația ajunge <b>la timp</b>.
Ce e interoperabilitatea? || Capacitatea de a comunica <b>cu aliații (NATO)</b>.
Cine face legătura cu subordonații? || <b>Eșalonul superior</b> (de sus în jos).
Între vecini, cine face legătura? || Cel din <b>stânga</b> spre cel din <b>dreapta</b>.
Între sprijin și sprijinit? || <b>Cel care sprijină</b>.
Cel mai sigur mijloc față de interceptare? || <b>Firul</b> (și curierii).
Principalul mijloc în mișcare? || <b>Radioul</b>.
Organizarea cea mai fiabilă a legăturilor? || <b>În rețea (nodal)</b>: traficul ocolește nodurile distruse.
Ce e modulația? || „Punerea” informației pe o <b>undă purtătoare</b> de frecvență mare.
AM vs FM? || AM variază <b>amplitudinea</b>; FM variază <b>frecvența</b> și e mai rezistentă la zgomot.
Avantajul BLU (SSB)? || Ocupă <b>jumătate din bandă</b> și economisește putere.
Stația cu PTT lucrează în…? || <b>Semi-duplex</b> (pe rând).
Telefonul lucrează în…? || <b>Duplex</b> (simultan).
Banda vocii la telefon? || <b>300–3400 Hz</b>
Gama HF? || <b>3–30 MHz</b>, unde <b>scurte (decametrice)</b>.
Gama VHF? || <b>30–300 MHz</b>, unde <b>ultrascurte (metrice)</b>.
Banda VHF tactică? || <b>30–88 MHz</b>
Formula lungimii de undă? || <b>λ = 300 / f[MHz]</b> metri
λ la 30 MHz? La 300 MHz? || <b>10 m</b>. <b>1 m</b>.
Antena bici are lungimea…? || <b>λ/4</b>; e verticală și <b>omnidirecțională</b>.
Antena bici pentru 75 MHz? || λ = 4 m → <b>1 m</b>
Dipolul are lungimea…? Impedanța? || <b>λ/2</b>; aproximativ <b>73 Ω</b>.
Ce antenă la radioreleu? || <b>Directivă</b> (câștig mare, o singură direcție).
Polarizarea antenelor celor doi corespondenți? || <b>Aceeași</b>.
SWR ideal? || <b>1:1</b>
Cum mărești bătaia VHF și ocolești dealurile? || <b>Retranslație</b> (releu) pe un punct înalt.
:::
