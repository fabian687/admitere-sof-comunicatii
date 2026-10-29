---
nr: 12
id: medii-transmisie
titlu: Medii de transmisie
tema: Medii de transmisie
parte: S
stele: 2
itemi: 1–2
timp: 55 min
grile: S08
sursa: A. S. Tanenbaum, Rețele de calculatoare, ed. a III-a 1998, pag. 76–92 · ed. a IV-a 2003, pag. 82–98 · T. Rădulescu, Rețele de telecomunicații, 2005, pag. 94–98
---

::: pe-scurt
**Prin ce merge semnalul**: fire răsucite, cablu coaxial, fibră optică sau aer (radio, microunde, infraroșu, laser). Plus **două formule** care spun **câți biți pe secundă** încap într-un canal: **Nyquist** și **Shannon**, și **decibelii**. Pică des: **de ce se răsucesc firele**, **50 Ω / 75 Ω**, **reflexia totală** și **calculele simple**.
:::

::: fisa Lărgimea de bandă
- Orice mediu **atenuează** frecvențele diferit. Lasă să treacă bine doar un **interval de frecvențe** = **lărgimea de bandă B**, în **Hz**.
- Un semnal digital (dreptunghiular) este o **sumă de sinusoide** (**Fourier**).
- Dacă banda e **prea îngustă**, semnalul se **deformează** și biții nu mai pot fi deosebiți.

> 🌍 Banda e ca **lățimea unei țevi**: cu cât e mai lată, cu atât trece mai multă apă (mai mulți biți) pe secundă.
:::

::: fisa Nyquist – canal FĂRĂ zgomot ⚠️
**Debitul maxim = 2 · B · log₂(V)** [bit/s]

- **B** = lărgimea de bandă (Hz);
- **V** = câte **niveluri** distincte are semnalul.

Pentru semnal **binar** (V = 2, log₂2 = 1): **D_max = 2B**.

| V (niveluri) | log₂V |
|---|---|
| 2 | 1 |
| 4 | 2 |
| 8 | 3 |
| 16 | 4 |

> 🧮 Canal **3 kHz**, binar → 2 × 3000 × 1 = **6000 bit/s**.
> Cu **4 niveluri** → 2 × 3000 × 2 = **12.000 bit/s**.
> Canal **4 kHz**, **8 niveluri** → 2 × 4000 × 3 = **24 kbit/s**.

> 💡 **Nyquist = „N”o noise** (fără zgomot) și are **2** în față.
:::

::: fisa Shannon – canal CU zgomot ⚠️
**C = B · log₂(1 + S/N)** [bit/s]

- **S/N** = raportul semnal/zgomot, ca **raport de puteri** (**nu** în dB!).
- Dacă ți se dă în dB, îl **transformi întâi**: 30 dB → 1000.

> 🧮 **Exemplul clasic (Tanenbaum):** canal telefonic **3000 Hz**, **30 dB** → S/N = 1000 → C = 3000 × log₂(1001) ≈ 3000 × 9,97 ≈ **30.000 bit/s**.

> 🧮 Canal **1 MHz**, **20 dB** → S/N = 100 → C = 10⁶ × log₂101 ≈ 10⁶ × 6,66 ≈ **6,66 Mbit/s**.

- ⚠️ **Shannon este o limită absolută**: **niciun** truc de codare nu o poate depăși.
- **Nyquist** = cât poți scoate **fără zgomot**. **Shannon** = maximul posibil **cu zgomot**.

> 🌍 Shannon e ca o **discuție într-un bar gălăgios**: cu cât muzica (zgomotul) e mai tare față de vocea ta (semnalul), cu atât poți spune mai puține lucruri pe minut.
:::

::: fisa Decibelii, rapid
**S/N [dB] = 10 · log₁₀(S/N)**

| Raport de puteri | dB |
|---|---|
| ×2 | **+3 dB** |
| ×10 | **+10 dB** |
| ×100 | **+20 dB** |
| ×1000 | **+30 dB** |
| ×½ | **−3 dB** |

- **dBm** = puterea raportată la **1 mW**: **0 dBm = 1 mW**; **30 dBm = 1 W**; **40 dBm = 10 W**.
- **Atenuarea** unui cablu se dă în **dB/km** (sau dB/100 m). Atenuările în dB **se adună**.

> 🧮 Un cablu atenuează **3 dB** → ajunge **jumătate** din putere (50%).
> Stația emite **10 W** = 10.000 mW → 10 · log₁₀(10.000) = **40 dBm**.

> 💡 **Fiecare zero = 10 dB.** 1000 are 3 zerouri → **30 dB**. 100 → **20 dB**. Iar **3 dB = dublu sau jumătate**.
:::

