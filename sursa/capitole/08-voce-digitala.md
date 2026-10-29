---
nr: 8
id: voce-digitala
titlu: Cum devine vocea digitală (PCM)
tema: Conversia analog-numerică a semnalelor – eșantionare, cuantizare, codare
parte: S
stele: 3
itemi: 1–3
timp: 45 min
grile: S09, S11
sursa: T. Rădulescu, Rețele de telecomunicații (2005), pag. 13–17
---

::: pe-scurt
Capitolul **cel mai logic**: **3 pași** (eșantionare → cuantizare → codare) și **o înmulțire**: **8000 × 8 = 64 kbit/s**. Dacă înțelegi desenul, rezolvi aproape orice grilă **fără să tocești**. Tot aici sunt și grilele de calcul din toată specialitatea.
:::

::: fisa De ce digitizăm vocea
| Avantaj | De ce |
|---|---|
| **Regenerare** | pe drum, repetoarele **refac perfect** semnalul (doar decid „0 sau 1”). **Zgomotul nu se adună.** |
| **Criptare** | biții se criptează ușor → **secret** (esențial în armată) |
| **Multiplexare** | multe canale pe același fir (vezi cap. 10) |
| **Totul în aceeași rețea** | voce, date, imagine – toate devin biți |
| ❌ **Dezavantaj** | ocupă **bandă mai mare** (64 kbit/s față de 4 kHz analogic) |

> 🌍 Copiezi o casetă de pe altă casetă: fiecare copie e mai **hârâită** (analogic). Copiezi un fișier MP3: a 100-a copie e **identică** cu prima (digital).
:::

::: fisa Cei 3 pași
{{desen:pcm|1. Iei „poze” ale undei la intervale egale. 2. Rotunjești fiecare valoare la cea mai apropiată treaptă. 3. Scrii treapta în binar.}}

| Pas | Ce faci | Pe scurt |
|---|---|---|
| **1. Eșantionare** | măsori semnalul la **intervale egale de timp** | discret **în timp** |
| **2. Cuantizare** | **rotunjești** fiecare valoare la cel mai apropiat **nivel** | discret **în valoare** |
| **3. Codare** | scrii fiecare nivel ca **număr binar** (0 și 1) | biți |

Toți trei la un loc se numesc **PCM** (*modulația impulsurilor în cod*).

> 🌍 Filmezi o mașină: **eșantionarea** = câte cadre pe secundă faci. **Cuantizarea** = câte culori are aparatul. **Codarea** = salvezi poza ca fișier.
:::

::: fisa Pasul 1: eșantionarea și regula lui 2
> **Teorema eșantionării:** ca să poți reface semnalul, eșantionezi cu o frecvență **cel puțin dublă** față de cea mai mare frecvență din semnal.
>
> **fₑ ≥ 2 × f_max**

- **Vocea la telefon** e limitată la **3,4 kHz** → s-ar cere minimum 6,8 kHz → se folosește **8 kHz** (8000 de eșantioane pe secundă).
- Un eșantion la fiecare **1/8000 s = 125 µs**.
- Dacă eșantionezi **prea rar**, apare **aliasing**: semnalul se „deghizează” în altă frecvență și **nu mai poate fi refăcut**.
- De aceea, **înainte** de eșantionare se pune un **filtru trece-jos (anti-aliasing)**.

> 🌍 **Aliasing-ul** îl vezi în filmele cu mașini: roțile par că se învârt **invers**. Camera face prea puține cadre pe secundă față de cât de repede se învârte roata.

> 🧮 f_max = **4 kHz** → fₑ ≥ **8 kHz**. Un semnal de **5 kHz** eșantionat la **8 kHz**? 8 < 10 → **aliasing**.
:::

::: fisa Pasul 2: cuantizarea și eroarea ei
- Cu **n biți** ai **2ⁿ niveluri**: **8 biți → 256** de niveluri, **7 biți → 128**, **16 biți → 65.536**.
- **Eroarea de cuantizare** = diferența dintre valoarea reală și treapta aleasă. E de **maximum ±jumătate de pas**.
- ⚠️ E **singura pierdere ireversibilă** din tot procesul.
- **Mai mulți biți = trepte mai mici = eroare mai mică.** Fiecare bit în plus aduce **≈ +6 dB** calitate.
- **Compandarea** (cuantizare neuniformă): trepte **mici** pentru sunetele **slabe** și **mari** pentru cele puternice. Calitate bună cu **același număr de biți**.
  - **Legea A** → **Europa (și România)**. **Legea µ** → America de Nord, Japonia.

> 🌍 Cuantizarea e ca o **scară**: nu poți sta între două trepte. Cu cât treptele sunt mai mici (mai mulți biți), cu atât poți sta mai aproape de înălțimea dorită.
:::

::: fisa Formula de aur: debitul PCM
> **Debit = frecvența de eșantionare × biți pe eșantion**

