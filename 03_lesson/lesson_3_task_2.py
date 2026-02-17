from smartphone import Smartphone

catalog = [
    Smartphone('Nokia', '2110', '+79869951213'),
    Smartphone('Honor', 'X7d', '+79159164848'),
    Smartphone('Samsung Galaxy', "A52", '+79991593663'),
    Smartphone('HUAWEI Mate', 'X7', '+79831437993'),
    Smartphone('iPhone', '15 mini', '+79771775797')
]

for smartphone in catalog:
    print(f'{smartphone.mark} - {smartphone.model}. {smartphone.number}')
