class Vehiculo:
    
    def _init_(self,placa,marca,modelo,kilometraje):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
        
    #los cuatro atributos generales
    def getPlaca (self):
        return self.placa
    def getMarca (self):
        return self.marca
    def getModelo (self):
        return self.modelo
    def getKilometraje (self):
        return self.kilometraje
    
    #metodo
    def mostrarVehiculo(self):
        print ("\nPlaca: "+self.getPlaca()+"\nMarca: " +self.getMarca()+"\nModelo: "+self.getModelo()+"\nKilometraje: "+str(self.getKilometraje()))

placa = raw_input ("Ingresa la placa: ")
marca = raw_input ("Ingresa la marca: ")
modelo = raw_input ("Ingresa el modelo: ")
kilometraje = input ("Ingresa el kilometraje: ")
v = Vehiculo(placa,marca,modelo,kilometraje)
v.mostrarVehiculo()


