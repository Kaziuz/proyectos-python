from pathlib import Path
import platform
import os


def def_open_file(file, mode="r"):
    # Abrimos un archivo en modo lectura por defecto
    return open(file, mode)


def def_read_file(file):
    # Leemos el contenido de un archivo
    return file.read()


def def_write_file(file, text):
    # Escribimos en un archivo
    return file.write(text)


def def_close_file(file):
    # Cerramos un archivo
    return file.close()


def def_eliminate_file(file):
    # Eliminamos un archivo
    file.unlink()
    if not file.exists():
        print("La receta fue borrada")
        return
    else:
        print("La receta no pudo ser borrada")
        return


def def_eliminate_cat(route_recipes):
    # Eliminamos una categoría/carpeta
    category_sel = ""  # inicializamos la variable
    for index, category in def_read_cate(route_recipes):  # leemos las categorías
        if index == int(valid_cat):  # si la categoría elegida es igual a la categoría actual
            category_sel = category  # guardamos la categoría elegida
            path_cat_delete = route_recipes / category_sel  # creamos la ruta de la categoría a eliminar
            os.rmdir(path_cat_delete)  # eliminamos la categoría
            if not path_cat_delete.exists():  # verificamos si la categoría fue eliminada
                print("La categoría fue eliminada")
                return
            else:
                print("La categoría no pudo ser eliminada")
                return


def def_create_category(route_project):
    # Creamos una nueva categoría
    name_new_cate = input("Escriba el nombre de la nueva categoría: ")  # pedimos el nombre de la nueva categoría
    path_new_cat = route_project / name_new_cate  # creamos la ruta de la nueva categoría
    if not path_new_cat.exists():  # verificamos si la categoría ya existe
        os.makedirs(route_project / name_new_cate)  # creamos la nueva categoría
        print(f"Categoría {name_new_cate} creada")
    else:
        print(f"La categoría {name_new_cate} ya existe")


def def_create_file(name_file, route_recipes):
    # Esta función se encarga de crear una nueva receta en una categoría/carpeta dada
    # y devuelve la ruta donde fue creada
    recipe_with_extension = name_file + ".txt"  # agregamos la extensión al nombre de la receta
    route_category = os.path.split(route_recipes[0][1])  # obtenemos la categoría de la receta
    route_folder = Path(route_category[0])  # creamos la ruta de la categoría
    new_recipe_route = route_folder / recipe_with_extension  # creamos la ruta de la nueva receta
    new_recipe_route.touch()  # creamos la nueva receta
    if new_recipe_route.exists():  # verificamos si se creo la receta
        print("El archivo fue creado")
    else:
        print("Hubo un error al crear el archivo")
        return
    recipe_route = new_recipe_route.resolve()  # Obtengo la ruta del nuevo archivo
    return recipe_route


def def_clean_console():
    # Limpio la consola
    system = platform.system()  # obtengo el sistema operativo
    if system == "Darwin" or system == "Linux":
        os.system("clear")
    else:
        os.system("cls")  # Windows


def def_read_cate(route_recipes):
    # Muestra las categorías/carpetas actuales del sistema de recetas
    categories = []
    counter = 0
    for category in os.listdir(route_recipes):  # Obtener las carpetas/categorías dentro de recetas
        counter += 1
        categories.append((counter, category))  # Guarda las categorías
    return categories


def def_board_cate(route):
    # creamos y mostramos un tablero con las categorías existentes
    board = ""
    for index, folder in enumerate(route.iterdir()):
        idx = f"[{index+1}] - "
        board = board + idx + folder.name + "\n"
    return board


def def_board_reci(routes_recipes):
    # Creamos y mostramos un tablero con las recetas de la categoría elegida
    board = ""
    for index, recipe in routes_recipes:  # Iteramos sobre las recetas
        idx = f"[{index}] - "  # Obtenemos el índice de la receta
        name_recipe = recipe.name.split(".")[0]  # Obtenemos el nombre de la receta
        board = board + idx + name_recipe + "\n"  # Mostramos el índice y el nombre de la receta
    return board


