"""
Конвертация данных в json
"""

data_blog = [
    {"name": "Путешествия по миру",
     "tagline": "Откройте новые горизонты и погрузитесь в удивительные "
                "приключения вместе с нами!",
     },
    {"name": "Кулинарные искушения",
     "tagline": "Раскройте вкусовые грани и наслаждайтесь миром кулинарии "
                "вместе с нами!",
     },
    {"name": "Фитнес и здоровый образ жизни",
     "tagline": "Позаботьтесь о своем здоровье, достигните физической формы "
                "и ощутите преимущества активного образа жизни!",
     },
    {"name": "ИТ-новости и технологии",
     "tagline": "Будьте в курсе последних новостей, трендов и инноваций "
                "в мире информационных технологий!",
     },
    {"name": "Мода и стиль",
     "tagline": "Выражайте свою индивидуальность, следите за модными "
                "тенденциями и создавайте неповторимые образы вместе с нами!",
     },
]

data_author = [
    {"name": "alexander89",
     "email": "alexander89@gmail.com",
     },
    {"name": "ekaterina_blog",
     "email": "ekaterina.blog@yahoo.com",
     },
    {"name": "maxim_writer",
     "email": "maxim.writer@hotmail.com",
     },
    {"name": "anna_journey",
     "email": "anna.journey@gmail.com",
     },
    {"name": "sergey_reads",
     "email": "sergey.reads@yahoo.com",
     },
    {"name": "olga_creative",
     "email": "olga.creative@gmail.com",
     },
    {"name": "dmitry_thinker",
     "email": "dmitry.thinker@hotmail.com",
     },
    {"name": "natalia_author",
     "email": "natalia.author@yahoo.com",
     },
    {"name": "ivan_wordsmith",
     "email": "ivan.wordsmith@gmail.com",
     },
    {"name": "marina_inspires",
     "email": "marina.inspires@yahoo.com",
     },
    {"name": "vladimir_writer",
     "email": "vladimir.writer@mail.ru",
     },
    {"name": "irina_blogger",
     "email": "irina.blogger@yandex.ru",
     },
    {"name": "andrey_author",
     "email": "andrey.author@rambler.ru",
     },
    {"name": "elena_thoughts",
     "email": "elena.thoughts@list.ru",
     },
    {"name": "alexandra_creative",
     "email": "alexandra.creative@inbox.ru",
     },
    {"name": "nikolay_blog",
     "email": "nikolay.blog@mail.ru",
     },
    {"name": "svetlana_writer",
     "email": "svetlana.writer@yandex.ru",
     },
    {"name": "roman_author",
     "email": "roman.author@rambler.ru",
     },
    {"name": "larisa_thinker",
     "email": "larisa.thinker@list.ru",
     },
    {"name": "dmitriy_creative",
     "email": "dmitriy.creative@inbox.ru",
     },
]

