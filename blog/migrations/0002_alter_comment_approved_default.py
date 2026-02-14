from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="approved",
            field=models.BooleanField(default=False),
        ),
    ]
