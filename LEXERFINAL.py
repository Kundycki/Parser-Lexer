import ply.lex as lex

tokens = [
    "EQUIPOS", "INTEGRANTES", "DIRECCION", "NOMBRE", "EDAD", "CARGO", "FOTO", "EMAIL",
    "HABILIDADES", "SALARIO", "ACTIVO", "PROYECTOS", "ESTADO", "RESUMEN",
    "FECHA_INICIO", "FECHA_FIN", "VIDEO", "CONCLUSION", "FIRMA_DIGITAL", "NOMBRE_EQUIPO", "IDENTIDAD_EQUIPO",
    "ASIGNATURA", "CARRERA", "UNIVERSIDAD_REGIONAL", "VERSION", "CALLE", "CIUDAD", "PAIS",
    "ALIANZA_EQUIPO", "LINK", "TAREAS", 
    "LLAVE_IZQ", "LLAVE_DER", "CORCHETE_IZQ", "CORCHETE_DER", "DOS_PUNTOS", "COMA",
    "PUNTO", "ARROBA", "COMILLAS", "BARRA", "GUION", "GUION_BAJO", "NUMERAL", "ADMIRACION",
    "PORCENTAJE", "AMPERSAND", "APOSTROFE", "PARENTESIS_IZQ", "PARENTESIS_DER", "ASTERISCO",
    "MAS", "PUNTO_Y_COMA", "MENOR", "IGUAL", "MAYOR", "INTERROGACION", "BARRA_INV", "ACENTO_CIRCUNFLEJO",
    "BARRA_VERTICAL", "VIRGULILLA", "ACENTO_GRAVE",
    "BOOLEANO", "NULO", "HTTP", "HTTPS", "NUM", "STRING", "FLOAT",
    "DATE","DOMINIO", "EXTENSION", "RUTA",
    "PROTOCOLO", "PUERTO", "URL", "INTEGER"
]

t_LLAVE_IZQ       = r'\{'
t_LLAVE_DER       = r'\}'
t_CORCHETE_IZQ    = r'\['
t_CORCHETE_DER    = r'\]'
t_COMA            = r','
t_DOS_PUNTOS      = r':'
t_PUNTO           = r'\.'

def t_DATE(t):
     r'"(19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"'; t.value = t.value[1:-1]; return t

def t_FLOAT(t): 
    r'\d+\.\d{2}'; t.value = float(t.value); return t

def t_BOOLEANO(t): 
    r'true|false'; t.value = t.value == 'true'; return t

def t_NULO(t): 
    r'null'; t.value = None; return t

def t_NUM(t): 
    r'\d+'; t.value = int(t.value); return t

def t_EQUIPOS(t): 
    r'"equipos"'; t.value = t.value[1:-1]; return t

def t_NOMBRE_EQUIPO(t):
     r'"nombre_equipo"'; t.value = t.value[1:-1]; return t

def t_IDENTIDAD_EQUIPO(t): 
    r'"identidad_equipo"'; t.value = t.value[1:-1]; return t

def t_LINK(t): 
    r'"link"'; t.value = t.value[1:-1]; return t

def t_ASIGNATURA(t): 
    r'"asignatura"'; t.value = t.value[1:-1]; return t

def t_CARRERA(t): 
    r'"carrera"'; t.value = t.value[1:-1]; return t

def t_UNIVERSIDAD_REGIONAL(t): 
    r'"universidad_regional"'; t.value = t.value[1:-1]; return t

def t_DIRECCION(t): 
    r'"direccion"'; t.value = t.value[1:-1]; return t

def t_CALLE(t): 
    r'"calle"'; t.value = t.value[1:-1]; return t

def t_CIUDAD(t):
     r'"ciudad"'; t.value = t.value[1:-1]; return t

def t_PAIS(t):
     r'"pais"'; t.value = t.value[1:-1]; return t

def t_ALIANZA_EQUIPO(t):
     r'"alianza_equipo"'; t.value = t.value[1:-1]; return t

def t_INTEGRANTES(t):
     r'"integrantes"'; t.value = t.value[1:-1]; return t

def t_NOMBRE(t):
     r'"nombre"'; t.value = t.value[1:-1]; return t

def t_EDAD(t):
     r'"edad"'; t.value = t.value[1:-1]; return t

def t_CARGO(t):
     r'"cargo"'; t.value = t.value[1:-1]; return t


def t_FOTO(t):
     r'"foto"'; t.value = t.value[1:-1]; return t

def t_EMAIL(t):
     r'"email"'; t.value = t.value[1:-1]; return t

def t_HABILIDADES(t):
     r'"habilidades"'; t.value = t.value[1:-1]; return t

def t_SALARIO(t): 
    r'"salario"'; t.value = t.value[1:-1]; return t

def t_ACTIVO(t): 
    r'"activo"'; t.value = t.value[1:-1]; return t

def t_PROYECTOS(t): 
    r'"proyectos"'; t.value = t.value[1:-1]; return t

def t_ESTADO(t):
    r'"estado"'; t.value = t.value[1:-1]; return t

def t_RESUMEN(t):
     r'"resumen"'; t.value = t.value[1:-1]; return t

def t_TAREAS(t):
     r'"tareas"'; t.value = t.value[1:-1]; return t

def t_FECHA_INICIO(t): 
    r'"fecha_inicio"'; t.value = t.value[1:-1]; return t

def t_FECHA_FIN(t):
     r'"fecha_fin"'; t.value = t.value[1:-1]; return t

def t_VIDEO(t):
     r'"video"'; t.value = t.value[1:-1]; return t

def t_CONCLUSION(t): 
    r'"conclusion"'; t.value = t.value[1:-1]; return t

def t_VERSION(t):
     r'"version"'; t.value = t.value[1:-1]; return t

def t_FIRMA_DIGITAL(t): 
    r'"firma_digital"'; t.value = t.value[1:-1]; return t

def t_STRING(t): r'"([^\"]|\.)*"'; t.value = t.value[1:-1]; return t


def t_newline(t): r'\n+'; t.lexer.lineno += len(t.value)
t_ignore = ' \t\r'

### Error léxico
def t_error(t):
    print(f"Caracter no reconocido: {t.value[0]}")
    t.lexer.skip(1)

#### Construcción del lexer
lexer = lex.lex()