# WarDeckOfCards

1.  Programos tikslas: Sukurti python programa 2-4 žaidėjams žaisti kortų žaidimą remiantis sėkme.

2.  Eiga: pradeti programą pasirenkant kiek bus žaidžiančių žaidėjų naudojant ‚input‘, bei aprašyti kortų kaladę į sarašą (Kortu_kalade), taip pat importuoti ‚random‘ Kortu_kalade sumaišymui

3.  Toliau apsirašyti funkcija Kortu_kalade sumaišyti random tvarka, kiekvienos naujos partijos pradžioje.
Kadangi Kortu_kalade turi ir variables ir stringu turėsiu priskirti J, Q, K, A kortoms skaitines vertes, kad būtų galima palyginti kuri korta yra aukštesnė.
Apsirašysiu ir pagrindinę funkcija patikrinančią kurio žaidėjo korta yra aukščiausia reikės kelių skirtingu funkciju priklausomai nuo to kiek žaidėjų žais. Tačiau priscipas labai panašus naudosiu ‚if‘ ir ‚elif‘ patikrinti visiem galimiem variantam, nepamirstant lygiūjų galimybę, tada bus kreipiamasi į funkcija kuri leis lygiosioms pabaigusiems žaidėjams traukti korta is naujo ir programa atliks skaičiavimus iš naujo
Praėjus pirmajam roundui kortos kurios buvo ištrauktos iš Kortu_kalade bus panaikintos iš sarašo, kad kito roundo pradžioje jų nebutų galima ištraukti.
4.  Žaidimas truks tol kol kortų užteks visiems žaidėjams roundo pradžioje, paprasčiausiai užteks naudoti ‚len(Kortu_kalade)‘ ir patikrins ar visiems užtenka kortų prieš kiekvieną dalinimą
5.  Jeigu viskas pavyks tikslingai, pletoti tai grafinėje aplinkoje
