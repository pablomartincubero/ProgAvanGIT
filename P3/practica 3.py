import re

class Time:

    #class attributes
    TIME_FORMATS = ("AM","PM","24 HOURS")
    time_count = 0

    def __init__(self):

        self.hours= 0    # Stores the hours
        self.minutes= 0    # Stores the minutes (0 to 59)
        self.seconds= 0     # Stores the seconds (0 to 59)
        self.format= None
        Time.time_count += 1


    def assign_format(self, pszFormat):

        pszFormat = pszFormat.upper()
        if pszFormat in Time.TIME_FORMATS:
            self.format = pszFormat
            return True
        return False


    def is_24hour_format(self):
    
        if self.format == "24 HOURS":
            return True
        else:
            return False


    def _is_valid_time(self):        

        if self.is_24hour_format() == True:
            return 0<=self.hours<=23 and 0<=self.minutes<=59 and 0<=self.seconds<=59
        else:
            return 0<=self.hours<=11 and 0<=self.minutes<=59 and 0<=self.seconds<=59


    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):

        if self.assign_format(pszFormato):

            self.hours = nHoras                   #Hours (1 to 12 AM/PM, 0 to 23 for 24 hours).
            self.minutes = nMinutos               #Minutes (0 to 59).
            self.seconds = nSegundos              #Seconds (0 to 59).
    
            if self._is_valid_time():
                return True
            else:
                print("Valores de tiempo no validos")
        else:
            print("Formato invalido")
        return False
        

    def get_time(self):
    
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"


    @classmethod
    def from_string(cls, time_string):
        pattern = r"(\d{2}):(\d{2}):(\d{2})\s?(AM|PM|24 HOURS)"
        match = re.match(pattern, time_string.upper())
        if match:
            hours, minutes, seconds, time_format = match.groups()
            hours, minutes, seconds = int(hours), int(minutes), int(seconds)
            new_time = cls()
            if new_time.set_time(hours, minutes, seconds, time_format):
                return new_time
        print("Invalid time string format.")
        return None



    @staticmethod
    def is_valid_format(time_format):
        if time_format.upper() in Time.TIME_FORMATS:
            return True
        else:
            return False    
        

    @classmethod
    def get_time_count(cls):
        return cls.time_count


def display_time(time_obj):
    if time_obj:
        print(f"El tiempo es: {time_obj.get_time()}")
    else:
       print("No tiene objeto en el display")


def main():
    current_time = None
  
    while True:
        print("\nMenú:")
        print("1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena (formato HH:MM:SS)")
        print("4. Terminar")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                nHoras = int(input("Introduce la hora: "))
                nMinutos = int(input("Introduce los minutos: "))
                nSegundos = int(input("Introduce los segundos: "))
                pszFormato = input("Introduce el formato de la hora(AM,PM,24 HOURS): ")
                if not Time.is_valid_format(pszFormato):
                    print("formato invalido")
                    continue
            
                current_time = Time()
                if not current_time.set_time(nHoras, nMinutos, nSegundos, pszFormato):
                    current_time = None
                else:
                    print("Hora registrada")
            except ValueError:
                print("Incorrecto. Por favor, introduzca un valor numerico.")
        
        elif opcion == '2':
            display_time(current_time)
        
        elif opcion == "3":
            time_str = input("Introduce el valor de la hora (formato HH:MM:SS): ")
            current_time = Time.from_string(time_str)
            if current_time:
                print("El tiempo ha sido creado.")
            else:
                print("Fallo al crear el tiempo.")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break   
        
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()