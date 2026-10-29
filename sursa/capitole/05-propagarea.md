---
nr: 5
id: propagarea
titlu: Cum ajung undele radio departe (propagarea)
tema: Propagarea undelor radio – unda de suprafață, ionosfera, unda directă, orizontul radio
parte: S
stele: 3
itemi: 2–3
timp: 60 min
grile: S10
sursa: A. S. Tanenbaum, Rețele de calculatoare, ed. a III-a, pag. 86–92; F.T.-T.-5.1 și F.T.-T.-5.2 (propagarea undelor)
---

::: pe-scurt
O undă radio poate ajunge la destinație pe **3 drumuri**: **pe lângă pământ** (unda de suprafață), **reflectată din cer** de ionosferă (unda spațială, în **HF**) sau **în linie dreaptă** (unda directă, în **VHF**). Dacă știi desenul de mai jos, știi tot capitolul.
:::

::: fisa Cele 3 drumuri ale undei radio
{{desen:propagare|HF: unda de suprafață merge pe lângă sol, unda spațială se întoarce din ionosferă. Între ele rămâne zona de tăcere. Unda directă (VHF) apare în desenul cu orizontul radio.}}

| Drumul | Cum merge | Gama | Cât de departe |
|---|---|---|---|
| **Unda de suprafață** | **pe lângă sol**, urmând curbura Pământului | LF, MF, HF de jos | zeci–sute de km |
| **Unda spațială** (ionosferică) | urcă, **se întoarce din ionosferă** și coboară departe | **HF** | sute–**mii** de km |
| **Unda directă** | **în linie dreaptă**, de la antenă la antenă | **VHF, UHF** | până la **orizont** |

> 🌍 **Unda de suprafață** = apa care curge pe lângă pământ. **Unda spațială** = mingea aruncată în tavan care cade departe. **Unda directă** = lanterna: luminează doar ce „vede”.
:::

::: fisa Regula de buzunar a frecvenței
- **Frecvență mică** → unda **ocolește obstacolele**, „curge” pe lângă Pământ, dar transportă **puține date**.
- **Frecvență mare** → unda se comportă **ca lumina**: merge **drept**, face **umbre** în spatele dealurilor, se **reflectă**, e **absorbită de ploaie** (la GHz).

> 💡 **Cu cât frecvența crește, cu atât unda seamănă mai mult cu lumina.**
:::

::: fisa Ionosfera: „oglinda” din cer pentru HF
**Ionosfera** = straturi de aer **ionizat de Soare**, la **60–500 km** altitudine.

| Strat | Unde | Ce face |
|---|---|---|
| **D** | 60–90 km | există **doar ziua**; **absoarbe** frecvențele joase. **Dispare noaptea.** |
| **E** | 90–130 km | ziua, reflectă parțial |
| **F1, F2** | 200–400 km | **F2 e cel mai important pentru HF la distanță**. **Noaptea F1 și F2 se unesc** într-un singur strat F. |

**MUF** (frecvența maximă utilizabilă) = cea mai mare frecvență care **încă se mai întoarce** spre Pământ. ⚠️ **Peste MUF, unda trece prin ionosferă și se pierde în spațiu.**

**Ziua sau noaptea?**
- **Ziua** Soarele ionizează puternic → poți folosi **frecvențe HF mai mari**.
- **Noaptea** ionizarea scade → MUF scade → **cobori frecvența**.

> 🌍 Ionosfera e ca o **plasă de tenis**: ziua e întinsă și ține și mingi rapide (frecvențe mari). Noaptea se lasă, iar mingile rapide trec prin ea, așa că trebuie să arunci mai încet (frecvențe mai mici).

> 🧮 Ai legătură HF ziua pe **8 MHz**, iar seara dispare. Ce faci? **Cobori frecvența** (de exemplu la 4–5 MHz).
:::

::: fisa Zona de tăcere și NVIS
**Zona de tăcere** = zona în care **nu se aude nimic**: unda de suprafață **s-a stins**, iar unda spațială **încă n-a coborât**.

> 🧮 Doi operatori HF la **60 km** unul de altul **nu se aud**, dar o stație la **600 km** se aude bine. De ce? Sunt în **zona de tăcere**.

**Soluția: NVIS** (*Near Vertical Incidence Skywave*):
- trimiți unda **aproape vertical**, în sus;
- ea se întoarce **în jurul tău**, pe o rază de **0–300 km**, deci **acoperă zona de tăcere** și văile dintre munți;
- folosești **frecvențe HF joase (2–10 MHz)** și o **antenă orizontală, montată jos**.

> 🌍 E ca un **duș**: arunci apa drept în sus și cade peste tot în jurul tău.
:::

