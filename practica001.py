import tkinter as tk
from tkinter import ttk, scrolledtext, Menu
from tkinter import messagebox as mBox

def printAll():
    resultado = ''
    for k, v in entries.items():
        if not v[1].get():
            mBox.showinfo('Imprimir todo', 'Por favor termine de llenar los campos')
            return
        else:
            resultado += k.capitalize() + ': ' + v[1].get() + '\n'
    for k, v in comboBoxes.items():
        resultado += k.capitalize() + ': ' + v[1].get() + '\n'
    gustos = 'Te gusta: '
    for k, v in checkButtons.items():
        if v[1].get():
            gustos += '\n    ' + k.capitalize()

    if gustos == 'Te gusta: ':
        gustos = 'No te gusta nada'

    seleccionado = variableRadioButtons.get()
    opcion = 1
    resultado += '\n'+gustos
    resultado += '\nEstado Civil: '
    for k, v in radioButtons.items():
        if opcion == seleccionado:
            resultado += k.capitalize()
            break
        opcion += 1
    textObjetivo = scrollText['ObjetivoVida'].get(1.0, tk.END)
    if textObjetivo == '\n':
        mBox.showinfo('Imprimir todo', 'Por favor llene todos los campos')
        return
    resultado += '\nObjetivo de la vida: ' + textObjetivo
    mBox.showinfo('Imprimir todo', resultado)

def imprimirDatosPersonales():
    resultado = ''
    for k, v in entries.items():
        if not v[1].get():
            mBox.showinfo('Datos Personales', 'Por favor termine de llenar los campos')
            break
        else:
            resultado += k.capitalize() + ': ' + v[1].get() + '\n'
    else:
        for k, v in comboBoxes.items():
            resultado += k.capitalize() + ': ' + v[1].get() + '\n'
        mBox.showinfo('Datos Personales', resultado)

def funcionSalir():
    window.quit()
    window.destroy()
    exit()

def funcionCajaMensaje():
    mBox.showinfo('Acerca de', 'Elaborado por: \nDiego Alexis Rossell Coria')

def imprimirDatosExtras():
    gustos = 'Te gusta: '
    for k, v in checkButtons.items():
        if v[1].get():
            gustos += '\n    ' + k.capitalize()

    if gustos == 'Te gusta: ':
        gustos = 'No te gusta nada'

    seleccionado = variableRadioButtons.get()
    opcion = 1
    resultado = gustos
    resultado += '\nEstado Civil: '
    for k, v in radioButtons.items():
        if opcion == seleccionado:
            resultado += k.capitalize()
            break
        opcion += 1
    textObjetivo = scrollText['ObjetivoVida'].get(1.0, tk.END)
    if textObjetivo == '\n':
        mBox.showinfo('Datos Extras', 'Por favor llene todos los campos')
        return
    resultado += '\nObjetivo de la vida: ' + textObjetivo
    mBox.showinfo('Datos Extras', resultado)

def makeLabel(window, fieldName, texto, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1, ipady = 5):
    labels[fieldName] = ttk.Label(window, text = texto)
    labels[fieldName].grid(column = noColumn, row = noRow, columnspan = noColumnSpan, rowspan = noRowSpan, ipady = ipady)

def makeEntry(window, fieldName, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1):
    entries[fieldName] = (ttk.Entry(window), tk.StringVar())
    entries[fieldName][0].configure(textvariable = entries[fieldName][1])
    entries[fieldName][0].grid(row = noRow, column = noColumn, rowspan = noRowSpan, columnspan = noColumnSpan)

def makeComboBox(window, fieldName, options, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1, State = 'readonly'):
    comboBoxes[fieldName] = (ttk.Combobox(window), tk.StringVar())
    comboBoxes[fieldName][0].configure(textvariable = comboBoxes[fieldName][1], state = State)
    comboBoxes[fieldName][0]['values'] = options
    comboBoxes[fieldName][0].current(0)
    comboBoxes[fieldName][0].grid(row = noRow, column = noColumn, rowspan = noRowSpan, columnspan = noColumnSpan)

def makeCheckButton(window, fieldName, texto, noRow, noColumn, ipady = 5, ipadx = 5):
    checkButtons[fieldName] = (tk.Checkbutton(window), tk.StringVar())
    checkButtons[fieldName][0].configure(text = texto, var = checkButtons[fieldName][1], onvalue = fieldName.capitalize(), offvalue = '')
    checkButtons[fieldName][0].grid(row = noRow, column = noColumn, ipady = ipady, ipadx = ipadx)

def makeRadioButtons(window, fieldName, variable,value, texto, noRow, noColumn, ipady = 5, ipadx = 5):
    radioButtons[fieldName] = tk.Radiobutton(window)
    radioButtons[fieldName].configure(text = texto, variable = variable, value = value)
    radioButtons[fieldName].grid(row = noRow, column = noColumn, ipady = ipady, ipadx = ipadx)

def makeScrolledText(window, fieldName, row, column, width, height, wrap):
    scrollText[fieldName] = scrolledtext.ScrolledText(window)
    scrollText[fieldName].configure(width = width, height = height, wrap = wrap)
    scrollText[fieldName].grid(column = column, row = row, columnspan = 2)

def makeButton(window, fieldName, texto, function, noRow, noColumn, noRowSpan = 1, noColumnSpan = 1):
    buttons[fieldName] = ttk.Button(window, text = texto, command = function)
    buttons[fieldName].grid(row = noRow, column = noColumn, rowspan = noRowSpan, columnspan = noColumnSpan, ipadx = 5, ipady = 5)

def nextRow(field):
    indexes[field]['row'] += 1

def nextColumn(field):
    indexes[field]['column'] += 1

def wrap(field):
    nextRow(field)
    indexes[field]['column'] = 0

