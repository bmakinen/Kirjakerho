# Kirjakerho

## Sovelluksen toiminnot

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään sovellukseen kirja-arvosteluja. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kirja-arvosteluja.
- Käyttäjä näkee sovellukseen lisätyt kirja-arvostelut. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kirja-arvostelut.
- Käyttäjä pystyy etsimään kirja-arvosteluja hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä kirja-arvosteluja.

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
