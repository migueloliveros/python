#
#match
# https://docs.python.org/3/reference/compound_stmts.html#the-match-statement

dia_semana = "viernes"
horario = "noche"
vacaciones = True

match dia_semana, horario:
    case "lunes" | "miercoles", "mañana":
        print ("Curso de Python")
    case "martes" | "jueves", "tarde":
        print("Pasear")
    case "viernes", t if t == "noche" or vacaciones:
        print("Quedar amigos")

    case _:
        print("Tiempo libre")