data_author_profile = [
    {
        "author": "alexander89",
        "bio": "Стремлюсь к тому, чтобы делиться своими знаниями и вдохновлять других.",
        "avatar": "downloaded_avatars/1.jpg",
        "phone_number": None,
        "city": "Москва"},
    {
        "author": "ekaterina_blog",
        "bio": "Исследую мир через слова и пишу о том, что меня вдохновляет.",
        "avatar": None,
        "phone_number": "+79523842943",
        "city": "Екатеринбург"},
    {
        "author": "maxim_writer",
        "bio": "В поисках новых историй и приключений. Рад поделиться своими мыслями и идеями.",
        "avatar": "downloaded_avatars/2.jpg",
        "phone_number": "+79993854785",
        "city": "Нижний Новгород"},
    {
        "author": "anna_journey",
        "bio": None,
        "avatar": None,
        "phone_number": None,
        "city": None},
    {
        "author": "sergey_reads",
        "bio": "Люблю погружаться в мир слов и раскрывать их магию через свои произведения.",
        "avatar": "downloaded_avatars/3.jpg",
        "phone_number": "+79500535005",
        "city": "Санкт-Петербург"},
    {
        "author": "olga_creative",
        "bio": "Размышляю о жизни и передаю свои мысли через письменное слово.",
        "avatar": "downloaded_avatars/4.png",
        "phone_number": "+79328949823",
        "city": "Казань"},
    {
        "author": "dmitry_thinker",
        "bio": "Вдохновение находится в малых деталях, и я стараюсь их передать через свои тексты.",
        "avatar": "downloaded_avatars/5.jpg",
        "phone_number": "+79853759733",
        "city": "Самара"},
    {
        "author": "natalia_author",
        "bio": None,
        "avatar": "downloaded_avatars/4.png",
        "phone_number": None,
        "city": None},
    {
        "author": "ivan_wordsmith",
        "bio": "Погружаюсь в разные темы и делюсь своими увлечениями с читателями.",
        "avatar": "downloaded_avatars/6.jpg",
        "phone_number": "+79993249574",
        "city": "Санкт-Петербург"},
    {
        "author": "marina_inspires",
        "bio": "Чувствую, что слова имеют силу изменить мир, поэтому я пишу.",
        "avatar": None,
        "phone_number": "+79457344794",
        "city": "Москва"},
    {
        "author": "vladimir_writer",
        "bio": "Захватываю воображение и вношу каплю вдохновения в каждое свое произведение.",
        "avatar": None,
        "phone_number": None,
        "city": None},
    {
        "author": "irina_blogger",
        "bio": "Мои истории - это отражение моего внутреннего мира и наблюдений о внешнем.",
        "avatar": "downloaded_avatars/7.jpg",
        "phone_number": "+79009009090",
        "city": "Санкт-Петербург"},
    {
        "author": "andrey_author",
        "bio": "Исследую разнообразие жизни и выражаю свои мысли через письменное искусство.",
        "avatar": "downloaded_avatars/8.jpg",
        "phone_number": "+79696502575",
        "city": "Москва"},
    {
        "author": "elena_thoughts",
        "bio": None,
        "avatar": None,
        "phone_number": None,
        "city": "Владивосток"},
    {
        "author": "alexandra_creative",
        "bio": None,
        "avatar": None,
        "phone_number": None,
        "city": None},
    {
        "author": "nikolay_blog",
        "bio": "Пытаюсь поймать красоту мира и передать ее через мои слова.",
        "avatar": "downloaded_avatars/9.jpg",
        "phone_number": "+79158765678",
        "city": "Казань"},
    {
        "author": "svetlana_writer",
        "bio": "Слова - это кисть, которой я создаю картины своих идей и эмоций.",
        "avatar": None,
        "phone_number": None,
        "city": None},
    {
        "author": "roman_author",
        "bio": "Слова - это инструмент, с помощью которого я строю свой мир и делюсь им с другими.",
        "avatar": None,
        "phone_number": "+79258659900",
        "city": "Ростов-на-Дону"},
    {
        "author": "larisa_thinker",
        "bio": None,
        "avatar": None,
        "phone_number": None,
        "city": None},
    {
        "author": "dmitriy_creative",
        "bio": None,
        "avatar": None,
        "phone_number": None,
        "city": "Красноярск"},
]

