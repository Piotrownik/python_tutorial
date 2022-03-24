# print("hello")
# x = 3
# y = 7
# z = x + y
# print(z)

# #to combine two variables 
#clear to clear terminal
# print(f"hello,    {full_name.upper()}!") #I can use also title,lower etc.
# print("{} {}".format(first, last)) #to combine two variables 

#print("\tfull_name")#to add a tabulation to the text 

#print ("Languages:\nPython\nC\nJavaScript") #adding new line 
#print ("Languages:\n\tPython\nC\nJavaScript")  #adding new line + adding tabulation 
#x = "  p iotrek"
#print(x.strip())#you can use lstrip and rstript. You can't remove from inside, it's other function for that 

#EXCERCISE 2-4
#x = "piotr"
#print(x.upper())#
#F is a format and it takes the variables together so i can make changes/combine 

#EXCERCISE 2-5
# x = """
# Albert Enstein once said, "A person who never made a mistake never tried anything new" """
# print(x)

#EXCERCISE 2-9
#x = 5
#y = "my favorite number is "
#print(f"my favorite number is {x}") #f allows to add integer at the end 

#EXCERCISE 3-2
#names = ["Ibrahim", "Malik", "Hanifa"]
#print(names[-1])
#print(f"Hello {names[1]}!")


#append, insert, del(removes object), pop(takes out  to other object) 
#EXCERCISE 3-4
# guests = ["Bob MArley",  "Obama",  "Drake"]
# print(guests[0])
#print(f"Hey {guests[0]}, how are you {guests[1]}, what's up {guests[-1]} my brother? Cheers to everyone!")

#EXCERCISE 3-5 - zamiana elementu na liście
# guests[2]="Michael Jackson"
# print(guests)

#guests.insert(0, "trump") 
#print(guests)

#not_invited=guests.pop()#taking out the last  item
#print(f"I can invite only 2 people, sorry that we can't invite you to the dinner {not_invited}")

#del guests[0:]#to remove object
#print(guests)

#reverse/sort/len
#EXCERCISE 3-8

#cars=["yamaha",  "mercedes", "fiat", "bmw"]
# print(sorted(cars, reverse=False)) #temporary sort
# print(sorted(cars, reverse=True)) #temporary sort
#cars.sort()#permanent sort
# cars.reverse()
#print(sorted(cars, reverse=False))
# print(cars)
# cars.reverse()
# print(cars)
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

#EXCERCISE 3-9
#len(guests)#WHY IT'S  NOT  WORKING? 

#   chapter 4
#magicians = ["Bartek", "Jacek", "Adriana"]

# for magician in magicians:
#     print(f"{magician.upper()}, to bylo dobre!") #loop with text

# for  magician in magicians:
#     print(f"{magician.lower()}, to było dobre!")
#     print(f"a teraz wypierdalaj!, {magician.upper()}. \n") #more advanced loop \n - zostawia pusty wiersz
# print("dziekujemy wszystkim za przybycie!") #brak wciecia oznacza, ze komenda pojdzie tylko raz 

#EXCERCISE 4-1

# pizzas = ["margharitta", "Vesuvio", "Hawajska"]

# for pizza in pizzas:
#     print(f"To moja ulubiona pizza {pizza}")
# print("szczerze mówiac to kocham wszystkie pizze")

#EXCERCISE 4-3
# for cyfra in range(1,1000000):# if the code executes too long ctrl+c
#     print(cyfra)

#EXCERCISE 4-5

# liczby = list(range(1,1000000))
# print(min(liczby))
# print(max(liczby))
# print(sum(liczby))

#EXCERCISE 4-6
# nieparzyste = []
# for value in range(2,20,1):#jak zrobic nieparzyste? trzeci argument mowi co ktora liczbę pokazać
#     liczba = value
#     nieparzyste.append(liczba)
# print(nieparzyste)

#EXCERCISE 4-7 - podnoszenie do potęgi wartości 
# potega = []

# for value in range(3,30):
#     square = value**2 #**kwargs is a common idiom to allow arbitrary number of arguments to functions
#     potega.append(square)
# print(potega)

##Exercise  4-10 Iteracja przez wycinek
# pizzas = ["Margharitta", "Vesuvio", "Hawajska", "Torino"]

# print("pierwsze trzy elementy listy to:")
# for pizza in pizzas[1:2]:#:2 for the first two elements. ":"- for all elements
#     print(pizza.upper())

##Exercise  4-11  tworzenie  kopi listy. Nastepnie dodanie po jednej wartosci dla rozróznienia oba z nich 

