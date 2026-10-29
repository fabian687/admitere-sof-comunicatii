---
nr: 11
id: comutatie
titlu: Circuite, mesaje, pachete; STM și ATM
tema: Moduri de transfer pentru semnale digitale (comutație de circuite, mesaje, pachete; STM și ATM)
parte: S
stele: 2
itemi: 1–2
timp: 50 min
grile: S06
sursa: T. Rădulescu, Rețele de telecomunicații, Thalia 2005, pag. 26–29, 52–61, 67–87, 327–341 · A. S. Tanenbaum, Rețele de calculatoare, ed. a III-a, 1998, pag. 56–60, 115–119, 416–419, 426–427
---

::: pe-scurt
**Cum împarți o rețea între mulți utilizatori.** Ori **rezervi o cale** pentru fiecare (comutație de **circuite**, STM), ori **tai informația în bucăți** și le trimiți când e nevoie (comutație de **mesaje** și **pachete**, ATM). Pică des: **cele 3 faze**, **store-and-forward**, **datagramă vs circuit virtual** și **celula ATM de 53 de octeți**.
:::

::: fisa Cele două „filozofii”
Ai multe surse (telefoane, calculatoare) care vor să trimită date prin **aceeași rețea**. Cum împarți rețeaua între ele?

1. **Rezervi** o cale pentru fiecare comunicare, cât durează ea → **comutație de circuite**. La nivel de transmisie: **STM**.
2. **Nu rezervi nimic.** Tai informația în bucăți și le trimiți **când e nevoie**, împărțind rețeaua cu ceilalți → **comutație de mesaje / pachete**. La nivel de transmisie: **ATM**.

{{desen:comutatie|Sus: la comutația de circuite calea A–B e rezervată de la început până la sfârșit. Jos: la comutația de pachete, bucățile merg prin noduri și împart liniile cu alții.}}

> 🌍 **Circuite** = **închiriezi un taxi** doar pentru tine: e liber tot drumul, dar plătești și când stă la semafor. **Pachete** = **autobuzul**: împarți locul cu alții, e mai ieftin, dar uneori aștepți.
:::

::: fisa Comutația de circuite
Între cei doi corespondenți se face o **cale rezervată, cap la cap**, pe toată durata comunicării.

**3 faze:**
1. **Stabilirea** conexiunii (apelul) – se rezervă calea;
2. **Transferul** datelor pe calea rezervată;
3. **Eliberarea** (desfacerea) conexiunii.

| ✅ Avantaje | ❌ Dezavantaje |
|---|---|
| **întârziere mică și constantă** după stabilire → ideal pentru **voce în timp real** | durează **stabilirea** legăturii |
| ordinea datelor e **garantată** | **calea e ocupată și când nu se transmite nimic** (pauzele din conversație) → **ineficientă** pentru date în rafale |
| capacitatea e **garantată** | dacă un nod cade, **conexiunea se pierde** |

**Exemplul clasic:** **rețeaua telefonică** tradițională.

> 💡 **S – T – E**: **S**tabilire, **T**ransfer, **E**liberare.
:::

::: fisa Comutația de mesaje
- **Nu** se stabilește o cale în avans.
- **Tot mesajul** e trimis primului nod. Nodul îl **memorează complet**, apoi îl **retransmite** mai departe.
- Asta se numește **memorează și retransmite** (*store-and-forward*).

| ✅ | ❌ |
|---|---|
| folosire mai bună a liniilor | **întârzieri mari și variabile** |
| nu trebuie stabilită legătura | nodurile au nevoie de **memorie mare** (mesajele pot fi oricât de lungi) |
| | un mesaj lung **blochează** linia pentru ceilalți |

**Exemplu istoric:** rețelele de **telegrafie** (telex).

> 🌍 Ca o **scrisoare care trece prin oficii poștale**: fiecare oficiu o primește întreagă, o ține, apoi o trimite la următorul.
:::

::: fisa Comutația de pachete
- Mesajul se **împarte în pachete** de **lungime limitată**. Fiecare are un **antet** (adresă, număr de ordine etc.).
- Fiecare pachet trece prin noduri tot prin **memorează și retransmite**.

**Avantaje:**
- **Întârziere totală mai mică** decât la mesaje: un nod retransmite primul pachet **în timp ce îl primește pe al doilea** (efect de **„bandă rulantă”**, *pipelining*).
- **Folosire foarte eficientă** a liniilor: rețeaua se împarte **statistic** între utilizatori.
- **Robustețe**: dacă un nod cade, pachetele îl pot **ocoli**.

**Dezavantaje:** **întârziere variabilă** (*jitter*), posibile **pierderi** și **congestie**.

