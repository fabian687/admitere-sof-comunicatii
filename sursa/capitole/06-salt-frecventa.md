---
nr: 6
id: salt-frecventa
titlu: Stația radio VHF și saltul de frecvență
tema: Generalități despre comunicațiile radio, performanțele saltului de frecvență, propagarea în VHF
parte: S
stele: 3
itemi: 2–3
timp: 50 min
grile: S02
sursa: F.T.-T.-5.2 Manualul instrucției operatorului stațiilor radio cu salt de frecvență în gama VHF (2007), Cap. II art. 11–31
---

::: pe-scurt
Stațiile radio de luptă lucrează în **VHF (30–88 MHz)** și folosesc **saltul de frecvență (FH)**: sar de pe o frecvență pe alta de sute de ori pe secundă, ca inamicul să nu le poată **asculta**, **bruia** sau **localiza**. La grilă se întreabă **avantajele FH** și **ce trebuie să aibă stațiile în comun**.
:::

::: fisa Radioul: plusuri și minusuri
| ✅ Avantaje | ❌ Dezavantaje |
|---|---|
| legătura se face **repede** | poate fi **interceptată** (ascultată) |
| merge **în mișcare** | poate fi **bruiată** |
| ajunge în locuri **greu accesibile** | stația poate fi **localizată prin radiogoniometrie**, apoi lovită |
| un mesaj ajunge **la mulți deodată** (rețea) | depinde de **teren** și de propagare |

**Radiogoniometrie** = aflarea **poziției** unui emițător după **direcția** din care vine semnalul.
:::

::: fisa Războiul electronic, pe scurt
| Prescurtare | Cine o face | Ce înseamnă |
|---|---|---|
| **ESM** (sprijin electronic) | inamicul | **ascultă**, interceptează, **localizează** |
| **ECM** (contramăsuri) | inamicul | **bruiază**, înșală |
| **ECCM** (contra-contramăsuri) | **noi** | **ne apărăm**: **salt de frecvență**, criptare, putere mică, disciplină radio |

> 💡 **Saltul de frecvență este o măsură ECCM**: ne protejează de bruiaj și interceptare.
:::

::: fisa Ce este saltul de frecvență (FH)
În loc să emită mereu pe **aceeași** frecvență, stația **sare** pe altă frecvență de **sute de ori pe secundă**, după o ordine **pseudo-aleatoare** (pare la întâmplare, dar e calculată). **Toate stațiile din rețea sar deodată**, pe aceleași frecvențe și în aceeași ordine.

{{desen:salt-frecventa|Fiecare pătrățel e un „salt” de câteva milisecunde. Doar stațiile care știu cheia pot urmări traseul.}}

Tehnica face parte din familia **spectrului împrăștiat**: semnalul ocupă, în timp, o bandă **mult mai largă** decât are nevoie.

> 🌍 **Doi prieteni care schimbă canalul TV după un plan secret**, la fiecare secundă. Cine se uită din afară vede doar bucăți fără sens. Ei doi, pentru că au același plan și același ceas, urmăresc filmul întreg.
:::

::: fisa Ce trebuie să aibă stațiile în comun
Ca să poată lucra împreună în FH, stațiile trebuie să aibă **aceleași 4 lucruri**:

| Element | La ce folosește |
|---|---|
| **Setul de frecvențe** (*hopset*) | **pe ce frecvențe** se sare |
| **Cheia de salt (TRANSEC)** | **în ce ordine** se sare. E **secretă**. |
| **Sincronizarea timpului** | **când** se sare: toate în același moment |
| **Identificatorul rețelei** | ca mai multe rețele să lucreze în aceeași bandă fără să se încurce |

> ⚠️ **Fără sincronizarea timpului NU există legătură în FH.** Variantele de grilă care spun „nu necesită sincronizare” sunt greșite.

> 🌍 E ca un **dans în grup**: toți trebuie să știe **pașii** (cheia), **muzica** (setul de frecvențe) și să pornească **pe aceeași bătaie** (sincronizarea).
:::

::: fisa Avantajele saltului de frecvență – pică sigur
1. **Rezistă la bruiaj**: bruiajul pe o frecvență strică doar **câteva salturi**, iar erorile se corectează.
2. **Greu de interceptat (LPI)**: cel care ascultă **nu știe unde vei fi** în clipa următoare.
3. **Greu de detectat și localizat (LPD)**: fiecare salt e foarte scurt, iar energia e împrăștiată.
4. **Rezistă la fading**: o frecvență proastă afectează doar câteva salturi.
5. **Mai multe rețele în aceeași bandă**: cu chei și identificatori diferiți, rețelele se „ciocnesc” rar.
6. **Securitate mai mare**, mai ales împreună cu **criptarea**.

