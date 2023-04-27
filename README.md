# MiniJava Compiler  

- This is a User Interfaces that let you edit code from ".java" files and compiles them using miniJava syntax.

## Interface
- Run python ui.py to run the UI
- It's made with Tkinter
- It has basic text editing tools like saving,copy-paste,opening file...
- Clicking on Run Tab then compile. It will execute miniJava.exe and compiles the code in the Code Textbox and shows the lexical, syntaxic and semantic errors in the Console Textbox.
- It will also generate assembly code which can be seen in MiniCompiler/generatedCode.txt
### Execution:


https://user-images.githubusercontent.com/51765101/234975384-d655b6c7-1762-4797-ac62-6b69ca33acaa.mp4



## MiniJava Syntax
- The Syntax_Generator folder contains the lex (.l), yacc (.y) and semantic files that generates miniJava.exe.
- It also can generate really simple assembly code.
- miniJava.exe checks the content of a file (given as argument) and analyse it lexically with lex to generate tokens then uses them check its syntax, and saves the variables in a symbols table to verify if they were implemented correctly (declaration, initialisation and usage).

#### MiniJava BNF
- This compiler doesn't contain every Java rule.
- There some basic keywords,simple types,attributes and methods in classes. Not all operators are available too.


```
Program	::=	MainClass ( ClassDeclaration )* <EOF>

MainClass	::=	"class" Identifier "{" "public" "static" "void" "main" "(" "String" "[" "]" Identifier ")" "{" Statement "}" "}"

ClassDeclaration	::=	"class" Identifier ( "extends" Identifier )? "{" ( VarDeclaration )* ( MethodDeclaration )*  "}"

VarDeclaration	::=	Type Identifier ";"

MethodDeclaration	::=	"public" Type Identifier "(" ( Type Identifier ( "," Type Identifier )* )? ")" "{" ( VarDeclaration )* ( Statement )* "return" Expression ";" "}"

Type	::=	"int" "[" "]"
	|	"boolean"
	|	"int"
	|	Identifier

Statement	::=	"{" ( Statement )* "}"

	|	"if" "(" Expression ")" Statement "else" Statement

	|	"while" "(" Expression ")" Statement

	|	"System.out.println" "(" Expression ")" ";"

	|	Identifier "=" Expression ";"

	|	Identifier "[" Expression "]" "=" Expression ";"

Expression	::=	Expression ( "&&" | "<" | "+" | "-" | "*" ) Expression

	|	Expression "[" Expression "]"

	|	Expression "." "length"

	|	Expression "." Identifier "(" ( Expression ( "," Expression )* )? ")"

	|	<INTEGER_LITERAL>
	|	<BOOLEAN_LITERAL>

	|	Identifier

	|	"this"
	|	"new" "int" "[" Expression "]"

	|	"new" Identifier "(" ")"

	|	"!" Expression

	|	"(" Expression ")"

Identifier	::=	<IDENTIFIER>

```