::: fisa Perechea torsadată
**Două fire de cupru izolate, răsucite** unul în jurul celuilalt.

⚠️ **De ce se răsucesc?** Ca să **reducă interferențele electromagnetice** și **diafonia** (*crosstalk*, „scurgerea” semnalului între perechi vecine). Perturbațiile induse în cele două fire se **anulează**.

- Folosire: **bucla locală telefonică** și **rețele locale (Ethernet)**.
- **UTP** = **neecranată** (*Unshielded*): ieftină, cea mai răspândită.
- **STP** = **ecranată** (*Shielded*): mai bună la perturbații, mai scumpă.
- **Cat 3** – telefonie, 10 Mbit/s. **Cat 5** – **mai multe răsuciri pe cm** și izolație mai bună → **100 Mbit/s**. **Cat 5e/6** → 1 Gbit/s și peste.
- Distanța: câțiva **km** în analogic; pentru date de mare viteză, ~**100 m** (Ethernet).
- ✅ ieftină, ușor de instalat. ❌ bandă limitată, sensibilă la perturbații, atenuare mare.

> 💡 **U**TP = **U**nshielded = fără ecran. **S**TP = **S**hielded = cu ecran.
:::

::: fisa Cablul coaxial
Din interior spre exterior: **conductor central** de cupru → **izolator (dielectric)** → **ecran** (tresă / folie) → **manta**.

**Ecranul** îi dă **imunitate mai bună la zgomot** și **bandă mai mare** decât perechea torsadată.

| | **Bandă de bază** | **Bandă largă** |
|---|---|---|
| Impedanță | **50 Ω** | **75 Ω** |
| Semnal | **digital** | **analogic** (cu FDM) |
| Folosire | rețele locale vechi (Ethernet 10Base2/10Base5) | **televiziunea prin cablu** (CATV) |

> 💡 **75 Ω = televizorul** din sufragerie. **50 Ω = digital**, rețelele vechi.

> 🌍 E cablul care intră în **televizor** de la cablu TV.
:::

::: fisa Fibra optică – cum funcționează ⚠️
Informația merge ca **impulsuri de lumină**: **1 = lumină**, **0 = întuneric**.

**3 componente:**
1. **sursa de lumină** – **LED** sau **dioda laser**;
2. **mediul** – **fibra** de sticlă (sau plastic), foarte subțire;
3. **detectorul** – **fotodioda**, care transformă lumina în impuls electric.

**De ce rămâne lumina în fibră?** Prin **reflexie totală internă**. **Miezul** (*core*) are **indicele de refracție mai mare** decât **învelișul** (*cladding*). O rază care lovește peretele sub un unghi mai mare decât **unghiul critic** se **reflectă total** și rămâne în miez.

{{desen:fibra|Raza de lumină se lovește de peretele miezului și se întoarce înapoi, iar și iar: reflexia totală internă. Miezul are indice de refracție mai mare decât învelișul.}}

> 🌍 Ca o **minge de biliard** care tot ricoșează de mantinele și merge înainte pe masa lungă.
:::

::: fisa Multimod sau monomod
| Tip | Miezul | Cum merge lumina | Folosire |
|---|---|---|---|
| **Multimod** | mare (**~50 µm**) | **multe raze** (moduri), la unghiuri diferite → **dispersie modală** | distanțe **scurte**, **LED** |
| **Monomod** | foarte mic (**~8–10 µm**) | practic **în linie dreaptă**, **un singur mod** | **distanțe mari**, viteze mari, **laser** |

- **Dispersia** = impulsurile se **lățesc** pe drum și ajung să se suprapună. Limitează viteza și distanța. Soluții: impulsuri speciale (**solitoni**), fibră **monomod**.
- **Ferestrele de transmisie** (atenuare minimă), în infraroșu: **0,85 µm**, **1,30 µm**, **1,55 µm**. Cea mai mică atenuare: **1,55 µm**, ~**0,2 dB/km**.

> ⚠️ Capcană: **dispersia modală** apare la **multimod**, pentru că razele merg pe drumuri de **lungimi diferite** și ajung la momente diferite.

> 💡 **Mono = unu**: un singur drum, deci merge **departe**.
:::

::: fisa Fibra față de cupru
| ✅ Avantaje fibră | ❌ Dezavantaje fibră |
|---|---|
| **lărgime de bandă uriașă** | interfețele (emițătoare/receptoare) sunt **scumpe** |
| **atenuare foarte mică** → repetoare la **zeci de km** | **fragilă** la îndoire |
| **imună** la perturbații electromagnetice (și la fulgere) | **un singur sens** pe o fibră → trebuie **2 fibre** |
| **greu de interceptat** (nu radiază) → **securitate** | joncțiunile (sudurile, conectorii) sunt delicate |
| **ușoară, subțire**, nu se corodează | |