# pizzas = ["Margharitta", "Vesuvio", "Hawajska", "Torino", "Pepperoni"]

# Friends_pizzas = pizzas[:4]# bez wpisania kwadratowego nawiasu i liczby obie listy byłyby identyczne do końca kodu
# pizzas.append("Vegetariana")
# Friends_pizzas.append("Mexicana")

# print("Moje  ulubione rodzaje pizzy  to:")
# for pizza in pizzas:
#     print(pizza.lower())

# print("Ulubione rodzaje pizzy mojego przyjaciela to:")
# for pizza in Friends_pizzas:
#     print(pizza.upper())


#4-13 Creating  tuple

# dishes  = ("pizza", "kebab", "sushi", "pasta")

# for dish in dishes:
#     print(dish.title())

#dishes[0] = "ice creams"#  new elements can't  be assigned to tuple

# dishes = ("french fries", "kebab", "sushi", "chips")

# print("zmienione potrawy:")
# for dish in dishes:
#     print(dish)


# = for assigning a value to variable, == for comparing, != sprawdzenie nierownosci 
#wartosc boolowska = test warunkowy 

#TASK 5.1 # type Python3  to open the terminal 
#car = ["subaru"]
#print(car == "bmw")

# for cars in car:
#     if cars == "subaru":#remember about colon #in order this to work it has to be a list
#         print("to jest dobra odpowiedź")
#     else: #it's not required 
#         print("to jest zła odpowiedź") 

#if i want to run  this test over variable code must be different: 
# auto = 'bmw'
# for i in auto:
#     print(i)

# liczba = 0
# print(liczba != 0)

# ingridients = ["onions","cucumber","eggplant","tomato"]

# for ingridient in ingridients:
#     if ingridient == "tomato":
#         print("moj ulubiony skladnik")
#     else:
#         print("niekonieczny składnik")


#to check whether the element is on the list use in terminal this:
#ingridients = ["onions","cucumber","eggplant","tomato"]
#'onions' in ingridients

#OR
# ingridients = ["onions","cucumber","eggplant","tomato"]
# another_ingridient = "kiwi"

# if another_ingridient not in ingridients:
#     print(f"mozna jeszcze dodac jeszcze {another_ingridient.title()}")

#TASK 5.3 IF, IF ELSE, IF -ELIF-ELSE (executed till test is not passed)

# alien_color  = 'zielony'
# #print(alien_color)

# if alien_color == "zielony":#if color is not on  the list there will be no output 
#      print("you gained 5 points")

#second way
# alien_color  = 'zielony', 'zółty', 'czerwony'
# selected_color = "zółty"
# if selected_color in alien_color:
#     print("you gained 5 points")

# if alien_color == 'zielony':
#     print("you gained 5 points")
# elif alien_color ==  'niebieski':
#     print("there is no color ")


#TASK 5.4 if-else 
#alien_color  = 'zielony'

# if alien_color ==  "zielony":
#     print("you gained 5 points")
# else:
#     print("you gained 10 points")

# alien_color  = ['zielony', "zółty", 'czerwony']

# kolor = 'zielony'

# for i in alien_color:
#     if i == kolor:
#         print("you gained 5 points")
#     else:
#         print("you gained 10 points")

#TASK 5.5 if-elif-else
# alien_color  = 'zielony', 'zółty', 'czerwony'
# kolor_1 = 'zielony'
# kolor_2 = 'zółty'

# for i in alien_color:
#     if i == kolor_1:
#         print("you  gained 5 points")
#     elif i == kolor_2:
#         print("you gained 10 points")
#     else:
#         print("you gained 15 points")

#TASK 5.6 if-elif-else
# age = 44

# if age < 2:
#     print("niemowlęcie")
# elif age >= 2 and age < 4:
#     print("dziecko, uczy sie chodzic")
# elif age >= 4 and age < 13:
#     print("dziecko")
# elif age >= 13 and age < 20:
#     print("nastolatek")
# elif  age >= 20 and age < 65:
#     print("dorosły")
# else:
#     print("senior")

#5.7 
# favorite_fruits = ["kiwi", "banana", 'apple']

# for i in favorite_fruits:
#     if i == "kiwi":
#         print(f"Naprawdę lubisz {i}")
#     if i =="banana":
#         print(f"naprawdę lubisz {i}")
#     if i =="apple":
#         print(f"naprawdę lubisz {i}")
#     if i =="peach":
#         print(f"naprawdę lubisz {i}")

