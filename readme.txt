1) Als je een nieuwe gebruiker wilt maken kunt u de volgende commando gebruiken
python3 main.py add-user --username naam --address "adress" --payment betaalmethode
Voorbeeld
python3 main.py add-user --username dirk --address "theebos 13" --payment AI

2) Als u een lijst wilt van users kunt u deze command gebruiken
python3 main.py user-list

3) Als u een lijst wilt maken van de producten die een klant heeft dan kunt u de volgende commando gebruiken:
python3 main.py show-products-user --user-id id van user 
een voorbeeld:
python3 main.py show-products-user --user-id 1   

3) Als u een product wilt toevoegen aan de webshop kunt u de volgende commando gebruiken
python3 main.py create-catalog-product --product-name naam van het product --description "een beschrijving" --price hoeveel elk product kost --stock hoeveel we in vooraad hebben  
een voorbeeld: 
python3 main.py create-catalog-product --product-name apple --description "an amazing computer" --price 500 --stock 100   

4) Als u een product uit onze webwinkel wilt verwijderen We kunnen het product zoeken via id of naam
Om via een id te zoeken dan kunt u deze commando gebruiken:
python3 main.py remove-catalog-product --id id van het product dat u wilt verwijderen
een voorbeeld:
python3 main.py remove-catalog-product --id 5

Als u het via naam wilt zoeken en verwijderen dan kunt u deze commando gebruken
python3 main.py remove-catalog-product --product-name naam van het product dat u wilt verwijderen
een voorbeeld:
python3 main.py remove-catalog-product --product-name laptop

5) Als u een tag wilt aanmaken dan kunt u de volgende commando gebruiken:
python3 main.py create-tag --tag-name naam van de tag
een voorbeeld:
python3 main.py create-tag --tag-name stoel

6) Als u een tag wilt koppelen aan een product dan kunt u de volgende commando gebruiken:
python3 main.py pair-product-tag --product-id id van het product --tag-id id van de tag
een voorbeel :
python3 main.py pair-product-tag --product-id 1 --tag-id 4  

7) Als u een lijst van alle producten die gekoppeld zijn aan een tag dan kunt u deze commando gebruiken:
python3 main.py list-products-on-tag --tag-id een tag id
een voorbeeld:
python3 main.py list-products-on-tag --tag-id 4

9) Als u een product witl opzoeken kunt u de volgende commando gebruiken:
python3 main.py search --product naam van het product
Een voorbeeld:
python3 main.py search --product banana

Het zou rekening moeten houden met spellingsfouten maar dit is niet 100% correct
Als ik bijvoorbeeld frui opzoek dan zou het fruit moeten opzoeken



20) Als u een overzicht wilt hebben van de revenue dan kunt u deze commando gebruiken:
python3 main.py revenue --startdate start datum --enddate eind datum
een voorbeeld:
python3 main.py revenue --startdate 2020-1-1 --enddate 2022-10-10