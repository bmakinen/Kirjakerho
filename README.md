# Kirjakerho

## Sovelluksen toiminnot

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan kirja-arvosteluja.
- Käyttäjä näkee sovellukseen lisätyt kirja-arvostelut.
- Käyttäjä pystyy etsimään kirja-arvosteluja hakusanalla.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät ilmoitukset.
- Käyttäjä pystyy valitsemaan luokittelun (kirjan genre ja arvosana). 

## Sovelluksen asennus

Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokantataulut:

```
$ sqlite3 database.db < schema.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```