#the same but without for loop
# if "kiwi" in favorite_fruits:
#     print("Naprawdę lubisz kiwi!")
# if "banana" in favorite_fruits:
#     print("naprawdę lubisz banany")
# if "apple" in favorite_fruits:
#     print("naprawdę lubisz jabłka")
# if "peach" in favorite_fruits:
#     print("naprawdę lubisz brzoskiwnie")

#\n - zostawia wiersz wolnego  miejsca 

#TASK 5.8 
# usernames = ["kupi", "gumi","batman","spiderman", "admin"}
# for i in usernames:
#     if i == "admin": #when comparing values i dont need to use "if i in"
#         print(f"Witaj {i.title()}! Czy chcesz przejrzec dzisiejszy raport?")
#     else:
#         print(f"Witaj, {i.title()}! Dziekujemy, ze ponowanie sie zalogowaleś!") 

#TASK 5.9
# if usernames:
#     for i in usernames:
#         print(f"Siemanko {i}")
# else:
#     print("musimy znaleźć jakichs uytkowników")

#TASK 5.10
# current_users = ["Kupi", "Gumi","Gatman","Spiderman", "Admin"]
# new_users = ["john", "mark", "paul", "kupi"]

# current_users_lower = []

# for i in current_users:
#     current_users_lower.append(i.lower())

# for i in new_users:
#     if i.lower() in current_users_lower: #when i  cehck  for availability i need  to use in
#         print(f"Nazwa {i.title()} zajeta")
#     else:
#         print(f"you can use {i.title()}")

#TASK 5.11
#numbers = [1,2,3,4,5,6,7,8,9] #one way of reating  list
# numbers = list(range(1,10)) #other way of creating list
# print(numbers)
# for i in numbers: 
#     if i == 1:
#         print(f"{i}st")
#     elif i ==2:
#         print(f"{i}nd")
#     else:
#         print(f"{i}th")


##Slowniki  pary klucz-wartosc we use {} brackets

#TASK 6.1 
# friend = {"first name":"Ibo", "last  name":"Musayev", "age":24,  "city":"Warsaw"}
# print(friend)

#TASK 6.2 przypisywanie nowych kluczy 
# people = {"adam": 5,"janusz":6,"mateusz":88}
# people["Ibo"]= 5
# print(people)

#TASK 6.3
# glossary = {
#     'append:':'dodawanie',
#     'len:':'dlugosc',
#     'del:':'usuwanie',
#     'range:':'tworzenie listy',
#     }
# #first method
# for key, value in glossary.items(): #I can  use  also other  assignments than key and value
#     print(f"funkcja {key} oznacza {value} \n")

#second method, which DOESN'T WORK  
# word = 'append:'
# print("\n" + word.title() + ": " + glossary[word])

# word = 'len:'
# print("\n" + word.title() + ": " + glossary[word])

# word = 'del:'
# print("\n" + word.title() + ": " + glossary[word])

# word = 'range:'
# print("\n" + word.title() + ": " + glossary[word])


#set to have unique values 
#{} these  brackets we use for glossary and zbiory (nie ma kolejnosci w nich)

#TASK 6.4 the same as  i did in 6.3
# glossary = {
#     'append:':'dodawanie',
#     'len:':'dlugosc',
#     'del:':'usuwanie',
#     'range:':'tworzenie listy',
#     }

# for key, value in glossary.items(): #I can  use  also other  assignments than key and value
#     print(f"funkcja {key} oznacza {value} \n")

#TASK 6.5 
# rivers = {"nil":"egypt","wisla":"poland", "dunaj":"austria"}

# for key, value in rivers.items():
#     print(f"{key} przeplywa przez {value}\n")

# for value in rivers.values():#if i want  to print  only values or keys I use either keys(), values()
#     print(f"{value}\n")

#TASK 6.6 

# Favorite_languages = {
#     'janek':'python',
#     'sara':'c',
#     'edward':'ruby',
#     'pawel':'python',
# } 

# names = ["janek","bartek","mateusz","radek"] 

#my method 
# for key in Favorite_languages.keys():
#     print(f"\n thank you for your involvement {key}")

# for i in names:
#     if i not in Favorite_languages.keys():
#         print(f" \n i invite you {i}")

# correct method  below 
# for  name in names:
#     if name in Favorite_languages.keys():
#         print(f"thank you for participating {name}")
#     else:
#         print(f"\n would you take part in  the pooling, {name}?")

