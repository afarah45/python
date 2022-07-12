states = [
"Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
"Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana",
"Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","MontanaNebraska",
"Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina", "NorthDakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island",
"South Carolina","SouthDakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington",
"WestVirginia","Wisconsin","Wyoming"]

print("Congraulations!!. You won United States Visa lotters.")
selection = int(input("Please enter a any number from 0-47. The system will pick state for you!\n"))

try:
    print("Conratulations! You are going to " + states[selection])
except:
  print("oops! inavlid state number.")
  int(input("Please try again"))