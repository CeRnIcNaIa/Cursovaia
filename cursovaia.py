import pyowm as pyowm

print("Введите город:")
city = input()
owm = pyowm.OWM('5bd97b5b31d6823422c7d512b7aff0f0')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

print('Меню:')
print('1. Прогноз погоды')
print('2. Влажность воздуха')
print('3. Осадки')
print('4. Ветер')
print('5. Вся информация')
cmd = input('Выберите пукнт меню: ')


class Main():
    def release(self):
        pass


class DatabaseHelper:
    database_connection = None
    data: str = ''

    def __new__(cls):
        if cls.database_connection is None:
            cls.database_connection: DatabaseHelper = object.__new__(cls)
        return cls.database_connection

    def select_data(self) -> str:
        return self.data

    def insert_data(self, new_data: str):
        self.data = new_data


class Scale():
    def get_temperature(self) -> float:
        pass


class Weather(Main):
    def release(self):
        print(f"Сегодня {c_weather.get_temperature()} °C")
        print(f"По Фаренгейту: {round(f_weather.get_temperature(), 2)} F")


class WeatherCelsius(Scale):
    def __init__(self, temperature: float):
        self.curent_temperature = temperature

    def get_temperature(self) -> float:
        return self.curent_temperature


class WeatherFarengeit:
    def __init__(self, temperature: float):
        self.curent_temperature = temperature

    def get_temperature(self) -> float:
        return self.curent_temperature


class AdapterWeatherFarengeit(Scale):
    def __init__(self, weather_farengeit: WeatherFarengeit):
        self.weather_farengeit = weather_farengeit

    def get_temperature(self) -> float:
        return ((self.weather_farengeit.get_temperature()) * 9 / 5 + 32)


class Air_humidity(Main):
    def release(self):
        print(f"Влажность воздуха {humidity} %")


class Precipitation(Main):
    def release(self):
        if precip == {}:
            print(f"Осадков нет ")
        else:
            print(f'Осадки: {precip}')


class Wind(Main):
    def release(self):
        if direction >= 350 or direction <= 10:
            print('Напрвление ветра: север')
        elif direction > 10 or direction < 80:
            print('Направление ветра: северо-восток')
        elif direction >= 80 or direction <= 100:
            print('Направление ветра: восток')
        elif direction > 100 or direction < 170:
            print('Направление ветра: юго-восток')
        elif direction >= 170 or direction <= 190:
            print('Направление ветра: юг')
        elif direction > 190 or direction < 260:
            print('Направление ветраЖ юго-запад')
        elif direction >= 260 or direction <= 280:
            print('Направление ветра: запад')
        else:
            print('Направление ветра: северо-запад')
        print(f"Скорость ветра: {speed} км/ч")


class Application:
    def create(self) -> Main:
        pass


class Weather_btn(Application):
    def create(self):
        return Weather()


class Air_humidity_btn(Application):
    def create(self):
        return Air_humidity()


class Precipitation_btn(Application):
    def create(self):
        return Precipitation()


class Wind_btn(Application):
    def create(self):
        return Wind()


class Client:
    def get(self):
        pass


class Database:
    def insert(self):
        print('История просмотра записана')

    def delete(self):
        print('История просмотра очищена')


class History:
    def __init__(self):
        self.client = Client()
        self.database = Database()

    def add_history(self):
        self.client.get()
        self.database.insert()

    def delete_history(self):
        self.database.delete()


class State():
    def __init__(self):
        self.weather: 'Weather' = None

    def next_state(self):
        pass

    def previous_state(self):
        pass


class WeatherState:
    def __init__(self, state: State):
        self.set_state(state)

    def set_state(self, state: State):
        self.state = state
        self.state.weather_state = self

    def next_state(self):
        self.state.next_state()

    def previous_state(self):
        self.state.previous_state()


class MinTemperature(State):
    def next_state(self):
        print(f'Из {min} °C в {max} °C')
        self.weather_state.set_state(MaxTemperature())

    def previous_state(self):
        print('min')


class MaxTemperature(State):
    def next_state(self):
        print('max')

    def previous_state(self):
        print(f'Из {max} °C в {min} °C')
        self.weather_state.set_state(MinTemperature())


class Reader():
    def parse(self, url: str):
        pass


class ResourceReader:
    def __init__(self, reader: Reader):
        self.reader = reader

    def set_srategy(self, reader: Reader):
        self.reader = reader

    def read(self, url: str):
        self.reader.parse(url)


class SiteReader(Reader):
    def parse(self, url: str):
        print('ИНформация взята с сайта:', url)


if __name__ == "__main__":
    connection1 = DatabaseHelper()
    connection1.insert_data('')

    connection2 = DatabaseHelper()
    print(connection2.select_data())

    if cmd == '1':
        temp = w.temperature('celsius')['temp']
        c: float = temp
        f: float = temp
        c_weather = WeatherCelsius(c)
        f_weather = AdapterWeatherFarengeit(WeatherFarengeit(f))
        creator = Weather_btn()
        weather = creator.create()

        weather.release()

        weather_state = WeatherState(MinTemperature())

        min = w.temperature('celsius')['temp_min']
        max = w.temperature('celsius')['temp_max']
        weather_state.next_state()
        weather_state.previous_state()

    if cmd == '2':
        humidity = w.humidity
        creator = Air_humidity_btn()
        air_humidity = creator.create()

        air_humidity.release()

    if cmd == '3':
        precip = w.rain
        creator = Precipitation_btn()
        precipitation = creator.create()

        precipitation.release()

    if cmd == '4':
        direction = w.wind()['deg']
        speed = w.wind()['speed']
        creator = Wind_btn()
        wind = creator.create()

        wind.release()

    if cmd == '5':
        temp = w.temperature('celsius')['temp']
        c: float = temp
        f: float = temp
        c_weather = WeatherCelsius(c)
        f_weather = AdapterWeatherFarengeit(WeatherFarengeit(f))
        creator = Weather_btn()
        weather = creator.create()

        weather.release()

        weather_state = WeatherState(MinTemperature())

        min = w.temperature('celsius')['temp_min']
        max = w.temperature('celsius')['temp_max']
        weather_state.next_state()
        weather_state.previous_state()

        humidity = w.humidity
        creator = Air_humidity_btn()
        air_humidity = creator.create()

        air_humidity.release()

        precip = w.rain
        creator = Precipitation_btn()
        precipitation = creator.create()

        precipitation.release()

        direction = w.wind()['deg']
        speed = w.wind()['speed']
        creator = Wind_btn()
        wind = creator.create()

        wind.release()

    resource_reader = ResourceReader(SiteReader())

    url = 'https://openweathermap.org'
    resource_reader.read(url)
