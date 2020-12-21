import requests

pregunta = input("Titulo de la pelicula")

API_KEY="4ccc02fa"

url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

class PeticionError(Exception):
    pass

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == "False":
            raise PeticionError(datos["Error"])
        else: 
            return datos
    else: 
        raise "Error en consulta por id:" + respuesta.status_code)

repetir = "S"

while repetir == "S":
    pregunta = input("Titulo de la película: ")

    respuesta = peticion(url_template.format(API_KEY, 's', pregunta))
    if isinstance(respuesta, str):
        print(respuesta)
    else:
        primera_peli = respuesta['Search'][0]
        clave = primera_peli['imdbID']

        respuesta = peticion(url_template.format(API_KEY, 'i', clave))
        if isinstance(respuesta, str):
            print (respuesta)
        else: 
            titulo = respuesta['Title']
            agno = respuesta['Year']
            director = respuesta ['Director']
            print("La peli '{}', estrenada en el año {}, fue dirigida por {}".format(titulo, agno, director))

    repetir = input("Quiere otra peli? (S/N) ")
    repetir = repetir.upper()