> 🧮 **Telefonia digitală:** 8000 × 8 = **64.000 bit/s = 64 kbit/s**. Acesta e **canalul telefonic digital de bază**.

> 🧮 **Muzică de CD:** 44.100 × 16 biți × 2 canale (stereo) ≈ **1,41 Mbit/s**.

> 🧮 **ADPCM:** 8000 × 4 biți = **32 kbit/s**.

| Metodă | Ideea | Debit voce |
|---|---|---|
| **PCM** | codezi **valoarea** fiecărui eșantion | **64 kbit/s** |
| **DPCM / ADPCM** | codezi doar **diferența** față de eșantionul anterior | **32 kbit/s** (ADPCM) |
| **Modulație delta** | **1 bit pe eșantion**: „crește” sau „scade”. Defect: **supraîncărcarea pantei** (nu ține pasul cu variațiile rapide). | 16–32 kbit/s |
:::

::: fisa La recepție
**Decodare** (din biți în trepte) → **filtru trece-jos de refacere** (netezește treptele) → **sunetul inițial**.
:::

::: fisa Toate calculele din specialitate, pe o pagină
| Formula | Exemplu |
|---|---|
| **λ = 300 / f[MHz]** | 50 MHz → **6 m**; 3 MHz → **100 m** |
| **bici = λ/4, dipol = λ/2** | 60 MHz → λ = 5 m → bici **1,25 m** |
| **orizont d ≈ 4,12(√h₁+√h₂)** | 4 m și 25 m → 4,12 × 7 ≈ **29 km** |
| **fₑ ≥ 2 f_max** | 3,4 kHz → **6,8 kHz** |
| **debit PCM = fₑ × n** | 8 kHz × 8 = **64 kbit/s** |
| **niveluri = 2ⁿ** | 8 biți → **256** |
| **Nyquist: D = 2B·log₂V** | 3 kHz, 16 niveluri → 2 × 3000 × 4 = **24 kbit/s** |
| **Shannon: C = B·log₂(1+S/N)** | 3 kHz, 30 dB (=1000) → ≈ **30 kbit/s** |
| **dB = 10·log₁₀(raport)** | 3 dB = ×2; 10 dB = ×10; 20 dB = ×100; 30 dB = ×1000 |
| **dBm** (față de 1 mW) | 1 mW = **0 dBm**; 100 mW = **20 dBm**; 1 W = **30 dBm** |
| **E1 = 32 × 8 × 8000** | **2,048 Mbit/s** |
| **T1 = 193 × 8000** | **1,544 Mbit/s** |
| **crossbar n × n** | 50 × 50 → **2500** de puncte |

> 💡 La examen **nu ai calculator**. De aceea toate grilele folosesc **numere rotunde**: puteri ale lui 2 (2, 4, 8, 16), pătrate (1, 4, 9, 16, 25, 100) și puteri ale lui 10.
:::

::: flash
Cei 3 pași ai conversiei analog-numerice? || <b>Eșantionare → cuantizare → codare</b>
Ce e eșantionarea? || Măsurarea semnalului la <b>intervale egale de timp</b>.
Ce e cuantizarea? || <b>Rotunjirea</b> fiecărui eșantion la cel mai apropiat nivel.
Ce e codarea? || Scrierea fiecărui nivel în <b>binar</b>.
Cum se numesc toți trei la un loc? || <b>PCM</b> – modulația impulsurilor în cod.
Teorema eșantionării? || <b>fₑ ≥ 2 × f_max</b>
Frecvența de eșantionare la telefon? || <b>8 kHz</b> (vocea până la 3,4 kHz).
Timpul dintre două eșantioane la 8 kHz? || <b>125 µs</b>
Ce apare dacă eșantionezi prea rar? || <b>Aliasing</b>.
Ce filtru pui înainte de eșantionare? || <b>Trece-jos (anti-aliasing)</b>.
Câte niveluri cu 8 biți? Cu 7? || <b>256</b>; <b>128</b>.
Eroarea maximă de cuantizare? || <b>±jumătate de pas</b>; e ireversibilă.
Cum reduci zgomotul de cuantizare? || Cu <b>mai mulți biți</b> pe eșantion (+6 dB/bit).
Legea de compandare în Europa? || <b>Legea A</b> (legea µ în SUA/Japonia).
Formula debitului PCM? || <b>fₑ × n</b> (eșantioane/s × biți)
Debitul canalului telefonic digital? || <b>8000 × 8 = 64 kbit/s</b>
ADPCM – debit? || <b>32 kbit/s</b>
Modulația delta – câți biți pe eșantion? || <b>1 bit</b>.
Defectul modulației delta? || <b>Supraîncărcarea pantei</b>.
Avantajul principal al digitalului pe distanțe mari? || <b>Regenerarea</b>: zgomotul nu se acumulează.
Dezavantajul PCM față de analogic? || Cere <b>bandă mai mare</b>.
Ce refăce semnalul la recepție? || <b>Filtrul trece-jos de refacere</b>.
:::
