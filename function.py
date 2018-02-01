# Defining function with no parameter
def hello_world():
    return "Hello World"
# Defining function with parameter
def area_rect(x, y):
    return x * y
# printing Hello World
print(hello_world())
# printing area of rectangle
print(area_rect(4, 5))

# defining global variable.
peri = 0;
def peri_rect(l, b):
   peri = 2 * (l + b);
   print "Perimeter inside function : ", peri
   return peri
# calling peri_rect() function
peri_rect( 2, 3);
print "Perimeter outside the function : ", peri
