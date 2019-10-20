# nlp_project
Экзаменационный проект по курсу автоматической обработки естественного языка.


[Краткий Отчет](https://docs.google.com/document/d/1jZ8E6HFWZidTLh2Z_70svKKH_F-r_SqsVvZLyJgc-88/edit?usp=sharing)

[Презентация](https://docs.google.com/presentation/d/1Djw1Sg8QhrgH5YEXnsr87Gv3Oxcr4Tsax28dFRbQonI/edit?usp=sharing)

В этом репозитории вы найдете следующие файлы:

1) udpipe.py и [russian-syntagrus-ud-2.4-190531.udpipe](https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2998/russian-syntagrus-ud-2.4-190531.udpipe?sequence=74&isAllowed=y) - файлы необходимые для работы парсера (помимо библиотеки ufal.udpipe)
2) udpipe_test.py - скрипт для тестирования
3) input.txt - файл с предложениями для разметки, он же testset
4) conll18_ud_eval.py - скрипт для подсчета метрик LAS (F-мера), MLAS и BLEX
5) output.txt и gold.txt - выдача парсера и золотой стандарт для сравнения
6) output_preprocessed.txt - выдача парсера с учетом препроцессинга (выделение всех кавычек пробелами)
7) output_hard.txt и gold_hard.txt - выдача парсера и золотой стандарт только для более сложных предложений