def def_count_reci(route_recipes):
    # Función que cuenta la cantidad de recetas en cada una de las
    # categorías/carpetas existentes
    count = 0
    for txt in route_recipes.glob("**/*.txt"):  # Itera dentro de cada categoría/carpeta los archivos .txt que hay
        count += 1
    return count


def def_route_recipe(num_recipe, route_recipes):
    # Lee las recetas de una categoría/carpeta elegida
    # y devuelve la ruta de esas recetas
    categories = def_read_cate(route_recipes)
    choice_category = []
    recipes = []

    for index, category in enumerate(categories):
        if index + 1 == int(num_recipe):  # con la opción elegida saco la categoría elegida
            choice_category = category
            break

    route_recipes = Path(route_recipes, choice_category[1])  # creo la ruta para la categoría elegida
    counter = 0

    for file in Path(route_recipes).glob("*.txt"):  # Obtengo todas las recetas dentro de la categoría
        counter += 1
        idx_recipe = (counter, file)  # Guardo las recetas
        recipes.append(idx_recipe)  # Guardo las recetas

    return recipes


def def_main_board():
    # Muestra un tablero de opciones para que el usuario elija que hacer
    board = """
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa
    """
    return board


def def_read_selection(msg):
    choice = input(msg)
    return choice


def def_valid_opt_board(choice, nu_min, nu_max):
    # Valida si la opción ingresada por el usuario el valida
    if choice.isnumeric():
        if int(choice) >= nu_min and int(choice) < nu_max:
            return True
        else:
            print("Ha ingresado una opción fuera del rango. \n")
            return False
    else:
        print("Ha ingresado una opción incorrecta. \n")
        return False


def def_valid_opt(choice, nu_min, nu_max, board):
    # Repite el proceso de pedir una opción válida hasta que la sea
    while not def_valid_opt_board(choice, nu_min, nu_max):
        print(board)
        choice = def_read_selection("Elija una de las anteriores opciones para continuar: ")
    return choice


def def_valid_opt_end(choice):
    # Válida si la opción ingresada por el usuario es válida para continuar o finalizar el programa
    if choice.isalpha():
        if choice.lower() == "s" or choice.lower() == "f":
            return True
        else:
            print("Nose que ingresaste pero no es una opción valida. \n")
            return False
    elif choice.isnumeric():
        print("No esta permitido ingresar un numero. \n")
        return False
    else:
        print("Ese caracter no esta en la opciones permitidas \n")
        return False


def def_repeat_valid_opt_end(opt):
    # Repite el proceso de leer una opción hasta que es válida para finalizar o seguir el programa
    while not def_valid_opt_end(opt):
        opt = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
    return opt


def def_find_recipe(opt_recipe, routes_recipe):
    # Esta función busca en las rutas proporcionadas la receta elegida
    # y devuelve la ruta de la receta
    sel_recipe = 0  # inicializamos la variable
    for index, recipe in routes_recipe:  # iteramos sobre las recetas
        if int(opt_recipe) == index:  # si la receta elegida es igual a la receta actual
            sel_recipe = recipe  # guardamos la receta elegida

    full_path_file = os.path.split(sel_recipe)  # obtenemos la ruta de la receta
    folder_file = Path(full_path_file[0])
    route_file = folder_file / full_path_file[1]
    return route_file


def def_end_start_program(choice):
    # Finaliza el programa o vuelve al menu principal
    if choice == "s":
        def_clean_console()
        return False
    else:
        return True


def def_start():
    # Mensaje de bienvenida al usuario
    def_clean_console()
    print("*" * 50)
    print("*" * 5 + " BIENVENIDO AL ADMINISTRADOR DE RECETAS " + "*" * 5)
    print("*" * 50)
    print(f"Las recetas se ubican en: {locat_recip}")
    print(f"Total de recetas: {def_count_reci(locat_recip)}")


# Variables
end_program = False
location_project = f"{os.getcwd()}/6.Recetario/recetario"
locat_recip = Path(location_project, "Recetas")

