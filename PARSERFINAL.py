import ply.yacc as yacc
from LEXERFINAL import tokens, lexer
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def p_json(p):
    'json : LLAVE_IZQ contenido LLAVE_DER'
    p[0] = p[2]

def p_contenido(p):
    '''contenido : campos_principales'''
    p[0] = p[1]

def p_campos_principales(p):
    '''campos_principales : campo_principal
                          | campo_principal COMA campos_principales
                          | empty'''
    
    if len(p) == 1:
        p[0] = {}
    elif len(p) == 2:
        p[0] = {p[1][0]: p[1][1]}
    else:
        p[0] = {**{p[1][0]: p[1][1]}, **p[3]}

def p_campo_principal(p):
    '''campo_principal : VERSION DOS_PUNTOS STRING
                       | EQUIPOS DOS_PUNTOS CORCHETE_IZQ lista_equipos CORCHETE_DER
                       | FIRMA_DIGITAL DOS_PUNTOS STRING
                       | FIRMA_DIGITAL DOS_PUNTOS NULO'''
    if p[1] == "equipos":
        p[0] = (p[1], p[4])
    else:
        p[0] = (p[1], p[3])

def p_lista_equipos(p):
    '''lista_equipos : equipo
                     | equipo COMA lista_equipos
                     | empty'''
    if len(p) == 2 and p[1] is None:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_equipo(p):
    'equipo : LLAVE_IZQ campos_equipo LLAVE_DER'
    p[0] = p[2]

def p_campos_equipo(p):
    '''campos_equipo : campo_equipo
                     | campo_equipo COMA campos_equipo
                     | empty'''
    if len(p) == 1:
        p[0] = {}
    elif len(p) == 2:
        p[0] = {p[1][0]: p[1][1]}
    else:
        p[0] = {**{p[1][0]: p[1][1]}, **p[3]}

def p_campo_equipo(p):
    '''campo_equipo : NOMBRE_EQUIPO DOS_PUNTOS STRING
                    | IDENTIDAD_EQUIPO DOS_PUNTOS STRING
                    | LINK DOS_PUNTOS STRING
                    | ASIGNATURA DOS_PUNTOS STRING
                    | CARRERA DOS_PUNTOS STRING
                    | UNIVERSIDAD_REGIONAL DOS_PUNTOS STRING
                    | VERSION DOS_PUNTOS STRING
                    | ALIANZA_EQUIPO DOS_PUNTOS STRING
                    | DIRECCION DOS_PUNTOS direccion
                    | INTEGRANTES DOS_PUNTOS CORCHETE_IZQ lista_integrantes CORCHETE_DER
                    | PROYECTOS DOS_PUNTOS CORCHETE_IZQ lista_proyectos CORCHETE_DER
                    | FIRMA_DIGITAL DOS_PUNTOS STRING'''
    
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:  
        p[0] = (p[1], p[4])

def p_direccion(p):
    'direccion : LLAVE_IZQ campos_direccion LLAVE_DER'
    p[0] = p[2]

def p_campos_direccion(p):
    '''campos_direccion : campo_direccion
                        | campo_direccion COMA campos_direccion
                        | empty'''
    if len(p) == 1:
        p[0] = {}
    elif len(p) == 2:
        p[0] = {p[1][0]: p[1][1]}
    else:
        p[0] = {**{p[1][0]: p[1][1]}, **p[3]}

def p_campo_direccion(p):
    '''campo_direccion : CALLE DOS_PUNTOS STRING
                       | CIUDAD DOS_PUNTOS STRING
                       | PAIS DOS_PUNTOS STRING'''
    p[0] = (p[1], p[3])

def p_lista_integrantes(p):
    '''lista_integrantes : integrante
                         | integrante COMA lista_integrantes
                         | empty'''
    if len(p) == 2 and p[1] is None:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_integrante(p):
    'integrante : LLAVE_IZQ campos_integrante LLAVE_DER'
    p[0] = p[2]

def p_campos_integrante(p):
    '''campos_integrante : campo_integrante
                         | campo_integrante COMA campos_integrante
                         | empty'''
    if len(p) == 1:
        p[0] = {}
    elif len(p) == 2:
        p[0] = {p[1][0]: p[1][1]}
    else:
        p[0] = {**{p[1][0]: p[1][1]}, **p[3]}

