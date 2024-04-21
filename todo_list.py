# Storing the to do list
# Setting it into an array
lists = []

def displayList():
      print("Here are your list")
      for list in lists:
            print(f"- {list}")
            
def addList():
      lists.append(list)
      print(f"Added list: {list}")
      
def removeList():
      if list in lists:
            lists.remove(list)
            print(f"Removed list: {list}")
            
      else:
            print("List not being found, sorry.")
            
while True: 
      print("\nOptions:")
      print("1. Add a list")
      print("2. Remove a list")
      print("3. Show all list")
      print("4. Exit")
      choice = input("What would you like to do? ")
      
      if choice == "1":
            listAdd = input("Enter the task you'd like to add: ")
            addList(listAdd)
      elif choice == "2":
            listRemove = input("Enter which list you'd like to remove: ")
            removeList(listRemove)
      elif choice == "3":
            displayList()
      elif choice == "4":
            print("Goodbye, now...")
            break
      else:
            print("Your input is invalid, please enter from these list: 1, 2, 3, or 4. Thank you")
            