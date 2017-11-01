# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20171011_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=63, choices=[('ab', 'Abkhazian'), ('ace', 'Achinese'), ('ach', 'Acoli'), ('ada', 'Adangme'), ('ady', 'Adyghe'), ('aa', 'Afar'), ('afh', 'Afrihili'), ('af', 'Afrikaans'), ('agq', 'Aghem'), ('ain', 'Ainu'), ('ak', 'Akan'), ('akk', 'Akkadian'), ('bss', 'Akoose'), ('akz', 'Alabama'), ('sq', 'Albanian'), ('ale', 'Aleut'), ('arq', 'Algerian arabic'), ('ase', 'American sign language'), ('am', 'Amharic'), ('egy', 'Ancient egyptian'), ('grc', 'Ancient greek'), ('anp', 'Angika'), ('njo', 'Ao naga'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('arc', 'Aramaic'), ('aro', 'Araona'), ('arp', 'Arapaho'), ('arw', 'Arawak'), ('hy', 'Armenian'), ('rup', 'Aromanian'), ('frp', 'Arpitan'), ('as', 'Assamese'), ('ast', 'Asturian'), ('asa', 'Asu'), ('cch', 'Atsam'), ('av', 'Avaric'), ('ae', 'Avestan'), ('awa', 'Awadhi'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bfq', 'Badaga'), ('ksf', 'Bafia'), ('bfd', 'Bafut'), ('bqi', 'Bakhtiari'), ('ban', 'Balinese'), ('bal', 'Baluchi'), ('bm', 'Bambara'), ('bax', 'Bamun'), ('bjn', 'Banjar'), ('bas', 'Basaa'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('bbc', 'Batak toba'), ('bar', 'Bavarian'), ('bej', 'Beja'), ('be', 'Belarusian'), ('bem', 'Bemba'), ('bez', 'Bena'), ('bn', 'Bengali'), ('bew', 'Betawi'), ('bho', 'Bhojpuri'), ('bik', 'Bikol'), ('bin', 'Bini'), ('bpy', 'Bishnupriya'), ('bi', 'Bislama'), ('byn', 'Blin'), ('zbl', 'Blissymbols'), ('brx', 'Bodo'), ('bs', 'Bosnian'), ('brh', 'Brahui'), ('bra', 'Braj'), ('pt_BR', 'Brazilian portuguese'), ('br', 'Breton'), ('bug', 'Buginese'), ('bg', 'Bulgarian'), ('bum', 'Bulu'), ('bua', 'Buriat'), ('my', 'Burmese'), ('cad', 'Caddo'), ('frc', 'Cajun french'), ('yue', 'Cantonese'), ('cps', 'Capiznon'), ('car', 'Carib'), ('ca', 'Catalan'), ('cay', 'Cayuga'), ('ceb', 'Cebuano'), ('tzm', 'Central atlas tamazight'), ('dtp', 'Central dusun'), ('ckb', 'Central kurdish'), ('esu', 'Central yupik'), ('shu', 'Chadian arabic'), ('chg', 'Chagatai'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('chr', 'Cherokee'), ('chy', 'Cheyenne'), ('chb', 'Chibcha'), ('cgg', 'Chiga'), ('qug', 'Chimborazo highland quichua'), ('zh', 'Chinese'), ('chn', 'Chinook jargon'), ('chp', 'Chipewyan'), ('cho', 'Choctaw'), ('cu', 'Church slavic'), ('chk', 'Chuukese'), ('cv', 'Chuvash'), ('nwc', 'Classical newari'), ('syc', 'Classical syriac'), ('ksh', 'Colognian'), ('swb', 'Comorian'), ('sw_CD', 'Congo swahili'), ('cop', 'Coptic'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('mus', 'Creek'), ('crh', 'Crimean turkish'), ('hr', 'Croatian'), ('cs', 'Czech'), ('dak', 'Dakota'), ('da', 'Danish'), ('dar', 'Dargwa'), ('fa_AF', 'Dari'), ('dzg', 'Dazaga'), ('del', 'Delaware'), ('din', 'Dinka'), ('dv', 'Divehi'), ('doi', 'Dogri'), ('dgr', 'Dogrib'), ('dua', 'Duala'), ('nl', 'Dutch'), ('dyu', 'Dyula'), ('dz', 'Dzongkha'), ('frs', 'Eastern frisian'), ('efi', 'Efik'), ('arz', 'Egyptian arabic'), ('eka', 'Ekajuk'), ('elx', 'Elamite'), ('ebu', 'Embu'), ('egl', 'Emilian'), ('en', 'English'), ('myv', 'Erzya'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('pt_PT', 'European portuguese'), ('es_ES', 'European spanish'), ('ee', 'Ewe'), ('ewo', 'Ewondo'), ('ext', 'Extremaduran'), ('fan', 'Fang'), ('fat', 'Fanti'), ('fo', 'Faroese'), ('hif', 'Fiji hindi'), ('fj', 'Fijian'), ('fil', 'Filipino'), ('fi', 'Finnish'), ('nl_BE', 'Flemish'), ('fon', 'Fon'), ('gur', 'Frafra'), ('fr', 'French'), ('fur', 'Friulian'), ('ff', 'Fulah'), ('gaa', 'Ga'), ('gag', 'Gagauz'), ('gl', 'Galician'), ('gan', 'Gan chinese'), ('lg', 'Ganda'), ('gay', 'Gayo'), ('gba', 'Gbaya'), ('gez', 'Geez'), ('ka', 'Georgian'), ('de', 'German'), ('aln', 'Gheg albanian'), ('bbj', 'Ghomala'), ('glk', 'Gilaki'), ('gil', 'Gilbertese'), ('gom', 'Goan konkani'), ('gon', 'Gondi'), ('gor', 'Gorontalo'), ('got', 'Gothic'), ('grb', 'Grebo'), ('el', 'Greek'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('guz', 'Gusii'), ('gwi', 'Gwich\u02bcin'), ('hai', 'Haida'), ('ht', 'Haitian creole'), ('hak', 'Hakka chinese'), ('ha', 'Hausa'), ('haw', 'Hawaiian'), ('he', 'Hebrew'), ('hz', 'Herero'), ('hil', 'Hiligaynon'), ('hi', 'Hindi'), ('ho', 'Hiri motu'), ('hit', 'Hittite'), ('hmn', 'Hmong'), ('hu', 'Hungarian'), ('hup', 'Hupa'), ('iba', 'Iban'), ('ibb', 'Ibibio'), ('is', 'Icelandic'), ('io', 'Ido'), ('ig', 'Igbo'), ('ilo', 'Iloko'), ('smn', 'Inari sami'), ('id', 'Indonesian'), ('izh', 'Ingrian'), ('inh', 'Ingush'), ('ia', 'Interlingua'), ('ie', 'Interlingue'), ('iu', 'Inuktitut'), ('ik', 'Inupiaq'), ('ga', 'Irish'), ('it', 'Italian'), ('jam', 'Jamaican creole english'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kaj', 'Jju'), ('dyo', 'Jola-fonyi'), ('jrb', 'Judeo-arabic'), ('jpr', 'Judeo-persian'), ('jut', 'Jutish'), ('kbd', 'Kabardian'), ('kea', 'Kabuverdianu'), ('kab', 'Kabyle'), ('kac', 'Kachin'), ('kgp', 'Kaingang'), ('kkj', 'Kako'), ('kl', 'Kalaallisut'), ('kln', 'Kalenjin'), ('xal', 'Kalmyk'), ('kam', 'Kamba'), ('kbl', 'Kanembu'), ('kn', 'Kannada'), ('kr', 'Kanuri'), ('kaa', 'Kara-kalpak'), ('krc', 'Karachay-balkar'), ('krl', 'Karelian'), ('ks', 'Kashmiri'), ('csb', 'Kashubian'), ('kaw', 'Kawi'), ('kk', 'Kazakh'), ('ken', 'Kenyang'), ('kha', 'Khasi'), ('km', 'Khmer'), ('kho', 'Khotanese'), ('khw', 'Khowar'), ('ki', 'Kikuyu'), ('kmb', 'Kimbundu'), ('krj', 'Kinaray-a'), ('rw', 'Kinyarwanda'), ('kiu', 'Kirmanjki'), ('tlh', 'Klingon'), ('bkm', 'Kom'), ('kv', 'Komi'), ('koi', 'Komi-permyak'), ('kg', 'Kongo'), ('kok', 'Konkani'), ('ko', 'Korean'), ('kfo', 'Koro'), ('kos', 'Kosraean'), ('avk', 'Kotava'), ('khq', 'Koyra chiini'), ('ses', 'Koyraboro senni'), ('kpe', 'Kpelle'), ('kri', 'Krio'), ('kj', 'Kuanyama'), ('kum', 'Kumyk'), ('ku', 'Kurdish'), ('kru', 'Kurukh'), ('kut', 'Kutenai'), ('nmg', 'Kwasio'), ('ky', 'Kyrgyz'), ('quc', 'K\u02bciche\u02bc'), ('lad', 'Ladino'), ('lah', 'Lahnda'), ('lkt', 'Lakota'), ('lam', 'Lamba'), ('lag', 'Langi'), ('lo', 'Lao'), ('ltg', 'Latgalian'), ('la', 'Latin'), ('es_419', 'Latin american spanish'), ('lv', 'Latvian'), ('lzz', 'Laz'), ('lez', 'Lezghian'), ('lij', 'Ligurian'), ('li', 'Limburgish'), ('ln', 'Lingala'), ('lfn', 'Lingua franca nova'), ('lzh', 'Literary chinese'), ('lt', 'Lithuanian'), ('liv', 'Livonian'), ('jbo', 'Lojban'), ('lmo', 'Lombard'), ('nds', 'Low german'), ('nds_NL', 'Low saxon'), ('sli', 'Lower silesian'), ('dsb', 'Lower sorbian'), ('loz', 'Lozi'), ('lu', 'Luba-katanga'), ('lua', 'Luba-lulua'), ('lui', 'Luiseno'), ('smj', 'Lule sami'), ('lun', 'Lunda'), ('luo', 'Luo'), ('lb', 'Luxembourgish'), ('luy', 'Luyia'), ('mde', 'Maba'), ('mk', 'Macedonian'), ('jmc', 'Machame'), ('mad', 'Madurese'), ('maf', 'Mafa'), ('mag', 'Magahi'), ('vmf', 'Main-franconian'), ('mai', 'Maithili'), ('mak', 'Makasar'), ('mgh', 'Makhuwa-meetto'), ('kde', 'Makonde'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mnc', 'Manchu'), ('mdr', 'Mandar'), ('man', 'Mandingo'), ('mni', 'Manipuri'), ('gv', 'Manx'), ('mi', 'Maori'), ('arn', 'Mapuche'), ('mr', 'Marathi'), ('chm', 'Mari'), ('mh', 'Marshallese'), ('mwr', 'Marwari'), ('mas', 'Masai'), ('mzn', 'Mazanderani'), ('byv', 'Medumba'), ('men', 'Mende'), ('mwv', 'Mentawai'), ('mer', 'Meru'), ('mgo', 'Meta\u02bc'), ('es_MX', 'Mexican spanish'), ('mic', 'Micmac'), ('dum', 'Middle dutch'), ('enm', 'Middle english'), ('frm', 'Middle french'), ('gmh', 'Middle high german'), ('mga', 'Middle irish'), ('nan', 'Min nan chinese'), ('min', 'Minangkabau'), ('xmf', 'Mingrelian'), ('mwl', 'Mirandese'), ('lus', 'Mizo'), ('ar_001', 'Modern standard arabic'), ('moh', 'Mohawk'), ('mdf', 'Moksha'), ('ro_MD', 'Moldavian'), ('lol', 'Mongo'), ('mn', 'Mongolian'), ('mfe', 'Morisyen'), ('ary', 'Moroccan arabic'), ('mos', 'Mossi'), ('mua', 'Mundang'), ('ttt', 'Muslim tat'), ('mye', 'Myene'), ('naq', 'Nama'), ('na', 'Nauru'), ('nv', 'Navajo'), ('ng', 'Ndonga'), ('nap', 'Neapolitan'), ('ne', 'Nepali'), ('new', 'Newari'), ('sba', 'Ngambay'), ('nnh', 'Ngiemboon'), ('jgo', 'Ngomba'), ('yrl', 'Nheengatu'), ('nia', 'Nias'), ('niu', 'Niuean'), ('nog', 'Nogai'), ('nd', 'North ndebele'), ('frr', 'Northern frisian'), ('lrc', 'Northern luri'), ('se', 'Northern sami'), ('nso', 'Northern sotho'), ('no', 'Norwegian'), ('nb', 'Norwegian bokm\xe5l'), ('nn', 'Norwegian nynorsk'), ('nov', 'Novial'), ('nus', 'Nuer'), ('nym', 'Nyamwezi'), ('ny', 'Nyanja'), ('nyn', 'Nyankole'), ('tog', 'Nyasa tonga'), ('nyo', 'Nyoro'), ('nzi', 'Nzima'), ('nqo', 'N\u2019ko'), ('oc', 'Occitan'), ('oj', 'Ojibwa'), ('ang', 'Old english'), ('fro', 'Old french'), ('goh', 'Old high german'), ('sga', 'Old irish'), ('non', 'Old norse'), ('peo', 'Old persian'), ('pro', 'Old proven\xe7al'), ('or', 'Oriya'), ('om', 'Oromo'), ('osa', 'Osage'), ('os', 'Ossetic'), ('ota', 'Ottoman turkish'), ('pal', 'Pahlavi'), ('pfl', 'Palatine german'), ('pau', 'Palauan'), ('pi', 'Pali'), ('pam', 'Pampanga'), ('pag', 'Pangasinan'), ('pap', 'Papiamento'), ('ps', 'Pashto'), ('pdc', 'Pennsylvania german'), ('fa', 'Persian'), ('phn', 'Phoenician'), ('pcd', 'Picard'), ('pms', 'Piedmontese'), ('pdt', 'Plautdietsch'), ('pon', 'Pohnpeian'), ('pl', 'Polish'), ('pnt', 'Pontic'), ('pt', 'Portuguese'), ('prg', 'Prussian'), ('pa', 'Punjabi'), ('qu', 'Quechua'), ('raj', 'Rajasthani'), ('rap', 'Rapanui'), ('rar', 'Rarotongan'), ('rif', 'Riffian'), ('rgn', 'Romagnol'), ('ro', 'Romanian'), ('rm', 'Romansh'), ('rom', 'Romany'), ('rof', 'Rombo'), ('root', 'Root'), ('rtm', 'Rotuman'), ('rug', 'Roviana'), ('rn', 'Rundi'), ('ru', 'Russian'), ('rue', 'Rusyn'), ('rwk', 'Rwa'), ('ssy', 'Saho'), ('sah', 'Sakha'), ('sam', 'Samaritan aramaic'), ('saq', 'Samburu'), ('sm', 'Samoan'), ('sgs', 'Samogitian'), ('sad', 'Sandawe'), ('sg', 'Sango'), ('sbp', 'Sangu'), ('sa', 'Sanskrit'), ('sat', 'Santali'), ('sc', 'Sardinian'), ('sas', 'Sasak'), ('sdc', 'Sassarese sardinian'), ('stq', 'Saterland frisian'), ('saz', 'Saurashtra'), ('sco', 'Scots'), ('gd', 'Scottish gaelic'), ('sly', 'Selayar'), ('sel', 'Selkup'), ('seh', 'Sena'), ('see', 'Seneca'), ('sr', 'Serbian'), ('sh', 'Serbo-croatian'), ('srr', 'Serer'), ('sei', 'Seri'), ('ksb', 'Shambala'), ('shn', 'Shan'), ('sn', 'Shona'), ('ii', 'Sichuan yi'), ('scn', 'Sicilian'), ('sid', 'Sidamo'), ('bla', 'Siksika'), ('szl', 'Silesian'), ('zh_Hans', 'Simplified chinese'), ('sd', 'Sindhi'), ('si', 'Sinhala'), ('sms', 'Skolt sami'), ('den', 'Slave'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('xog', 'Soga'), ('sog', 'Sogdien'), ('so', 'Somali'), ('snk', 'Soninke'), ('nr', 'South ndebele'), ('alt', 'Southern altai'), ('sdh', 'Southern kurdish'), ('sma', 'Southern sami'), ('st', 'Southern sotho'), ('es', 'Spanish'), ('srn', 'Sranan tongo'), ('zgh', 'Standard moroccan tamazight'), ('suk', 'Sukuma'), ('sux', 'Sumerian'), ('su', 'Sundanese'), ('sus', 'Susu'), ('sw', 'Swahili'), ('ss', 'Swati'), ('sv', 'Swedish'), ('gsw', 'Swiss german'), ('syr', 'Syriac'), ('shi', 'Tachelhit'), ('tl', 'Tagalog'), ('ty', 'Tahitian'), ('dav', 'Taita'), ('tg', 'Tajik'), ('tly', 'Talysh'), ('tmh', 'Tamashek'), ('ta', 'Tamil'), ('trv', 'Taroko'), ('twq', 'Tasawaq'), ('tt', 'Tatar'), ('te', 'Telugu'), ('ter', 'Tereno'), ('teo', 'Teso'), ('tet', 'Tetum'), ('th', 'Thai'), ('bo', 'Tibetan'), ('tig', 'Tigre'), ('ti', 'Tigrinya'), ('tem', 'Timne'), ('tiv', 'Tiv'), ('tli', 'Tlingit'), ('tpi', 'Tok pisin'), ('tkl', 'Tokelau'), ('to', 'Tongan'), ('fit', 'Tornedalen finnish'), ('zh_Hant', 'Traditional chinese'), ('tkr', 'Tsakhur'), ('tsd', 'Tsakonian'), ('tsi', 'Tsimshian'), ('ts', 'Tsonga'), ('tn', 'Tswana'), ('tcy', 'Tulu'), ('tum', 'Tumbuka'), ('aeb', 'Tunisian arabic'), ('tr', 'Turkish'), ('tk', 'Turkmen'), ('tru', 'Turoyo'), ('tvl', 'Tuvalu'), ('tyv', 'Tuvinian'), ('tw', 'Twi'), ('kcg', 'Tyap'), ('udm', 'Udmurt'), ('uga', 'Ugaritic'), ('uk', 'Ukrainian'), ('umb', 'Umbundu'), ('hsb', 'Upper sorbian'), ('ur', 'Urdu'), ('ug', 'Uyghur'), ('uz', 'Uzbek'), ('vai', 'Vai'), ('ve', 'Venda'), ('vec', 'Venetian'), ('vep', 'Veps'), ('vi', 'Vietnamese'), ('vo', 'Volap\xfck'), ('vot', 'Votic'), ('vun', 'Vunjo'), ('vro', 'V\xf5ro'), ('wa', 'Walloon'), ('wae', 'Walser'), ('war', 'Waray'), ('wbp', 'Warlpiri'), ('was', 'Washo'), ('guc', 'Wayuu'), ('cy', 'Welsh'), ('vls', 'West flemish'), ('bgn', 'Western balochi'), ('fy', 'Western frisian'), ('mrj', 'Western mari'), ('wal', 'Wolaytta'), ('wo', 'Wolof'), ('wuu', 'Wu chinese'), ('xh', 'Xhosa'), ('hsn', 'Xiang chinese'), ('yav', 'Yangben'), ('yao', 'Yao'), ('yap', 'Yapese'), ('ybb', 'Yemba'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zap', 'Zapotec'), ('dje', 'Zarma'), ('zza', 'Zaza'), ('zea', 'Zeelandic'), ('zen', 'Zenaga'), ('za', 'Zhuang'), ('gbz', 'Zoroastrian dari'), ('zu', 'Zulu'), ('zun', 'Zuni')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='timezone',
            field=models.CharField(default=b'', max_length=100, blank=True, choices=[(b'Africa/Abidjan', b'Africa/Abidjan'), (b'Africa/Accra', b'Africa/Accra'), (b'Africa/Addis_Ababa', b'Africa/Addis_Ababa'), (b'Africa/Algiers', b'Africa/Algiers'), (b'Africa/Asmara', b'Africa/Asmara'), (b'Africa/Bamako', b'Africa/Bamako'), (b'Africa/Bangui', b'Africa/Bangui'), (b'Africa/Banjul', b'Africa/Banjul'), (b'Africa/Bissau', b'Africa/Bissau'), (b'Africa/Blantyre', b'Africa/Blantyre'), (b'Africa/Brazzaville', b'Africa/Brazzaville'), (b'Africa/Bujumbura', b'Africa/Bujumbura'), (b'Africa/Cairo', b'Africa/Cairo'), (b'Africa/Casablanca', b'Africa/Casablanca'), (b'Africa/Ceuta', b'Africa/Ceuta'), (b'Africa/Conakry', b'Africa/Conakry'), (b'Africa/Dakar', b'Africa/Dakar'), (b'Africa/Dar_es_Salaam', b'Africa/Dar_es_Salaam'), (b'Africa/Djibouti', b'Africa/Djibouti'), (b'Africa/Douala', b'Africa/Douala'), (b'Africa/El_Aaiun', b'Africa/El_Aaiun'), (b'Africa/Freetown', b'Africa/Freetown'), (b'Africa/Gaborone', b'Africa/Gaborone'), (b'Africa/Harare', b'Africa/Harare'), (b'Africa/Johannesburg', b'Africa/Johannesburg'), (b'Africa/Juba', b'Africa/Juba'), (b'Africa/Kampala', b'Africa/Kampala'), (b'Africa/Khartoum', b'Africa/Khartoum'), (b'Africa/Kigali', b'Africa/Kigali'), (b'Africa/Kinshasa', b'Africa/Kinshasa'), (b'Africa/Lagos', b'Africa/Lagos'), (b'Africa/Libreville', b'Africa/Libreville'), (b'Africa/Lome', b'Africa/Lome'), (b'Africa/Luanda', b'Africa/Luanda'), (b'Africa/Lubumbashi', b'Africa/Lubumbashi'), (b'Africa/Lusaka', b'Africa/Lusaka'), (b'Africa/Malabo', b'Africa/Malabo'), (b'Africa/Maputo', b'Africa/Maputo'), (b'Africa/Maseru', b'Africa/Maseru'), (b'Africa/Mbabane', b'Africa/Mbabane'), (b'Africa/Mogadishu', b'Africa/Mogadishu'), (b'Africa/Monrovia', b'Africa/Monrovia'), (b'Africa/Nairobi', b'Africa/Nairobi'), (b'Africa/Ndjamena', b'Africa/Ndjamena'), (b'Africa/Niamey', b'Africa/Niamey'), (b'Africa/Nouakchott', b'Africa/Nouakchott'), (b'Africa/Ouagadougou', b'Africa/Ouagadougou'), (b'Africa/Porto-Novo', b'Africa/Porto-Novo'), (b'Africa/Sao_Tome', b'Africa/Sao_Tome'), (b'Africa/Tripoli', b'Africa/Tripoli'), (b'Africa/Tunis', b'Africa/Tunis'), (b'Africa/Windhoek', b'Africa/Windhoek'), (b'America/Adak', b'America/Adak'), (b'America/Anchorage', b'America/Anchorage'), (b'America/Anguilla', b'America/Anguilla'), (b'America/Antigua', b'America/Antigua'), (b'America/Araguaina', b'America/Araguaina'), (b'America/Argentina/Buenos_Aires', b'America/Argentina/Buenos_Aires'), (b'America/Argentina/Catamarca', b'America/Argentina/Catamarca'), (b'America/Argentina/Cordoba', b'America/Argentina/Cordoba'), (b'America/Argentina/Jujuy', b'America/Argentina/Jujuy'), (b'America/Argentina/La_Rioja', b'America/Argentina/La_Rioja'), (b'America/Argentina/Mendoza', b'America/Argentina/Mendoza'), (b'America/Argentina/Rio_Gallegos', b'America/Argentina/Rio_Gallegos'), (b'America/Argentina/Salta', b'America/Argentina/Salta'), (b'America/Argentina/San_Juan', b'America/Argentina/San_Juan'), (b'America/Argentina/San_Luis', b'America/Argentina/San_Luis'), (b'America/Argentina/Tucuman', b'America/Argentina/Tucuman'), (b'America/Argentina/Ushuaia', b'America/Argentina/Ushuaia'), (b'America/Aruba', b'America/Aruba'), (b'America/Asuncion', b'America/Asuncion'), (b'America/Atikokan', b'America/Atikokan'), (b'America/Bahia', b'America/Bahia'), (b'America/Bahia_Banderas', b'America/Bahia_Banderas'), (b'America/Barbados', b'America/Barbados'), (b'America/Belem', b'America/Belem'), (b'America/Belize', b'America/Belize'), (b'America/Blanc-Sablon', b'America/Blanc-Sablon'), (b'America/Boa_Vista', b'America/Boa_Vista'), (b'America/Bogota', b'America/Bogota'), (b'America/Boise', b'America/Boise'), (b'America/Cambridge_Bay', b'America/Cambridge_Bay'), (b'America/Campo_Grande', b'America/Campo_Grande'), (b'America/Cancun', b'America/Cancun'), (b'America/Caracas', b'America/Caracas'), (b'America/Cayenne', b'America/Cayenne'), (b'America/Cayman', b'America/Cayman'), (b'America/Chicago', b'America/Chicago'), (b'America/Chihuahua', b'America/Chihuahua'), (b'America/Costa_Rica', b'America/Costa_Rica'), (b'America/Creston', b'America/Creston'), (b'America/Cuiaba', b'America/Cuiaba'), (b'America/Curacao', b'America/Curacao'), (b'America/Danmarkshavn', b'America/Danmarkshavn'), (b'America/Dawson', b'America/Dawson'), (b'America/Dawson_Creek', b'America/Dawson_Creek'), (b'America/Denver', b'America/Denver'), (b'America/Detroit', b'America/Detroit'), (b'America/Dominica', b'America/Dominica'), (b'America/Edmonton', b'America/Edmonton'), (b'America/Eirunepe', b'America/Eirunepe'), (b'America/El_Salvador', b'America/El_Salvador'), (b'America/Fort_Nelson', b'America/Fort_Nelson'), (b'America/Fortaleza', b'America/Fortaleza'), (b'America/Glace_Bay', b'America/Glace_Bay'), (b'America/Godthab', b'America/Godthab'), (b'America/Goose_Bay', b'America/Goose_Bay'), (b'America/Grand_Turk', b'America/Grand_Turk'), (b'America/Grenada', b'America/Grenada'), (b'America/Guadeloupe', b'America/Guadeloupe'), (b'America/Guatemala', b'America/Guatemala'), (b'America/Guayaquil', b'America/Guayaquil'), (b'America/Guyana', b'America/Guyana'), (b'America/Halifax', b'America/Halifax'), (b'America/Havana', b'America/Havana'), (b'America/Hermosillo', b'America/Hermosillo'), (b'America/Indiana/Indianapolis', b'America/Indiana/Indianapolis'), (b'America/Indiana/Knox', b'America/Indiana/Knox'), (b'America/Indiana/Marengo', b'America/Indiana/Marengo'), (b'America/Indiana/Petersburg', b'America/Indiana/Petersburg'), (b'America/Indiana/Tell_City', b'America/Indiana/Tell_City'), (b'America/Indiana/Vevay', b'America/Indiana/Vevay'), (b'America/Indiana/Vincennes', b'America/Indiana/Vincennes'), (b'America/Indiana/Winamac', b'America/Indiana/Winamac'), (b'America/Inuvik', b'America/Inuvik'), (b'America/Iqaluit', b'America/Iqaluit'), (b'America/Jamaica', b'America/Jamaica'), (b'America/Juneau', b'America/Juneau'), (b'America/Kentucky/Louisville', b'America/Kentucky/Louisville'), (b'America/Kentucky/Monticello', b'America/Kentucky/Monticello'), (b'America/Kralendijk', b'America/Kralendijk'), (b'America/La_Paz', b'America/La_Paz'), (b'America/Lima', b'America/Lima'), (b'America/Los_Angeles', b'America/Los_Angeles'), (b'America/Lower_Princes', b'America/Lower_Princes'), (b'America/Maceio', b'America/Maceio'), (b'America/Managua', b'America/Managua'), (b'America/Manaus', b'America/Manaus'), (b'America/Marigot', b'America/Marigot'), (b'America/Martinique', b'America/Martinique'), (b'America/Matamoros', b'America/Matamoros'), (b'America/Mazatlan', b'America/Mazatlan'), (b'America/Menominee', b'America/Menominee'), (b'America/Merida', b'America/Merida'), (b'America/Metlakatla', b'America/Metlakatla'), (b'America/Mexico_City', b'America/Mexico_City'), (b'America/Miquelon', b'America/Miquelon'), (b'America/Moncton', b'America/Moncton'), (b'America/Monterrey', b'America/Monterrey'), (b'America/Montevideo', b'America/Montevideo'), (b'America/Montserrat', b'America/Montserrat'), (b'America/Nassau', b'America/Nassau'), (b'America/New_York', b'America/New_York'), (b'America/Nipigon', b'America/Nipigon'), (b'America/Nome', b'America/Nome'), (b'America/Noronha', b'America/Noronha'), (b'America/North_Dakota/Beulah', b'America/North_Dakota/Beulah'), (b'America/North_Dakota/Center', b'America/North_Dakota/Center'), (b'America/North_Dakota/New_Salem', b'America/North_Dakota/New_Salem'), (b'America/Ojinaga', b'America/Ojinaga'), (b'America/Panama', b'America/Panama'), (b'America/Pangnirtung', b'America/Pangnirtung'), (b'America/Paramaribo', b'America/Paramaribo'), (b'America/Phoenix', b'America/Phoenix'), (b'America/Port-au-Prince', b'America/Port-au-Prince'), (b'America/Port_of_Spain', b'America/Port_of_Spain'), (b'America/Porto_Velho', b'America/Porto_Velho'), (b'America/Puerto_Rico', b'America/Puerto_Rico'), (b'America/Punta_Arenas', b'America/Punta_Arenas'), (b'America/Rainy_River', b'America/Rainy_River'), (b'America/Rankin_Inlet', b'America/Rankin_Inlet'), (b'America/Recife', b'America/Recife'), (b'America/Regina', b'America/Regina'), (b'America/Resolute', b'America/Resolute'), (b'America/Rio_Branco', b'America/Rio_Branco'), (b'America/Santarem', b'America/Santarem'), (b'America/Santiago', b'America/Santiago'), (b'America/Santo_Domingo', b'America/Santo_Domingo'), (b'America/Sao_Paulo', b'America/Sao_Paulo'), (b'America/Scoresbysund', b'America/Scoresbysund'), (b'America/Sitka', b'America/Sitka'), (b'America/St_Barthelemy', b'America/St_Barthelemy'), (b'America/St_Johns', b'America/St_Johns'), (b'America/St_Kitts', b'America/St_Kitts'), (b'America/St_Lucia', b'America/St_Lucia'), (b'America/St_Thomas', b'America/St_Thomas'), (b'America/St_Vincent', b'America/St_Vincent'), (b'America/Swift_Current', b'America/Swift_Current'), (b'America/Tegucigalpa', b'America/Tegucigalpa'), (b'America/Thule', b'America/Thule'), (b'America/Thunder_Bay', b'America/Thunder_Bay'), (b'America/Tijuana', b'America/Tijuana'), (b'America/Toronto', b'America/Toronto'), (b'America/Tortola', b'America/Tortola'), (b'America/Vancouver', b'America/Vancouver'), (b'America/Whitehorse', b'America/Whitehorse'), (b'America/Winnipeg', b'America/Winnipeg'), (b'America/Yakutat', b'America/Yakutat'), (b'America/Yellowknife', b'America/Yellowknife'), (b'Antarctica/Casey', b'Antarctica/Casey'), (b'Antarctica/Davis', b'Antarctica/Davis'), (b'Antarctica/DumontDUrville', b'Antarctica/DumontDUrville'), (b'Antarctica/Macquarie', b'Antarctica/Macquarie'), (b'Antarctica/Mawson', b'Antarctica/Mawson'), (b'Antarctica/McMurdo', b'Antarctica/McMurdo'), (b'Antarctica/Palmer', b'Antarctica/Palmer'), (b'Antarctica/Rothera', b'Antarctica/Rothera'), (b'Antarctica/Syowa', b'Antarctica/Syowa'), (b'Antarctica/Troll', b'Antarctica/Troll'), (b'Antarctica/Vostok', b'Antarctica/Vostok'), (b'Arctic/Longyearbyen', b'Arctic/Longyearbyen'), (b'Asia/Aden', b'Asia/Aden'), (b'Asia/Almaty', b'Asia/Almaty'), (b'Asia/Amman', b'Asia/Amman'), (b'Asia/Anadyr', b'Asia/Anadyr'), (b'Asia/Aqtau', b'Asia/Aqtau'), (b'Asia/Aqtobe', b'Asia/Aqtobe'), (b'Asia/Ashgabat', b'Asia/Ashgabat'), (b'Asia/Atyrau', b'Asia/Atyrau'), (b'Asia/Baghdad', b'Asia/Baghdad'), (b'Asia/Bahrain', b'Asia/Bahrain'), (b'Asia/Baku', b'Asia/Baku'), (b'Asia/Bangkok', b'Asia/Bangkok'), (b'Asia/Barnaul', b'Asia/Barnaul'), (b'Asia/Beirut', b'Asia/Beirut'), (b'Asia/Bishkek', b'Asia/Bishkek'), (b'Asia/Brunei', b'Asia/Brunei'), (b'Asia/Chita', b'Asia/Chita'), (b'Asia/Choibalsan', b'Asia/Choibalsan'), (b'Asia/Colombo', b'Asia/Colombo'), (b'Asia/Damascus', b'Asia/Damascus'), (b'Asia/Dhaka', b'Asia/Dhaka'), (b'Asia/Dili', b'Asia/Dili'), (b'Asia/Dubai', b'Asia/Dubai'), (b'Asia/Dushanbe', b'Asia/Dushanbe'), (b'Asia/Famagusta', b'Asia/Famagusta'), (b'Asia/Gaza', b'Asia/Gaza'), (b'Asia/Hebron', b'Asia/Hebron'), (b'Asia/Ho_Chi_Minh', b'Asia/Ho_Chi_Minh'), (b'Asia/Hong_Kong', b'Asia/Hong_Kong'), (b'Asia/Hovd', b'Asia/Hovd'), (b'Asia/Irkutsk', b'Asia/Irkutsk'), (b'Asia/Jakarta', b'Asia/Jakarta'), (b'Asia/Jayapura', b'Asia/Jayapura'), (b'Asia/Jerusalem', b'Asia/Jerusalem'), (b'Asia/Kabul', b'Asia/Kabul'), (b'Asia/Kamchatka', b'Asia/Kamchatka'), (b'Asia/Karachi', b'Asia/Karachi'), (b'Asia/Kathmandu', b'Asia/Kathmandu'), (b'Asia/Khandyga', b'Asia/Khandyga'), (b'Asia/Kolkata', b'Asia/Kolkata'), (b'Asia/Krasnoyarsk', b'Asia/Krasnoyarsk'), (b'Asia/Kuala_Lumpur', b'Asia/Kuala_Lumpur'), (b'Asia/Kuching', b'Asia/Kuching'), (b'Asia/Kuwait', b'Asia/Kuwait'), (b'Asia/Macau', b'Asia/Macau'), (b'Asia/Magadan', b'Asia/Magadan'), (b'Asia/Makassar', b'Asia/Makassar'), (b'Asia/Manila', b'Asia/Manila'), (b'Asia/Muscat', b'Asia/Muscat'), (b'Asia/Nicosia', b'Asia/Nicosia'), (b'Asia/Novokuznetsk', b'Asia/Novokuznetsk'), (b'Asia/Novosibirsk', b'Asia/Novosibirsk'), (b'Asia/Omsk', b'Asia/Omsk'), (b'Asia/Oral', b'Asia/Oral'), (b'Asia/Phnom_Penh', b'Asia/Phnom_Penh'), (b'Asia/Pontianak', b'Asia/Pontianak'), (b'Asia/Pyongyang', b'Asia/Pyongyang'), (b'Asia/Qatar', b'Asia/Qatar'), (b'Asia/Qyzylorda', b'Asia/Qyzylorda'), (b'Asia/Riyadh', b'Asia/Riyadh'), (b'Asia/Sakhalin', b'Asia/Sakhalin'), (b'Asia/Samarkand', b'Asia/Samarkand'), (b'Asia/Seoul', b'Asia/Seoul'), (b'Asia/Shanghai', b'Asia/Shanghai'), (b'Asia/Singapore', b'Asia/Singapore'), (b'Asia/Srednekolymsk', b'Asia/Srednekolymsk'), (b'Asia/Taipei', b'Asia/Taipei'), (b'Asia/Tashkent', b'Asia/Tashkent'), (b'Asia/Tbilisi', b'Asia/Tbilisi'), (b'Asia/Tehran', b'Asia/Tehran'), (b'Asia/Thimphu', b'Asia/Thimphu'), (b'Asia/Tokyo', b'Asia/Tokyo'), (b'Asia/Tomsk', b'Asia/Tomsk'), (b'Asia/Ulaanbaatar', b'Asia/Ulaanbaatar'), (b'Asia/Urumqi', b'Asia/Urumqi'), (b'Asia/Ust-Nera', b'Asia/Ust-Nera'), (b'Asia/Vientiane', b'Asia/Vientiane'), (b'Asia/Vladivostok', b'Asia/Vladivostok'), (b'Asia/Yakutsk', b'Asia/Yakutsk'), (b'Asia/Yangon', b'Asia/Yangon'), (b'Asia/Yekaterinburg', b'Asia/Yekaterinburg'), (b'Asia/Yerevan', b'Asia/Yerevan'), (b'Atlantic/Azores', b'Atlantic/Azores'), (b'Atlantic/Bermuda', b'Atlantic/Bermuda'), (b'Atlantic/Canary', b'Atlantic/Canary'), (b'Atlantic/Cape_Verde', b'Atlantic/Cape_Verde'), (b'Atlantic/Faroe', b'Atlantic/Faroe'), (b'Atlantic/Madeira', b'Atlantic/Madeira'), (b'Atlantic/Reykjavik', b'Atlantic/Reykjavik'), (b'Atlantic/South_Georgia', b'Atlantic/South_Georgia'), (b'Atlantic/St_Helena', b'Atlantic/St_Helena'), (b'Atlantic/Stanley', b'Atlantic/Stanley'), (b'Australia/Adelaide', b'Australia/Adelaide'), (b'Australia/Brisbane', b'Australia/Brisbane'), (b'Australia/Broken_Hill', b'Australia/Broken_Hill'), (b'Australia/Currie', b'Australia/Currie'), (b'Australia/Darwin', b'Australia/Darwin'), (b'Australia/Eucla', b'Australia/Eucla'), (b'Australia/Hobart', b'Australia/Hobart'), (b'Australia/Lindeman', b'Australia/Lindeman'), (b'Australia/Lord_Howe', b'Australia/Lord_Howe'), (b'Australia/Melbourne', b'Australia/Melbourne'), (b'Australia/Perth', b'Australia/Perth'), (b'Australia/Sydney', b'Australia/Sydney'), (b'Canada/Atlantic', b'Canada/Atlantic'), (b'Canada/Central', b'Canada/Central'), (b'Canada/Eastern', b'Canada/Eastern'), (b'Canada/Mountain', b'Canada/Mountain'), (b'Canada/Newfoundland', b'Canada/Newfoundland'), (b'Canada/Pacific', b'Canada/Pacific'), (b'Europe/Amsterdam', b'Europe/Amsterdam'), (b'Europe/Andorra', b'Europe/Andorra'), (b'Europe/Astrakhan', b'Europe/Astrakhan'), (b'Europe/Athens', b'Europe/Athens'), (b'Europe/Belgrade', b'Europe/Belgrade'), (b'Europe/Berlin', b'Europe/Berlin'), (b'Europe/Bratislava', b'Europe/Bratislava'), (b'Europe/Brussels', b'Europe/Brussels'), (b'Europe/Bucharest', b'Europe/Bucharest'), (b'Europe/Budapest', b'Europe/Budapest'), (b'Europe/Busingen', b'Europe/Busingen'), (b'Europe/Chisinau', b'Europe/Chisinau'), (b'Europe/Copenhagen', b'Europe/Copenhagen'), (b'Europe/Dublin', b'Europe/Dublin'), (b'Europe/Gibraltar', b'Europe/Gibraltar'), (b'Europe/Guernsey', b'Europe/Guernsey'), (b'Europe/Helsinki', b'Europe/Helsinki'), (b'Europe/Isle_of_Man', b'Europe/Isle_of_Man'), (b'Europe/Istanbul', b'Europe/Istanbul'), (b'Europe/Jersey', b'Europe/Jersey'), (b'Europe/Kaliningrad', b'Europe/Kaliningrad'), (b'Europe/Kiev', b'Europe/Kiev'), (b'Europe/Kirov', b'Europe/Kirov'), (b'Europe/Lisbon', b'Europe/Lisbon'), (b'Europe/Ljubljana', b'Europe/Ljubljana'), (b'Europe/London', b'Europe/London'), (b'Europe/Luxembourg', b'Europe/Luxembourg'), (b'Europe/Madrid', b'Europe/Madrid'), (b'Europe/Malta', b'Europe/Malta'), (b'Europe/Mariehamn', b'Europe/Mariehamn'), (b'Europe/Minsk', b'Europe/Minsk'), (b'Europe/Monaco', b'Europe/Monaco'), (b'Europe/Moscow', b'Europe/Moscow'), (b'Europe/Oslo', b'Europe/Oslo'), (b'Europe/Paris', b'Europe/Paris'), (b'Europe/Podgorica', b'Europe/Podgorica'), (b'Europe/Prague', b'Europe/Prague'), (b'Europe/Riga', b'Europe/Riga'), (b'Europe/Rome', b'Europe/Rome'), (b'Europe/Samara', b'Europe/Samara'), (b'Europe/San_Marino', b'Europe/San_Marino'), (b'Europe/Sarajevo', b'Europe/Sarajevo'), (b'Europe/Saratov', b'Europe/Saratov'), (b'Europe/Simferopol', b'Europe/Simferopol'), (b'Europe/Skopje', b'Europe/Skopje'), (b'Europe/Sofia', b'Europe/Sofia'), (b'Europe/Stockholm', b'Europe/Stockholm'), (b'Europe/Tallinn', b'Europe/Tallinn'), (b'Europe/Tirane', b'Europe/Tirane'), (b'Europe/Ulyanovsk', b'Europe/Ulyanovsk'), (b'Europe/Uzhgorod', b'Europe/Uzhgorod'), (b'Europe/Vaduz', b'Europe/Vaduz'), (b'Europe/Vatican', b'Europe/Vatican'), (b'Europe/Vienna', b'Europe/Vienna'), (b'Europe/Vilnius', b'Europe/Vilnius'), (b'Europe/Volgograd', b'Europe/Volgograd'), (b'Europe/Warsaw', b'Europe/Warsaw'), (b'Europe/Zagreb', b'Europe/Zagreb'), (b'Europe/Zaporozhye', b'Europe/Zaporozhye'), (b'Europe/Zurich', b'Europe/Zurich'), (b'GMT', b'GMT'), (b'Indian/Antananarivo', b'Indian/Antananarivo'), (b'Indian/Chagos', b'Indian/Chagos'), (b'Indian/Christmas', b'Indian/Christmas'), (b'Indian/Cocos', b'Indian/Cocos'), (b'Indian/Comoro', b'Indian/Comoro'), (b'Indian/Kerguelen', b'Indian/Kerguelen'), (b'Indian/Mahe', b'Indian/Mahe'), (b'Indian/Maldives', b'Indian/Maldives'), (b'Indian/Mauritius', b'Indian/Mauritius'), (b'Indian/Mayotte', b'Indian/Mayotte'), (b'Indian/Reunion', b'Indian/Reunion'), (b'Pacific/Apia', b'Pacific/Apia'), (b'Pacific/Auckland', b'Pacific/Auckland'), (b'Pacific/Bougainville', b'Pacific/Bougainville'), (b'Pacific/Chatham', b'Pacific/Chatham'), (b'Pacific/Chuuk', b'Pacific/Chuuk'), (b'Pacific/Easter', b'Pacific/Easter'), (b'Pacific/Efate', b'Pacific/Efate'), (b'Pacific/Enderbury', b'Pacific/Enderbury'), (b'Pacific/Fakaofo', b'Pacific/Fakaofo'), (b'Pacific/Fiji', b'Pacific/Fiji'), (b'Pacific/Funafuti', b'Pacific/Funafuti'), (b'Pacific/Galapagos', b'Pacific/Galapagos'), (b'Pacific/Gambier', b'Pacific/Gambier'), (b'Pacific/Guadalcanal', b'Pacific/Guadalcanal'), (b'Pacific/Guam', b'Pacific/Guam'), (b'Pacific/Honolulu', b'Pacific/Honolulu'), (b'Pacific/Kiritimati', b'Pacific/Kiritimati'), (b'Pacific/Kosrae', b'Pacific/Kosrae'), (b'Pacific/Kwajalein', b'Pacific/Kwajalein'), (b'Pacific/Majuro', b'Pacific/Majuro'), (b'Pacific/Marquesas', b'Pacific/Marquesas'), (b'Pacific/Midway', b'Pacific/Midway'), (b'Pacific/Nauru', b'Pacific/Nauru'), (b'Pacific/Niue', b'Pacific/Niue'), (b'Pacific/Norfolk', b'Pacific/Norfolk'), (b'Pacific/Noumea', b'Pacific/Noumea'), (b'Pacific/Pago_Pago', b'Pacific/Pago_Pago'), (b'Pacific/Palau', b'Pacific/Palau'), (b'Pacific/Pitcairn', b'Pacific/Pitcairn'), (b'Pacific/Pohnpei', b'Pacific/Pohnpei'), (b'Pacific/Port_Moresby', b'Pacific/Port_Moresby'), (b'Pacific/Rarotonga', b'Pacific/Rarotonga'), (b'Pacific/Saipan', b'Pacific/Saipan'), (b'Pacific/Tahiti', b'Pacific/Tahiti'), (b'Pacific/Tarawa', b'Pacific/Tarawa'), (b'Pacific/Tongatapu', b'Pacific/Tongatapu'), (b'Pacific/Wake', b'Pacific/Wake'), (b'Pacific/Wallis', b'Pacific/Wallis'), (b'US/Alaska', b'US/Alaska'), (b'US/Arizona', b'US/Arizona'), (b'US/Central', b'US/Central'), (b'US/Eastern', b'US/Eastern'), (b'US/Hawaii', b'US/Hawaii'), (b'US/Mountain', b'US/Mountain'), (b'US/Pacific', b'US/Pacific'), (b'UTC', b'UTC')]),
        ),
    ]