::: fisa Orizontul radio în VHF
În VHF, unda merge în linie dreaptă, iar **Pământul e curbat**. Așa că bătaia e limitată de **orizont**.

{{desen:orizont-radio|Cu cât antenele sunt mai sus, cu atât „se văd” de mai departe peste curbura Pământului.}}

> **d [km] ≈ 4,12 × (√h₁ + √h₂)**   (h₁, h₂ = înălțimile antenelor, în **metri**)

> 🧮 Antene la **4 m** și **4 m**: d = 4,12 × (2 + 2) ≈ **16 km**.
> Antene la **9 m** și **16 m**: d = 4,12 × (3 + 4) ≈ **29 km**.
> Releu la **100 m** și stație la **4 m**: d = 4,12 × (10 + 2) ≈ **49 km**.

- Orizontul **radio** e cu ~15% **mai departe** decât cel **optic** (3,57·√h), pentru că atmosfera (**refracția troposferică**) curbează puțin unda în jos.

> 🌍 Ca atunci când te urci pe un bloc: vezi mai departe. De aceea **releele se pun pe dealuri**.
:::

::: fisa Atenuarea și alte fenomene
- În spațiu liber, puterea scade cu **pătratul distanței (1/d²)**. **Distanța dublă → −6 dB** (de 4 ori mai slab).
- Pierderea crește și cu **frecvența**.
- **Fading** = semnalul **scade și crește periodic**, pentru că mai multe unde sosesc pe drumuri diferite și se „bat” între ele.
- **Ploaia** atenuează la frecvențe **de ordinul GHz**.
- **Ducting troposferic** = rar, unda VHF/UHF ajunge **anormal de departe** din cauza vremii.
- **Difuzia troposferică (tropo-scatter)** = legături **dincolo de orizont**, folosind împrăștierea undelor în troposferă.
- **Activitatea solară** (ciclu de ~11 ani, furtuni solare) influențează **HF**.
- **Viteza undelor radio** = **3·10⁸ m/s** (viteza luminii), **aceeași pentru orice frecvență**. Au fost prezise de **Maxwell** și demonstrate de **Hertz**.
:::

::: flash
Cele 3 drumuri ale undei radio? || <b>Unda de suprafață</b>, <b>unda spațială (ionosferică)</b>, <b>unda directă</b>.
Cum se propagă LF/MF? || Ca <b>undă de suprafață</b>, pe lângă sol.
Cum ajunge HF la mii de km? || Prin <b>reflexie pe ionosferă</b> (unda spațială).
Cum se propagă VHF/UHF? || Prin <b>undă directă</b>, în linie de vedere.
Unde e atenuarea undei de suprafață cea mai mică? || Deasupra <b>apei sărate (mării)</b>.
Ce e ionosfera? || Straturi de aer <b>ionizat de Soare</b>, la 60–500 km.
Stratul care absoarbe ziua și dispare noaptea? || <b>Stratul D</b>.
Stratul cel mai important pentru HF la distanță? || <b>F2</b> (noaptea, F1 și F2 se unesc în <b>F</b>).
Ce e MUF? || <b>Frecvența maximă utilizabilă</b>: cea mai mare care încă se întoarce din ionosferă.
Ce se întâmplă peste MUF? || Unda <b>trece prin ionosferă</b> și se pierde.
Noaptea, în HF, folosești frecvențe…? || <b>Mai mici</b> decât ziua.
Ce e zona de tăcere? || Zona dintre sfârșitul undei de suprafață și locul unde <b>revine unda spațială</b>.
Ce e NVIS? || Unda HF trimisă <b>aproape vertical</b>, pentru 0–300 km; acoperă zona de tăcere.
NVIS – ce frecvențe și ce antenă? || <b>HF joase (2–10 MHz)</b>, antenă <b>orizontală, joasă</b>.
Formula orizontului radio? || <b>d ≈ 4,12(√h₁ + √h₂)</b> km, h în metri.
Antene la 9 m și 16 m – orizontul? || 4,12 × 7 ≈ <b>29 km</b>.
De ce e orizontul radio mai departe decât cel optic? || Din cauza <b>refracției troposferice</b>.
Distanța se dublează – cu cât scade semnalul? || <b>6 dB</b> (de 4 ori).
Ce e fadingul? || Variația semnalului din cauza <b>interferenței undelor</b> sosite pe drumuri diferite.
Ploaia afectează ce frecvențe? || Pe cele de <b>ordinul GHz</b>.
Viteza undelor radio? || <b>3·10⁸ m/s</b>, aceeași pentru orice frecvență.
Cine a prezis undele EM? Cine le-a demonstrat? || <b>Maxwell</b>; <b>Hertz</b>.
:::