> ⚠️ La grilă „avantaj al fibrei” → de obicei **imunitatea la perturbații EM** sau **banda uriașă**. „Dezavantaj” → **interfețe scumpe** / **fragilă** / **un singur sens**.
:::

::: fisa Mediile fără fir
Undele se propagă cu **c = 3·10⁸ m/s**; **λ · f = c**.

| Mediu | Ce trebuie să știi |
|---|---|
| **Radio** (LF–VHF) | **omnidirecțional**, **trece prin clădiri**. Frecvențele joase urmăresc solul; HF se reflectă pe ionosferă |
| **Microunde** (> 100 MHz, GHz) | **linie dreaptă**, **antene parabolice directive**, **relee (turnuri)** la câteva zeci de km din cauza curburii Pământului; **absorbite de ploaie** la frecvențe mari; sensibile la **fading multicale**. Folosire: **radioreleu**, telefonie la distanță, satelit |
| **Infraroșu** | distanțe **foarte mici** (telecomenzi); **nu trece prin pereți** → securitate bună într-o cameră |
| **Laser în aer liber** | legătură între **două clădiri**, bandă mare, ieftină; **afectat de ploaie, ceață** și de curenții de convecție (aer cald) |

**Spectrul**, crescător în frecvență: **radio → microunde → infraroșu → lumină vizibilă → ultraviolet → raze X → raze gamma**. Comunicațiile folosesc partea de jos, până la lumina vizibilă.

> 🌍 **Infraroșul** e **telecomanda televizorului**: nu poți schimba canalul din altă cameră, pentru că nu trece prin perete.

> 💡 Spectrul: **„Radioul Mic Inventează Lumini Ultra Xtra Gama”**: Radio, Microunde, Infraroșu, Lumină, Ultraviolet, X, Gamma.
:::

::: flash
Formula Nyquist? || <b>2 · B · log₂V</b> (canal fără zgomot).
3 kHz, semnal binar – debit Nyquist? || <b>6000 bit/s</b>.
4 kHz, 8 niveluri – debit Nyquist? || <b>24 kbit/s</b> (2 × 4000 × 3).
Formula Shannon? || <b>B · log₂(1 + S/N)</b> (canal cu zgomot).
30 dB = ce raport de puteri? || <b>1000</b>.
20 dB = ? || <b>100</b>.
3000 Hz, 30 dB – capacitatea Shannon? || ≈ <b>30.000 bit/s</b>.
Atenuare 3 dB – cât ajunge? || ≈ <b>jumătate</b> din putere.
1 W în dBm? || <b>30 dBm</b>.
10 W în dBm? || <b>40 dBm</b>.
Se poate depăși limita Shannon? || <b>Nu</b>, e limită absolută.
De ce se răsucesc firele? || Ca să <b>reducă interferențele și diafonia</b>.
UTP? || Pereche torsadată <b>neecranată</b>.
Cat 5 față de Cat 3? || <b>Mai multe răsuciri pe cm</b>, izolație mai bună → 100 Mbit/s.
Coaxial de bandă de bază? || <b>50 Ω</b>, digital.
Coaxial de bandă largă (CATV)? || <b>75 Ω</b>, analogic.
Coaxial față de torsadat? || <b>Imunitate mai bună la zgomot</b> și <b>bandă mai mare</b>.
Cele 3 componente ale sistemului optic? || <b>Sursă (LED/laser) + fibră + detector (fotodiodă)</b>.
Ce transformă lumina în semnal electric? || <b>Fotodioda</b>.
De ce rămâne lumina în fibră? || <b>Reflexie totală internă</b>.
Fibra monomod? || Miez <b>~8–10 µm</b>, un singur mod, <b>distanțe mari</b>, laser.
De ce apare dispersia modală la multimod? || Razele merg pe <b>drumuri de lungimi diferite</b>.
Ferestrele optice? || <b>0,85 / 1,30 / 1,55 µm</b>.
Fereastra cu cea mai mică atenuare? || <b>1,55 µm</b> (~0,2 dB/km).
Lățirea impulsurilor de lumină se numește…? || <b>Dispersie</b>.
Un avantaj al fibrei? || <b>Imună la perturbații EM</b>, bandă uriașă, greu de interceptat.
Un dezavantaj al fibrei? || <b>Interfețe scumpe</b>, fragilă, un singur sens pe fibră.
Microundele se propagă…? || <b>În linie dreaptă</b>, cu antene parabolice și relee; absorbite de ploaie.
Avantajul de securitate al infraroșului? || <b>Nu trece prin pereți</b>.
Laserul în aer liber e afectat de…? || <b>Ploaie, ceață</b>, curenți de convecție.
:::
