---
nr: 10
id: multiplexare
titlu: Trunchiuri și multiplexare
tema: Trunchiuri, multiplexare și comutație
parte: S
stele: 2
itemi: 1–2
timp: 50 min
grile: S07
sursa: A. S. Tanenbaum, Rețele de calculatoare, ed. a III-a, 1998, pag. 108–114 și 120–128 (sistemul telefonic: trunchiuri și multiplexare, comutație)
---

::: pe-scurt
Cum trimiți **multe convorbiri pe același fir**. Înveți **bucla locală** și **trunchiul**, cele trei feluri de multiplexare (**FDM, WDM, TDM**), cifrele lui **T1 și E1** și cum arată un **comutator** în centrală. Pică mai ales **cifrele**: **2,048 Mbit/s**, **64 kbit/s**, **125 µs**, **n²**.
:::

::: fisa Bucla locală, trunchiul și centrala
Rețeaua telefonică are **3 piese**:

| Piesa | Ce este | Cum arată |
|---|---|---|
| **Bucla locală** (*local loop*) | legătura **abonat – centrala locală** | **o pereche de fire torsadate**, semnal **analogic**, **câte una pe abonat** |
| **Trunchiul** (*trunk*) | legătura **centrală – centrală** | **digital**, **multiplexat**: **foarte multe convorbiri simultan** (fibră, coaxial, radioreleu) |
| **Centrala** (oficiul de comutație) | face **comutația** | leagă intrarea potrivită de ieșirea potrivită |

> 🌍 **Bucla locală** e **aleea** de la casa ta până la drumul principal: e doar a ta. **Trunchiul** e **autostrada** dintre orașe: pe ea merg mii de mașini deodată. **Centrala** e **nodul rutier** care trimite fiecare mașină pe drumul ei.

> ℹ️ În armată e la fel: un **trunchi** între două noduri de comunicații (de exemplu o legătură radioreleu) poartă **multe canale** de voce și date multiplexate.
:::

::: fisa Ce înseamnă multiplexare
**Multiplexare** = **mai multe semnale pe același mediu** (fir, fibră, radioreleu).

**De ce?** Un mediu are capacitate **mult mai mare** decât un singur canal de voce. E **mai ieftin** să pui multe canale pe același mediu decât să tragi câte un fir pentru fiecare.

- **MUX (multiplexorul)** = **combină** mai multe canale într-unul.
- **DEMUX (demultiplexorul)** = le **separă** la celălalt capăt.

Sunt **3 feluri**:
- **FDM** – împarte **frecvența**;
- **WDM** – împarte **lungimea de undă** (culoarea luminii), pe **fibră**;
- **TDM** – împarte **timpul**.
:::

::: fisa FDM – fiecare cu frecvența lui
**FDM** (*Frequency Division Multiplexing*) = banda totală se **împarte în subbenzi**. Fiecare canal ocupă **permanent** subbanda lui.

- Între canale se lasă **benzi de gardă**, ca să nu se încurce între ele.
- Un canal telefonic primește **4 kHz** (3,1 kHz voce + benzi de gardă).
- Se potrivește semnalelor **analogice**.

{{desen:fdm-tdm|Sus, FDM: fiecare canal are bucata lui de frecvență, tot timpul. Jos, TDM: fiecare canal are toată banda, dar doar câte o felie de timp, pe rând.}}

> 🌍 **Posturile de radio FM**: fiecare emite **pe frecvența lui**, toate în același timp, și tu alegi una din ele.
:::

::: fisa Ierarhia FDM: grup, supergrup, mastergrup
| Nivel | Ce conține | Câte canale |
|---|---|---|
| **Grup** | 12 canale × 4 kHz = **48 kHz** (banda **60–108 kHz**) | **12** |
| **Supergrup** | **5 grupuri** | **60** |
| **Grup master** (mastergrup) | **5 supergrupuri** | **300** |

ℹ️ Standardul Bell folosește 10 supergrupuri = 600 de canale. Standardul CCITT/ITU: 5 supergrupuri = **300**.

> 💡 **12 → ×5 → ×5**: **12**, **60**, **300**. Un grup are **12** canale, ca **lunile anului**.
:::

::: fisa WDM – FDM pe fibră optică
**WDM** (*Wavelength Division Multiplexing*) = **FDM pe fibră optică**.

- Fiecare canal folosește o **lungime de undă diferită** a luminii (altă „culoare”).
- Culorile se combină și se separă cu o **prismă / rețea de difracție**.
- Componentele sunt **pasive**, deci foarte fiabile.
- Permite **capacități uriașe** pe o singură fibră.

> 🌍 Ca **lumina albă printr-o prismă**: se desface în culori. La WDM fiecare culoare duce alt canal, pe aceeași fibră.
:::

::: fisa TDM – fiecare la rândul lui
**TDM** (*Time Division Multiplexing*) = fiecare canal folosește **toată banda**, dar **doar o felie scurtă de timp (slot)**, **pe rând** (*round-robin*).

