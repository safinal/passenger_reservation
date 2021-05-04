# Generated by Django 3.2.1 on 2021-05-04 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Railway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(choices=[('Tehran', 'Tehran'), ('Mashhad', 'Mashhad'), ('Eşfahān', 'Eşfahān'), ('Karaj', 'Karaj'), ('Tabrīz', 'Tabrīz'), ('Shīrāz', 'Shīrāz'), ('Qom', 'Qom'), ('Ahvāz', 'Ahvāz'), ('Kermānshāh', 'Kermānshāh'), ('Orūmīyeh', 'Orūmīyeh'), ('Rasht', 'Rasht'), ('Kermān', 'Kermān'), ('Zāhedān', 'Zāhedān'), ('Eslāmshahr', 'Eslāmshahr'), ('Hamadān', 'Hamadān'), ('Yazd', 'Yazd'), ('Arāk', 'Arāk'), ('Ardabīl', 'Ardabīl'), ('Bandar ‘Abbās', 'Bandar ‘Abbās'), ('Zanjān', 'Zanjān'), ('Kāshān', 'Kāshān'), ('Qazvīn', 'Qazvīn'), ('Sanandaj', 'Sanandaj'), ('Khorramābād', 'Khorramābād'), ('Sārī', 'Sārī'), ('Gorgān', 'Gorgān'), ('Shahrīār', 'Shahrīār'), ('Shahr-e Qods', 'Shahr-e Qods'), ('Malārd', 'Malārd'), ('Sartā', 'Sartā'), ('Dezfūl', 'Dezfūl'), ('Bābol', 'Bābol'), ('Būkān', 'Būkān'), ('Sabzevār', 'Sabzevār'), ('Āmol', 'Āmol'), ('Pākdasht', 'Pākdasht'), ('Najafābād', 'Najafābād'), ('Borūjerd', 'Borūjerd'), ('Madan', 'Madan'), ('Qarchak', 'Qarchak'), ('Varāmīn', 'Varāmīn'), ('Neyshābūr', 'Neyshābūr'), ('Sāveh', 'Sāveh'), ('Khomeynī Shahr', 'Khomeynī Shahr'), ('Qā’em Shahr', 'Qā’em Shahr'), ('Nasīm Shahr', 'Nasīm Shahr'), ('Bojnūrd', 'Bojnūrd'), ('Bandar-e Būshehr', 'Bandar-e Būshehr'), ('Khowy', 'Khowy'), ('Fardīs', 'Fardīs'), ('Bīrjand', 'Bīrjand'), ('Marāgheh', 'Marāgheh'), ('Sīrjān', 'Sīrjān'), ('Shāhīn Shahr', 'Shāhīn Shahr'), ('Malāyer', 'Malāyer'), ('Saqqez', 'Saqqez'), ('Bandar-e Māhshahr', 'Bandar-e Māhshahr'), ('Mahābād', 'Mahābād'), ('Rafsanjān', 'Rafsanjān'), ('Shahr-e Kord', 'Shahr-e Kord'), ('Semnān', 'Semnān'), ('Golmeh', 'Golmeh'), ('Gonbad-e Kāvūs', 'Gonbad-e Kāvūs'), ('Shāhrūd', 'Shāhrūd'), ('Marvdasht', 'Marvdasht'), ('Qūchān', 'Qūchān'), ('Jahrom', 'Jahrom'), ('Kamālshahr', 'Kamālshahr'), ('Torbat-e Ḩeydarīyeh', 'Torbat-e Ḩeydarīyeh'), ('Pīrānshahr', 'Pīrānshahr'), ('Marīvān', 'Marīvān'), ('Andīmeshk', 'Andīmeshk'), ('Shahreẕā', 'Shahreẕā'), ('Zābol', 'Zābol'), ('Khorramshahr', 'Khorramshahr'), ('Marand', 'Marand'), ('Jīroft', 'Jīroft'), ('Bam', 'Bam'), ('Behbahān', 'Behbahān'), ('Dorūd', 'Dorūd'), ('Naz̧arābād', 'Naz̧arābād'), ('Moḩammad Shahr', 'Moḩammad Shahr'), ('Īrānshahr', 'Īrānshahr'), ('Fasā', 'Fasā'), ('Borāzjān', 'Borāzjān'), ('Bāneh', 'Bāneh'), ('Yāsūj', 'Yāsūj'), ('Chābahār', 'Chābahār'), ('Robāţ Karīm', 'Robāţ Karīm'), ('Khāk-e ‘Alī', 'Khāk-e ‘Alī'), ('Kāshmar', 'Kāshmar'), ('Shūshtar', 'Shūshtar'), ('Ahar', 'Ahar'), ('Masjed Soleymān', 'Masjed Soleymān'), ('Torbat-e Jām', 'Torbat-e Jām'), ('Kāzerūn', 'Kāzerūn'), ('Shīrvān', 'Shīrvān'), ('Salmās', 'Salmās'), ('Alīgūdarz', 'Alīgūdarz'), ('Bonāb', 'Bonāb'), ('Tākestān', 'Tākestān'), ('Oshnavīyeh', 'Oshnavīyeh'), ('Bandar-e Genāveh', 'Bandar-e Genāveh'), ('Zarand', 'Zarand'), ('Mobārakeh', 'Mobārakeh'), ('Dāmghān', 'Dāmghān'), ('Tāybād', 'Tāybād'), ('Zarrīn Shahr', 'Zarrīn Shahr'), ('Ārān Bīdgol', 'Ārān Bīdgol'), ('Hashtpar', 'Hashtpar'), ('Bījār', 'Bījār'), ('Sardasht', 'Sardasht'), ('Rāmhormoz', 'Rāmhormoz'), ('Golpāyegān', 'Golpāyegān'), ('Aznā', 'Aznā'), ('Naţanz', 'Naţanz'), ('Takāb', 'Takāb'), ('Darcheh', 'Darcheh'), ('Sarāb', 'Sarāb'), ('Bāft', 'Bāft'), ('Khalkhāl', 'Khalkhāl'), ('Falāvarjān', 'Falāvarjān'), ('Sarpol-e Z̄ahāb', 'Sarpol-e Z̄ahāb'), ('Shāhīn Dezh', 'Shāhīn Dezh'), ('Qahderījān', 'Qahderījān'), ('Hādīshahr', 'Hādīshahr'), ('Fūman', 'Fūman'), ('Semīrom', 'Semīrom'), ('Sheybān', 'Sheybān'), ('Kelīshād va Sūdarjān', 'Kelīshād va Sūdarjān'), ('Goldasht', 'Goldasht'), ('Khvānsār', 'Khvānsār'), ('Gaz', 'Gaz'), ('Khowrzūq', 'Khowrzūq'), ('Maḩmūdābād Nemūneh', 'Maḩmūdābād Nemūneh'), ('Kabūdarāhang', 'Kabūdarāhang'), ('Taft', 'Taft'), ('Dehāqān', 'Dehāqān'), ('Tīrān', 'Tīrān'), ('Amlash', 'Amlash'), ('Ardestān', 'Ardestān'), ('Fāmenīn', 'Fāmenīn'), ('Fereydūnshahr', 'Fereydūnshahr'), ('Reẕvānshahr', 'Reẕvānshahr'), ('Ahram', 'Ahram'), ('Poldasht', 'Poldasht'), ('Qaşr-e Shīrīn', 'Qaşr-e Shīrīn'), ('Komījān', 'Komījān'), ('Chādegān', 'Chādegān'), ('Khūr', 'Khūr'), ('Chelgard', 'Chelgard'), ('Esfarāyen', 'Esfarāyen'), ('Khondāb', 'Khondāb'), ('Īlām', 'Īlām'), ('Eshtehārd', 'Eshtehārd'), ('Alvand', 'Alvand'), ('Fereydūn Kenār', 'Fereydūn Kenār'), ('Bandar-e Anzalī', 'Bandar-e Anzalī'), ('Lāhījān', 'Lāhījān'), ('Maḩmūdābād', 'Maḩmūdābād'), ('Bābolsar', 'Bābolsar'), ('Bandar-e Torkaman', 'Bandar-e Torkaman'), ('Langarūd', 'Langarūd'), ('Jūybār', 'Jūybār'), ('Āstāneh-ye Ashrafīyeh', 'Āstāneh-ye Ashrafīyeh'), ('Kangān', 'Kangān'), ('Bandar-e ‘Asalūyeh', 'Bandar-e ‘Asalūyeh'), ('Āstārā', 'Āstārā'), ('Şowme‘eh Sarā', 'Şowme‘eh Sarā'), ('Bandar-e Gaz', 'Bandar-e Gaz'), ('Hashtgerd', 'Hashtgerd'), ('Fārsān', 'Fārsān'), ('‘Ajab Shīr', '‘Ajab Shīr'), ('Khorramdarreh', 'Khorramdarreh'), ('Pīshvā', 'Pīshvā'), ('Rey', 'Rey'), ('Pārsābād', 'Pārsābād'), ('Mīāndoāb', 'Mīāndoāb'), ('Narmāshīr', 'Narmāshīr'), ('Māsāl', 'Māsāl'), ('‘Alīābād-e Katūl', '‘Alīābād-e Katūl'), ('Malekān', 'Malekān'), ('‘Abbāsābād', '‘Abbāsābād'), ('Ābādān', 'Ābādān'), ('Nahāvand', 'Nahāvand'), ('Naqadeh', 'Naqadeh'), ('Behshahr', 'Behshahr'), ('Āzādshahr', 'Āzādshahr'), ('Javānrūd', 'Javānrūd'), ('Rāmīān', 'Rāmīān'), ('Zehak', 'Zehak'), ('Rūdsar', 'Rūdsar'), ('Galūgāh', 'Galūgāh'), ('Bahār', 'Bahār'), ('Rāmsar', 'Rāmsar'), ('Asadābād', 'Asadābād'), ('Shaft', 'Shaft'), ('Nekā', 'Nekā'), ('Kord Kūy', 'Kord Kūy'), ('Nowshahr', 'Nowshahr'), ('Harsīn', 'Harsīn'), ('Gālīkesh', 'Gālīkesh'), ('Kavār', 'Kavār'), ('Chālūs', 'Chālūs'), ('Āq Qalā', 'Āq Qalā'), ('Tonekābon', 'Tonekābon'), ('Oskū', 'Oskū'), ('Qeshm', 'Qeshm'), ('Eslāmābād-e Gharb', 'Eslāmābād-e Gharb'), ('Pāveh', 'Pāveh'), ('Meybod', 'Meybod'), ('Dūst Moḩammad Khān', 'Dūst Moḩammad Khān'), ('Mīnūdasht', 'Mīnūdasht'), ('Tūyserkān', 'Tūyserkān'), ('Mollās̄ānī', 'Mollās̄ānī'), ('Namīn', 'Namīn'), ('Ābyek', 'Ābyek'), ('Lordegān', 'Lordegān'), ('Abhar', 'Abhar'), ('Showţ', 'Showţ'), ('Ţorqabeh', 'Ţorqabeh'), ('Dowlatābād', 'Dowlatābād'), ('Shūsh', 'Shūsh'), ('Kūhdasht', 'Kūhdasht'), ('Damāvand', 'Damāvand'), ('Eyvān', 'Eyvān'), ('Nūrābād', 'Nūrābād'), ('Āz̄arshahr', 'Āz̄arshahr'), ('Şaḩneh', 'Şaḩneh'), ('Kāmyārān', 'Kāmyārān'), ('Shahrak-e Bākharz', 'Shahrak-e Bākharz'), ('Bāgh-e Malek', 'Bāgh-e Malek'), ('Sīāhkal', 'Sīāhkal'), ('Shabestar', 'Shabestar'), ('Borūjen', 'Borūjen'), ('Kahnūj', 'Kahnūj'), ('Jam', 'Jam'), ('Kherāmeh', 'Kherāmeh'), ('Shādegān', 'Shādegān'), ('Aleshtar', 'Aleshtar'), ('Razan', 'Razan'), ('Maşīrī', 'Maşīrī'), ('Sar‘eyn', 'Sar‘eyn'), ('Kalāleh', 'Kalāleh'), ('Qarah Ẕīā’ od Dīn', 'Qarah Ẕīā’ od Dīn'), ('Shāzand', 'Shāzand'), ('Sarvābād', 'Sarvābād'), ('Khomeyn', 'Khomeyn'), ('Mīnāb', 'Mīnāb'), ('Darreh Shahr', 'Darreh Shahr'), ('Chenārān', 'Chenārān'), ('Nūr', 'Nūr'), ('Sūsangerd', 'Sūsangerd'), ('Rūdān', 'Rūdān'), ('Gomīshān', 'Gomīshān'), ('Omīdīyeh', 'Omīdīyeh'), ('Tajrīsh', 'Tajrīsh'), ('Shalamzār', 'Shalamzār'), ('Dehdasht', 'Dehdasht'), ('Germī', 'Germī'), ('Pā’īn-e Bāzār-e Rūdbār', 'Pā’īn-e Bāzār-e Rūdbār'), ('Ravānsar', 'Ravānsar'), ('Dārān', 'Dārān'), ('Meshgīn Shahr', 'Meshgīn Shahr'), ('Sonqor', 'Sonqor'), ('Bīleh Savār', 'Bīleh Savār'), ('Mohr', 'Mohr'), ('Jolfā', 'Jolfā'), ('Qorveh', 'Qorveh'), ('Estahbān', 'Estahbān'), ('Dehgolān', 'Dehgolān'), ('Do Gonbadān', 'Do Gonbadān'), ('Fīrūzābād', 'Fīrūzābād'), ('Bostānābād', 'Bostānābād'), ('Neqāb', 'Neqāb'), ('Fārūj', 'Fārūj'), ('Khalīlābād', 'Khalīlābād'), ('Mīāneh', 'Mīāneh'), ('Sarābleh', 'Sarābleh'), ('Sīsakht', 'Sīsakht'), ('Sepīdān', 'Sepīdān'), ('Arsanjān', 'Arsanjān'), ('Sūrak', 'Sūrak'), ('Sarāb-e Dūreh', 'Sarāb-e Dūreh'), ('Joghtāy', 'Joghtāy'), ('Farīmān', 'Farīmān'), ('Bū’īn Zahrā', 'Bū’īn Zahrā'), ('Dārāb', 'Dārāb'), ('Farmahīn', 'Farmahīn'), ('Rāmshīr', 'Rāmshīr'), ('Pol-e Sefīd', 'Pol-e Sefīd'), ('Herīs', 'Herīs'), ('Maḩallāt', 'Maḩallāt'), ('Gāvbandī', 'Gāvbandī'), ('Ţāleqān', 'Ţāleqān'), ('Bozghān', 'Bozghān'), ('Līkak', 'Līkak'), ('Gīlān-e Gharb', 'Gīlān-e Gharb'), ('Lālī', 'Lālī'), ('Mākū', 'Mākū'), ('Sarvestān', 'Sarvestān'), ('Charām', 'Charām'), ('Dowlatābād', 'Dowlatābād'), ('Hashtrūd', 'Hashtrūd'), ('Deyr', 'Deyr'), ('Seyah Cheshmeh', 'Seyah Cheshmeh'), ('Delījān', 'Delījān'), ('Tāzehābād', 'Tāzehābād'), ('Khomārlū', 'Khomārlū'), ('Ardal', 'Ardal'), ('Ābbar', 'Ābbar'), ('Mahdīshahr', 'Mahdīshahr'), ('Qal‘eh-ye Khvājeh', 'Qal‘eh-ye Khvājeh'), ('Rābor', 'Rābor'), ('Lāmerd', 'Lāmerd'), ('Zarrīnābād', 'Zarrīnābād'), ('Dīvāndarreh', 'Dīvāndarreh'), ('Şafāshahr', 'Şafāshahr'), ('Sīrīk', 'Sīrīk'), ('Kerend-e Gharb', 'Kerend-e Gharb'), ('Nīr', 'Nīr'), ('Marāveh Tappeh', 'Marāveh Tappeh'), ('Bandar-e Lengeh', 'Bandar-e Lengeh'), ('Bāsht', 'Bāsht'), ('Eslāmābād', 'Eslāmābād'), ('Ābdānān', 'Ābdānān'), ('Poldokhtar', 'Poldokhtar'), ('Bandar-e Deylam', 'Bandar-e Deylam'), ('Dargaz', 'Dargaz'), ('Gīvī', 'Gīvī'), ('Sa‘ādat Shahr', 'Sa‘ādat Shahr'), ('Qīr', 'Qīr'), ('Varazqān', 'Varazqān'), ('Fahraj', 'Fahraj'), ('Āshkhāneh', 'Āshkhāneh'), ('Solţānābād', 'Solţānābād'), ('Ābādeh', 'Ābādeh'), ('Sarakhs', 'Sarakhs'), ('Feyẕābād', 'Feyẕābād'), ('Bastak', 'Bastak'), ('Ḩājjīābād', 'Ḩājjīābād'), ('Haftkel', 'Haftkel'), ('Khowrmūj', 'Khowrmūj'), ('Fīrūzkūh', 'Fīrūzkūh'), ('Gerāsh', 'Gerāsh'), ('Shahr-e Qadīm-e Lār', 'Shahr-e Qadīm-e Lār'), ('Nūrābād', 'Nūrābād'), ('Rāsak', 'Rāsak'), ('Fāryāb', 'Fāryāb'), ('Hoveyzeh', 'Hoveyzeh'), ('‘Anbarābād', '‘Anbarābād'), ('Roshtkhvār', 'Roshtkhvār'), ('Anār', 'Anār'), ('Manūjān', 'Manūjān'), ('Bandar-e Khamīr', 'Bandar-e Khamīr'), ('Arakvāz-e Malekshāhī', 'Arakvāz-e Malekshāhī'), ('Kaleybar', 'Kaleybar'), ('Arzū’īyeh', 'Arzū’īyeh'), ('Khvāf', 'Khvāf'), ('Māmūnīyeh', 'Māmūnīyeh'), ('Māhneshān', 'Māhneshān'), ('Āshtīān', 'Āshtīān'), ('Garmeh', 'Garmeh'), ('Eqlīd', 'Eqlīd'), ('Nīkshahr', 'Nīkshahr'), ('Neyrīz', 'Neyrīz'), ('Gonābād', 'Gonābād'), ('Kalāt-e Nāderī', 'Kalāt-e Nāderī'), ('Sūrīān', 'Sūrīān'), ('Zābolī', 'Zābolī'), ('Qarah Āghāj', 'Qarah Āghāj'), ('Sūrān', 'Sūrān'), ('Konārak', 'Konārak'), ('Dehlorān', 'Dehlorān'), ('Bardsīr', 'Bardsīr'), ('Qā’en', 'Qā’en'), ('Ḩājjīābād', 'Ḩājjīābād'), ('Moḩammadābād', 'Moḩammadābād'), ('Bardaskan', 'Bardaskan'), ('Asadīyeh', 'Asadīyeh'), ('Khonj', 'Khonj'), ('Hendījān', 'Hendījān'), ('Abarkūh', 'Abarkūh'), ('Tafresh', 'Tafresh'), ('Sorkheh', 'Sorkheh'), ('Garmsār', 'Garmsār'), ('Ārādān', 'Ārādān'), ('Farāshband', 'Farāshband'), ('Qal‘eh Ganj', 'Qal‘eh Ganj'), ('Khāsh', 'Khāsh'), ('Jājarm', 'Jājarm'), ('Ferdows', 'Ferdows'), ('Ḩājjīābād', 'Ḩājjīābād'), ('Bajestān', 'Bajestān'), ('Mehrīz', 'Mehrīz'), ('Ashkez̄ar', 'Ashkez̄ar'), ('Mehrān', 'Mehrān'), ('Shahr-e Bābak', 'Shahr-e Bābak'), ('Dalgān', 'Dalgān'), ('Kūhbanān', 'Kūhbanān'), ('Sardasht', 'Sardasht'), ('Sarbīsheh', 'Sarbīsheh'), ('Mayāmey', 'Mayāmey'), ('Shahr-e Herāt', 'Shahr-e Herāt'), ('Boshrūyeh', 'Boshrūyeh'), ('Bāfq', 'Bāfq'), ('Jāsk', 'Jāsk'), ('Ardakān', 'Ardakān'), ('Sarāyān', 'Sarāyān'), ('Rāvar', 'Rāvar'), ('Nehbandān', 'Nehbandān'), ('Ţabas', 'Ţabas'), ('Nā’īn', 'Nā’īn')], max_length=100)),
                ('companies', models.ManyToManyField(to='train.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.PositiveSmallIntegerField(choices=[(1, 'One Star'), (2, 'Two Star'), (3, 'Three Star'), (4, 'Four Star'), (5, 'Five Star')])),
                ('coupes_capacity', models.PositiveSmallIntegerField(choices=[(4, 'Four Beds'), (6, 'Six Beds')])),
                ('total_capacity', models.PositiveSmallIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.company')),
                ('current_railway', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='train.railway')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateField()),
                ('starting_time', models.TimeField()),
                ('remain_tickets', models.PositiveSmallIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('destination_railway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='train.railway')),
                ('origin_railway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_city', to='train.railway')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='train.train')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('tracking_code', models.CharField(max_length=20)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='train.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
