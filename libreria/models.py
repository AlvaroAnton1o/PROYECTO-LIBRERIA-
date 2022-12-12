import re
# /////////////////////////////////////////
# Funcion para verificar valides de correos
# /////////////////////////////////////////
def validar_correo(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None
#//////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////
# Funcion para verificar valides de contraseña
# //////////////////////////////////////////////////

def validar_contra(contra): 
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    
    pat = re.compile(reg)
    
    mat = re.search(pat, contra)
    
    global val 
    
    if mat:
        val = True
    else:
        val = False
    
    return val

    

# def v_c(contra):

#     largo = re.compile(r'.{8,}')
#     digito = re.compile(r'\d+')
#     letra_may = re.compile(r'[A-Z]+')
#     letra_min = re.compile(r'[a-z]+')

#     validaciones = [(largo, "largo menor que ocho"),
#                     (digito, "no tiene digitos"),
#                     (letra_min, "no tiene letras minúsculas"),
#                     (letra_may, "no tiene letras mayúsculas")]
    
    


#     valida = True
#     for validacion, mensaje in validaciones:
#         if not validacion.search(contra):
#             print(f"{contra}: {mensaje}")
#             valida = False

#     if valida:
#         print(f" ok")
