# Generated by Django 4.2.4 on 2024-04-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0012_alter_car_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="year",
            field=models.IntegerField(
                choices=[
                    (2005, 2005),
                    (2006, 2006),
                    (2007, 2007),
                    (2008, 2008),
                    (2009, 2009),
                    (2010, 2010),
                    (2011, 2011),
                    (2012, 2012),
                    (2013, 2013),
                    (2014, 2014),
                    (2015, 2015),
                    (2016, 2016),
                    (2017, 2017),
                    (2018, 2018),
                    (2019, 2019),
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                    (2024, 2024),
                ]
            ),
        ),
    ]