#task  6.7 
# friend = {"first_name":"Ibo", "last_name":"Musayev", "age":24, "city":"Warsaw"}
# friend_2 = {"first_name":"Kamil", "last_name":"Chudzik", "age":25, "city":"Zary"}
# friend_3 = {"first_name":"Mateusz", "last_name":"Niznik", "age":25, "city":"Warsaw"}

# people = [friend, friend_2, friend_3]

# print(people)

# for person in people:
#     print(f"\n{person}")

#OR

# for person in people:
#     first_name = person["first_name"]
#     age = str(person["age"])
#     city = person["city"]
#     print(first_name + " from " + city + " is " + age + " old") # + we use with strings like age

#task  6.8
# Mia = {"animal":"dog","owner":"Michal"}
# Ellie = {"animal":"dog","owner":"Ola"}
# Lajka = {"animal":"dog","owner":"Slawek"}

# pets = [Mia, Ellie, Lajka]

# for pet in pets:
#     animal = pet["animal"]
#     owner = pet["owner"]
#     print(" is a ", animal, " of ", owner) #it's better to use comma for lists 

#task  6.9
# favorite_places =  {"piotrek":"wildwood", "Ibo":"berlin", "ola":"amsterdam"}

# for key, value in favorite_places.items():
#     print(f"Favorite place of {key} is {value}")

#task  6.10
# Favorite_numbers = {
#     "ibo":['5','8'],
#     "piotrek":['199','201'],
#     "michal":['77','88'],
#     }

# for key, value in Favorite_numbers.items():
#     print(f"Favorite number of {key}")
#     for number in value:
#         print(f" is {number}")

#second method 
# for key, value in Favorite_numbers.items():
#     for number in value:
#         print(f"favorite number of  {key} is {number}")


#task  6.11 Glossary in glossary
# cities = {
#     "Warszawa":{
#         "country":"poland",
#         "population":"2 million",
#         "fact":"Capitol of poland",
#     },
#     "Poznan":{
#         "country":"poland",
#         "population":"0.5 million",
#         "fact":"nice people",
#     },
#     "Wroclaw":{
#         "country":"poland",
#         "population":"0.5 million",
#         "fact":"party city",
#     }
# }

# for key, value in cities.items():
#     print(f"The city of {key} is located")
#     country = f"{value['country']}"
#     population = f"{value['population']}"
#     fact = f"{value['fact']}"

#     print(f" in {country}.")
#     print(f"This city has the population of {population}")
#     print(f" and the fact about this city is that it is {fact}")


#CHAPTER 7  functions: input() for text values, while(), int()-converts  to number
# %  - modulo operator that gives back residuals

#TASK 7.1
# cars  = input("jaki samochod chcialbys wypozyczyc? ")

# print(f"Chwileczke, sprawdze, czy mamy dostepny samochod {cars}")

#TASK 7.2

# table = input("Na ile osob chcesz zarezerwowac stolik? ")

# table = int(table)

# if table > 8:
#     print("please wait for the table")
# else:
#     print("stolik jest gotowy")

#TASK 7.3
# number = input("prosze podaj dowolna liczbe ")
# number = int(number)
# print(number%10)

#WHILE - works unitll condition is met. += adding additional output 
#flaga - definiowanie dodatkowej zmiennej, ktora okresla  jak  dlugo program ma dzialac
#TRUE - bedzie  dzialac tak dlugo jak jest TRUE
#FALSE - Zakonczy swoje dzialanie wtedy
#flag uzywa sie jezeli wiele zdarzen prowadzi do konca programu

#break - wskazuje wykonywane i  niewykonywane wiersze kodu
#countinue - powrot na poczatek pętli 
#to stop indefinite run of while insert Ctrl +  C

#TASK7.4
# prompt = "\n prosze podac dodatki do pizzy \n"
# prompt += "\n napisz 'stop', zeby zakonczyc dzialanie programu "

# message = ""

# while message != "stop":
#     message = input(prompt)
#     if message != "stop":
#         print(f"\n skladnik {message} zostal dodany")

#message = ""#ustawiamy  to zeby python mial do  czego zrobic porownanie argumentu while

#below is the second method however it displays word  "stop"
# while message != "stop":
#     message = input(prompt)
#         print(f" \n {message} zostal dodany")

#TASK 7.5

# prompt = " Prosze podac swoj wiek: "
# prompt += " Cena biletu wynosi: "

# while True:
#     number = input(message)


# message != "koniec":
#     message = input(prompt)
#     print





#hehe











#PREPARE STATISTICAL MODELS 











