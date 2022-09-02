from covids.models import Covid, Genre
import csv 
def run():
    with open('covids/green.csv',encoding='utf-8' ) as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Covid.objects.all().delete()
        Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre, _ = Genre.objects.get_or_create(name=row[1])

            covid = Covid(title=row[0],
                        troubled=row[2],
                        level=row[3],
                        genre=genre)
            covid.save()