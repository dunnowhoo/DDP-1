from turtle import *
import tkinter as tk
title("Super Mario Bros Tower")

# Membaca dan memvalidasi input dari pengguna
while(True) :
      num_towers = numinput("Tower to Build", "Enter the number of towers you want to build (integer):", minval = 1)
      if num_towers.is_integer() :
            num_towers = int(num_towers)
            break
      else :
            tk.messagebox.showerror("Input Error", "Your input is not integer")
             

if num_towers > 1:
      while (True) :
            distance = numinput("Distance Between Towers", "Enter the distance between towers (integer):", minval=2, maxval=5)
            if distance.is_integer() :
                  distance = int(distance)
                  break
            else :
                  tk.messagebox.showerror("Input Error", "Your input is not integer")
      while (True) :
            layer_difference = numinput("Tower Layer Difference", "Difference in layers between towers (min 2, max 5):", minval=2, maxval=5)
            if layer_difference.is_integer() :
                  layer_difference = int(layer_difference)
                  break
            else :
                  tk.messagebox.showerror("Input Error", "Your input is not integer")
else:
      distance = 0
      layer_difference = 0

while (True) :
      width = numinput("Brick Width", "The width of a brick (min 1, max 35):", minval = 1, maxval=35)
      if width.is_integer() :
                  width = int(width)
                  break
      else :
                  tk.messagebox.showerror("Input Error", "Your input is not integer")
while (True) :
      height = numinput("Brick Height", "The height of a brick (min 1, max 25):", minval = 1, maxval=25)
      if height.is_integer() :
                 height = int(height)
                 break
      else :
            tk.messagebox.showerror("Input Error", "Your input is not integer")
while (True) :
      layers = numinput("The Number of First Tower Layers", "Enter the number of layers for the first tower (max 25):", minval = 1, maxval=25)
      if layers.is_integer() :
                  layers = int(layers)
                  break
      else :
                  tk.messagebox.showerror("Input Error", "Your input is not integer")
while (True) :
      body_width = numinput("Layer Width", "Enter the width of a layer (max 10):", minval = 1, maxval=10)
      if body_width.is_integer() :
                  body_width = int(body_width)
                  break
      else :
                  tk.messagebox.showerror("Input Error", "Your input is not integer")
             
#Mengatur Kecepatan Pen
speed(10000000000)

#Menghitung total bricks
total_bricks = ((num_towers/2) * ((2*body_width*layers) + (num_towers -1)*layer_difference*body_width)) + (body_width + 1)*num_towers

#Menuliskan pesan 
penup()
goto(-300,-300)
pendown()
write(f"{num_towers} Super Mario Towers have been built with a total of {(int(total_bricks))} bricks", font=("Arial", 16, "bold"))

#Menggambar Badan Tower
for i in range (1, num_towers + 1):
      #Koordinat mula-mula agar selalu ditengah screen
      x = -1/2 * num_towers * (width * body_width + distance*width)
      y = -250

      for j in range(1, (layers+1) + (layer_difference*(i-1))) : 
            if (i == 1) :
                 penup()
                 goto(x,y)
            else :
                 x = x + ((width*body_width) + (distance*width))*(i-1)
                 goto(x,y)
            pendown()
            for k in range(1,body_width+1) :
                  pendown()
                  begin_fill()
                  fillcolor("#CA7F65")
                  forward(width)
                  left(90)
                  forward(height)
                  left(90)
                  forward(width)
                  left(90)
                  forward(height)
                  end_fill()
                  left(90)
                  x += width
                  penup()
                  goto(x, y)
            #Kembali ke posisi paling kiri tower
            x = -1/2 * num_towers * (width * body_width + distance*width)
            y += height
      
      y = -250
      #Menggambar Topi Tower
      penup()
      if i == 1 :
            goto(x + width/2, y + (layers * height))
      else :
            x = x + (((width*body_width) + (distance*width)) * (i-1)) + (width/2)
            y = y + (layers*height) + (layer_difference*height*(i-1))
            goto(x,y)

      for l in range (1, body_width + 2) :
            pendown()
            begin_fill()
            fillcolor("#693424")
            left(90)
            forward(height)
            left(90)
            forward(width)
            left(90)
            forward(height)
            left(90)
            forward(width)
            end_fill()
            if (l == 1 and i == 1) :
                  x += width * 1.5
                  y += (layers * height)
            else :
                  x += width
            penup()
            goto(x, y)

      #Menggambar Jamur
      if (i == 1) :
            #Menghitung koordinat X untuk badan jamur
            x1 = -1/2 * num_towers * (width * body_width + distance*width)
            x2 = x1 + (width * body_width)
            x3 = (x1 + x2)/2 - (width/2)
      else :
            #Menghitung koordinat X untuk badan jamur kedua dan seterusnya
            x1 = x1 + ((width*body_width) + (distance*width))
            x2 = x2 + ((width*body_width) + (distance*width))
            x3 = (x1 + x2)/2 - (width/2)
      y3 = -250 + (layers*height) + (layer_difference*height*(i-1)) + height
      goto(x3,y3)
      pendown()
      fillcolor("wheat")
      begin_fill()
      left(90)
      forward(width)
      right(90)
      forward(width)
      right(90)
      forward(width)
      right(90)
      forward(width)
      right(90)
      forward(width)
      end_fill()

      #Menggambar Topi Jamur
      begin_fill()
      fillcolor("Red")
      right(90)
      forward(1.5*width)
      left(90)
      circle(width,180)
      left(90)
      forward(width)
      end_fill()
      penup()

      body_width+= 1
      
hideturtle()
done()