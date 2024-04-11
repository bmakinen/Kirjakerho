# Kirjakerho
Sovelluksessa voi arvostella kirjoja ja lukea muiden antamia arvosteluja. 

Sovelluksen ominaisuuksia:
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi antaa arvion (tähdet ja kommentti) kirjasta ja lukea muiden antamia arvosteluja.
- Kirjoja voi hakea genren, kirjailijan tai kirjan nimen perusteella.
- Jos haettua kirjaa ei löydy, käyttäjä voi lisätä sen sovellukseen.
- Käyttäjä näkee myös listan kymmenestä parhaiten arvostellusta kirjasta.
- Käyttäjä voi tallentaa omaan listaan kirjoja, jotka haluaa tulevaisuudessa lukea.

Välipalautus 2:
Käyttäjä voi kirjautua sisään ja ulos ja luoda uuden tunnuksen.

Testausohjeet:
Kloonaa repositio koneellesi ja siirry sen juurikansioon.  
Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaisesti:  
DATABASE_URL=<tietokannan-paikallinen-osoite>  
SECRET_KEY=<salainen-avain>

Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla   
python3 -m venv venv  
source venv/bin/activate  
pip install -r ./requirements.txt  

Määritä vielä tietokannan skeema komennolla   
psql < schema.sql

Nyt voit käynnistää sovelluksen komennolla  
flask run
