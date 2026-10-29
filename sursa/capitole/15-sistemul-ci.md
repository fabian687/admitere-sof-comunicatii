---
nr: 15
id: sistemul-ci
titlu: Sistemul C&I al Forțelor Terestre și plutonul C&I
tema: Sprijinul de comunicații și informatică în operațiile Forțelor Terestre; mijloacele de comunicații și informatică ale plutonului C&I
parte: S
stele: 2
itemi: 2–3
timp: 60 min
grile: S04, S05
sursa: F.T.-10 Manualul sprijinului de comunicații și informatică în operațiile Forțelor Terestre (Sibiu 2007), Cap. II art. 39–77, Cap. III art. 126–145 · F.T./T-4 Manualul pentru luptă al plutonului de comunicații și informatică (Sibiu 2007), Cap. II art. 22–28, 40–52
---

::: pe-scurt
Cum arată **rețeaua de comunicații a armatei** de la general până la soldat, și **ce are în dotare plutonul tău** (viitoarea ta unitate). Înveți **nivelurile sistemului**, **nodurile**, **COMSEC/TRANSEC**, **principiile**, **cine are ce structură C&I** și cele **două subsisteme ale plutonului**: **local** (în PC) și **radio** (spre exterior).
:::

::: fisa Avertisment: manualele nu sunt publice
> ℹ️ Manualele **F.T.-10** și **F.T./T-4** nu sunt publice. Capitolul descrie **arhitectura standard** a unui sistem tactic de comunicații (NATO, la care s-a aliniat doctrina românească), explicată logic. **Denumirile exacte** ale structurilor din manualele din 2007 și **modelele concrete** de echipamente se verifică în manual și la unitate (tabelul „de completat” de la final).
:::

::: fisa Ideea de bază: un sistem pe 3 niveluri
Sistemul de comunicații și informatică (SCI) leagă **toate punctele de comandă (PC)**, de la nivel strategic până la soldat.

{{desen:sistem-ci|Rețea radio de luptă la nivel tactic, noduri de tranzit și de acces în sistemul de zonă, și rețeaua locală a unui punct de comandă.}}

| Nivel | Cum se leagă |
|---|---|
| **Strategic** | sistem **fix** (permanent): fibră, radioreleu fix, centre de comunicații |
| **Operativ** | sistem de **campanie de zonă**: noduri + radioreleu + satelit |
| **Tactic** | **rețele radio de luptă (CNR)** + sisteme locale la PC |

Componentele sunt **complementare**: fiecare face ce face mai bine.

> 🌍 Ca **rețeaua de drumuri**: autostrada (sistemul fix), drumurile naționale (sistemul de zonă) și potecile din sat (radioul de luptă). Ai nevoie de toate.
:::

::: fisa Rețeaua radio de luptă (CNR)
**CNR** (*Combat Net Radio*) = stațiile **HF, VHF, UHF** ale unităților care luptă, organizate în **rețele radio**.

- Este **principalul** mijloc care **merge în mișcare** la nivelurile cele mai joase (grupă, pluton, companie, batalion).
- **VHF cu salt de frecvență (FH)**, 30–88 MHz → distanțe **mici și medii**.
- **HF** → distanțe **mari** și legătura cu cei aflați dincolo de linia de vedere.

> 💡 La întrebarea „ce mijloc merge **în mișcare** la nivel tactic?” → **rețeaua radio de luptă (CNR)**.
:::

::: fisa Sistemul de zonă – „coloana vertebrală”
Sistemul de zonă (sistemul de trunchiuri) este **coloana vertebrală** (*backbone*) a comunicațiilor din teatrul de operații.

- Are **noduri de comunicații** legate între ele prin **radioreleu de mare capacitate** (trunchiuri multiplexate), **satelit** și **fibră/cablu**.
  - **Noduri de tranzit (de trunchi)** → formează **rețeaua în ochiuri** (*mesh*). Dacă un nod cade, traficul se **re-rutează automat** pe altă cale.
  - **Noduri de acces** → **conectează punctele de comandă** la rețea.
  - **Puncte de acces radio** pentru abonați mobili → stațiile de pe vehicule intră în rețea ca într-o rețea de telefonie mobilă.
- Oferă **voce, date, video**, cu capacitate mare, pe zone întinse.

