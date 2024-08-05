class Country:
    def __init__(self, name: str, population: int, measure: int):
        self.name = name
        self.population = population
        self.measure = measure

    def is_big(self) -> bool:
        return self.population > 20000000 or self.measure > 3000000

    def compare(self, next_country) -> str:
        self_density = self.population / self.measure
        next_density = next_country.population / next_country.measure

        if self_density > next_density:
            result = "larger"
        elif self_density < next_density:
            result = "smaller"
        else:
            result = "same"
        return f"{self.name} has {result} density than {next_country.name}"

country_1 = Country("Australia", 23545500, 7692024)
country_2 = Country("Andorra", 76098, 468)

print(f"Is {country_1.name} big? {country_1.is_big()}")
print(f"Is {country_2.name} big? {country_2.is_big()}")

print(country_1.compare(country_2))