data_entry = [
    {"blog": "Путешествия по миру",
     "headline": "Изучение красот Мачу-Пикчу",
     "body_text": """Древний город Мачу-Пикчу, скрытый среди гор Анд, привлекает 
путешественников со всего мира своей уникальной красотой и загадочностью. 
Изучение этого археологического чуда предлагает нам уникальную возможность 
погрузиться в инковскую культуру и исследовать их удивительные инженерные 
достижения. Путешественники могут отправиться на треккинговый маршрут, 
подняться на вершину Хуайна Пикчу и насладиться потрясающим видом на 
древний город. Изучение Мачу-Пикчу - это не только путешествие во времени, 
но и возможность узнать больше о древних цивилизациях и их наследии.""",
     "pub_date": "2022-04-01",
     "authors": ["ivan_wordsmith", "alexander89"],
     "number_of_comments": 2,
     "number_of_pingbacks": 10,
     "rating": None,
     },
    {"blog": "Путешествия по миру",
     "headline": "Приключения в Амазонке",
     "body_text": """Амазонка - это не просто река, это целый мир приключений 
и загадок. Встреча с дикой природой Амазонки позволит вам увидеть 
уникальную биоразнообразие и ощутить мощь естественной силы. Прогулка на 
каноэ по реке, ночные походы в джунгли, наблюдение за экзотическими 
животными и птицами - все это ожидает вас в Амазонке. Погрузитесь в 
зеленый мир самой большой тропической джунгли на Земле и откройте для 
себя удивительные приключения, которые запомнятся на всю жизнь.""",
     "pub_date": "2022-08-01",
     "authors": ["dmitriy_creative"],
     "number_of_comments": 14,
     "number_of_pingbacks": 30,
     "rating": 5,
     },
    {"blog": "Путешествия по миру",
     "headline": "Знакомство с Парижем",
     "body_text": """Париж - город любви, искусства и изысканности. 
Знакомство с Парижем - это погружение в его узкие улочки, исторические 
достопримечательности и культурную сцену. Прогулка по набережной Сены, 
посещение Эйфелевой башни, музея Лувр и собора Парижской Богоматери - 
это всего лишь некоторые из знаковых мест, которые стоит посетить. 
Парижские кафе, булочные и рестораны предлагают богатство французской 
кухни и возможность насладиться неповторимой атмосферой этого 
удивительного города.""",
     "pub_date": "2022-06-01",
     "authors": ["anna_journey", "ekaterina_blog", "olga_creative"],
     "number_of_comments": 7,
     "number_of_pingbacks": 5,
     "rating": 4.7,
     },
    {"blog": "Путешествия по миру",
     "headline": "Открывая тайны Колизея",
     "body_text": """Колизей - величественная арена, свидетель исторических 
сражений и развлечений древнего Рима. Откройте для себя его тайны и 
узнайте больше о жизни в античной Римской империи. Исследуйте 
архитектурные детали, узнайте о роли Колизея в культуре и развлечениях 
древних римлян. Посетите музей, расположенный внутри Колизея, где вы 
сможете увидеть артефакты, связанные с его историей. Путешествие во 
времени через посещение Колизея откроет перед вами удивительный мир 
древнего Рима.""",
     "pub_date": "2022-09-01",
     "authors": ["marina_inspires", "elena_thoughts"],
     "number_of_comments": 2,
     "number_of_pingbacks": 5,
     "rating": 3.3,
     },
    {"blog": "Путешествия по миру",
     "headline": "Оазисы Сахары: красота и опасность",
     "body_text": """Сахара - самая большая пустыня на планете, и в ее сердце 
скрыты удивительные оазисы. Погрузитесь в суровую красоту Сахары и 
откройте для себя места, где жизнь пробивает себе путь сквозь песчаные 
дюны. Оазисы предлагают прохладу, зелень и свежую воду в иссушающей 
пустыне. Однако, несмотря на красоту, Сахара также представляет 
опасность своими экстремальными температурами и отсутствием воды. 
Познакомьтесь с удивительным миром Сахары и увидьте, как природа 
адаптируется к таким непростым условиям жизни.""",
     "pub_date": "2023-04-01",
     "authors": ["andrey_author", "vladimir_writer", "nikolay_blog"],
     "number_of_comments": 4,
     "number_of_pingbacks": 0,
     "rating": 3.4,
     },
    {"blog": "Кулинарные искушения",
     "headline": "Рецепты блюд из итальянской кухни",
     "body_text": """Итальянская кухня славится своим богатством вкусов и 
разнообразием блюд. В этой статье мы поделимся с вами несколькими 
классическими рецептами, которые позволят вам окунуться в мир 
итальянской гастрономии. Вы узнаете, как приготовить настоящую пасту аль 
денте, как приготовить вкуснейшие пиццы с разнообразными начинками и как 
приготовить итальянские десерты, например, тирамису. Раскройте секреты 
итальянской кухни и порадуйте себя и своих близких аутентичными и 
вкусными блюдами.""",
     "pub_date": "2023-01-01",
     "authors": ["dmitriy_creative", "roman_author"],
     "number_of_comments": 10,
     "number_of_pingbacks": 0,
     "rating": 3.5,
     },
    {"blog": "Кулинарные искушения",
     "headline": "Приготовление собственного хлеба",
     "body_text": """Аромат свежеиспеченного хлеба заполняет дом и создает 
уютную атмосферу. В этой статье мы расскажем вам о процессе 
приготовления хлеба в домашних условиях. Вы узнаете, как подготовить 
тесто, как правильно расстойку и выпекать хлеб. Мы также поделимся с 
вами различными рецептами хлеба, от классического французского багета до 
ароматного кукурузного хлеба. Приготовьте свой собственный хлеб и 
наслаждайтесь его неповторимым вкусом и ароматом.""",
     "pub_date": "2023-08-01",
     "authors": ["alexander89"],
     "number_of_comments": 7,
     "number_of_pingbacks": 7,
     "rating": 2.3,
     },
    {"blog": "Кулинарные искушения",
     "headline": "Экзотические специи и их использование",
     "body_text": """Экзотические специи добавляют в блюда особый вкус и 
аромат. В этой статье мы представим вам несколько интересных 
экзотических специй и расскажем, как их использовать в кулинарии. 
Узнайте о чили, корице, куркуме, кардамоне и других специях, которые 
придают блюдам уникальные оттенки. Мы также поделимся с вами рецептами, 
в которых экзотические специи станут настоящими героями. Откройте новые 
гастрономические горизонты с помощью экзотических специй.""",
     "pub_date": "2022-12-01",
     "authors": ["irina_blogger", "vladimir_writer"],
     "number_of_comments": 2,
     "number_of_pingbacks": 4,
     "rating": 4.2,
     },
    {"blog": "Кулинарные искушения",
     "headline": "Десерты для настоящих сладкоежек",
     "body_text": """Нет ничего лучше, чем насладиться вкусным десертом после 
обеда или вечернего ужина. В этой статье мы представим вам несколько 
рецептов десертов, которые понравятся настоящим сладкоежкам. Вы узнаете, 
как приготовить шоколадный торт, воздушные пирожные, фруктовые салаты и 
многое другое. Мы также поделимся с вами советами по украшению десертов, 
чтобы они выглядели так же аппетитно, как и вкусны. Разбудите свою 
сладкую сторону и порадуйте себя и своих близких великолепными 
десертами.""",
     "pub_date": "2023-12-01",
     "authors": ["irina_blogger"],
     "number_of_comments": 4,
     "number_of_pingbacks": 9,
     "rating": 4.9,
     },
    {"blog": "Кулинарные искушения",
     "headline": "Гастрономическое путешествие по Франции",
     "body_text": """Франция - страна, известная своей утонченной кухней и 
богатством гастрономического наследия. В этой статье мы предлагаем вам 
отправиться в увлекательное гастрономическое путешествие по Франции. Вы 
узнаете о различных региональных блюдах, таких как рататуй из Ниццы, 
крепкий сырный суфле из Савойи, нежное фуа-гра из Лангедока и многое 
другое. Мы расскажем вам о французских винных регионах и предложим 
подборки местных вин, которые отлично сочетаются с блюдами. Погрузитесь 
во французскую гастрономию и насладитесь великолепными вкусами и 
ароматами.""",
     "pub_date": "2023-01-01",
     "authors": ["ivan_wordsmith", "vladimir_writer"],
     "number_of_comments": 5,
     "number_of_pingbacks": 5,
     "rating": 4.8,
     },
    {"blog": "Фитнес и здоровый образ жизни",
     "headline": "Упражнения для поддержания физической формы",
     "body_text": """В этой статье мы представим вам набор упражнений, 
которые помогут поддерживать вашу физическую форму. Вы узнаете о 
различных видах тренировок, включая кардио, силовые упражнения и 
гибкость. Мы также поделимся с вами советами по правильной технике 
выполнения упражнений и расскажем о преимуществах регулярных 
тренировок.""",
     "pub_date": "2023-10-01",
     "authors": ["ivan_wordsmith"],
     "number_of_comments": 2,
     "number_of_pingbacks": 3,
     "rating": 5,
     },
    {"blog": "Фитнес и здоровый образ жизни",
     "headline": "Здоровое питание: полезные рецепты",
     "body_text": """В этой статье вы найдете полезные рецепты, которые 
помогут вам поддерживать здоровое питание. Мы поделимся с вами идеями 
для здоровых завтраков, обедов и ужинов, а также вкусными и полезными 
перекусами. Вы узнаете о важности баланса питательных веществ и получите 
рекомендации по выбору качественных продуктов.""",
     "pub_date": "2023-05-01",
     "authors": ["irina_blogger"],
     "number_of_comments": 7,
     "number_of_pingbacks": 20,
     "rating": 3.9,
     },
    {"blog": "Фитнес и здоровый образ жизни",
     "headline": "Топ-10 фитнес-тренеров для вдохновения",
     "body_text": """В этой статье мы представим вам десять вдохновляющих 
фитнес-тренеров, которые помогут вам достичь ваших фитнес-целей. Мы 
расскажем вам о их достижениях, тренировочных программах и философии 
здорового образа жизни. Вы сможете найти тренера, который соответствует 
вашим потребностям и станет вашим источником мотивации.""",
     "pub_date": "2024-01-01",
     "authors": ["elena_thoughts"],
     "number_of_comments": 1,
     "number_of_pingbacks": 4,
     "rating": 2.9,
     },
    {"blog": "Фитнес и здоровый образ жизни",
     "headline": "Как правильно заниматься йогой",
     "body_text": """В этой статье мы расскажем вам о правильном подходе к 
занятиям йогой. Вы узнаете о различных стилях йоги, основных асанах и 
дыхательных упражнениях. Мы также поделимся с вами советами по созданию 
комфортной атмосферы для практики йоги и о том, как получить 
максимальную пользу от этой древней практики.""",
     "pub_date": "2024-04-01",
     "authors": ["dmitriy_creative", "alexander89"],
     "number_of_comments": 0,
     "number_of_pingbacks": 0,
     "rating": 4.1,
     },
    {"blog": "Фитнес и здоровый образ жизни",
     "headline": "Секреты успешного похудения",
     "body_text": """В этой статье мы раскроем перед вами секреты успешного 
похудения. Вы узнаете о правильном подходе к питанию, регулярной 
физической активности и психологической поддержке. Мы поделимся с вами 
стратегиями управления весом, методами измерения прогресса и советами по 
поддержанию мотивации в течение всего процесса похудения.""",
     "pub_date": "2023-04-01",
     "authors": ["maxim_writer"],
     "number_of_comments": 5,
     "number_of_pingbacks": 4,
     "rating": 4.2,
     },
    {"blog": "ИТ-новости и технологии",
     "headline": "Последние тренды в мире искусственного интеллекта",
     "body_text": """В этой статье мы расскажем о последних трендах в мире 
искусственного интеллекта. Вы узнаете о новейших разработках, применении 
искусственного интеллекта в различных областях, таких как медицина, 
транспорт, финансы и многое другое. Мы также обсудим перспективы и 
вызовы, с которыми сталкиваются исследователи и разработчики в этой 
инновационной сфере.""",
     "pub_date": "2024-04-01",
     "authors": ["sergey_reads", "irina_blogger"],
     "number_of_comments": 0,
     "number_of_pingbacks": 0,
     "rating": 4.7,
     },
    {"blog": "ИТ-новости и технологии",
     "headline": "Развитие интернета вещей: будущее или реальность?",
     "body_text": """В этой статье мы рассмотрим развитие интернета вещей и 
выясним, насколько это будущее уже стало реальностью. Вы узнаете о 
принципах работы интернета вещей, его преимуществах и вызовах. Мы также 
рассмотрим конкретные примеры применения интернета вещей в различных 
сферах, таких как умный дом, здравоохранение, промышленность и 
транспорт.""",
     "pub_date": "2022-02-01",
     "authors": ["irina_blogger"],
     "number_of_comments": 8,
     "number_of_pingbacks": 8,
     "rating": 4.4,
     },
    {"blog": "ИТ-новости и технологии",
     "headline": "Новые гаджеты и устройства: обзор рынка",
     "body_text": """В этой статье мы представим вам обзор рынка новых 
гаджетов и устройств. Вы узнаете о самых актуальных технологических 
новинках, таких как смартфоны, ноутбуки, планшеты, умные часы и другие 
устройства. Мы расскажем о их особенностях, возможностях и тенденциях 
развития. Эта статья поможет вам быть в курсе последних технологических 
достижений и сделать информированный выбор при покупке нового гаджета.""",
     "pub_date": "2021-06-01",
     "authors": ["andrey_author"],
     "number_of_comments": 20,
     "number_of_pingbacks": 1,
     "rating": 3.5,
     },
    {"blog": "ИТ-новости и технологии",
     "headline": "Кибербезопасность: защита вашей конфиденциальности",
     "body_text": """В этой статье мы обсудим вопросы кибербезопасности и 
защиты вашей конфиденциальности в цифровом мире. Вы узнаете о 
распространенных угрозах, с которыми сталкиваются пользователи, 
и о методах защиты от киберпреступников. Мы поделимся с вами советами по 
созданию надежных паролей, использованию антивирусных программ, защите 
своих персональных данных и осознанному поведению в онлайн-среде.""",
     "pub_date": "2021-09-01",
     "authors": ["alexander89"],
     "number_of_comments": 12,
     "number_of_pingbacks": 6,
     "rating": 3.8,
     },
    {"blog": "ИТ-новости и технологии",
     "headline": "Инновации в области виртуальной реальности",
     "body_text": """В этой статье мы расскажем о последних инновациях в 
области виртуальной реальности. Вы узнаете о новейших разработках, 
использующих виртуальную и дополненную реальность, и о том, как эти 
технологии меняют различные отрасли, включая игровую индустрию, 
образование, медицину и бизнес. Мы также обсудим потенциал и перспективы 
развития виртуальной реальности и ее влияние на нашу жизнь.""",
     "pub_date": "2021-08-01",
     "authors": ["anna_journey"],
     "number_of_comments": 12,
     "number_of_pingbacks": 25,
     "rating": 4.9,
     },
    {"blog": "Мода и стиль",
     "headline": "Тенденции моды на текущий сезон",
     "body_text": """В этой статье мы расскажем о главных тенденциях моды на 
текущий сезон. Вы узнаете о модных цветах, принтах, фасонах и 
аксессуарах, которые будут актуальны в этом сезоне. Мы также предложим 
вам идеи и советы по созданию стильных образов с использованием новых 
модных трендов. Будьте в тренде и выглядите модно в этом сезоне!""",
     "pub_date": "2022-09-01",
     "authors": ["dmitry_thinker", "natalia_author", "ivan_wordsmith"],
     "number_of_comments": 8,
     "number_of_pingbacks": 20,
     "rating": 5,
     },
    {"blog": "Мода и стиль",
     "headline": "Как создать стильный образ на каждый день",
     "body_text": """В этой статье мы поделимся с вами секретами создания 
стильного образа на каждый день. Вы узнаете о базовых элементах 
гардероба, которые помогут вам выглядеть модно и уверенно в любой 
ситуации. Мы предложим вам простые идеи по комбинированию одежды, 
выбору аксессуаров и созданию гармоничного образа. Будьте стильными 
каждый день и выражайте свою индивидуальность через моду!""",
     "pub_date": "2024-11-01",
     "authors": ["nikolay_blog", "roman_author"],
     "number_of_comments": 0,
     "number_of_pingbacks": 0,
     "rating": None,
     },
    {"blog": "Мода и стиль",
     "headline": "История моды: от ретро до современности",
     "body_text": """В этой статье мы проведем вас через историю моды, 
начиная от ретро стиля до современных тенденций. Вы узнаете о модных 
эпохах, значимых дизайнерах и их влиянии на моду. Мы расскажем о 
ключевых характеристиках каждой эпохи и источниках вдохновения. 
Погрузитесь в мир моды и узнайте, как прошлое влияет на современные 
тенденции.""",
     "pub_date": "2023-06-01",
     "authors": ["irina_blogger"],
     "number_of_comments": 2,
     "number_of_pingbacks": 10,
     "rating": None,
     },
    {"blog": "Мода и стиль",
     "headline": "Уход за кожей и волосами: лучшие советы",
     "body_text": """В этой статье мы поделимся с вами лучшими советами по 
уходу за кожей и волосами. Вы узнаете о правильном выборе косметики, 
ежедневном уходе, сезонных рекомендациях и основных принципах ухода за 
кожей и волосами. Мы также расскажем о домашних рецептах и натуральных 
продуктах, которые помогут вам сохранить здоровье и красоту кожи и 
волос.""",
     "pub_date": "2023-02-01",
     "authors": ["alexander89"],
     "number_of_comments": 0,
     "number_of_pingbacks": 1,
     "rating": None,
     },
    {"blog": "Мода и стиль",
     "headline": "Интервью с известными модельерами и дизайнерами",
     "body_text": """В этой статье мы представим вам интервью с известными 
модельерами и дизайнерами. Вы узнаете о их вдохновении, творческом 
процессе и философии моды. Мы зададим им вопросы о ключевых трендах, 
их видении стиля и роли моды в современном обществе. Будьте в курсе 
мировой моды и получите вдохновение от талантливых дизайнеров!""",
     "pub_date": "2023-02-01",
     "authors": ["ivan_wordsmith"],
     "number_of_comments": 0,
     "number_of_pingbacks": 2,
     "rating": 4,
     },
]

if __name__ == "__main__":
    from json import dump

    with open("blogs.json", "w", encoding="utf-8") as f:
        dump(data_blog, f, ensure_ascii=False, indent=4)
    with open("authors.json", "w", encoding="utf-8") as f:
        dump(data_author, f, ensure_ascii=False, indent=4)
    with open("authors_profile.json", "w", encoding="utf-8") as f:
        dump(data_author_profile, f, ensure_ascii=False, indent=4)
    with open("entrys.json", "w", encoding="utf-8") as f:
        dump(data_entry, f, ensure_ascii=False, indent=4)