**Dezavantaje:** cere **sincronizare**, gestionarea **cheilor** și **planurilor de frecvențe**, echipamente **mai complexe**.

| | Frecvență fixă | Salt de frecvență |
|---|---|---|
| Bruiaj | vulnerabil | **rezistent** |
| Interceptare / localizare | ușoare | **dificile** |
| Complexitate | mică | mare (chei, sincronizare) |
:::

::: fisa VHF: totul depinde de înălțime și de teren
**VHF** = **30–300 MHz**, lungimi de undă **10 m – 1 m**. Stațiile de luptă folosesc **30–88 MHz**.

- Se propagă prin **undă directă**, **în linie de vedere**.
- ⚠️ **Nu se întoarce din ionosferă**: o **străbate**. Deci VHF **nu face legături la mii de km**.
- Ocolește puțin crestele prin **difracție** (mai bine la frecvențele de jos, 30–50 MHz).
- **Pădurea** (mai ales udă) **absoarbe** semnalul.
- În spatele unui deal apare o **zonă de umbră radio**.
- Reflexiile pe clădiri și stânci produc **propagare multicale** și **fading**.

**Orizontul radio:** d ≈ **4,12 × (√h₁ + √h₂)** km.

> 🧮 Antene la **4 m** ambele: d ≈ 4,12 × 4 ≈ **16 km**. Releu la **100 m** + stație la **4 m**: d ≈ 4,12 × 12 ≈ **49 km**. De aceea **releele stau pe dealuri**.
:::

::: fisa Ce faci practic dacă nu ai legătură
- **Urcă** pe un punct mai înalt sau **mută-te** câțiva metri. Contează mult.
- Nu sta **în spatele** unui deal sau al unei clădiri față de corespondent.
- Verifică **antena**: să fie întinsă **vertical**, cu aceeași polarizare.
- Folosește **puterea minimă necesară**: te ascunzi de inamic și economisești bateria.
- Cere **retranslație** (releu).
:::

::: flash
Principalul avantaj al radioului față de fir? || Se realizează <b>repede</b> și merge <b>în mișcare</b>.
Dezavantajele radioului? || Poate fi <b>interceptat, bruiat</b>, iar stația poate fi <b>localizată</b>.
Ce e radiogoniometria? || Aflarea <b>poziției</b> unui emițător după direcția semnalului.
FH e ESM, ECM sau ECCM? || <b>ECCM</b> (protecția noastră).
Ce e saltul de frecvență? || Schimbarea <b>pseudo-aleatoare și sincronă</b> a frecvenței, de multe ori pe secundă, de toate stațiile din rețea.
FH face parte din tehnica…? || <b>Spectrului împrăștiat</b>.
Cele 4 lucruri comune pentru FH? || <b>Setul de frecvențe, cheia (TRANSEC), sincronizarea timpului, ID-ul rețelei</b>.
Cheia de salt e de tip…? || <b>TRANSEC</b>.
Fără sincronizare în FH? || <b>Nu există legătură.</b>
De ce rezistă FH la bruiaj? || Bruiajul atinge doar <b>câteva salturi</b>, iar erorile se corectează.
LPI = ? || <b>Probabilitate mică de interceptare</b>: nu se știe unde va fi următorul salt.
Mai multe rețele FH în aceeași bandă – cum? || Cu <b>chei/identificatori diferiți</b>.
Banda VHF și lungimea de undă? || <b>30–300 MHz</b>, <b>10 m – 1 m</b> (tactic 30–88 MHz).
Cum se propagă VHF? || Prin <b>undă directă</b>, în linie de vedere.
VHF și ionosfera? || O <b>străbate</b>; nu se întoarce.
Ce e zona din spatele dealului? || <b>Zonă de umbră radio</b>.
Cum ocolește VHF crestele? || Prin <b>difracție</b>.
Pădurea udă în VHF? || <b>Absoarbe</b> semnalul.
Semnal venit pe mai multe drumuri? || <b>Propagare multicale</b> → fading.
Antene la 4 m – orizontul radio? || Aproximativ <b>16 km</b>.
Cea mai eficientă măsură pentru bătaie mai mare în VHF? || <b>Antene mai sus</b>, puncte dominante.
Ce putere folosești? || <b>Puterea minimă necesară</b>.
:::