- Se potrivește perfect semnalelor **digitale**.
- Datele sunt organizate în **cadre**. Un cadru are **câte un slot pentru fiecare canal**.
- Cadrul se repetă de **8000 de ori pe secundă**, adică la fiecare **125 µs** (cât e eșantionarea vocii, vezi capitolul despre voce digitală).

> 🧮 Durata cadrului: **1 / 8000 s = 125 µs**.

> 🌍 Ca la **frizer** cu un singur scaun: fiecare client stă pe scaun **câte puțin**, pe rând, și apoi se reia runda.
:::

::: fisa FDM sau TDM – comparația
| | **FDM** | **TDM** |
|---|---|---|
| Ce se împarte | **frecvența** (banda) | **timpul** |
| Fiecare canal are | o **subbandă**, **tot timpul** | **toată banda**, **o felie de timp** |
| Cum se separă canalele | **benzi de gardă** | **sincronizare** (bit/cuvânt de încadrare) |
| Potrivit pentru | semnale **analogice** | semnale **digitale** |

> 💡 **F**DM = **F**recvență. **T**DM = **T**imp. **W**DM = **W**ave (undă de lumină).

> ⚠️ Capcană: „benzi de gardă” merg cu **FDM**, nu cu TDM. TDM se ține în ordine prin **sincronizare**.
:::

::: fisa T1 și E1 – purtătoarele digitale ⚠️
Aici sunt **calculele care pică**.

**E1 (Europa, inclusiv România):**
- **32 de sloturi** × **8 biți** = **256 de biți / cadru**;
- 256 × 8000 = **2.048.000 bit/s = 2,048 Mbit/s**;
- din cele 32 de sloturi: **30 pentru voce/date**, **1 pentru sincronizare (încadrare)**, **1 pentru semnalizare**.

{{desen:cadru-e1|Cadrul E1: 32 de sloturi a câte 8 biți, repetat de 8000 de ori pe secundă. 30 de sloturi duc voce sau date, 1 duce sincronizarea, 1 duce semnalizarea.}}

**T1 (America de Nord, Japonia):**
- **24 de canale** × **8 biți** = 192 de biți + **1 bit de încadrare** = **193 de biți / cadru**;
- 193 × 8000 = **1,544 Mbit/s**.

**Un slot = un canal telefonic digital (DS0):** 8 biți × 8000 = **64 kbit/s**.

| Sistem | Canale de voce | Biți/cadru | Debit |
|---|---|---|---|
| **T1** | **24** | **193** | **1,544 Mbit/s** |
| **E1** | **30** (+2 de serviciu) | **256** | **2,048 Mbit/s** |

> 🧮 **E1:** 32 × 8 × 8000 = **2.048.000 bit/s = 2,048 Mbit/s**.

> ⚠️ Capcană: E1 are **32 de sloturi**, dar doar **30 de canale de voce**. Citește atent dacă întrebarea cere sloturi sau canale.
:::

::: fisa PDH – ierarhia „aproape sincronă”
**PDH** (ierarhia digitală **plesiocronă**) = nivelurile se multiplexează cu ceasuri **aproape** sincrone. Diferențele se acoperă cu **biți de justificare**.

Fiecare nivel ≈ **4 × nivelul anterior** (+ biți de justificare):

| Nivel | Debit | Canale de 64 kbit/s |
|---|---|---|
| **E1** | **2,048** Mbit/s | 30 |
| **E2** | **8,448** Mbit/s | 120 |
| **E3** | **34,368** Mbit/s | 480 |
| **E4** | **139,264** Mbit/s | 1920 |

> 💡 **Plesio-** = „aproape”. **Plesiocron** = **aproape sincron** → de aceea are nevoie de biți de justificare.
:::

::: fisa SDH – ierarhia sincronă
**SDH** (ierarhia digitală **sincronă**; în America: **SONET**) = toate echipamentele au **același ceas**. Asta face mai ușoară extragerea unui singur canal.

| SDH | SONET | Debit |
|---|---|---|
| — | STS-1 / OC-1 | 51,84 Mbit/s |
| **STM-1** | STS-3 / OC-3 | **155,52 Mbit/s** |
| **STM-4** | OC-12 | **622,08 Mbit/s** |
| **STM-16** | OC-48 | **2488,32 Mbit/s** (≈ 2,5 Gbit/s) |
| **STM-64** | OC-192 | ≈ **10 Gbit/s** |

- Fiecare nivel este **exact × 4** față de cel anterior.
- Cadrul SDH durează tot **125 µs**.

> 🧮 Câte canale de 64 kbit/s încap teoretic în STM-1, fără biții de serviciu? 155.520 / 64 = **2430**. Practic, STM-1 transportă **63 de fluxuri E1** = **1890** de canale de voce.

> 💡 **155 → 622 → 2488 → ~10 000**: de fiecare dată **× 4**.
:::

