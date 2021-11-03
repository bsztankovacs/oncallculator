# oncallculator

Készenléti díj kalkulátor a [2012. évi I. törvény [ Mt. (új) ]](https://net.jogtar.hu/jogszabaly?docid=a1200001.tv)
alapján. A kalkuláció nyolc órás, hagyományos nappali (ún. "9-to-5") munkarendben dolgozó emberek számára készült,
akiknek nincsen egyéb, erre vonatkozó külön megállapodása a munkáltatójával rögzítve munkaszerződésben.
****
On-call salary/pay calculator for regular employees who work 9-to-5 with no specific agreements in their work contract.

## Vonatkozó jogszabályok

Munka törvénykönyve, 66. A bérpótlék - 139-143. §

## Számolási alap

Az alábbi díjak megilletik a munkavállalót, amennyiben ettől eltérő megállapodás nem születik a munkáltató és a
munkavállaló között.

`alapber` = alapbér, a havi alapbér összegének 174-el elosztott része (139. §. (1) a))

- 20% bérpótlék a munkaidőn kívüli órákra
    - a munkaidőn kívüli órákra, tehát 8 órás munkavégzés esetén a következő munkaidő kezdetéig, 16 órára. Ez alól
      kivételnek minősülnek azok az órák, amikor munkavégzés történik a készenlét időtartama alatt - 144. § (2))

Ha készenlét során munkavégzésre kerül sor, akkor - mivel ez munkaidőn kívüli munkavégzést jelent - a rendkívüli
munkaidőre vonatkozó bérpótlékok használata (139-143. §)

Magyarázat: [`06 - 22`/`22 - 06`]

- Hétköznapokon 50%-os bérpótlék [`1.5 * alapber` / `1.65 * alapber`] 
    - VAGY az alapbér [`1.0 * alapber` / `1.15 * alapber`] és a munkavégzés idejénél nem kevesebb szabadidő biztosítása, amire
      szintén az alapbér [`1.0 * alapber`] arányos része jár
- Hétvégéken, munkaszüneti napokon: 100%-os bérpótlék [`2.0 * alapber` / `2.15 * alapber`]
    - VAGY [`1.5 * alapber` / `1.65 * alapber`] és a munkavégzés idejénél nem kevesebb szabadidő biztosítása, amire
      szintén az alapbér [`1.0 * alapber`] arányos része jár
- 22 és 6 óra között +15% bérpótlék (142. §) jár.

## Előkészületek / Preliminaries

Mielőtt nekikezdenél, javasolt a következőket összegyűjtened a gyors haladás érdekében:

- Készenléti órák száma,
- Készenlétben dolgozott órák száma, a következő bontásban _(külön gyűjtve azokat az órákat amelyeket 22 és 06 óra
  között kezdtél meg, illetve amelyeket a készenléti időtartam alatt, munkaidőn kívül dolgoztál)_:
    - Készenlétben dolgozott órák száma hétköznapokon,
    - Készenlétben dolgozott órák száma hétvégéken vagy munkaszüneti napokon.
- Python 3.10+ (szükséges a futtatáshoz)

**** 
Before you start, you should gather the following for quicker progress:

- On-call hours
- Worked hours during on-call _(separately counting hours that were started during night (between 10 PM and 6 AM) and
  other worked hours, during on-call but not started during night (between 6 AM and 10 PM except the regular working
  hours))_

## Használat / Usage

Futtasd a `main.py`-t Pythonnal, válassz nyelvet és válaszolj a kérdésekre.
****
Run `main.py` with Python, select language and answer the questions.

## Jogi nyilatkozat

A készítő ezt a **GitHub repositoryt** (továbbiakban: **kódbázist**) kizárólag saját indíttatásból készítette, semmilyen
külső hatás, jogsérelem vagy bármi egyéb hátrányos helyzet nem játszott közre abban hogy ez elkészüljön, sem a készítő
bármely múltbeli, jelenbeli vagy jövőbeli munkáltatójától, sem mástól. Az ebben a kódbázisban található anyagok,
futtatható szkriptek és azok eredménye nem minősül jogi segítségnyújtásnak, hivatalos állásfoglalásnak, jogi
iránymutatásának, valamint munkajogi tanácsadásának sem. A készítő nem vállal felelősséget a használatból, valamint
annak eredményéből fakadó etikai és jogi vitákért. A Munka Törvénykönyvének a kódbázis anyagainak készítésekor fennálló
tartalma alapján készült (2021. november 3.), a Munka Törvénykönyve esetleges változásait **nem** követik a kódbázisban
található anyagok automatikusan.