Cree un programa donde existe un laberinto con una salida donde eres un raton que puedes controlar hacia donde se mueve y hay un gato que intenta atraparte, el raton debe llegar a la salida sin ser atrapado por el raton para ganar, si el gato te alcanza pierdes.

Un problema que estaba teniendo es que el gato no colisionaba con el raton para atraparlo y era por mi funcion de verificar hacia donde puede moverse un personaje, yo usaba solo un tablero unico para todo pero el lugar en donde se encontraba el raton lo consideraba como un muro y no lo consideraba una ruta viable, lo solucione realizando una copia de la estructura del laberinto solo con los caminos y muros.