def p_campo_integrante(p):
    '''campo_integrante : NOMBRE DOS_PUNTOS STRING
                        | EDAD DOS_PUNTOS NUM
                        | CARGO DOS_PUNTOS STRING
                        | FOTO DOS_PUNTOS STRING
                        | EMAIL DOS_PUNTOS STRING
                        | HABILIDADES DOS_PUNTOS STRING
                        | SALARIO DOS_PUNTOS salario
                        | ACTIVO DOS_PUNTOS BOOLEANO'''
    p[0] = (p[1], p[3])

def p_salario(p):
    '''salario : FLOAT
               | NUM'''
    p[0] = p[1]

def p_lista_proyectos(p):
    '''lista_proyectos : proyecto
                       | proyecto COMA lista_proyectos
                       | empty'''
    if len(p) == 2 and p[1] is None:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_proyecto(p):
    'proyecto : LLAVE_IZQ campos_proyecto LLAVE_DER'
    p[0] = p[2]

def p_campos_proyecto(p):
    '''campos_proyecto : campo_proyecto
                       | campo_proyecto COMA campos_proyecto
                       | empty'''
    if len(p) == 1:
        p[0] = {}
    elif len(p) == 2:
        p[0] = {p[1][0]: p[1][1]}
    else:
        p[0] = {**{p[1][0]: p[1][1]}, **p[3]}

def p_campo_proyecto(p):
    '''campo_proyecto : NOMBRE DOS_PUNTOS STRING
                      | ESTADO DOS_PUNTOS STRING
                      | RESUMEN DOS_PUNTOS STRING
                      | TAREAS DOS_PUNTOS CORCHETE_IZQ lista_tareas CORCHETE_DER
                      | FECHA_INICIO DOS_PUNTOS DATE
                      | FECHA_FIN DOS_PUNTOS DATE
                      | VIDEO DOS_PUNTOS STRING
                      | CONCLUSION DOS_PUNTOS STRING'''
    if len(p) == 4:
        p[0] = (p[1], p[3])
    else:
        p[0] = (p[1], p[4])

def p_lista_tareas(p):
    '''lista_tareas : tarea
                    | tarea COMA lista_tareas
                    | empty'''
    if len(p) == 2 and p[1] is None:
        p[0] = []
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_tarea(p):
    'tarea : LLAVE_IZQ campos_tarea LLAVE_DER'
    p[0] = p[2]

def p_campos_tarea(p):
    '''campos_tarea : campo_tarea
                    | campo_tarea COMA campos_tarea
                    | empty'''
    if len(p) == 1:
        p[0] = {}
    elif len(p) == 2:
        p[0] = {p[1][0]: p[1][1]}
    else:
        p[0] = {**{p[1][0]: p[1][1]}, **p[3]}

def p_campo_tarea(p):
    '''campo_tarea : NOMBRE DOS_PUNTOS STRING
                   | ESTADO DOS_PUNTOS STRING
                   | RESUMEN DOS_PUNTOS STRING
                   | FECHA_INICIO DOS_PUNTOS DATE
                   | FECHA_INICIO DOS_PUNTOS NULO
                   | FECHA_FIN DOS_PUNTOS DATE
                   | FECHA_FIN DOS_PUNTOS NULO'''
    p[0] = (p[1], p[3])


def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        token_value = p.value
        lineno = p.lineno
        token_type = p.type
        
        if token_type == 'STRING' and hasattr(p.lexer, 'lexdata'):
            lines = p.lexer.lexdata.split('\n')
            if lineno <= len(lines):
                line_content = lines[lineno - 1].strip()
                
                if '"' in line_content and not line_content.endswith(',') and not line_content.endswith('{') and not line_content.endswith('['):
                    print(f"Error de sintaxis en línea {lineno}")
                    print(f"Línea problemática: {line_content}")
                    print(f"Posible causa: Falta una coma (,) al final de la línea")
                    print(f"Sugerencia: Agregar ',' después de '{token_value}'")
                else:
                    print(f"Error de sintaxis en línea {lineno}")
                    print(f"Línea problemática: {line_content}")
                    print(f"Token inesperado: '{token_value}' (tipo: {token_type})")
            else:
                print(f"Error de sintaxis en línea {lineno}, token inesperado: '{token_value}' (tipo: {token_type})")
        else:
            print(f"Error de sintaxis en línea {lineno}, token inesperado: '{token_value}' (tipo: {token_type})")
            
        if hasattr(p, 'lexer') and hasattr(p.lexer, 'lexdata'):
            print(f"Contexto: Se esperaba un token válido después del elemento anterior")
    else:
        print("Error de sintaxis: fin de entrada inesperado.")
        print("Posible causa: El JSON está incompleto o falta cerrar llaves/corchetes")

