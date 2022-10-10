# Крестики нолики

print("*" * 10, " Крестики-нолики для двух игроков ", "*" * 10)

cell = list(range(1,10))

def draw_board(cell):
   print("-" * 13)
   for i in range(3):
      print("|", cell[0+i*3], "|", cell[1+i*3], "|", cell[2+i*3], "|")
      print("-" * 13)

def take_input(gamer_two):
   valid = False
   while not valid:
      gamer_one = input("Куда поставим " + gamer_two+"? ")
      try:
         gamer_one = int(gamer_one)
      except:
         print("Некорректный ввод. Вы не правильно ввели число?")
         continue
      if gamer_one >= 1 and gamer_one <= 9:
         if(str(cell[gamer_one-1]) not in "XO"):
            cell[gamer_one-1] = gamer_two
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9")

def check_win(cell):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if cell[each[0]] == cell[each[1]] == cell[each[2]]:
          return cell[each[0]]
   return False

def main(cell):
    counter = 0
    win = False
    while not win:
        draw_board(cell)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(cell)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(cell)
main(cell)

input("Нажмите Enter для выхода!")