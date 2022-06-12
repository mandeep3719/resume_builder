from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cv_images')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name-Surname')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('telephone', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('career_summary', models.TextField(blank=True, verbose_name='Career Summary')),
                ('linkedin', models.CharField(blank=True, max_length=255)),
                ('github', models.CharField(blank=True, max_length=255)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('code', models.CharField(blank=True, default='', max_length=8, unique=True)),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=38)),
                ('order', models.IntegerField(default=100000)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='cvbuilder.resume')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvbuilder.template'),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=100000)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='cvbuilder.resume')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=100000)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='cvbuilder.resume')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True)),
                ('tech', models.TextField(blank=True)),
                ('order', models.IntegerField(default=100000)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='cvbuilder.resume')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, verbose_name='Department')),
                ('duration', models.CharField(max_length=255)),
                ('order', models.IntegerField(default=100000)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='cvbuilder.resume')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('order', models.IntegerField(default=100000)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='cvbuilder.resume')),
            ],
            options={
                'verbose_name': 'Achievement',
                'verbose_name_plural': 'Achievements',
            },
        ),
    ]
