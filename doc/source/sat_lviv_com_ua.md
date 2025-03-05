# “Спецавтотранс - Львів” (САТ)

Підтримка календаря надається [Спецавтотранс - Львів](https://sat-lviv.com.ua/), що обслуговує Львівську область, Україна.

## Конфігурація через configuration.yaml

```yaml
waste_collection_schedule:
    sources:
    - name: sat_lviv_com_ua
      args:
        id: ID
```

### Конфігураційні змінні

**id**  
_(число) (обов’язково)_ : унікальний ідентифікатор вашої угоди 

## Приклад

```yaml
waste_collection_schedule:
    sources:
    - name: sat_lviv_com_ua
      args:
        id: 12345
        
```

## Як отримати свій ідентифікатор

Ідентифікатор - це номер угоди з кінцквим клієнтом.

## Стан рахунку

Стан рахунку ви можете перевірити за посиланням <https://sat-lviv.com.ua/stan-rakhunku?keyword={id}>