window = tk.Tk()
window.title('Sistema Escolar')
window.resizable(0, 0)

labels = {}
entries = {}
comboBoxes = {}
buttons = {}
checkButtons = {}
radioButtons = {}
scrollText = {}
indexes = {
    'window': {
        'row': 0,
        'column': 0
    },
    'tabDatosPersonales': {
        'row': 0,
        'column': 0
    },
    'tabDatosExtras': {
        'row': 0,
        'column': 0
    }
}

tabControl = ttk.Notebook(window)
tabDatosPersonales = ttk.Frame(window)
tabControl.add(tabDatosPersonales, text = 'Datos Personales')
tabControl.grid(column = indexes['window']['column'], row = indexes['window']['row'])
nextColumn('window')
datosExtras = ttk.Frame(window)
tabControl.add(datosExtras, text = 'Datos Extras')
tabControl.grid(column = indexes['window']['column'], row = indexes['window']['row'])
wrap('window')

# Nombre
makeLabel(tabDatosPersonales, 'nombre', 'Nombre', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
nextColumn('tabDatosPersonales')
makeEntry(tabDatosPersonales, 'nombre', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')

# ApellidoPaterno
makeLabel(tabDatosPersonales, 'apellidoPaterno', 'Apellido Paterno', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
nextColumn('tabDatosPersonales')
makeEntry(tabDatosPersonales, 'apellidoPaterno', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')

# Apellido Materno
makeLabel(tabDatosPersonales, 'apellidoMaterno', 'Apellido Materno', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
nextColumn('tabDatosPersonales')
makeEntry(tabDatosPersonales, 'apellidoMaterno', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')

# Direccion
makeLabel(tabDatosPersonales, 'direccion', 'Direccion', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
nextColumn('tabDatosPersonales')
makeEntry(tabDatosPersonales, 'direccion', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')

# Colonia
makeLabel(tabDatosPersonales, 'colonia', 'Colonia', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
nextColumn('tabDatosPersonales')
colonias = ('Guadalupe', 'Aguaclara', 'Valle Quieto')
makeComboBox(tabDatosPersonales, 'colonia', colonias, indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')

# Ciudad
makeLabel(tabDatosPersonales, 'ciudad', 'Ciudad', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
nextColumn('tabDatosPersonales')
ciudades = ('Morelia', 'Charo', 'Lazaro Cardenas')
makeComboBox(tabDatosPersonales, 'ciudad', ciudades, indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')

# Municipio
makeLabel(tabDatosPersonales, 'municipio', 'Municipio', indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
nextColumn('tabDatosPersonales')
municipios = ('Morelia', 'Patzcuaro', 'Tzintzuntzan')
makeComboBox(tabDatosPersonales, 'municipio', municipios, indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')
nextColumn('tabDatosPersonales')

# Boton ImprimirDatosPersonales
makeButton(tabDatosPersonales, 'imprimirDatosPersonales', 'Imprimir Datos', imprimirDatosPersonales, indexes['tabDatosPersonales']['row'], indexes['tabDatosPersonales']['column'])
wrap('tabDatosPersonales')

# Checkbuttons
makeLabel(datosExtras, 'pasatiempos', 'Pasatiempos', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'], 1, 5)
nextRow('tabDatosExtras')
makeCheckButton(datosExtras, 'Leer', 'Leer', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
nextColumn('tabDatosExtras')
makeCheckButton(datosExtras, 'Peliculas', 'Peliculas', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
nextColumn('tabDatosExtras')
makeCheckButton(datosExtras, 'RedesSociales', 'Redes Sociales', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
wrap('tabDatosExtras')

# RadioButtons
makeLabel(datosExtras, 'estado', 'Estado Civil', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'], 1, 5)
variableRadioButtons = tk.IntVar()
nextRow('tabDatosExtras')
makeRadioButtons(datosExtras, 'soltero', variableRadioButtons, 1, 'Soltero', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
nextColumn('tabDatosExtras')
makeRadioButtons(datosExtras, 'casado', variableRadioButtons, 2, 'Casado', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
nextColumn('tabDatosExtras')
makeRadioButtons(datosExtras, 'viudo', variableRadioButtons, 3, 'Viudo', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
wrap('tabDatosExtras')
radioButtons['soltero'].select()

# Objetivo de la vida
makeLabel(datosExtras, 'objetivo', 'Objetivo de la Vida', indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
makeScrolledText(datosExtras, fieldName = 'ObjetivoVida', row = indexes['tabDatosExtras']['row'], column = indexes['tabDatosExtras']['column'],width = 30, height = 3, wrap = tk.WORD)
scrollText['ObjetivoVida'].insert(1.0, '')
nextColumn('tabDatosExtras')
nextColumn('tabDatosExtras')

# Boton imprimir datos datosExtras
makeButton(datosExtras, 'imprimirExtras', 'Imprimir Datos', imprimirDatosExtras, indexes['tabDatosExtras']['row'], indexes['tabDatosExtras']['column'])
wrap('tabDatosExtras')

# Menu bar
barra_menu = Menu(window)
window.config(menu = barra_menu)

# Menu archivo
menuArchivo = Menu(barra_menu)
menuArchivo.add_command(label = 'Imprimir', command = printAll)
menuArchivo.add_separator()
menuArchivo.add_command(label = 'Salir', command = funcionSalir)
barra_menu.add_cascade(label = 'Sistema', menu = menuArchivo)

# Menu ayuda
menuAyuda = Menu(barra_menu, tearoff = 0)
menuAyuda.add_command(label = 'Acerca de', command = funcionCajaMensaje)
barra_menu.add_cascade(label = 'Ayuda', menu = menuAyuda)

window.mainloop()