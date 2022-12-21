# TNT LIBRARY

Customized library for C that deals integers numbers and texts input.

# HOW TO USE IT?

1. Firstly you need the library tnt.h on your computer, so copy and paste it on a folder you will use it on a file that ends with **.c** or clone this repository;
2. Secondly let your code knows that tnt.h exists then type **#include "tnt.h"** on the top of your file;
3. Then when you have your code done you must turns source code into machine code typing **clang -o program_name program_name.c**;

![tnt](https://user-images.githubusercontent.com/68133032/208797666-1892d2d0-0ffb-4902-9251-a6b09b375eb5.png)

**ATTENTION:** As you can see in the image above we need free() the variables that use the grabText() function because it is being alocated memory to hold text. So, to check if your code does not have any memory leak or errors type **valgrind ./program_name**.
