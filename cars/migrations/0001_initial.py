# Generated by Django 4.1.7 on 2023-03-05 06:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cars",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_title", models.CharField(max_length=150)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("BA", "Baringo"),
                            ("BO", "Bomet"),
                            ("BN", "Bungoma"),
                            ("BS", "Busia"),
                            ("EL", "Elgeyo marakwet"),
                            ("EM", "Embu"),
                            ("GA", "Garissa"),
                            ("HO", "Homabay"),
                            ("IS", "Isiolo"),
                            ("KA", "Kajiado"),
                            ("KK", "Kakamega"),
                            ("KE", "Kericho"),
                            ("KI", "Kiambu"),
                            ("KL", "Kilifi"),
                            ("KR", "Kirinyaga"),
                            ("KS", "Kisii"),
                            ("KU", "Kisumu"),
                            ("KT", "Kitui"),
                            ("KW", "Kwale"),
                            ("LA", "Laikipia"),
                            ("LM", "Lamu"),
                            ("MA", "Machakos"),
                            ("MK", "Makueni"),
                            ("MN", "Mandera"),
                            ("ME", "Meru"),
                            ("MI", "Migori"),
                            ("MR", "Marsabit"),
                            ("MO", "Mombasa"),
                            ("MU", "Muranga"),
                            ("NA", "Nairobi"),
                            ("NK", "Nakuru"),
                            ("NN", "Nandi"),
                            ("NR", "Narok"),
                            ("NY", "Nyamira"),
                            ("ND", "Nyandarua"),
                            ("NE", "Nyeri"),
                            ("SA", "Samburu"),
                            ("SI", "Siaya"),
                            ("TA", "Taita Taveta"),
                            ("TN", "Tana River"),
                            ("TH", "Tharaka Nithi"),
                            ("TR", "Tra Nzoia"),
                            ("TU", "Turkana"),
                            ("UA", "Uasin Gishu"),
                            ("VI", "Vihiga"),
                            ("WA", "Wajir"),
                            ("WE", "West Pokot"),
                        ],
                        max_length=80,
                    ),
                ),
                ("city", models.CharField(max_length=30)),
                ("color", models.CharField(max_length=150)),
                ("model", models.CharField(max_length=150)),
                (
                    "year",
                    models.IntegerField(
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
                        ],
                        verbose_name="year",
                    ),
                ),
                ("condition", models.CharField(max_length=150)),
                ("price", models.IntegerField()),
                ("description", models.TextField(max_length=600)),
                ("car_image", models.ImageField(upload_to="images/%Y/%m/%d/")),
                (
                    "car_image_1",
                    models.ImageField(blank=True, upload_to="images/%Y/%m/%d/"),
                ),
                (
                    "car_image_2",
                    models.ImageField(blank=True, upload_to="images/%Y/%m/%d/"),
                ),
                (
                    "car_image_3",
                    models.ImageField(blank=True, upload_to="images/%Y/%m/%d/"),
                ),
                (
                    "car_image_4",
                    models.ImageField(blank=True, upload_to="images/%Y/%m/%d/"),
                ),
                (
                    "feature",
                    models.CharField(
                        choices=[
                            ("Cruise Control", "Cruise Control"),
                            ("Audio Interface", "Audio Interface"),
                            ("Airbags", "Airbags"),
                            ("Air Conditioning", "Air Conditioning"),
                            ("Seat Heating", "Seat Heating"),
                            ("Alarm System", "Alarm System"),
                            ("ParkAssist", "ParkAssist"),
                            ("Power Steering", "Power Steering"),
                            ("Reversing Camera", "Reversing Camera"),
                            ("Direct Fuel Injection", "Direct Fuel Injection"),
                            ("Auto Start/Stop", "Auto Start/Stop"),
                            ("Wind Deflector", "Wind Deflector"),
                            ("Bluetooth Handset", "Bluetooth Handset"),
                        ],
                        max_length=80,
                    ),
                ),
                ("body_style", models.CharField(max_length=90)),
                ("engine", models.CharField(max_length=80)),
                ("transmission", models.CharField(max_length=150)),
                ("interior", models.CharField(max_length=150)),
                ("miles", models.IntegerField()),
                (
                    "doors",
                    models.CharField(
                        choices=[
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                        ],
                        max_length=150,
                    ),
                ),
                ("passengers", models.IntegerField()),
                ("vin_no", models.CharField(max_length=75)),
                ("milage", models.IntegerField()),
                ("fuel_type", models.CharField(max_length=150)),
                ("no_of_owners", models.CharField(max_length=150)),
                ("is_featured", models.BooleanField(max_length=150)),
                (
                    "created_date",
                    models.DateField(blank=True, default=datetime.datetime),
                ),
            ],
        ),
    ]