> 🌍 **Nodurile de tranzit** sunt **intersecțiile** mari; **nodurile de acces** sunt **intrările** în fiecare cartier. Dacă o intersecție se blochează, ocolești pe altă stradă: asta e rețeaua în ochiuri.

> ⚠️ Capcană: **nod de acces** = leagă un **PC** la rețea. **Nod de tranzit** = leagă **noduri între ele**.
:::

::: fisa Alte piese ale sistemului
- **Sistemul local al PC**: rețeaua locală (LAN, telefonie, terminale) din interiorul PC. Leagă **celulele statului major** între ele și cu **nodul de acces**.
- **Comunicațiile prin satelit**: pentru **distanțe mari**, dincolo de linia de vedere (**BLOS**), pentru legătura cu **eșaloanele superioare** și cu **forțele din misiuni externe**.
- **Sistemul informatic (C2IS)**: aplicațiile prin care statul major **planifică**, **vede situația** (imaginea operațională comună) și **transmite ordine și rapoarte**. Merge **peste** infrastructura de comunicații.
- **Managementul sistemului**: planificarea și gestionarea **frecvențelor**, **managementul rețelei** (configurare, monitorizare, re-rutare) și al **cheilor criptografice**.
:::

::: fisa Securitatea: COMSEC, TRANSEC, INFOSEC
| Sigla | Ce protejează | Exemple |
|---|---|---|
| **COMSEC** | **comunicațiile** | **criptare**, chei, materiale criptografice |
| **TRANSEC** | **transmisia** | **salt de frecvență**, putere redusă, antene directive |
| **INFOSEC** | **informația** din sisteme informatice | parole, controlul accesului |
| securitate **fizică** și a **personalului** | locurile și oamenii | pază, verificarea persoanelor |

> 💡 **COM**SEC = **COM**unicații = **cifrezi**. **TRAN**SEC = **TRAN**smisie = **ascunzi emisia** (salt, putere mică).
:::

::: fisa Principiile sprijinului C&I
| Principiu | Ce înseamnă |
|---|---|
| **Planificare centralizată, execuție descentralizată** | un singur plan de comunicații, executat de fiecare eșalon |
| **Redundanța** | **cel puțin două căi** independente către fiecare PC important |
| **Prioritatea** | întâi legăturile cele mai importante |
| **Flexibilitatea** | sistemul se reconfigurează după situație |
| **Continuitatea** | inclusiv pe timpul deplasării PC |
| **Securitatea** | criptare și protecție împotriva războiului electronic |
| **Interoperabilitatea** | compatibilitate cu aliații (NATO) |
| **Standardizarea** | echipamente și proceduri comune |

**Deplasarea PC fără pierderea legăturii** se face **pe eșaloane**: o parte a centrului de comunicații **rămâne** și ține legătura, cealaltă se **mută**, se instalează și **preia** legătura. Abia apoi se mută prima parte.

> 🌍 Ca atunci când **muți o echipă de fotbal pe teren nou**: jucătorii nu pleacă toți odată, ca să nu rămână poarta goală.
:::

::: fisa Cine are ce structură C&I
**Regula:** **fiecare eșalon** are propria structură C&I, potrivită ca mărime. Ea realizează **centrul de comunicații** al PC și legăturile cu subordonații („**de sus în jos**”).

| Eșalon | Structura C&I tipică |
|---|---|
| **Statul Major / comandamente operative** | structuri C&I de nivel operativ (batalioane/regimente C&I) |
| **Divizie** | **batalion de comunicații și informatică** |
| **Brigadă** | **batalion / companie de C&I** |
| **Batalion** | **pluton de comunicații și informatică (Pl.C.I.)** |
| **Companie** | **grupă / echipă de comunicații** (operatori radio) |

**Atribuții generale ale structurilor C&I:**
- **planifică, instalează, exploatează și mențin** sistemele eșalonului;
- **realizează centrele de comunicații** ale PC;
- asigură **securitatea** comunicațiilor;
- **restabilesc** legăturile întrerupte;
- asigură **mentenanța** echipamentelor;
- fac **managementul frecvențelor** și al rețelelor la nivelul lor.

Șeful structurii C&I este și **consilierul comandantului** pentru comunicații și informatică. La statul major corespunde compartimentului **J6 / G6 / S6**. La **batalion și brigadă** compartimentul se notează **S6**.

