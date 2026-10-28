# Admitere SOF în activitate – Comunicații (017) · 2026–2027

**Materialul complet de pregătire** pentru concursul de admitere la **cursul de formare a subofițerilor în activitate**, Școala de Instruire pentru Comunicații, Tehnologia Informației și Apărare Cibernetică, **specialitatea Comunicații (017)**. Seria a II-a: **3 decembrie 2026**.

Structura respectă **exact tematica și bibliografia** din Anexa 5 a Metodologiei 2026–2027.

---

## Start rapid

1. Citește **[Ghidul examenului și planul pe 5 săptămâni](00-ghid-examen.md)** (10 minute).
2. Ia capitolele **în ordinea din plan**. Fiecare are **teorie explicată logic** → **fișă rapidă** → **grile cu răspunsuri**.
3. Din săptămâna a 5-a: **[simulări complete](simulari/)** (45 de itemi, 90 de minute).
4. Zilnic, în ultima săptămână: **[fișa recapitulativă](fisa-recapitulativa.md)**.
5. **Quiz interactiv** (pe telefon): [`quiz/index.html`](quiz/index.html). Descarcă fișierul și deschide-l în browser. Merge **offline**, are mod de **simulare cu cronometru** și **„refă greșelile”**.

---

## Cuprins

### Pregătire de specialitate – 25 de itemi la examen

| Cap. | Tema din tematică | Grile |
|---|---|---|
| [S01](specialitate/S01.md) | Bazele comunicațiilor și informaticii: rolul SCI, tactica armei, linii radio, game de frecvență, antene | [42](grile/S01.md) |
| [S02](specialitate/S02.md) | Comunicații radio, **saltul de frecvență**, propagarea în **VHF** | [30](grile/S02.md) |
| [S03](specialitate/S03.md) | Rețele radio, **disciplina radio**, **radiotelefonie** (prowords, alfabet NATO) | [40](grile/S03.md) |
| [S04](specialitate/S04.md) | Sprijinul C&I în operațiile Forțelor Terestre | [18](grile/S04.md) |
| [S05](specialitate/S05.md) | Mijloacele plutonului C&I: subsistemul local și subsistemul radio de campanie | [13](grile/S05.md) |
| [S06](specialitate/S06.md) | Moduri de transfer: comutație de circuite / mesaje / pachete, **STM, ATM** | [28](grile/S06.md) |
| [S07](specialitate/S07.md) | Trunchiuri, **multiplexare** (FDM, TDM, **E1/T1**, PDH, SDH), comutație | [30](grile/S07.md) |
| [S08](specialitate/S08.md) | **Medii de transmisie**; Nyquist, Shannon, dB | [30](grile/S08.md) |
| [S09](specialitate/S09.md) | **Conversia analog-numerică** (eșantionare, cuantizare, PCM) | [29](grile/S09.md) |
| [S10](specialitate/S10.md) | **Propagarea undelor radio** (ionosferă, HF, VHF, NVIS) | [29](grile/S10.md) |
| [S11](specialitate/S11.md) | **Toate formulele + 27 de probleme rezolvate** | [23](grile/S11.md) |

### Legislație – 20 de itemi la examen

| Cap. | Actul | Grile |
|---|---|---|
| [L01](legislatie/L01.md) | Constituția României | [75](grile/L01.md) |
| [L02](legislatie/L02.md) | Legea 45/1994 a apărării naționale | [29](grile/L02.md) |
| [L03](legislatie/L03.md) | Legea 346/2006 privind organizarea și funcționarea MApN | [29](grile/L03.md) |
| [L04](legislatie/L04.md) | Legea 80/1995 privind statutul cadrelor militare | [61](grile/L04.md) |
| [L05](legislatie/L05.md) | Legea 121/2011 – misiuni în afara teritoriului | [15](grile/L05.md) |
| [L06](legislatie/L06.md) | Legea 122/2011 – regimul armelor, **uzul de armă** | [34](grile/L06.md) |
| [L07](legislatie/L07.md) | Legea 182/2002 – protecția informațiilor clasificate | [39](grile/L07.md) |
| [L08](legislatie/L08.md) | HG 585/2002 – standardele de protecție a informațiilor clasificate | [35](grile/L08.md) |
| [L09](legislatie/L09.md) | HG 106/2011 – Ghidul carierei militare | [15](grile/L09.md) |
| [L10](legislatie/L10.md) | RG-1 – Regulamentul de ordine interioară în unitate (M.38/2016) | [15](grile/L10.md) |
| [L11](legislatie/L11.md) | Regulamentul serviciului interior (M.26/2025) | [11](grile/L11.md) |
| [L12](legislatie/L12.md) | RG-3 – Regulamentul disciplinei militare (M.64/2013) | [14](grile/L12.md) |

### Antrenament

- **[8 simulări complete](simulari/)** – fiecare are 25 + 20 de itemi și barem cu explicații
- **[Quiz interactiv](quiz/index.html)** – toate cele **684 de grile**, pe capitole sau amestecate, cu simulare cronometrată
- **[Fișa recapitulativă](fisa-recapitulativa.md)** – toate cifrele și „cine decide ce”, pe 2 pagini

---

## ⚠️ Ce trebuie completat de la unitate

Unele documente din bibliografie **nu sunt publice integral**: **RG-1, RG-3, Regulamentul serviciului interior** (publicat în extras) și **manualele F.T. și C.I.** de comunicații. Pentru acestea, capitolele dau **structura, logica și regulile generale sigure**, plus **tabele „✍️ de completat”**. Le completezi cu documentul în față, de la unitate. Merită făcut: sunt puncte sigure.

Dacă faceți poze sau aveți PDF-urile cu aceste documente, ele pot fi adăugate aici și capitolele pot fi completate cu grile exacte.

---

## Pentru modificări (tehnic)

Grilele sunt scrise în `tools/intrebari/*.txt` (format simplu: `?` întrebare, `+` corect, `-` greșit, `=` explicație). Rulează:

```bash
python3 tools/build.py
```

Comanda regenerează `grile/`, `simulari/` și `quiz/index.html`. Variantele se amestecă automat, ca răspunsul corect să nu fie mereu pe aceeași literă.
