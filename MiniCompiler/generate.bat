flex miniJava.l
bison -d miniJava.y
gcc -o miniJava miniJava.tab.c lex.yy.c