> 🌍 **Mutarea cu mai multe mașini mici** în loc de un singur TIR: prima mașină pleacă deja în timp ce o încarci pe a doua. Ajungi mai repede.

> ⚠️ Capcană: de ce pachetele sunt mai rapide decât mesajele? Răspunsul bun e **„bandă rulantă”**: nodul trimite un pachet **în timp ce îl primește pe următorul**.
:::

::: fisa Datagramă sau circuit virtual ⚠️
Comutația de pachete are **două variante**:

| | **Datagramă** (fără conexiune) | **Circuit virtual** (orientat pe conexiune) |
|---|---|---|
| Se stabilește conexiunea? | **nu** | **da** (o „cale logică”) |
| Drumul pachetelor | **fiecare pachet independent** | toate pe **aceeași cale** |
| Ordinea de sosire | **poate fi diferită** (se reordonează la destinație) | **în ordine** |
| Adresa din pachet | **adresa completă** a destinației | doar un **identificator scurt** al circuitului |
| Dacă un nod cade | pachetele **ocolesc** | circuitul virtual **se pierde** |
| Exemple | **IP (Internet)** | **X.25, Frame Relay, ATM** |

> 💡 **Circuitul virtual** „pare” un circuit (cale fixă, ordine), dar **nu rezervă resursele doar pentru tine**: le împarte statistic cu ceilalți.

> 💡 **IP = datagramă.** X.25, Frame Relay, ATM = **circuit virtual**.
:::

::: fisa Cele trei, una lângă alta
| | Circuite | Mesaje | Pachete |
|---|---|---|---|
| Cale rezervată | **da** | nu | nu (circuitul virtual: cale logică) |
| Store-and-forward | nu | **da, tot mesajul** | **da, pe pachete** |
| Întârziere | **mică, constantă** | **mare, variabilă** | mică/medie, variabilă |
| Eficiența liniei | mică (la trafic în rafale) | bună | **foarte bună** |
| Potrivit pentru | **voce** | telegrame | **date** (și voce, cu QoS) |
:::

::: fisa Sincron, asincron, plesiocron
| Transmisia | Ce înseamnă |
|---|---|
| **Asincronă (start-stop)** | fiecare **caracter** are un **bit de start** și unul sau mai mulți **biți de stop**. Ceasul se sincronizează **la fiecare caracter**. Simplă, dar **ineficientă** (biți în plus). |
| **Sincronă** | datele merg în **blocuri (cadre) lungi**, iar ceasurile emițătorului și receptorului sunt **sincronizate permanent**. **Eficientă**. |
| **Plesiocronă** | ceasurile sunt **„aproape”** sincrone (aceeași frecvență nominală, mici abateri). Diferențele se compensează cu **biți de umplere (justificare)**. Exemplu: **PDH** (capitolul despre multiplexare). |

> 🌍 **Asincron** = vorbești cu pauze și spui „start” și „stop” la fiecare cuvânt. **Sincron** = doi soldați care merg **în pas**, tot timpul.
:::

::: fisa STM – modul de transfer sincron
- Se bazează pe **TDM**: fiecare canal primește **un slot fix** în fiecare cadru, **periodic**.
- Canalul se **recunoaște după poziția** lui în cadru.
- **Capacitatea e rezervată** chiar dacă sursa n-are ce trimite → **risipă** la traficul în rafale.
- E echivalentul **comutației de circuite**. Exemplu: rețeaua telefonică digitală (canale de **64 kbit/s**).

> 🌍 Ca un **loc rezervat la cinema**: e al tău, cu numărul tău, chiar dacă nu vii la film.
:::

::: fisa ATM – celulele de 53 de octeți ⚠️
**ATM** (*Asynchronous Transfer Mode*) trimite informația în **celule mici, de lungime fixă**:

**53 de octeți = 5 octeți antet + 48 de octeți informație utilă (payload).**

- **„Asincron”** = celulele unei surse **nu au poziții fixe** în timp. Se trimit **doar când există date**; locul liber îl folosesc alții → **multiplexare statistică**.
- ATM e **orientat pe conexiune**: folosește **circuite virtuale**. Antetul are **VPI** (calea virtuală) și **VCI** (canalul virtual).
- **De ce celule mici și fixe?**
  - **comutare rapidă în hardware** (toate au aceeași lungime);
  - **întârziere mică și previzibilă** → bună pentru **voce și video**.
- Duce **voce, date, video** în aceeași rețea, cu **clase de serviciu (QoS)**: **CBR** (rată constantă, ex. voce), **VBR** (variabilă), **ABR** (disponibilă), **UBR** (nespecificată).
- **Straturi:** **fizic** → **ATM** (comută celulele) → **AAL** (*ATM Adaptation Layer*, adaptează datele la celule).
- Viteze tipice: **155,52** și **622,08 Mbit/s** (peste SDH/SONET).