# Inicio del programa
while not end_program:
    def_start()
    print(def_main_board())
    opt_sel = def_read_selection("Elija una de las anteriores opciones para continuar: ")
    main_opt_sel = def_valid_opt(opt_sel, 1, 7, def_main_board())

    match int(main_opt_sel):
        case 1:
            # Mostramos y elegimos una categoría
            def_clean_console()
            print("[1] Leer receta. Elija una categoría: \n")
            print(def_board_cate(locat_recip))
            opt_sel = def_read_selection("Elija una de las anteriores opciones para continuar: ")
            count_cat = len(def_read_cate(locat_recip)) + 1
            valid_cat = def_valid_opt(opt_sel, 1, count_cat, def_board_cate(locat_recip))
            location_recipes = def_route_recipe(valid_cat, locat_recip)
            # verificamos si hay recetas para leer,
            # si si buscamos receta, si no, volvemos al final
            if len(location_recipes) > 0:
                # Buscamos la receta
                def_clean_console()
                print("Elija una receta: \n")
                print(def_board_reci(location_recipes))
                opt_recip = def_read_selection("Elija una de las anteriores opciones para continuar: ")
                count_recip = len(location_recipes) + 1
                valid_recip = def_valid_opt(opt_recip, 1, count_recip, def_board_reci(location_recipes))
                # leemos receta y la mostramos
                path_file = def_find_recipe(valid_recip, def_route_recipe(valid_cat, locat_recip))
                expose_file = def_open_file(path_file)
                see_file = def_read_file(expose_file)
                print("\n")
                print(see_file)
                def_close_file(expose_file)
                # Volvemos al menu principal o finalizamos el programa
                print("\n")
                end_selection = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
                valid_end_sel = def_repeat_valid_opt_end(end_selection)
                # Entramos a finalizar el programa o volver al menu inicial
                if not def_end_start_program(valid_end_sel):
                    pass  # volvemos al menu inicial
                else:
                    print("Ha salido del recetario")
                    end_program = True
                    break
            else:
                # Volvemos al menu principal o finalizamos el programa
                print("\n")
                print("Esta categoría no tiene recetas creadas")
                end_selection = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
                valid_end_sel = def_repeat_valid_opt_end(end_selection)
                if not def_end_start_program(valid_end_sel):
                    pass  # volvemos al menu inicial
                else:
                    print("Ha salido del recetario")
                    end_program = True
                    break
        case 2:
            # Mostramos y elegimos una categoría
            def_clean_console()
            print("[2] Crear receta. Elija una categoría: \n")
            print(def_board_cate(locat_recip))
            opt_sel = def_read_selection("Elija una de las anteriores opciones para continuar: ")
            count_cat = len(def_read_cate(locat_recip)) + 1
            valid_cat = def_valid_opt(opt_sel, 1, count_cat, def_board_cate(locat_recip))
            location_recipes = def_route_recipe(valid_cat, locat_recip)
            # Leemos nombre nueva receta y la creamos
            def_clean_console()
            new_recipe = input("Escriba el nombre de la nueva receta: ")
            route_new_recipe = def_create_file(new_recipe, location_recipes)
            # pedir que escriban el contenido de la receta
            def_clean_console()
            text_recipe = input("Escriba el contenido de la nueva receta: ")
            # abrir el archivo recién creado modo escritura
            recipe_file = def_open_file(route_new_recipe, "w")
            # escribir el archivo con el contenido ingresado
            def_write_file(recipe_file, text_recipe)
            def_close_file(recipe_file)
            # leemos receta y la mostramos
            recipe_file_wrote = def_open_file(Path(route_new_recipe))
            see_new_file = def_read_file(recipe_file_wrote)
            if see_new_file == text_recipe:
                print("El texto de la receta fue escrito! \n")
                print(see_new_file)
            else:
                print("No se pudo escribir el archivo")
            # Volvemos al menu principal o finalizamos el programa
            print("\n")
            end_selection = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
            valid_end_sel = def_repeat_valid_opt_end(end_selection)
            # Entramos a finalizar el programa o volver al menu inicial
            if not def_end_start_program(valid_end_sel):
                pass  # volvemos al menu inicial
            else:
                print("Ha salido del recetario")
                end_program = True
                break
        case 3:
            # Mostramos y elegimos una categoría
            def_clean_console()
            print("[3] Crear categoría. \n")
            print(def_board_cate(locat_recip))
            # Creamos categoría
            def_create_category(locat_recip)
            # Volvemos al menu principal o finalizamos el programa
            end_selection = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
            valid_end_sel = def_repeat_valid_opt_end(end_selection)
            # Entramos a finalizar el programa o volver al menu inicial
            if not def_end_start_program(valid_end_sel):
                pass  # volvemos al menu inicial
            else:
                print("Ha salido del recetario")
                end_program = True
                break
        case 4:
            # Mostramos y elegimos una categoría
            def_clean_console()
            print("[4] Eliminar receta. Elija una categoría: \n")
            print(def_board_cate(locat_recip))
            opt_sel = def_read_selection("Elija una de las anteriores opciones para continuar: ")
            count_cat = len(def_read_cate(locat_recip)) + 1
            valid_cat = def_valid_opt(opt_sel, 1, count_cat, def_board_cate(locat_recip))
            location_recipes = def_route_recipe(valid_cat, locat_recip)
            # verificamos si hay recetas para leer,
            # si si buscamos receta, si no, volvemos al final
            if len(location_recipes) > 0:
                # Buscamos la receta
                def_clean_console()
                print("Elija una receta a eliminar: \n")
                print(def_board_reci(location_recipes))
                opt_recip = def_read_selection("Elija una de las anteriores opciones para continuar: ")
                count_recip = len(location_recipes) + 1
                valid_recip = def_valid_opt(opt_recip, 1, count_recip, def_board_reci(location_recipes))
                # Borramos receta
                path_file = def_find_recipe(valid_recip, def_route_recipe(valid_cat, locat_recip))
                def_eliminate_file(path_file)
                # Volvemos al menu principal o finalizamos el programa
                print("\n")
                end_selection = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
                valid_end_sel = def_repeat_valid_opt_end(end_selection)
                # Entramos a finalizar el programa o volver al menu inicial
                if not def_end_start_program(valid_end_sel):
                    pass  # volvemos al menu inicial
                else:
                    print("Ha salido del recetario")
                    end_program = True
                    break
            else:
                # Volvemos al menu principal o finalizamos el programa
                print("\n")
                print("Esta categoría no tiene recetas creadas")
                end_selection = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
                valid_end_sel = def_repeat_valid_opt_end(end_selection)
                if not def_end_start_program(valid_end_sel):
                    pass  # volvemos al menu inicial
                else:
                    print("Ha salido del recetario")
                    end_program = True
                    break
        case 5:
            # Mostramos y elegimos una categoría
            def_clean_console()
            print("[5] Eliminar categoría. Elija una categoría: \n")
            print(def_board_cate(locat_recip))
            opt_sel = def_read_selection("Elija una de las anteriores opciones para continuar: ")
            count_cat = len(def_read_cate(locat_recip)) + 1
            valid_cat = def_valid_opt(opt_sel, 1, count_cat, def_board_cate(locat_recip))
            # Eliminamos categoría
            def_eliminate_cat(locat_recip)
            # Volvemos al menu principal o finalizamos el programa
            print("\n")
            end_selection = def_read_selection("Presione [s] para volver al menu principal. Presione [f] para finalizar: ")
            valid_end_sel = def_repeat_valid_opt_end(end_selection)
            # Entramos a finalizar el programa o volver al menu inicial
            if not def_end_start_program(valid_end_sel):
                pass  # volvemos al menu inicial
            else:
                print("Ha salido del recetario")
                end_program = True
                break
        case _:
            # Finalizamos el programa
            print("[6] Salir del programa: Ha salido del recetario")
            end_program = True
