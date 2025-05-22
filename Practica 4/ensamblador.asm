DATA SEGMENT
    primr DB "La impresion es := %lf",10,0
DATA ENDS

BSS SEGMENT
    resp DW 2 DUP(?)
BSS ENDS

CODE SEGMENT
    EXTRN printf:PROC
    PUBLIC sum, main

sum PROC
    PUSH BP
    MOV BP, SP
    SUB SP, 48
    MOV AX, [BP + 4]
    MOV DI, 2
    ADD AX, DI
    ADD SP, 48
    MOV SP, BP
    POP BP
    RET
sum ENDP

main PROC
    PUSH BP
    MOV BP, SP
    SUB SP, 48
    MOV WORD PTR [BP - 4], 22
    MOV WORD PTR [BP - 6], 12
    MOV AX, [BP - 4]
    MOV DI, AX
    CALL sum
    MOV WORD PTR [BP - 6], AX
    PUSH WORD PTR [BP - 6]
    FILD DWORD PTR [SP]
    FSTP QWORD PTR resp
    ADD SP, 2
    MOV AX, WORD PTR resp
    MOV DI, OFFSET primr
    MOV AL, 1
    CALL printf
    MOV AX, [BP - 6]
    ADD SP, 48
    MOV SP, BP
    MOV AX, 4C00H
    INT 21H
main ENDP

CODE ENDS
END