> 💡 **53 = 5 + 48.** Antetul e mic (**5**), datele sunt aproape tot (**48**).

> 🌍 Celulele ATM sunt ca **containerele standard** din port: toate au aceeași mărime, deci macaraua le mută repede, fără să se gândească.
:::

::: fisa STM sau ATM – comparația
| | **STM** | **ATM** |
|---|---|---|
| Unitatea de transfer | **slot** fix, periodic | **celulă de 53 de octeți** |
| Cum recunoști canalul | după **poziția** în cadru | după **eticheta din antet (VPI/VCI)** |
| Capacitatea | **fixă, rezervată** | **la cerere, statistică** |
| Eficiență la trafic în rafale | **mică** | **mare** |
| Seamănă cu | **comutația de circuite** | **comutația de pachete (circuit virtual)** |

> ⚠️ Capcană: în ATM „asincron” **nu** înseamnă start-stop. Înseamnă că celulele **nu au loc fix** în timp.
:::

::: fisa X.25 și Frame Relay
- **X.25** – rețea veche de pachete, cu circuite virtuale și **control al erorilor la fiecare nod**. **Lentă, dar sigură** pe linii proaste.
- **Frame Relay** – urmașul simplificat: **nu corectează erorile în noduri** (le lasă la capete), deci **mai rapid**. A apărut odată cu liniile digitale de calitate.

> 💡 **Frame Relay e mai rapid** pentru că **nu verifică erorile în fiecare nod**.
:::

::: flash
Ce se face între corespondenți în comutația de circuite? || O <b>cale rezervată</b>, cap la cap, pe toată durata.
Cele 3 faze ale comutației de circuite? || <b>Stabilire – transfer – eliberare</b>.
Rețeaua telefonică clasică folosește…? || <b>Comutație de circuite</b>.
Avantajul circuitelor pentru voce? || <b>Întârziere mică și constantă</b>.
Dezavantajul circuitelor la date în rafale? || Calea e <b>ocupată și în pauze</b> → ineficient.
„Memorează și retransmite” tot mesajul? || <b>Comutație de mesaje</b> (store-and-forward).
Dezavantaj comutație de mesaje? || <b>Întârzieri mari și variabile</b>, memorie mare în noduri.
Exemplu istoric de comutație de mesaje? || <b>Telegrafia (telex)</b>.
În comutația de pachete, mesajul este…? || <b>Împărțit în pachete</b> de lungime limitată, cu antet.
Avantajul principal al pachetelor? || <b>Folosire foarte eficientă</b> a liniilor (împărțire statistică).
De ce pachetele au întârziere mai mică decât mesajele? || <b>Bandă rulantă</b>: nodul trimite un pachet în timp ce îl primește pe următorul.
Datagramă – ce face fiecare pachet? || Merge <b>independent</b>; pot sosi în altă ordine.
Circuit virtual – cum merg pachetele? || Pe <b>aceeași cale</b>, <b>în ordine</b>.
IP folosește…? || <b>Datagrame</b>.
Exemple cu circuite virtuale? || <b>X.25, Frame Relay, ATM</b>.
Transmisia asincronă (start-stop)? || <b>Bit de start + bit(i) de stop</b> la fiecare caracter.
Transmisia sincronă? || <b>Blocuri lungi</b>, ceasuri <b>sincronizate permanent</b>.
Transmisia plesiocronă? || Ceasuri <b>aproape</b> sincrone → <b>biți de justificare</b>.
În STM canalul e identificat prin…? || <b>Poziția (slotul) în cadru</b>.
Dezavantajul STM? || Capacitatea e <b>rezervată și când nu se transmite</b>.
Lungimea celulei ATM? || <b>53 de octeți</b>.
Antetul ATM? Payload-ul? || <b>5 octeți</b>; <b>48 de octeți</b>.
„Asincron” în ATM înseamnă…? || Celulele <b>nu au poziții fixe</b> în timp; se trimit când există date.
Identificatorii din antetul ATM? || <b>VPI</b> (cale virtuală) și <b>VCI</b> (canal virtual).
De ce celule mici și fixe? || <b>Comutare rapidă în hardware</b> și <b>întârziere mică, previzibilă</b>.
Stratul care adaptează datele la celule? || <b>AAL</b> (ATM Adaptation Layer).
Clasa ATM cu rată constantă? || <b>CBR</b>.
De ce Frame Relay e mai rapid decât X.25? || <b>Nu corectează erorile în noduri</b>.
:::