> 💡 **Batalion → pluton C&I → S6.** Plutonul tău e la batalion.
:::

::: fisa Plutonul C&I – ce face
Plutonul C&I este structura de comunicații a **batalionului**. El:
- **instalează și exploatează centrul de comunicații al PC al batalionului**;
- face legăturile PC batalion **cu companiile** (subordonați), **cu eșalonul superior** și **cu vecinii / structurile care cooperează**;
- asigură **sistemul local** al PC (telefonie, rețea de date, terminale);
- asigură **securitatea** comunicațiilor și **mentenanța de nivel scăzut**.

**Compunere tipică (orientativ):** comanda plutonului, **grupa (grupele) radio**, **grupa de fir / telefonie**, **grupa de informatică / date**, vehicule și echipamente de alimentare. Compunerea exactă e în F.T./T-4 art. 22–28.
:::

::: fisa Subsistemul local (în PC)
**Ce este:** mijloacele care asigură comunicațiile **în interiorul PC** și **în imediata lui apropiere**. Leagă **celulele statului major**, comandantul și punctele de lucru între ele și cu subsistemele de transport (radio, radioreleu).

| Componentă | Rol |
|---|---|
| **Centrala (comutatorul) telefonică de campanie** | face **legăturile telefonice** între abonații PC și cu exteriorul (prin trunchiuri) |
| **Terminale telefonice** | la fiecare abonat |
| **Rețeaua locală de date (LAN)** | leagă **calculatoarele** / terminalele (switch-uri, routere) |
| **Cabluri de campanie** (fir, multiperechi, fibră) | mediul fizic al legăturilor locale |
| **Echipamente de criptare** | protejează traficul care **iese din PC** |
| **Interfețe cu radio / radioreleu** | conectează sistemul local la rețelele exterioare |
| **Surse de energie** (grupuri electrogene, acumulatori) | alimentează întregul centru |

✅ **Avantaje:** capacitate mare, siguranță (prin fir e **greu de interceptat și bruiat**).
❌ **Dezavantaje:** **timp de instalare** și **mobilitate redusă** față de radio.

> 🌍 E ca **telefonul și internetul din birou**: stabile și sigure, dar legate de un loc.
:::

::: fisa Subsistemul radio de campanie (spre exterior)
**Ce este:** stațiile radio ale plutonului (și ale batalionului) și rețelele organizate cu ele.

| Componentă | Rol |
|---|---|
| **Stații VHF (FH) portabile** (*manpack*) | pentru comandanți și operatori la pas; **rețelele batalionului și ale companiilor** |
| **Stații VHF (FH) vehiculare** | **putere mai mare, antene mai înalte → bătaie mai mare**, montate pe vehicule |
| **Stații HF** | **distanțe mari**, dincolo de linia de vedere (cu eșalonul superior) |
| **Stații de retranslație** | **măresc bătaia** și ocolesc obstacolele |
| **Antene** | adaptate gamei și distanței |
| **Echipamente de date prin radio** | mesaje text, poziții (GPS), date tactice |

**Rețelele radio tipice ale batalionului:**
- **rețeaua de comandă a batalionului** → **NCS = stația comandantului de batalion**;
- **rețeaua de comandă a eșalonului superior** (brigadă) → batalionul este **stație subordonată**;
- **rețele de cooperare** (artilerie, vecini);
- **rețele logistice / administrative**;
- rețele de **avertizare**.

> ⚠️ Capcană: în rețeaua **batalionului**, NCS e stația **comandantului de batalion**. În rețeaua **brigăzii**, batalionul e **stație subordonată**.
:::

::: fisa Cum se leagă cele două subsisteme
**Subsistemul local = „în PC”** (fix, mult trafic, fir). **Subsistemul radio = „spre exterior și în mișcare”**.

**Interfața** dintre ele permite ca un ofițer din PC să vorbească de la telefonul lui cu o stație radio din teren.

```
Eșalon superior (brigadă)
        ▲  radio HF/VHF, radioreleu, satelit
        │
CENTRUL DE COMUNICAȚII AL PC BATALION
  RADIO DE CAMPANIE  ◄─ interfață ─►  LOCAL (centrală, LAN, telefoane)
        │ rețele radio de comandă
        ▼
Companiile 1, 2, 3, compania de sprijin
```