::: fisa Comutatorul spațial: crossbar
**Comutația spațială** = se face o **cale fizică** prin comutator, de la o intrare la o ieșire.

**Crossbar** (matrice de puncte de comutație): **n intrări × n ieșiri**, cu câte un punct de cruce la fiecare intersecție → **n² puncte**.

- ✅ Avantaj: **fără blocare**. Orice intrare se poate lega de orice ieșire liberă.
- ❌ Dezavantaj: **n² crește foarte repede**. 1000 de linii = **1.000.000** de puncte, majoritatea nefolosite.
- **Comutatoarele în mai multe etaje** (multi-stage) folosesc mai puține puncte, dar pot avea **blocare**: nu găsești cale liberă deși ieșirea e liberă.

> 🧮 Crossbar **100 × 100** → 100 × 100 = **10.000** de puncte.

> 🌍 Crossbar-ul e ca o **tablă de șah** în care fiecare pătrățel e un întrerupător: rândul = cine sună, coloana = cine e sunat.
:::

::: fisa Comutatorul temporal: TSI
**Comutația temporală** lucrează pe semnale **TDM**. Ea **schimbă ordinea sloturilor** în cadru.

- Dispozitivul se numește **TSI** (*Time Slot Interchanger* – **interschimbătorul de intervale de timp**).
- Cum lucrează: sloturile cadrului de intrare se **scriu într-o memorie (RAM)** și se **citesc în altă ordine**, după o **tabelă**. Slotul canalului A ajunge pe poziția canalului B.
- Limitare: **viteza memoriei**.
- Centralele digitale moderne combină **temporal + spațial** (structuri **T-S-T**).

**Ierarhia centralelor:**
- **centrala locală** (*end office*) – aici sunt legați abonații;
- **centrala de tranzit / interurbană** (*toll office*) – leagă centralele între ele prin **trunchiuri**;
- dacă trunchiul direct e ocupat, apelul poate fi **rutat pe o cale alternativă**, prin centrale de nivel superior.

> 🌍 TSI-ul e ca un **dirigent care reașază elevii în bănci**: îi notează pe toți într-un catalog (memoria), apoi îi strigă în altă ordine.
:::

::: flash
Legătura abonat – centrala locală? || <b>Bucla locală</b> (pereche de fire torsadate, analogică).
Legătura centrală – centrală? || <b>Trunchiul</b> (digital, multiplexat).
Din ce e făcută clasic bucla locală? || <b>Pereche de fire torsadate</b>.
Ce e multiplexarea? || <b>Mai multe semnale pe același mediu</b>.
MUX / DEMUX? || MUX <b>combină</b> canalele; DEMUX le <b>separă</b>.
FDM împarte…? || <b>Frecvența</b> (banda) în subbenzi.
TDM împarte…? || <b>Timpul</b> în sloturi, pe rând.
Ce se lasă între canalele FDM? || <b>Benzi de gardă</b>.
WDM = ? || <b>FDM pe fibră optică</b> (lungimi de undă diferite).
Banda unui canal telefonic în FDM? || <b>4 kHz</b>.
Grup FDM? || <b>12 canale</b>, 48 kHz (60–108 kHz).
Supergrup FDM? || <b>5 grupuri = 60 de canale</b>.
Grup master (CCITT)? || <b>5 supergrupuri = 300 de canale</b>.
FDM se potrivește semnalelor…? TDM? || FDM – <b>analogice</b>; TDM – <b>digitale</b>.
T1 – câte canale? || <b>24 de canale</b>.
Câți biți are un cadru T1? || <b>193</b> (24 × 8 + 1 bit de încadrare).
Debitul T1? || <b>1,544 Mbit/s</b>.
Debitul E1? || <b>2,048 Mbit/s</b>.
Un cadru E1 conține…? || <b>32 de sloturi × 8 biți</b>: 30 voce, 1 sincronizare, 1 semnalizare.
Debitul unui canal telefonic digital? || <b>64 kbit/s</b> (8 biți × 8000).
Durata unui cadru TDM pentru voce? || <b>125 µs</b> (1/8000 s).
Ce e PDH? || Ierarhia <b>plesiocronă</b> (aproape sincronă), cu <b>biți de justificare</b>.
E3 – ce debit are? || ≈ <b>34 Mbit/s</b> (34,368).
STM-1? || <b>155,52 Mbit/s</b>.
STM-4? || <b>622,08 Mbit/s</b>.
Factorul între niveluri SDH? || <b>× 4</b>.
Crossbar n × n – câte puncte? || <b>n²</b>.
Crossbar 100 × 100? || <b>10.000</b> de puncte.
Avantajul crossbar? Dezavantajul? || <b>Fără blocare</b>; dar <b>n² crește foarte repede</b>.
Comutatorul în mai multe etaje poate avea…? || <b>Blocare</b>.
TSI = ? || <b>Interschimbătorul de intervale de timp</b>: schimbă ordinea sloturilor, prin <b>memorie</b>.
:::