def detectar_error_json_real(contenido_json): ##Detecta errores comunes en JSON y reporta la línea correcta.
    
    lines = contenido_json.split('\n')
    
    for i, line in enumerate(lines, 1):
        line_stripped = line.strip()
        
        if line_stripped and not line_stripped.startswith('{') and not line_stripped.startswith('['):
            if ('"' in line_stripped and 
                line_stripped.endswith('"') and 
                i < len(lines) and
                lines[i].strip().startswith('"')):
                return i, f"Falta coma (,) al final de la línea {i}"
            
            if (line_stripped.endswith(('true', 'false', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')) and
                i < len(lines) and
                lines[i].strip().startswith('"')):
                return i, f"Falta coma (,) al final de la línea {i}"
                
            if line_stripped.endswith(('}', ']')) and i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith('"') and not line_stripped.endswith(','):
                    return i, f"Falta coma (,) al final de la línea {i}"
    
    return None, None

def detectar_errores_lexicos(contenido_json): ##Detecta errores léxicos comunes como tokens mal escritos.
    tokens_esperados = {
        'nombre_equipo': 'NOMBRE_EQUIPO',
        'identidad_equipo': 'IDENTIDAD_EQUIPO', 
        'direccion': 'DIRECCION',
        'universidad_regional': 'UNIVERSIDAD_REGIONAL',
        'alianza_equipo': 'ALIANZA_EQUIPO',
        'integrantes': 'INTEGRANTES',
        'proyectos': 'PROYECTOS',
        'fecha_inicio': 'FECHA_INICIO',
        'fecha_fin': 'FECHA_FIN',
        'firma_digital': 'FIRMA_DIGITAL',
        'version': 'VERSION',
        'equipos': 'EQUIPOS',
        'nombre': 'NOMBRE',
        'cargo': 'CARGO',
        'edad': 'EDAD',
        'foto': 'FOTO',
        'email': 'EMAIL',
        'habilidades': 'HABILIDADES',
        'salario': 'SALARIO',
        'activo': 'ACTIVO',
        'estado': 'ESTADO',
        'resumen': 'RESUMEN',
        'tareas': 'TAREAS',
        'video': 'VIDEO',
        'conclusion': 'CONCLUSION',
        'calle': 'CALLE',
        'ciudad': 'CIUDAD',
        'pais': 'PAIS',
        'carrera': 'CARRERA',
        'asignatura': 'ASIGNATURA',
        'link': 'LINK'
    }
    
    errores_comunes = {
        'nombre_equipe': 'nombre_equipo',
        'identida_equipo': 'identidad_equipo',
        'direccion_': 'direccion',
        'universida_regional': 'universidad_regional',
        'alianz_equipo': 'alianza_equipo',
        'integrante': 'integrantes',
        'proyecto': 'proyectos',
        'fecha_incio': 'fecha_inicio',
        'fecha_fi': 'fecha_fin',
        'firm_digital': 'firma_digital',
        'versio': 'version',
        'equipo': 'equipos',
        'nombr': 'nombre',
        'crgo': 'cargo',
        'eda': 'edad',
        'fot': 'foto',
        'emai': 'email',
        'habilidade': 'habilidades',
        'salari': 'salario',
        'activ': 'activo',
        'estad': 'estado',
        'resume': 'resumen',
        'tarea': 'tareas',
        'vide': 'video',
        'conclusio': 'conclusion',
        'call': 'calle',
        'ciuda': 'ciudad',
        'pai': 'pais',
        'carrer': 'carrera',
        'asignatur': 'asignatura',
        'lin': 'link',
        'rgentina': 'argentina'
    }
    
    lines = contenido_json.split('\n')
    
    for i, line in enumerate(lines, 1):
        import re
        matches = re.findall(r'"([^"]+)"', line)
        
        for match in matches:
            if match in errores_comunes:
                return i, f"Token mal escrito: '{match}' debería ser '{errores_comunes[match]}'"
            
            for token_correcto in tokens_esperados.keys():
                if len(match) == len(token_correcto):
                    diferencias = sum(c1 != c2 for c1, c2 in zip(match, token_correcto))
                    if diferencias == 1:
                        return i, f"Posible error léxico: '{match}' es similar a '{token_correcto}'"
    
    return None, None

parser = yacc.yacc()

def analizar_entrada(codigo):
    resultado = parser.parse(codigo, lexer=lexer)
    if resultado is not None:
        print("Análisis sintáctico exitoso. Estructura válida.")
    else:
        print("Análisis sintáctico fallido.")

def traducir_a_html(datos_json): ##Convierte los datos parseados del JSON a un documento HTML según la consigna.
    
    html = []
    
    html.append('<!DOCTYPE html>')
    html.append('<html>')
    html.append('<head>')
    html.append('    <meta charset="UTF-8">')
    html.append('    <title>Equipos y Proyectos</title>')
    html.append('</head>')
    html.append('<body>')
    
    if 'version' in datos_json:
        html.append(f'    <p>Versión: {datos_json["version"]}</p>')
    

    if 'equipos' in datos_json and datos_json['equipos'] and len(datos_json['equipos']) > 0:
        for equipo in datos_json['equipos']:
            html.extend(generar_html_equipo(equipo))
    

    if 'firma_digital' in datos_json:
        if datos_json['firma_digital']:
            html.append(f'    <p>Firma Digital: {datos_json["firma_digital"]}</p>')
    
    html.append('</body>')
    html.append('</html>')
    
    return '\n'.join(html)

def generar_html_equipo(equipo): ##Genera el HTML para un equipo según la consigna.
    html = []
    
    html.append('    <div style="border: 1px solid grey; padding: 20px;">')
    
    if 'nombre_equipo' in equipo:
        html.append(f'        <h1>{equipo["nombre_equipo"]}</h1>')
    
    # Datos del equipo como párrafos según consigna
    if 'universidad_regional' in equipo:
        html.append(f'        <p>Universidad: {equipo["universidad_regional"]}</p>')
    
    if 'carrera' in equipo:
        html.append(f'        <p>Carrera: {equipo["carrera"]}</p>')
    
    if 'asignatura' in equipo:
        html.append(f'        <p>Asignatura: {equipo["asignatura"]}</p>')

    if 'link' in equipo:
        html.append(f'        <p>Enlace: <a href="{equipo["link"]}">{equipo["link"]}</a></p>')
    
    if 'identidad_equipo' in equipo:
        html.append(f'        <p>Identidad del Equipo:</p>')
        html.append(f'        <img src="{equipo["identidad_equipo"]}" alt="Identidad del equipo {equipo.get("nombre_equipo", "")}" style="max-width: 300px; height: auto; border: 2px solid #666; margin: 10px 0; display: block;">')
    
    if 'direccion' in equipo:
        direccion = equipo['direccion']
        if 'calle' in direccion:
            html.append(f'        <p>Calle: {direccion["calle"]}</p>')
        if 'ciudad' in direccion:
            html.append(f'        <p>Ciudad: {direccion["ciudad"]}</p>')
        if 'pais' in direccion:
            html.append(f'        <p>País: {direccion["pais"]}</p>')
    
    if 'alianza_equipo' in equipo:
        html.append(f'        <p>Alianza de equipo : {equipo["alianza_equipo"]}</p>')
    
    if 'integrantes' in equipo and equipo['integrantes'] and len(equipo['integrantes']) > 0:
        for integrante in equipo['integrantes']:
            html.extend(generar_html_integrante(integrante))

    if 'proyectos' in equipo and equipo['proyectos'] and len(equipo['proyectos']) > 0:
        for proyecto in equipo['proyectos']:
            html.extend(generar_html_proyecto(proyecto))
    
    html.append('    </div>')
    
    return html

def generar_html_integrante(integrante): ##Genera el HTML para un integrante según la consigna.
    html = []

    if 'nombre' in integrante:
        html.append(f'        <h2>{integrante["nombre"]}</h2>')
    

    html.append('        <ul>')
    
    if 'cargo' in integrante:
        html.append(f'            <li>Cargo: {integrante["cargo"]}</li>')
    
    if 'edad' in integrante:
        html.append(f'            <li>Edad: {integrante["edad"]}</li>')
    
    if 'email' in integrante:
        html.append(f'            <li>Email: {integrante["email"]}</li>')
    
    if 'foto' in integrante:
        html.append(f'            <li>Foto: <br><img src="{integrante["foto"]}" alt="Foto de {integrante.get("nombre", "integrante")}" style="max-width: 200px; height: auto; border: 1px solid #ccc; margin: 5px 0;"></li>')
    
    if 'habilidades' in integrante:
        html.append(f'            <li>Habilidades: {integrante["habilidades"]}</li>')
    
    if 'salario' in integrante:
        html.append(f'            <li>Salario: {integrante["salario"]}</li>')
    
    if 'activo' in integrante:
        estado = "Activo" if integrante["activo"] else "Inactivo"
        html.append(f'            <li>Estado: {estado}</li>')
    
    html.append('        </ul>')
    
    return html

def generar_html_proyecto(proyecto): ##Genera el HTML para un proyecto según la consigna.
    html = []
    
    if 'nombre' in proyecto:
        html.append(f'        <h3>{proyecto["nombre"]}</h3>')

    html.append('        <ul>')
    
    if 'estado' in proyecto:
        html.append(f'            <li>Estado: {proyecto["estado"]}</li>')
    
    if 'resumen' in proyecto:
        html.append(f'            <li>Resumen: {proyecto["resumen"]}</li>')
    
    if 'fecha_inicio' in proyecto:
        html.append(f'            <li>Fecha de Inicio: {proyecto["fecha_inicio"]}</li>')
    
    if 'fecha_fin' in proyecto:
        html.append(f'            <li>Fecha de Fin: {proyecto["fecha_fin"]}</li>')
    
    if 'video' in proyecto:
        html.append(f'            <li>Video: <a href="{proyecto["video"]}">{proyecto["video"]}</a></li>')
    
    if 'conclusion' in proyecto:
        html.append(f'            <li>Conclusión: {proyecto["conclusion"]}</li>')
    
    html.append('        </ul>')
    
    if 'tareas' in proyecto and proyecto['tareas'] and len(proyecto['tareas']) > 0:
        html.append('        <table border="1">')
        html.append('            <tr>')
        html.append('                <th>Nombre</th>')
        html.append('                <th>Estado</th>')
        html.append('                <th>Resumen</th>')
        html.append('                <th>Fecha Inicio</th>')
        html.append('                <th>Fecha Fin</th>')
        html.append('            </tr>')
        
        for tarea in proyecto['tareas']:
            html.append('            <tr>')
            html.append(f'                <td>{tarea.get("nombre", "")}</td>')
            html.append(f'                <td>{tarea.get("estado", "")}</td>')
            html.append(f'                <td>{tarea.get("resumen", "")}</td>')
            html.append(f'                <td>{tarea.get("fecha_inicio", "")}</td>')
            html.append(f'                <td>{tarea.get("fecha_fin", "")}</td>')
            html.append('            </tr>')
        
        html.append('        </table>')
    
    return html

def guardar_html(contenido_html, nombre_archivo="resultado.html"): ##Guarda el contenido HTML en un archivo.
    
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_html)
        print(f"Archivo HTML generado exitosamente: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"Error al guardar el archivo HTML: {e}")
        return False



def analizar_json_archivo(ruta_archivo): ##Analiza un archivo JSON y lo convierte a HTML.

    import sys
    import os
    print("Iniciando análisis JSON...")
    print(f"Archivo: {ruta_archivo}")
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return False
    
    try:
        print("Leyendo archivo JSON...")
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido_json = archivo.read()
        
        print(f"Archivo leído exitosamente ({len(contenido_json)} caracteres)")
        
        linea_error_lexico, mensaje_error_lexico = detectar_errores_lexicos(contenido_json)
        if linea_error_lexico:
            print(f"Error léxico detectado en línea {linea_error_lexico}")
            print(f"{mensaje_error_lexico}")
            lines = contenido_json.split('\n')
            if linea_error_lexico <= len(lines):
                print(f"Línea problemática: {lines[linea_error_lexico - 1].strip()}")
            print(f"Tipo de error: LÉXICO (token no reconocido o mal escrito)")
            return False

        linea_error, mensaje_error = detectar_error_json_real(contenido_json)
        if linea_error:
            print(f"Error sintáctico detectado en línea {linea_error}")
            print(f"{mensaje_error}")
            lines = contenido_json.split('\n')
            if linea_error <= len(lines):
                print(f"Línea problemática: {lines[linea_error - 1].strip()}")
            print(f"Tipo de error: SINTÁCTICO (estructura JSON incorrecta)")
            return False
        
        print("Iniciando análisis léxico...")
        lexer.input(contenido_json)
        

        tokens_encontrados = []
        lexer.input(contenido_json)
        for token in lexer:
            tokens_encontrados.append(token)
        
        print(f"Análisis léxico completado ({len(tokens_encontrados)} tokens encontrados)")
        
        print("Iniciando análisis sintáctico...")
        parser_obj = yacc.yacc()
        
        lexer.input(contenido_json)
        lexer.lexdata = contenido_json
        
        resultado_parser = parser_obj.parse(contenido_json, lexer=lexer)
        
        if resultado_parser is None:
            print("Error: El análisis sintáctico falló. El JSON no es válido según la gramática.")
            print("Revisa la sintaxis del JSON, especialmente:")
            print("• Comas entre elementos del mismo nivel")
            print("• Comillas en strings")
            print("• Llaves y corchetes balanceados")
            return False
        
        print("Análisis sintáctico completado exitosamente")
        print(f"Estructura encontrada: {list(resultado_parser.keys())}")        

        contenido_html = traducir_a_html(resultado_parser)
        
        nombre_base = os.path.splitext(os.path.basename(ruta_archivo))[0]
        archivo_salida = f"{nombre_base}_resultado.html"
        
        if guardar_html(contenido_html, archivo_salida):
            print(f"¡Proceso completado exitosamente!")
            print(f"Archivo HTML generado: {archivo_salida}")
            
            return True
        else:
            return False
            
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {ruta_archivo}")
        return False
    except UnicodeDecodeError:
        print(f"Error: No se pudo leer el archivo. Verifica la codificación.")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        return False


def procesar_con_traductor(ruta_archivo): ##Función auxiliar para procesar un archivo JSON con el traductor integrado.
    import os   
    exito = analizar_json_archivo(ruta_archivo)
    
    if exito:
        print("\n¡Análisis completado con éxito!")
        print("Puedes abrir el archivo HTML generado en tu navegador web.")
        return True
    else:
        print("\nEl análisis falló. Revisa los errores mostrados arriba.")
        return False


def main(): #Función principal
    import sys
    import os

    root = tk.Tk()
    root.withdraw()
        
    print("Interprete Json a HTML")
    print("=" * 55)
    
    parser = yacc.yacc()
    
    while True:
        opcion = simpledialog.askstring("Opciones de uso", 
                                       "Seleccione una opción:\n1. Ingresar ruta del archivo \n2. Leer desde archivo JSON \n3. Ingresar por texto \n4. Salir")
        
        if opcion == "1":
            print("Ingrese la ubicación del archivo .json:")
            archivo = simpledialog.askstring("Entrada", "Ingrese el texto:")
            
            if os.path.exists(archivo):
                resultado = analizar_json_archivo(archivo)
                if resultado:
                    print("\n ¡Análisis completado con éxito!")
                    print("Puedes abrir el archivo HTML generado en tu navegador web.")
                else:
                    print("\n El análisis falló. Revisa los errores mostrados arriba.")
            else:
                print("Archivo no encontrado. Intenta de nuevo.")
                continue
                
        elif opcion == "2":
            file_paths = filedialog.askopenfilenames(filetypes=[("JSON files", "*.json")])
            if not file_paths:
                    continue
                
            for file_path in file_paths:
                    analizar_json_archivo(file_path)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            archivo = file.read()
                        
                        result = parser.parse(archivo)
                        print("\n ¡Análisis completado con éxito!")
                        print("Puedes abrir el archivo HTML generado en tu navegador web.")
                        messagebox.showinfo("Éxito", f"El análisis del archivo {os.path.basename(file_path)} se completó exitosamente.")
                    
                    except Exception as e:
                        print(f"Error al procesar {file_path}:", str(e))
                        messagebox.showerror("Error", f"Error al procesar {os.path.basename(file_path)}: {str(e)}")
        elif opcion == "3":
            
            contenido = simpledialog.askstring("Entrada JSON", "Ingrese el contenido JSON:")
            
            if contenido and contenido.strip():
                try:
                    ast = parser.parse(contenido, lexer=lexer)
                    if ast:
                        print("Análisis sintáctico exitoso. Estructura válida.")
                        # Traducir a HTML
                        html_resultado = traducir_a_html(ast)
                        # Guardar HTML
                        guardar_html(html_resultado, "resultado_interactivo.html")
                        print("\n¡Traducción completada!")
                        print("Archivo HTML generado: resultado_interactivo.html")
                        
                        # Mostrar mensaje de éxito
                        messagebox.showinfo("Éxito", "El análisis del contenido JSON se completó exitosamente.")
                    else:
                        print("Error en el análisis sintáctico.")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("No se ingresó contenido válido o se canceló la operación.")
                
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4")
            continue

    print("\nAnalisis finalizado.")

if __name__ == "__main__":
    main()