> 💡 **Local = „în casă”. Radio = „în teren”. Interfața = „ușa” dintre ele.**
:::

::: fisa De completat din manual / de la unitate
Aici **nu inventăm** nimic. Notează din F.T./T-4 și din dotarea unității:

| Ce | Răspunsul tău |
|---|---|
| Tipul stației VHF FH portabile (denumire, gamă, putere) | **de completat** |
| Tipul stației VHF vehiculare (putere, bătaie) | **de completat** |
| Tipul stației HF (gamă, moduri, putere) | **de completat** |
| Tipul centralei telefonice de campanie (număr de abonați) | **de completat** |
| Tipul cablului de campanie | **de completat** |
| Compunerea exactă a Pl.C.I. (F.T./T-4 art. 22–28) | **de completat** |
:::

::: flash
Mijlocul principal care merge în mișcare la nivel tactic? || <b>Rețelele radio de luptă (CNR)</b>.
CNR = ? || <b>Combat Net Radio</b>: stații HF, VHF, UHF în rețele.
„Coloana vertebrală” a sistemului de campanie? || <b>Sistemul de zonă</b> (noduri + radioreleu + satelit).
Nodurile care conectează PC la sistemul de zonă? || <b>Nodurile de acces</b>.
Nodurile care formează rețeaua în ochiuri? || <b>Nodurile de tranzit (de trunchi)</b>.
Avantajul rețelei în ochiuri? || Dacă un nod cade, traficul se <b>re-rutează</b> pe altă cale.
Legăturile de mare capacitate între noduri? || <b>Radioreleu</b> (și satelit, fibră).
Rețeaua locală a PC face parte din…? || <b>Sistemul local al punctului de comandă</b>.
Satelitul se folosește pentru…? || <b>Distanțe mari</b> (dincolo de linia de vedere) și legătura cu eșaloanele superioare / misiunile externe.
COMSEC? || Securitatea <b>comunicațiilor</b>: criptare, chei.
TRANSEC? || Securitatea <b>transmisiei</b>: salt de frecvență, putere redusă, antene directive.
INFOSEC? || Securitatea <b>informației</b> din sistemele informatice.
Principiul „minimum 2 căi independente”? || <b>Redundanța</b>.
Cum se deplasează centrul de comunicații fără să piardă legătura? || <b>Pe eșaloane</b> (în salturi).
Principiul de planificare a sprijinului C&I? || <b>Planificare centralizată, execuție descentralizată</b>.
Structura C&I la batalion? || <b>Plutonul de comunicații și informatică</b>.
Compartimentul C&I la batalion / brigadă? || <b>S6</b>.
Structura C&I a fiecărui eșalon realizează în primul rând…? || <b>Centrul de comunicații</b> al PC.
Gestionarea frecvențelor și monitorizarea rețelelor fac parte din…? || <b>Managementul sistemului</b>.
Imaginea operațională comună și ordinele electronice vin de la…? || <b>Sistemul informatic (C2IS)</b>.
Plutonul C&I instalează și exploatează în principal…? || <b>Centrul de comunicații al PC batalion</b>.
Subsistemul local asigură comunicațiile…? || <b>În interiorul PC</b> și în imediata lui apropiere.
Rolul centralei telefonice de campanie? || Face <b>legăturile telefonice</b> între abonați și cu exteriorul.
Avantajul legăturilor prin fir? || <b>Greu de interceptat și bruiat</b>.
Dezavantajul legăturilor prin fir față de radio? || <b>Timp de instalare mai mare, mobilitate redusă</b>.
Subsistemul radio de campanie cuprinde…? || <b>Stații VHF (FH) portabile și vehiculare, stații HF, retranslație</b>, antene, accesorii.
Stațiile HF se folosesc pentru…? || <b>Distanțe mari</b> și legături dincolo de linia de vedere.
VHF vehiculare față de portabile? || <b>Putere mai mare, bătaie mai mare</b>.
Ce permite unui abonat telefonic din PC să vorbească la radio? || <b>Interfața</b> dintre sistemul local și cel radio.
NCS în rețeaua de comandă a batalionului? || <b>Stația comandantului de batalion</b>.
În rețeaua brigăzii, stația batalionului e…? || <b>Stație subordonată</b>.
Rolul echipamentelor de criptare din centrul de comunicații? || Să <b>protejeze traficul</b> care iese din PC.
:::
