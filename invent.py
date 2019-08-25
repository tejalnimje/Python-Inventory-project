file = open("inventory.txt", 'r+')
lines = file.readlines()
while(True):
    choice = int(input("\n 1.Buy item \n 2.View Item \n 3.Exit\n "))
    if choice == 1:
       print("Item \t price \t available count")
       items = []
       for line in lines:
           item, price, count = line.split(',')
           print( item, "\t", price, "\t", count)
           items.append(item)
       print("which item you want to buy:", items)
       item_choice = input()
       if item_choice == input():
        print("item is not available\n")
        break
       else:
          for l in range(len(lines)):
              if lines[l].split(',')[0] == item_choice:
                  item, price, count = lines[l].split(',')
                  count = int(count)-1
                  lines[l] = ','.join([item, price, str(count) + '\n'])
          print("thanks for buying")
    elif choice == 2:
          print("items\tprice\tavailablecount")
          for line in lines:
              item, price, count = line.split(',')
              print(item, " \t ", price, " \t ", count)
    else:
           file.seek(0)
           for lin in lines:
               file.write(line)
           file.close()
           break
