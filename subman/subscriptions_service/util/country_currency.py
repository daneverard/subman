from django.db import models

class CountryChoices(models.TextChoices):
    UNITED_STATES = "United States"
    CANADA = "Canada"
    UNITED_KINGDOM = "United Kingdom"
    JAPAN = "Japan"
    AUSTRALIA = "Australia"
    SWITZERLAND = "Switzerland"
    CHINA = "China"
    INDIA = "India"
    BRAZIL = "Brazil"
    RUSSIA = "Russia"
    SOUTH_AFRICA = "South Africa"
    MEXICO = "Mexico"
    SWEDEN = "Sweden"
    NORWAY = "Norway"
    DENMARK = "Denmark"
    SINGAPORE = "Singapore"
    HONG_KONG = "Hong Kong"
    NEW_ZEALAND = "New Zealand"
    SOUTH_KOREA = "South Korea"
    SAUDI_ARABIA = "Saudi Arabia"
    TURKEY = "Turkey"
    ARGENTINA = "Argentina"
    NIGERIA = "Nigeria"
    ISRAEL = "Israel"
    UAE = "United Arab Emirates"
    THAILAND = "Thailand"
    
    # Eurozone countries
    AUSTRIA = "Austria"
    BELGIUM = "Belgium"
    CYPRUS = "Cyprus"
    ESTONIA = "Estonia"
    FINLAND = "Finland"
    FRANCE = "France"
    GERMANY = "Germany"
    GREECE = "Greece"
    IRELAND = "Ireland"
    ITALY = "Italy"
    LATVIA = "Latvia"
    LITHUANIA = "Lithuania"
    LUXEMBOURG = "Luxembourg"
    MALTA = "Malta"
    NETHERLANDS = "Netherlands"
    PORTUGAL = "Portugal"
    SLOVAKIA = "Slovakia"
    SLOVENIA = "Slovenia"
    SPAIN = "Spain"


class CurrencyChoices(models.TextChoices):
    USD = "USD", "US Dollar"
    CAD = "CAD", "Canadian Dollar"
    GBP = "GBP", "Pound Sterling"
    JPY = "JPY", "Yen"
    AUD = "AUD", "Australian Dollar"
    CHF = "CHF", "Swiss Franc"
    CNY = "CNY", "Yuan Renminbi"
    INR = "INR", "Rupee"
    BRL = "BRL", "Real"
    RUB = "RUB", "Ruble"
    ZAR = "ZAR", "Rand"
    MXN = "MXN", "Peso"
    SEK = "SEK", "Swedish Krona"
    NOK = "NOK", "Norwegian Krone"
    DKK = "DKK", "Danish Krone"
    SGD = "SGD", "Singapore Dollar"
    HKD = "HKD", "Hong Kong Dollar"
    NZD = "NZD", "New Zealand Dollar"
    KRW = "KRW", "Won"
    SAR = "SAR", "Riyal"
    TRY = "TRY", "Lira"
    ARS = "ARS", "Peso"
    NGN = "NGN", "Naira"
    ILS = "ILS", "Shekel"
    AED = "AED", "Dirham"
    THB = "THB", "Baht"
    
    # Euro for Eurozone countries
    EUR = "EUR", "Euro"


# Dictionary to map countries to their default currencies
country_to_currency = {
    CountryChoices.UNITED_STATES: CurrencyChoices.USD,
    CountryChoices.CANADA: CurrencyChoices.CAD,
    CountryChoices.UNITED_KINGDOM: CurrencyChoices.GBP,
    CountryChoices.JAPAN: CurrencyChoices.JPY,
    CountryChoices.AUSTRALIA: CurrencyChoices.AUD,
    CountryChoices.SWITZERLAND: CurrencyChoices.CHF,
    CountryChoices.CHINA: CurrencyChoices.CNY,
    CountryChoices.INDIA: CurrencyChoices.INR,
    CountryChoices.BRAZIL: CurrencyChoices.BRL,
    CountryChoices.RUSSIA: CurrencyChoices.RUB,
    CountryChoices.SOUTH_AFRICA: CurrencyChoices.ZAR,
    CountryChoices.MEXICO: CurrencyChoices.MXN,
    CountryChoices.SWEDEN: CurrencyChoices.SEK,
    CountryChoices.NORWAY: CurrencyChoices.NOK,
    CountryChoices.DENMARK: CurrencyChoices.DKK,
    CountryChoices.SINGAPORE: CurrencyChoices.SGD,
    CountryChoices.HONG_KONG: CurrencyChoices.HKD,
    CountryChoices.NEW_ZEALAND: CurrencyChoices.NZD,
    CountryChoices.SOUTH_KOREA: CurrencyChoices.KRW,
    CountryChoices.SAUDI_ARABIA: CurrencyChoices.SAR,
    CountryChoices.TURKEY: CurrencyChoices.TRY,
    CountryChoices.ARGENTINA: CurrencyChoices.ARS,
    CountryChoices.NIGERIA: CurrencyChoices.NGN,
    CountryChoices.ISRAEL: CurrencyChoices.ILS,
    CountryChoices.UAE: CurrencyChoices.AED,
    CountryChoices.THAILAND: CurrencyChoices.THB,
    
    # Eurozone countries using EUR
    CountryChoices.AUSTRIA: CurrencyChoices.EUR,
    CountryChoices.BELGIUM: CurrencyChoices.EUR,
    CountryChoices.CYPRUS: CurrencyChoices.EUR,
    CountryChoices.ESTONIA: CurrencyChoices.EUR,
    CountryChoices.FINLAND: CurrencyChoices.EUR,
    CountryChoices.FRANCE: CurrencyChoices.EUR,
    CountryChoices.GERMANY: CurrencyChoices.EUR,
    CountryChoices.GREECE: CurrencyChoices.EUR,
    CountryChoices.IRELAND: CurrencyChoices.EUR,
    CountryChoices.ITALY: CurrencyChoices.EUR,
    CountryChoices.LATVIA: CurrencyChoices.EUR,
    CountryChoices.LITHUANIA: CurrencyChoices.EUR,
    CountryChoices.LUXEMBOURG: CurrencyChoices.EUR,
    CountryChoices.MALTA: CurrencyChoices.EUR,
    CountryChoices.NETHERLANDS: CurrencyChoices.EUR,
    CountryChoices.PORTUGAL: CurrencyChoices.EUR,
    CountryChoices.SLOVAKIA: CurrencyChoices.EUR,
    CountryChoices.SLOVENIA: CurrencyChoices.EUR,
    CountryChoices.SPAIN: CurrencyChoices.EUR,
}